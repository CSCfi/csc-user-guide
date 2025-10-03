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

Note also that with Mac you might need to disable Rosetta.

Another alternative is to build the image on an x64 VM, for example on pouta.csc.fi.

* Test your image. 
    * `-p 8888:8787` means bind Docker port 8787 to host port 8888.
    * If using cPouta, you need to open the host port also from Security groups. 
    * Open Jupyter/RStudio with web-browser: `localhost:8888` or `<cPouta-IP>:8888`

```
docker run -p 8888:8787 <yourimagename>
```

### Upload and link the image to your application

For the docker image to be used in your application. You need to host it somewhere, e.g. DockerHub or Rahti registry. 
Once you have it hosted somewhere, provide the link to your image in the application : `Manage Workspaces` > `Applications` > `Edit application` > `Container image`.