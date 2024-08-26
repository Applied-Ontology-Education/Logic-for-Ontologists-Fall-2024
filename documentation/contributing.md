## Contributing

- [Introduction](#introduction)
- [Git and GitHub](#git-and-github)
- [GitHub Workflow](#github-workflow)
- [Workflow for this Course](#workflow-for-this-course)
- [Merging using VSCode Command Palette](#vscode-merging-command")
- [Merging using VSCode Source Control](#vscode-merging-source")
- [Merging using Command Line](#vscode-merging-cli")
- [Further Resources](#resource)

<a name="introduction"></a>

## Introduction

The content of this file is adapted from the Github Classroom starter assignment, which is designed to give you a brief introduction to Git and GitHub. 

<a name="git-and-github"></a>

## Git and Github

**Git** is a system for tracking changes to your code, collaborating, and sharing. With Git you can track the changes you make to your project so you always have a record of what you’ve worked on and can easily revert back to an older version if need be. 

**GitHub** is a way to use Git online with an easy-to-use interface. 

<a name="github-workflow"></a>

## GitHub Workflow 

The **GitHub Flow** is a workflow that allows you to experiment and collaborate on your projects easily, without the risk of losing your previous work. 

A **repository** is where your project work happens--think of it as your project folder. It contains all of your project’s files and revision history.  You can work within a repository alone or invite others to collaborate with you on those files. Repositories also contain **README**s. You can add a README file to your repository to tell other people why your project is useful, what they can do with your project, and how they can use it. 

When a repository is created with GitHub, it’s stored remotely in the cloud. You can **clone** a repository to create a local copy on your computer and then use Git to sync the two. This makes it easier to fix issues, add or remove files, and push larger commits. Cloning a repository pulls down all the repository data that GitHub has at that point in time, including all versions of every file and folder for the project. This can be helpful if you experiment with your project and then realize you liked a previous version more. 

A **fork** is another way to copy a repository, but is usually used when you want to contribute to someone else’s project. Forking a repository allows you to freely experiment with changes without affecting the original project and is very popular when contributing to open source software projects.

**Committing** and **pushing** are how you can add the changes you made on your local machine to the main course repository so that your instructor can see your latest work. You should add a helpful **commit message** to remind yourself or your teammates what work you did. Once you have a commit or multiple commits that you’re ready to add to your repository, you can use the push command to add those changes to your remote repository. 

When working with branches, you can use a **pull request** to tell others about the changes you want to make and ask for their feedback. Once a pull request is opened, you can discuss and review the potential changes with collaborators and add more changes if need be. You can add specific people as reviewers of your pull request which shows you want their feedback on your changes! Once a pull request is ready-to-go, it can be merged into your main branch.

<a name="workflow-for-this-course"></a>

## Workflow for this Course

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

<a name="resources"></a>

##  Resources 
* [A short video explaining what GitHub is](https://www.youtube.com/watch?v=w3jLJU7DT5E&feature=youtu.be) 
* [Git and GitHub learning resources](https://docs.github.com/en/github/getting-started-with-github/git-and-github-learning-resources) 
* [Understanding the GitHub flow](https://guides.github.com/introduction/flow/)
* [How to use GitHub branches](https://www.youtube.com/watch?v=H5GJfcp3p4Q&feature=youtu.be)
* [Interactive Git training materials](https://githubtraining.github.io/training-manual/#/01_getting_ready_for_class)
* [GitHub's Learning Lab](https://lab.github.com/)
* [Education community forum](https://education.github.community/)
* [GitHub community forum](https://github.community/)

<a name="vscode-merging-command"></a>

## Merging Branches in VS Code Using the Command Palette

1. **Open VS Code**: Launch Visual Studio Code.

2. **Open the Command Palette**:
   - Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac) to open the Command Palette.

3. **Switch to the `master` (or `main`) Branch**:
   - Type `Git: Checkout to...` and select it from the dropdown.
   - Choose `master` or `main` from the list of branches.

4. **Pull the Latest Changes (Optional but Recommended)**:
   - Open the Command Palette again.
   - Type `Git: Pull` and select it from the dropdown.
   - Choose the remote branch you want to pull changes from, typically `origin/master` or `origin/main`.

5. **Merge the `dev` Branch into `master` (or `main`)**:
   - Open the Command Palette.
   - Type `Git: Merge Branch...` and select it.
   - Choose `dev` from the list of branches to merge into the currently checked-out branch (`master` or `main`).

6. **Resolve Any Merge Conflicts**:
   - If there are conflicts, VS Code will show them in the editor. Open the conflicted files.
   - Use the inline merge conflict resolution tools provided by VS Code to resolve the conflicts.

7. **Commit the Merge**:
   - If conflicts were resolved, go to the Source Control view to commit the merge.

8. **Push the Changes**:
   - Open the Command Palette.
   - Type `Git: Push` and select it to push the changes to the remote repository.

<a name="vscode-merging-source"></a>

## Merging Branches in VS Code Using Source Control View

1. **Open VS Code**: Launch Visual Studio Code.

2. **Open the Source Control View**:
   - Click on the Source Control icon in the [Activity Bar](https://code.visualstudio.com/docs/getstarted/userinterface) on the side of the window, or press `Ctrl+Shift+G` (Windows/Linux) or `Cmd+Shift+G` (Mac).

3. **Switch to the `master` (or `main`) Branch**:
   - Click on the branch name in the bottom-left corner of the Status Bar.
   - Select `master` or `main` from the list of branches to switch to it.

4. **Pull the Latest Changes (Optional but Recommended)**:
   - Click on the ellipsis (`...`) in the Source Control view.
   - Select `Pull` from the dropdown to fetch the latest changes from the remote repository.

5. **Merge the `dev` Branch into `master` (or `main`)**:
   - Click on the ellipsis (`...`) in the Source Control view.
   - Select `Merge Branch...`.
   - Choose `dev` from the list of branches to merge into the currently checked-out branch (`master` or `main`).

6. **Resolve Any Merge Conflicts**:
   - If there are conflicts, VS Code will highlight them in the editor. Open the conflicted files and use the inline tools to resolve them.

7. **Commit the Merge**:
   - If conflicts were resolved, you will see the merge changes in the Source Control view. Enter a commit message and commit the merge.

8. **Push the Changes**:
   - Click on the ellipsis (`...`) in the Source Control view.
   - Select `Push` to push the merged changes to the remote repository.

<a name="vscode-merging-cli"></a>

## Merging Branches Using Git in the Command Line

1. **Open Terminal and Navigate to Your Repository**:
   - cd /path/to/your/repo

2. **Fetch the Latest Changes from Remote (Optional but Recommended)**:
   - git fetch origin

3. **Switch to the Master (or Main) Branch**:
   - git checkout master (or git checkout main)

4. **Pull the Latest Changes to Master (or Main)**:
   - git pull origin master (git pull origin main)

5. **Merge the Dev Branch into Master (or Main)**:
   - git merge dev

6. **Resolve Any Merge Conflicts (If They Arise)**:
   - Open conflicted files in a text editor and resolve conflicts.
   - After resolving conflicts, add the resolved files:
   - git add <file>

7. **Complete the Merge if There Were Conflicts**:
   - git commit

8. **Push the Changes to the Remote Repository**:
   - git push origin master (git push origin main)

##  Resources 
* [A short video explaining what GitHub is](https://www.youtube.com/watch?v=w3jLJU7DT5E&feature=youtu.be) 
* [Git and GitHub learning resources](https://docs.github.com/en/github/getting-started-with-github/git-and-github-learning-resources) 
* [Understanding the GitHub flow](https://guides.github.com/introduction/flow/)
* [How to use GitHub branches](https://www.youtube.com/watch?v=H5GJfcp3p4Q&feature=youtu.be)
* [Interactive Git training materials](https://githubtraining.github.io/training-manual/#/01_getting_ready_for_class)
* [GitHub's Learning Lab](https://lab.github.com/)
* [Education community forum](https://education.github.community/)
* [GitHub community forum](https://github.community/)
