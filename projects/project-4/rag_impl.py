import chromadb
import os, json
from chromadb import Settings


def make_indexable(itm):
    item = {
        "document": [f"{itm.get('label')}: {itm.get('definition')}"]
        ,"metadata":  [{"label": itm.get('label'), "uri": itm.get('uri').__str__()}]
        , "id": [itm.get('uri').__str__()]
    }
    return item


class RAG():
    
    def __init__(self, index_name="", dbpath=None, rebuild = True):
        self.client = None
        self.collection = None
        self.index_name = index_name
        self.rebuild = rebuild
        self.dbpath=dbpath
        
    
    def build(self,):

        self.client =chromadb.PersistentClient(path=self.dbpath, 
                                          settings=Settings(anonymized_telemetry=False))

        if self.rebuild:
            try:
                self.client.delete_collection(name=self.index_name) 
            except Exception as e:
                pass

            self.collection = self.client.create_collection(
               name=self.index_name,
            )
        else:
            self.collection = self.client.get_collection(name=self.index_name)
        
        print(f"{self.index_name} document count: {self.collection.count()}.")
    
    
    
    def load(self, data, ingest_fun=make_indexable):
        loadcount = 0
        exceptions = []
        for d in data:
            item = ingest_fun(d)
            try:
                self.collection.add(
                    documents=item.get('document'), 
                    ids = item.get('id'),
                    metadatas=item.get('metadata')
                )
                loadcount += 1
            except:
                exceptions.append(d)
            

            if loadcount % 100 == 0:
                print(loadcount)             
        return {
            "load_result_doccount": self.collection.count()
            , "exceptions": exceptions
            , "exception_count": len(exceptions) 
        }

