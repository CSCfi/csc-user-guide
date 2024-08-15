# Guide for teachers and collaborators

Instructions on using the Noppe environment as a teacher or for collaboration.

## How to host a course or use Noppe for collaboration?

Noppe is built for hosting online courses. We support currently Jupyter and RStudio based content, with more
options to come in the future. The intended workflow is that you create one workspace per course, and arrange your 
exercises in one or more applications in that workspace.
Instead of a course you can also use Noppe for collaboration. The workflow is similar to creating a course environment and is described below.

### 1. Become a workspace owner and create a workspace
* Login to Noppe using your CSC account by choosing 'CSC Login' option after clicking 'Login'.
  If you don't have a CSC account yet, [see the instructions on how to create new user account](../../../accounts/how-to-create-new-user-account/).
* Open `Manage workspaces` from the left panel and create a new workspace.
    * Workspace type:
      * Fixed-time course with limited lifetime: Valid for limited months.
      * Long-running course with time-limited membership: Can be extended 13 months at a time. Intended for workspaces that offer continuous learning environment.
* If you don't see `Manage workspaces` option, please
    * Check that you logged in using your CSC account. Your user account on the bottom of the left navigation
      should look like 'csc/youraccountname'
    * Reload your browser
    * If the issue persists, contact Noppe support at servicedesk@csc.fi
 
### 2. Find or create custom images

* The easiest is to use an existing Docker image, look these repositories for suitable images:
    * [Docker image sources in noppe-public-images repository.](https://github.com/CSCfi/noppe-public-images)
    * [Rocker images](https://hub.docker.com/u/rocker) for different RStudio set-ups.
    * If you would need a few R/Python packages extra compared to existing images, it likely is easiest to add them run-time by the user.
* To create your own custom image, see [Creating custom Docker images](#creating-custom-docker-images) below.

### 3. Create an application in the workspace

Open `Manage workspaces` in the left navigation and select the workspace you want to work on. Create a new application 
through `Application wizard` or `Application form`-buttons.

**Application template** Template provides the base features for your application. Most of the templates are based on
container images maintained by Noppe team. Take a look at the 
[image sources in noppe-public-images repository](https://github.com/CSCfi/noppe-public-images). 
If you intend to use your own custom image, you can choose any template that matches your application type (Jupyter/RStudio).

**Application name** Give a valid meaningful name. This is the name under which participants will see the application.

**Application description** Fill a detailed description to helps users to understand more about the application.

**Container image** 
* If using existing image, then pre-filled based on chosen Application template.
* If using own custom image, then URL of the Docker image. 

**Session lifetime** The maximum lifetime for a single session. Sessions are deleted when they expire, thus making room 
for other users.

**Session memory** RAM memory reserved for each session. Workspaces have a limit for total memory for concurrent
sessions. Choosing a higher value here will affect the maximum number of concurrent sessions.

**Labels** Select the default labels or create custom labels. Labels are useful in searching applications. The icon for
the application is also selected based on assigned labels.

**Download Method** The location to download the course contents from. Choose `git clone` if you wish to clone a git
repository. Choose `Download from url` if you have contents hosted in Allas or other HTTP accessible location and provide the url. Content is downloaded to $HOME folder of any instance by default.

!!!Note

    The external location needs to be publicly accessible. For example git repositories should be public.

As an alternative, the course material can be provided through `shared` folder. The workspace owner can prepare the
shared folder in advance. The folder is visible for everyone, but is read-only for course participants.
[See data persistence document for more information](data_persistence.md).

**Work folder per user** Whether persistent user-based `my-work` folder is available for users in this application. 
This is enabled by default.

**Publication** Choose `save as draft` if you still need to test/change things in your application. Only after publication, which can be done here by choosing `publish immediately` or from the application menu (Manage workspaces > your workspace > your Application > 3 bars on right end of application > `publish`) later. Publication means that people with the join code can find the application. Your application will never appear for everyone. Only Noppe team can add self-learning and public-for-all applications.

### 4. Invite users

Once the content is ready, you can invite course participants / collaborators by sharing a workspace specific join code. The code can be found in
`Manage workspaces` view, in workspace list or on the Info tab of each workspace.

### 5. Promote users

Once the co-instructors/co-organizers/collaborators have signed in, you can find their name in the `members` tab (under `manage workspaces`), to give them rights to change things and see other participants sessions, `promote to co-owner` from the Menu column next to the members name.
Co-owners can do everything the owner can, except demoting the owner or deleting the workspace. For collaboration purposes, all collaborators should have co-owner rights, to be able to write to the shared folder in the workspace.

## Creating custom Docker images
If you cannot find a suitable image for your intended application, you will need to create and publish your own custom image for Noppe. Image can be created on your own computer or for example [cPouta](../pouta/index.md) instance.

Requirements: 

* A computer to create the Docker image, it should have [Docker](https://www.docker.com/) installed. In general Linux/Mac computer is recommended. In Windows likely admin rights are needed and using Docker might be challenging.
* A place to upload the Docker image, for example DockerHub or Quay.io. 

Steps to create your own custom Docker image:

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
# install a package with install2.r script
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

Note that with Mac, or on any ARM host, you need to tell docker to build x64 images so that they are compatible
with our cloud hosts. This can be done using "docker buildx".

```
docker buildx build --platform linux/amd64 ....
```

Another alternative is to build the image on an x64 VM, for example on pouta.csc.fi.

* Test your image. 
    * `-p 8888:8787` means bind Docker port 8787 to host port 8888.
    * If using cPouta, you need to open the host port also from Security groups. 
    * Open Jupyter/RStudio with web-browser: `localhost:8888` or `<cPouta-IP>:8888`

```
docker run -p 8888:8787 <yourimagename>
```

## Security guidelines for Workspace owners

- Noppe is not intended for sensitive data. Do not store sensitive data or data sets.
- Share join code only with users you wish to join your workspace.
- If you are creating custom images for your course, do not store any keys or sensitive data in the image.
- Delete the workspace as soon as the course is over.
