from rdflib import *
import json
from datetime import datetime, timedelta

class CommonCoreOntology():
    def __init__(self):
        self.cco = Graph().parse("../../../CommonCoreOntologies/src/cco-merged/CommonCoreOntologiesMerged.ttl")
        
        self.cco_ns = {x[0]:x[1] for x in self.cco.namespaces()}
        self.query_preamble = "\n".join([f"PREFIX {pfx}: <{self.cco_ns[pfx]}>" for pfx in self.cco_ns])
        
    def execute(self,querytext=""):
        q = "\n\n".join([self.query_preamble , querytext])
        start = datetime.now()
        res = self.cco.query(q)
        end = datetime.now()
        
        return {
            "result": {
                "query_duration_ms": round((end - start).microseconds / 1000,3), 
                "data": [c.asdict() for c in res]
            }
        }
    
    def execute_get_resultset(self,querytext=""):
        q = "\n\n".join([self.query_preamble , querytext])
        start = datetime.now()
        res = self.cco.query(q)
        end = datetime.now()
        
        #return {
        #    "result": {
        #        "query_duration_ms": round((end - start).microseconds / 1000,3), 
        #        "data": [c.asdict() for c in res]
        #    }
        #}   
        return {"results": res, "query_runtime_ms": round((end - start).microseconds / 1000,3)}
    
    
    #def get_count(self,count_query):
    #    return [r for r in res.query(count_query) ]

model = CommonCoreOntology() 