# Guide for teachers and collaborators

Instructions on using the CSC Notebooks environment as a teacher or for collaboration.

## How to host a course or use notebooks for collaboration?

CSC Notebooks is built for hosting online courses. We support currently Jupyter and RStudio based content, with more
options to come in the future. The intended workflow is that you create one workspace per course, and arrange your 
exercises in one or more applications in that workspace.
Instead of a course you can also use CSC Notebooks for collaboration. The workflow is similar to creating a course notebooks environment and is described below.

### 1. Become a workspace owner and creating a workspace
* Login to CSC Notebooks using your CSC account. Make note of your user account on the bottom of the left navigation
   bar. If you don't have a CSC account yet, 
   [see the instructions on how to create new user account](../../../accounts/how-to-create-new-user-account/).
* Send email to <notebooks@csc.fi> to request workspace owner rights. Please include your CSC user account in the mail. 
   We will add the capability to create your own workspaces to your account.
* Login to [CSC Notebooks](https://notebooks-beta.rahtiapp.fi/welcome) and check that you got workspace owner rights. 
It worked, if you see `Manage workspaces` tab in the left panel. 
* Create a new workspace.
 
### 2. Find or create custom images

* The easiest is to use an existing Docker image, look these repositories for suitable images:
    * [Docker image sources in notebook-images repository.](https://github.com/CSCfi/notebook-images/tree/master/builds)
    * [Rocker images](https://hub.docker.com/u/rocker) for different RStudio set-ups.
    * If you would need a few R/Python packages extra compared to existing images, it likely is easiest to add them run-time by the user.
* To create your own custom image, see [Creating custom Docker images](#creating-custom-docker-images) below.

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
* If using own custom image, then path to the Docker image. If using Rahti, then: `docker-registry.rahti.csc.fi/<yourprojectname>/<yourimagename>:<tag>` .

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

## Creating custom Docker images
If you cannot find a suitable image for your intended application, you will need to create and publish your own custom image for Notebooks. Image can be created on your own computer or for example [cPouta](../pouta/pouta-what-is.md) instance.

Requirements: 

* A computer to create the Docker image, it should have [Docker](https://www.docker.com/) installed. In general Linux/Mac computer is recommended. In Windows likely admin rights are needed and using Docker might be challenging.
* A place to upload the Docker image, for example CSC [Rahti](../rahti/rahti-what-is.md), DockerHub or Quay.io. In these instruction below CSC Rahti is used
    * If using Rahti, you need to have a project in Rahti. If needed, create a new project on [Rahti webpage](https://rahti.csc.fi:8443/). For Rahti also [oc tools](../rahti/usage/cli.md) are needed on the local/cPouta machine.

Steps to create your own custom Docker image and host it on Rahti registry:

### Create a Dockerfile  
   
Dockerfile contains a set of instructions to build a docker image. If unfamiliar with Dockerfile, see for example [Docker 101](https://www.paigeniedringhaus.com/blog/docker-101-fundamentals-the-dockerfile) and [Dockerfile reference](https://docs.docker.com/engine/reference/builder/).
   
#### Jupyter notebook example
For JupyterLab with some conda packages use the following as minimal example:

 ``` 
 # use jupyter minimal notebook as base for your image
 # it has eg conda already installed
 FROM jupyter/minimal-notebook

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
 RUN conda install --yes -c conda-forge <your-packages-here> \
   && conda clean -afy

 ```

For other package management systems, adjust the last `RUN` command accordingly. Make sure the package management system is available in `jupyter/minimal-notebook` base image or install it yourself (same way as ssh-client and less are installed in above example).
    
#### RStudio example
    
To build custom R images, you do not need to start from scratch. Many pre-built R images are already available in docker registries. Especially, the [rocker project](https://github.com/rocker-org/rocker-versioned2) contains a large set of images with various configurations provided in [DockerHub](https://hub.docker.com/u/rocker/). You can therefore start with one of these pre-existing images. 

For adding packages or configurations you can use [scripts provided by Rocker on their github page](https://github.com/rocker-org/rocker-versioned2/tree/master/scripts), edit them or write your own from scratch and copy them into the docker file system. These scripts usually contain system dependencies and required packages for your needs.

For RStudio with some packages, use the following Dockerfile as minimum example:

```bash
# Use Rocker RStudio as base for your image
FROM rocker/rstudio

# copy the desired installation script into docker file system, make sure that you have execute rights to the script
COPY install_xx.sh /rocker_scripts/

# install the custom packages and system dependencies by running the script
RUN /rocker_scripts/install_xx.sh
```
  
Below a few useful commands to install R packages from the command line or script, which can be used to write your own install script or edit the scripts provided by rocker:

```bash
# install a package with innstall2.r script
install2.r --error --deps TRUE packagename  
# Install R packages from CRAN
R -e "install.packages('packagename', repos='http://cran.rstudio.com/')" 
# Install R packages from Github using package managers like devtools and BiocManager. 
R --no-restore --no-save -e 'packagemanager::install_github("packagename",dependencies=TRUE)'
# Install R packages while specifying a specific version
R --no-restore --no-save -e 'packagemanager::install_version("packagename", version="version")'
# Script execution
R -e "source('/path/of/myscript.R')"  
```

### Build the image and test it 

* Build the image from dockerfile to current directory `.`

```
docker build -t "<yourimagename>" -f <yourimagename>.dockerfile .
```

* Test your image. 
    * `-p 8888:8787` means bind Docker port 8787 to host port 8888.
    * If using cPouta, you need to open the host port also from Security groups. 
    * Open Jupyter/RStudio with web-browser: `localhost:8888` or `<cPouta-IP>:8888`

```
docker run -p 8888:8787 <yourimagename>
```

### Add the image to Rahti registry
* Login to Rahti registry: 
    * In a web browser, open to [Rahti registry](https://registry-console.rahti.csc.fi/) and log in with your CSC username
    * On the `Overview` page, find the `login commands` section and the `Log into the registry` command. 
    * In terminal, use the command to log in to Rahti registry 

* Tag your docker image, eg based on versions (here: v0.1):
 ```
 docker tag <yourimagename> docker-registry.rahti.csc.fi/<yourrahtiproject>/<yourimagename>:v0.1
 ```

* Push your docker image to Rahti registry:
```
docker push docker-registry.rahti.csc.fi/<yourrahtiproject>/<yourimagename>:v0.1
```

* The new image should become visible in Rahti registry, see the ´Images´ tab. Now everything should be ready continuing from step 3 above.

## Security guidelines for Workspace owners

- CSC Notebooks is not intended for sensitive data. Do not store sensitive data or data sets.
- Share join code only with users you wish to join your workspace.
- If you are creating custom images for your course, do not store any keys or sensitive data in the image.
- Delete the workspace as soon as the course is over.
