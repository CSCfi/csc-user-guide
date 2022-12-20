# Using Allas from LUMI supercomputer


At the moment the LUMI object storage service, LUMI-O, is not yet in use and tools for 
using object storage services are not by default installed in LUMI-C. 
In this document we describe how you can install commonly used object storage clients 
to LUMI-C and how to configure connection to Allas object storage services. These tools 
can be used to access Lumi-O too when it becomes available.


## Installing Object Storage tools for Allas and Lumi-O

In this example we do the installation to the _/project_ area in Lumi so that 
all project members can utilize these tools. In this example we use example project _462000007_. 
Please use your own project number when installing these tools for your own use.

Once you have logged in to Lumi, move to the _/project_ disk area and make there a directory called _allas_.

```text
cd /project/project_462000007
mkdir allas
cd allas
```
Then, clone _allas-cli-utils_ repository to this location and continue to the cloned directory:
 
```text
git clone https://github.com/CSCfi/allas-cli-utils  
cd allas-cli-utils
```
      
Allas-cli-utils has a list of software dependencies that needs to be be installed. We use here the 
_lumi-container-wrapper_ tool to install most of them (s3cmd, Python OpenStack clinet, Python swift client,
zstdmt and crypt4gh). The installation is done with commands:

```text
module load LUMI lumi-container-wrapper
conda-containerize new --prefix /project/project_462000007/allas allas-dependencies.yaml
```
The command above will install the dependencies to a singularity container and make command-like 
execution scripts to a _bin_ directory that locates in the directory defined with the _--prefix_ option.
(in this case _/project/project_462000007/allas/bin_).

Finally we need to modify _a_env_conf_ file a bit so that _a-tools_ works smoothly.
Open the file:
```text
nano allas-cli-utils/a_env_conf
```

In this file do following modifications (remember to use your own project number in stead of
462000007)

```text
local_host=”lumi”
allas_conf_path="/project/project_462000007/allas/allas-cli-utils/allas_conf"
tmp_root="/scratch/project_462000007"
```

Next move to the allas directory and create a set up file _allas_setup.sh_ 
which will be use to simplify the setup process of Allas tools

```text
cd /project/project_462000007/allas 
nano allas_setup.sh
```
In the setup file will be used to add the installation directories to a-tools and object storage software 
your command path . In addition you create alias 'allas-conf' that runs source command for the 
connection setup script _allas_conf_. (remember here too to replace the project number with your own project)


```text
export PATH=/project/project_462000007/allas/allas-cli-utils:/project/project_462000007/allas/bin:$PATH
alias allas-conf="source /project/project_462000007/allas/allas-cli-utils/allas_conf"
``

Now the installation is ready. In the future you and your group members need to only 
run the setup commands decribed below, to enable object storage tools and to open connection to Allas and Lumo-O

## Opening connection from Lumi to Allas

Once the object storage tools have been installed to the project directory as describe above, then 
opening connection to Allas or Lumi-O requires first setting up the enviroment with command:

```text
source /project/project_your-project-number/allas/allas_setup.sh
```

Now commands like _allas-conf_, _rclone_, _swift_ or _a-put_ should work in the same way as in Puhti and Mahti.

Running command _allas-conf_ starts normal configuration process for swift based connetion to Allas:

```text
allas-conf
```

If you want to configure connetion Lumi-O, run command:
```text
allas-conf --lumi
```
This command asks you to connect with your browser to Lumi-O configuration sever, create credentials there and the copy the project nunber 
and keys for the setup tool. The setup process for Lumi-O will create environmeny variables, needed for _S3_ command and confuguration files for commands: _s3cmd_ and _rclone_. In addition you can define that a-commands will use by default Lumi-O storage server in stead of Allas. After that commands like _a-lits_, _a-put_ or _a-get_ will use your Lumi-O. If you don't c set Lumi-O as the defauly, you can add option _--lumi_ to a-commend to make use Lumi-O in stead of Allas. 

In the case of _rclone_,  Lumi-o configuration provides two _rclone remotes_: _lumi-o:_ and _lumi-pub:_ . The buckets used by _lumi-pub_ will be publicly visible in URL: https://_project-number_.lumidata.eu/_bucket_name_.

Note that you can have active connection to both Lumi-O and Allas in the same time.

For example, if you would first open Allas connection with command:

```text
source /project/project_your-project-number/allas/allas_setup.sh
allas-conf
```
And then open Lumo-O connection with:
```text
allas-conf --lumi
```
(when running the latter command we accept that Lumi-O will be the default erver for a-commands)
Now you can list the buckets available in Lumi-O with commands:

```text
a-list
```
or 
```text
rclone lsd lumi-o:
```
And in the same time you can list your buckets in Allas with commands:

```text
a-list --allas
```
or 
```text
rclone lsd allas:
```

Copying data from Allas to Lumi-O could now be done with command:

rclone copy

