# Guide for teachers and collaborators

Instructions on using the CSC Notebooks environment as a teacher or for collaboration.

## How to host a course or use notebooks for collaboration?

CSC Notebooks is built for hosting online courses. We support currently Jupyter and RStudio based content, with more
options to come in the future. The intended workflow is that you create one workspace per course, and arrange your 
exercises in one or more applications in that workspace.
Instead of a course you can also use CSC Notebooks for collaboration. The workflow is similar to creating a course notebooks environment and is described below.

### 1. Become a workspace owner and creating a workspace

1. Login to CSC Notebooks using your CSC account. Make note of your user account on the bottom of the left navigation
   bar. If you don't have a CSC account yet, 
   [see the instructions on how to create new user account](../../../accounts/how-to-create-new-user-account/).
2. Send email to <notebooks@csc.fi> to request workspace owner rights. Please include your CSC user account in the mail. 
   We will add the capability to create your own workspaces to your account.
3. Login to [CSC Notebooks](https://notebooks-beta.rahtiapp.fi/welcome) and check that you got workspace ower rights:
It worked, if you see `Manage workspaces` tab in the left panel. You can now use the `Create workspace` button to create a new workspace.
 
### 2. Create custom images, optional

Check the [image sources in notebook-images repository.](https://github.com/CSCfi/notebook-images/tree/master/builds). If you can find a suitable image for your application in the list, you can skip this step. If you cannot find a suitable image for your intended application, you will need to create and publish your own custom image for notebooks. Image can be created on your own computer or for example [cPouta](../pouta/pouta-what-is.md) instance.

Requirements: 

* A place to upload your Docker image, for example CSC [Rahti](../rahti/rahti-what-is.md), DockerHub or Quay.io.
* Docker installed 

Steps to create your own custom Docker image and host it on Rahti registry:

1. First create a Dockerfile  
   
   *Jupyte notebook example*:

    For JupyterLab with some conda packages use the following as minimal example:

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
    RUN conda install --yes -c conda-forge your-packages-here \
      && conda clean -afy

    ```

    For other package management systems, adjust the last `RUN` command accordingly. Make sure the package management system is available in `jupyter/minimal-notebook` base image or install it yourself (same way as ssh-client and less are installed in above example).
    
    *RStudio example*: 
    
    Dockerfile contains set of instructions to build an image of your interest. Fortunately, you don't need to start from the scratch to build custom R images.  Many pre-built R images are already available in docker registries. Especially, the [rocker project](https://github.com/rocker-org/rocker-versioned2) provides a large set of container images with various configurations in [DockerHub](https://hub.docker.com/u/rocker/). Youe can therefore start with pre-existing image to extend or further customise for your needs.

   Below is an example Dockerfile to create an RStudio image:

   ```bash
   # Check the full list of available base images [DockerHub](https://hub.docker.com/u/rocker/)
   # e.g., here start with rocker/rstudio:4.1.1 as base image (the first layer image) and extend as needed with rest of the layers of docker image
   # image tag/version (here: 4.1.1) must be used for reproducibility; avoid using "latest" tag
   FROM FROM rocker/rstudio:4.1.1

   ENV PATH=/usr/lib/rstudio-server/bin:$PATH

   # Add/modify these scripts for working with custom notebooks. Explore more about these scripts on [rocker github](https://github.com/rocker-org/rocker-versioned2/tree/master/scripts); 
   # These scripts usually contain system dependencies and required packages for your needs. 
   # if necessary one can modify the packages and package mannagers locally in the script and copy the script to docker file system before image building.

   COPY userconf.sh /rocker_scripts/
   COPY install_geospatial.sh /rocker_scripts/

   # install the custom packages and system dependencies
   RUN /rocker_scripts/install_geospatial.sh
   RUN /rocker_scripts/install_pandoc.sh

   # create volumes for storing data if any
   VOLUME /data
   COPY DataFiles /data/

   # Rtsudio is exposed on port 8787
   EXPOSE 8787

   CMD ["/init"]
   ```
   
   Briefly, the dockerfile uses `FROM` directive to pull a base image which in this case is Rstudio 4.1.1. This image already includes some system dependecies and R packages. `FROM` command must always be the first one in Dockerfile. Then, the commands beginning with `RUN` are the commands you would normally execute on your terminal and add additional layers on the top of base image. The `CMD` directive executes any initial scripts  every time you launch the docker container.

   Please note that the installation of R packages normally innvloves using `install.packages()` command. However, R package managers (Devtools,BiocManager) can also be used to install packages. Below are few example scenarios for installing R packages on commandline and useful when editing scripts (e.g.,install_geospatial.sh or similar ones):

```bash
  install2.r --error --deps TRUE packagename  # installing a package with innstall2.r script
  R -e "install.packages('packagename', repos='http://cran.rstudio.com/')" # Installing R packages from CRAN
  R --no-restore --no-save -e 'packagemanager::install_github("packagename",dependencies=TRUE)' # Installing R packages from github using package mannagers like devtools and BiocManager. 
  R --no-restore --no-save -e 'packagemanager::install_version("packagename", version="version")' # Installing R packages while specifying a specific version
  R -e "source('/path/of/myscript.R')" # script execution 
  ```
2. Build the image from dockerfile to current directory `.`

   ```
   docker build -t "<yourimagename>" -f <yourimagename>.dockerfile .
   ```
   
3. For publishing your image to Rahti, login to [Rahti registry](https://registry-console.rahti.csc.fi/)

4. Find the `login commands` on the `Overview` page and use one of them to login to Rahti registry from command line

5. Create a new project on Rahti webpage (or re-use one that you already have)

6. Tag your docker image, eg based on versions (here: v0.1):

    ```
    sudo docker tag <yourimagename> docker-registry.rahti.csc.fi/<yourrahtiproject>/<yourimagename>:v0.1
    ```

7. Push your docker image to Rahti registry:
   ```
   sudo docker push docker-registry.rahti.csc.fi/<yourrahtiproject>/<yourimagename>
   ```

### 3. Create an application in the workspace

Open `Manage workspaces` in the left navigation and select the workspace you want to work on. Create a new application 
through `Application wizard` or `Application form`-buttons.

**Application template** Template provides the base features for your application. Most of the templates are based on
container images maintained by Notebooks team. Take a look at the 
[image sources in notebook-images repository.](https://github.com/CSCfi/notebook-images/tree/master/builds). If you intend to use your own custom image, you can choose any of the templates which then determines only the memory and lifetime of your application.

**Application name** Give a valid meaningful name. This is the name under which participants will see the notebook in the list of notebooks.

**Application description** Fill a detailed description to helps users to understand more about the application.

**Container image** 
* If using existing image, then pre-filled based on chosen Application template.
* If using own custom image, then path to the Docker image. If you followd the custom image instructions above, you can find the link from Rahti web interface > projectname > imagename > Pulling repository, e.g. `docker-registry.rahti.csc.fi/<yourprojectname>/<yourimagename>:<tagyouwanttouse>` .

**Labels** Select the default labels or create custom labels. Labels are useful in searching applications. The icon for
the application is also selected based on assigned labels.

**Interface** JupyterLab or old Jupyter Notebook. Applicable only for Jupyter based applications.

**Download Method** The location to download the course contents from. Choose `git clone` if you wish to clone a git
repository. Choose `Download from url` if you have contents hosted in Allas or other HTTP accessible location and provide the url. Content is downloaded to $HOME folder of any instance by default.

!!!Note

    The external location needs to be publicly accessible. For example git repositories should be public.

As an alternative, the course material can be provided through `shared` folder. The workspace owner can prepare the
shared folder in advance. The folder is visible for everyone, but is read-only for course participants.
[See data persistence document for more information](data_persistence.md).

**Work folder per user** Whether persistent user-based `my-work` folder is available for users in this application. 
This is enabled by default.

**Publication** Choose `save as draft` if you still need to test/change things in your application. Only after publication, which can be done here by choosing `publish immediately` or from the application menu (Manage workspaces > your workspace > your Application > 3 bars on right end of application > `publish`) later. Publication means that people with the join code can find the application. Your application will never appear for everyone. Only CSC Notebooks team can add self-learning and public-for-all notebooks.

### 4. Invite users

Once the content is ready, you can invite course participants / collaborators by sharing a workspace specific join code. The code can be found in
`Manage workspaces` view, in workspace list or on the Info tab of each workspace.

### 5. Promote users

Once the co-instructors/co-organizers/collaborators have signed in, you can find their name in the `members` tab (under `manage workspaces`), to give them rights to change things and see other participants sessions, `promote to co-owner` from the Menu column next to the members name.
Co-owners can do everything the owner can, except demoting the owner or deleting the workspace. For collaboration purposes, all collaborators should have co-owner rights, to be able to write to the shared folder in the workspace.


## Security guidelines for Workspace owners

- CSC Notebooks is not intended for sensitive data. Do not store sensitive data or data sets.
- Share join code only with users you wish to join your workspace.
- If you are creating custom images for your course, do not store any keys or sensitive data in the image.
- Delete the workspace as soon as the course is over.
