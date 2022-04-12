# Guide for teachers and collaborators

Instructions on using the CSC Notebooks environment as a teacher or for collaboration.

## How to host a course or use notebooks for collaboration

CSC Notebooks is built for hosting online courses. We support currently Jupyter and RStudio based content, with more
options to come in the future. The intended workflow is that you create one workspace per course, and arrange your 
exercises in one or more applications in that workspace.
Instead of a course you can also use CSC Notebooks for collaboration. The workflow is similar to creating a course notebooks environment and is described below.

### 1. Becoming a workspace owner and creating a workspace

1. Login to CSC Notebooks using your CSC account. Make note of your user account on the bottom of the left navigation
   bar. If you don't have a CSC account yet, 
   [see the instructions on how to create new user account](../../../accounts/how-to-create-new-user-account/).
2. Send email to <notebooks@csc.fi> to request workspace owner rights. Please include your CSC user account in the mail. 
   We will add the capability to create your own workspaces to your account.
3. Login to [CSC Notebooks](https://notebooks-beta.rahtiapp.fi/welcome) and check that you got workspace ower rights:
It worked, if you see 'Manage workspaces' tab in the left panel. You can now use the *Create workspace* button to create a new workspace.
 
### 2. Custom images

Check the [image sources in notebook-images repository.](https://github.com/CSCfi/notebook-images/tree/master/builds). If you can find a suitable image for your application in the list, you can skip this step. If you cannot find a suitable image for your intended application, you will need to create and publish your own custom image for notebooks:

Requirements: 

* own CSC user account with [Rahti](../rahti/rahti-what-is.md) access, or another way to publish your image
* Docker installed (on own computer or [Pouta](../pouta/pouta-what-is.md) instance)

Steps to create your own custom image using Docker and host it on Rahti:

1. Create Docker file

    For Jupyter Lab with some conda packages use the following as minimal example:

    xxcourse.dockerfile:

    ```text 
    # use jupyter minimal notebook as base for your image
    # it has eg conda already installed
    FROM jupyter/minimal-notebook

    # add your name as maintainer, with your email address for future questions
    LABEL maintainer="your-name-here"

    #some first setup steps need to be run as root user
    USER root

    # set home environment variable to point to user directory
    ENV HOME /home/$NB_USER

    # install needed extra tools, eg ssh-client and less
    RUN apt-get update \
        && apt-get install -y ssh-client less \
        && apt-get clean

    # the user set here will be the user that students will use 
    USER $NB_USER

    ### Installing the needed conda packages and jupyter lab extensions. 
    # Run conda clean afterwards in same layer to keep image size lower
    RUN conda install --yes -c conda-forge \
    your-packages-here \
    && conda clean -afy

    ```

    For other package management systems, adjust the last `RUN` command accordingly. Make sure the package management system is available in jupyter/minimal-notebook or install it yourself (same way as ssh-client and less are installed in above example).

2. Build the image from dockerfile to current directory (.)
    `docker build -t "<yourimagename>" -f <yourimagename>.dockerfile .`

3. For publishing your image to Rahti, login to [Rahti registry](https://registry-console.rahti.csc.fi/)

4. Find the `login commands` on the `Overview` page and use one of them to login to Rahti registry from command line

5. Create a new project on Rahti webpage (or re-use one that you already have)

6. Tag your docker image, eg based on versions (here: v0.1):

    `sudo docker tag <yourimagename> docker-registry.rahti.csc.fi/<yourrahtiproject>/<yourimagename>:v0.1`

7. Push your docker image to Rahti registry:

    `sudo docker push docker-registry.rahti.csc.fi/<yourrahtiproject>/<yourimagename>`

### 3. Creating an application in the workspace

Open *Manage workspaces* in the left navigation and select the workspace you want to work on. Create a new application 
through *Application wizard* or *Application form* -buttons.

**Application template** Template provides the base features for your application. Most of the templates are based on
container images maintained by Notebooks team. Take a look at the 
[image sources in notebook-images repository.](https://github.com/CSCfi/notebook-images/tree/master/builds){target="_blank"}. If you intend to use your own custom image, you can choose any of the templates which then determines only the _memory_ and _lifetime_ of your application.

**Application name** Give a valid meaningful name. This is the name under which participants will see the notebook in the list of notebooks.

**Application description** Fill a detailed description to helps users to understand more about the application.

**Container image** Pre-filled based on chosen Application template.
Advanced usage: If you need different setup from what is provided in [image sources in notebook-images repository.](https://github.com/CSCfi/notebook-images/tree/master/builds), you can also [build 
your own image](getting_started.md/#custom-images), upload it to a public image registry (such as docker-registry in Rahti, DockerHub or Quay.io) and pointing *Container image* to it. If you followd the custom image instructions above, you can find the link from Rahti web interface > projectname > imagename > Pulling repository, e.g. `docker-registry.rahti.csc.fi/<yourprojectname>/<yourimagename>:<tagyouwanttouse>` .

**Labels** Select the default labels or create custom labels. Labels are useful in searching applications. The icon for
the application is also selected based on assigned labels.

**Interface** JupyterLab or old Jupyter notebooks. Applicable only for Jupyter based applications.

**Download Method** The location to download the course contents from. Choose *git clone* if you wish to clone a git
repository. Choose *Download from url* if you have contents hosted in Allas or other HTTP accessible location and provide the url. Content is downloaded to $HOME folder of any instance by default.

!!!Note

    The external location needs to be publicly accessible. For example git repositories should be public.

As an alternative, the course material can be provided through `shared` folder. The workspace owner can prepare the
shared folder in advance. The folder is visible for everyone, but is read-only for course participants.
[See data persistence document for more information](data_persistence.md).

**Work folder per user** Whether persistent user-based `my-work` folder is available for users in this application. 
This is enabled by default.

**Publication** Choose *save as draft* if you still need to test/change things in your application. Only after *publication*, which can be done here by choosing *publish immediately* or from the application menu (Manage workspaces > your workspace > your Application > 3 bars on right end of application > *publish*) later. Publication means that people with the join code can find the application. Your application will never appear for everyone. Only CSC Notebooks team can add self-learning and public-for-all notebooks.

### 4. Invite users

Once the content is ready, you can invite course participants / collaborators by sharing a workspace specific join code. The code can be found in
*Manage workspaces* view, in workspace list or on the Info tab of each workspace.
The users can enter the code by clicking *Join workspace* button located in the top bar. They can then see all published 
applications on top of the application list on the *Applications* page, and under *My workspaces* page as well.

### 5. Promote users

Once the co-instructors/co-organizers/collaborators have signed in, you can find their name in the *members* tab (under *manage workspaces*), to give them rights to change things and see other participants sessions, *promote to co-owner* from the Menu column next to the members name.
Co-owners can do everything the owner can, except demoting the owner or deleting the workspace. For collaboration purposes, all collaborators should have co-owner rights, to be able to write to the shared folder in the workspace.


## Security guidelines for Workspace owners

- CSC Notebooks is not intended for sensitive data. Do not store sensitive data or data sets.
- Share join code only with users you wish to join your workspace.
- If you are creating custom images for your course, do not store any keys or sensitive data in the image.
- Delete the workspace as soon as the course is over.
