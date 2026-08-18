
!!! success "Basic level"
    This is a simple tutorial to show how to deploy a web server using the Rahti [web interface](../../get-started/web-interface.md) using a git repository as a source

# Deploy from Git

How to set up a static web server in Rahti from a Git repository.

1. Create a project. [Instructions](../../get-started/projects.md)

2. In the Rahti web console. Select the plus sign on the top right corner and then _Import from Git_. 

    ![click_git](../../../../img/click_git.png)

3. Input the URL of the Git repository. Rahti will use that URL to clone the repository.  

    ![import_from_git](../../../../img/import_from_git_1.png)

    The `Advanced Git Options` allows you to change the "reference" (Branch, tag or commit) or the context dir. And also allows to add a secret to get access to the repository (username and password, or SSH keys).

4. After inputting the URL. Rahti will validate and analyze the repository. 

    ![import_from_git](../../../../img/import_from_git_2.png)

5. If the analysis was successful, the last step is to click on `Create`. After few minutes, the site should be available.

After this tutorial, you can check the [Webhooks](webhooks.md) article. Web hooks will allow you to automatically re-deploy this site for every change in the main master branch.
