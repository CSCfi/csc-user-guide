# Using Allas from LUMI supercomputer


At the moment the LUMI object storage service, LUMI-O, is not yet in use and tools for 
using object storage services are not by default installed in LUMI-C. 
In this document we describe how you can install commonly used object storage clients 
to LUMI-C and how to configure connection to Allas object storage services.


## Installing Allas tools

In this example we do the installation to the _/project_ area of a project so that 
all project members can utilize these tools. In this example we use example project _462000007_. 
Please use your own project number when installing these tools for your own project.

Once you have logged in to Lumi, move to the _/project_ disk area of the project and make there a directory called _allas_.

```text
/project/project_462000007
mkdir allas
cd allas
```
Then we clone allas-cli-utils repository to this location and continue to the cloned directory:
 
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
(in this case /project/project_462000007/allas/bin).

In addition we need to install _rclone_. Following commands add _rclone_ command to the same 
directory where other dependencies locate.

```text
cd /project/project_462000007/allas
wget https://downloads.rclone.org/rclone-current-linux-amd64.zip
unzip rclone-current-linux-amd64.zip
mv rclone-v1.58.0-linux-amd64/rclone bin/
```

Finally we need to modify _a_env_conf_ file a bit so that _a-tools_ work smoothly.
Open the file
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

Now the installation is ready. In the future you and your group members need to only 
run the connection configuration commands below, to enable object storage tools and to open connection to Allas.

## Opening connection from Lumi to Allas

When you want to use these object storage tools, add the installation directories to 
your command path (remember here too to replace the project number with your own project).

```text
export PATH=/project/project_462000007/allas/allas-cli-utils:/project/project_462000007/allas/bin:$PATH
```

Then open Allas connection with command:
```text
source /project/project_462000007/allas/allas-cli-utils/allas_conf
```

Now commands like _rclone_, _swift_ or _a-put_ should work in the same way as in Puhti and Mahti.
