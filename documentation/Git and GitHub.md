## Introduction to Git and Github

The content of this exercise is based on the Github Classroom starter assignment, which is designed to give you a brief introduction to GitHub. The task at the end of this README.md file is designed to help you practice using Github...

## Git and GitHub

**Git** is a system for tracking changes to your code, collaborating, and sharing. With Git you can track the changes you make to your project so you always have a record of what you’ve worked on and can easily revert back to an older version if need be. 

**GitHub** is a way to use Git online with an easy-to-use interface. 

## Understanding the GitHub Workflow 

The **GitHub Flow** is a workflow that allows you to experiment and collaborate on your projects easily, without the risk of losing your previous work. 

A **repository** is where your project work happens--think of it as your project folder. It contains all of your project’s files and revision history.  You can work within a repository alone or invite others to collaborate with you on those files. Repositories also contain **README**s. You can add a README file to your repository to tell other people why your project is useful, what they can do with your project, and how they can use it. 

When a repository is created with GitHub, it’s stored remotely in the cloud. You can **clone** a repository to create a local copy on your computer and then use Git to sync the two. This makes it easier to fix issues, add or remove files, and push larger commits. Cloning a repository pulls down all the repository data that GitHub has at that point in time, including all versions of every file and folder for the project. This can be helpful if you experiment with your project and then realize you liked a previous version more. 

A **fork** is another way to copy a repository, but is usually used when you want to contribute to someone else’s project. Forking a repository allows you to freely experiment with changes without affecting the original project and is very popular when contributing to open source software projects.

**Committing** and **pushing** are how you can add the changes you made on your local machine to the main course repository so that your instructor can see your latest work. You should add a helpful **commit message** to remind yourself or your teammates what work you did. Once you have a commit or multiple commits that you’re ready to add to your repository, you can use the push command to add those changes to your remote repository. 

When working with branches, you can use a **pull request** to tell others about the changes you want to make and ask for their feedback. Once a pull request is opened, you can discuss and review the potential changes with collaborators and add more changes if need be. You can add specific people as reviewers of your pull request which shows you want their feedback on your changes! Once a pull request is ready-to-go, it can be merged into your main branch.

**Issues** are a way to track enhancements, tasks, or bugs for your work on GitHub. Issues are a great way to keep track of all the tasks you want to work on for your project and let others know what you plan to work on. 

## Github Workflow for PHI-696

For the purposes of this course, I will maintain a central repository where all of the course material - such as this documentation - is located, and you will 'fork' that repository on your personal Github account. There, you will complete assignments, adding your answers to your personal Github page. 

When you add your submission to your personal Github repository, you will be prompted to either "commit to the main branch' or "create a new branch for this request and start a pull request. You will always choose to open a 'pull request'. The difference here is that by opening a pull request, you open the door for your peers to help you refine the submission. That in mind, when you open a pull request, you will tag other students in the class requesting that they review your work. You will work together to polish your answers. Once your reviewers have 'approved' your work, you will then 'merge' your work to your personal repository. 

Once you have merged your work there, you will open another pull request - this time tagging @johnbeve - so that I can review your work before merging it to the main course repository. 

You can visualize the process as something like:  

```mermaid
    gitGraph
       commit id: "1"
       commit id: "2"
       branch Your_Work
       checkout Your_Work
       commit id: "3"
       checkout main
       commit id: "4"
       checkout Your_Work
       branch Your_Work_in_PR
       commit id: "5"
       checkout Your_Work
       merge Your_Work_in_PR id: "Reviewed!"
       checkout main
       merge Your_Work id: "Submit Work"
       commit id: "6"
       checkout main
       commit id: "7"
  ```
Where the numbers instances where changes have been made to a repository. The top grey line represents the main course repository. At change - or 'commit' - 2, you create a copy of the repository and begin working. You periodically check to make sure that your copy is up to date with the main branch, and this is reflected in your making commit 3 then making commit 5. This is because commit 4 occurred on the main branch, but you - good student that you are - updated your personal repository to keep up with the main course repository. Eventually, you submit your work to the main branch and it is 'merged'. Afterwards, you'll be able to see your work on the main course repository. 


##  Resources 
* [A short video explaining what GitHub is](https://www.youtube.com/watch?v=w3jLJU7DT5E&feature=youtu.be) 
* [Git and GitHub learning resources](https://docs.github.com/en/github/getting-started-with-github/git-and-github-learning-resources) 
* [Understanding the GitHub flow](https://guides.github.com/introduction/flow/)
* [How to use GitHub branches](https://www.youtube.com/watch?v=H5GJfcp3p4Q&feature=youtu.be)
* [Interactive Git training materials](https://githubtraining.github.io/training-manual/#/01_getting_ready_for_class)
* [GitHub's Learning Lab](https://lab.github.com/)
* [Education community forum](https://education.github.community/)
* [GitHub community forum](https://github.community/)
