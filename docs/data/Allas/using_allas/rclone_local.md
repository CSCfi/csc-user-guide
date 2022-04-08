### Local Rclone configuration for Allas

Rclone can be installed in any operating system and thus it provides an effective way 
to use Allas from any computer. You can download a copy of rclone to your own computer 
form the link below.

   * [Rclone download site](https://rclone.org/downloads/)

Once you have Rclone installed you still need configure the connection to Allas. Rclone is a 
command line application so both configurarion and actual usage is normally done in a command 
line: _Terminal_ in Mac and Linux, _Command prompt_ or _Powershell_ in Windows.

### Configuring Allas connection in Mac and Linux (SWIFT and S3)

If you are using rclone in a local **Linux** or **Mac machine**, you can download 
the `allas_conf` script to set up the connection to your Allas project.

```text
wget https://raw.githubusercontent.com/CSCfi/allas-cli-utils/master/allas_conf
source allas_conf -u your-csc-username -p your-csc-project-name
```
Note that you should use the `-u` option to define your CSC username and -p to 
define the CSC project you want to use. For example:

```text
source allas_conf -u kkayttaj -p project_2001234
```
The command above defines a connection that uses SWIFT protocol and is valid in the current
terminal session for 8 hours. The Rclone _remote_ site name is in this case _allas:_. After 
configuration can for example list your buckets in Allas with command:
```text
rclone lsd allas:
```
If you want to use S3 protocol in setad of SWIFT, add option _- S3_ . 
```text
source allas_conf -u kkayttaj -p project_2001234 -m S3
```
Note that in order to run the command above you must have OpenStack client installed in your
local machgine. After configuring S3 commection to Allas, you can use it through Rclone remote 
called _s3allas:_ . For example:

```text
rclone lsd s3allas:
```
S3 connection is active untill you explicitly delete it with command:
```text
source allas_conf -u csc-user-name -p csc-project-name --s3remove
```

### Configuring Allas connection in Windows 

In cases where you can't use _allas_conf_ script you can configure the Allas connetion with 
command:

```text
rclone config
```
The command above launches a configration process that you can use to define new Rclone 
connetion. In Rclone thes connectytion definitions are called as _remotes_. 
Below we describe how to create SWIFT and S3 connections to Allas.

#### Configuring SWIFT connection in Windows

Start the process by executing command:

```text
rclone config
```
And do folloing selections:

   1. Select **n** to create a _New remote_
   2. Name the remote as: **allas**
   3. From the list of storage protocols, select the number that defines:
_OpenStack Swift (Rackspace Cloud Files, Memset Memstore, OVH)_
   4. Select authentication option **2** _OpenStack Swift (Rackspace Cloud Files, Memset Memstore, OVH)_
   5. After that select the default _blank_ setting for all the remaining settings until you are 
 back in the starting menu of the confguration process. There choose **q** to stop the configuraytion process.
 
In the case of SWIFT you need to do this configuration only once. In the configuration 
we defined that in case of _allas_, all data from the connection is red from environment 
variables.

Next we need create a text file that sets these variables. Open a new file in a text-only 
editor like _notepad_ in this example we name the settings file as _allas_env.cmd_ . 
In the file we use syntax:

```text
set VARIABLE=value
```
One way to check the values of the variables needed is to open terminal connection to 
[https://puhti.csc.fi](puhti.csc.fi) and activate there connection to the Allas project you 
wih to use. This is done in Puhti with commnads:

```text
module load allas
allas-conf
```
After that you can check the variable values with commands:

```text
echo $variable_name
```
Part of the variable settings are alwayy the same for Allas.
These static settings are listed below and you can copy them directly to
your settings file:

```text
set OS_USER_DOMAIN_NAME=Default
set OS_REGION_NAME=regionOne
set OS_INTERFACE=public
set OS_IDENTITY_API_VERSION=3
set OS_AUTH_URL=https://pouta.csc.fi:5001/v3
set OS_INTERFACE=public
```
Then there are some variables that are project or user specific so you need 
to change them only when you want to change the allas project you are using.

The project spesific variables are:

   * **OS_PROJECT_NAME**, name of the CSC project 
   * **OS_USERNAME**, your CSC usernane.
   * **OS_STORAGE_URL**, Check this value in Puhti with commad  _echo $OS_STORAGE_URL_ .

In the end you should have a text file (allas_conf.cmd) that looks something like below:
```text
set OS_USER_DOMAIN_NAME=Default
set OS_REGION_NAME=regionOne
set OS_INTERFACE=public
set OS_IDENTITY_API_VERSION=3
set OS_AUTH_URL=https://pouta.csc.fi:5001/v3
set OS_INTERFACE=public
set OS_PROJECT_NAME=project_2001234
set OS_USERNAME=kkayttaj
set OS_STORAGE_URL=https://a3s.fi:443/swift/v1/AUTH_5d68719ga0fh46deb5581a2625ee1a9d
```
In addition to the variables below you need to define OS_AUTH_TOKEN variable that contains
the actual authentication token. This token is valid only for 8 hours so you typically need 
to check and define it each time you start using rclone in your computer.

At the moment we don't have a tool for generating this value in Windows so you need to 
use Puhti (or some other machine that can run allas_conf tool) to generate this project 
specific temporary token. Then check the value in Puhti with command _echo $OS_AUTH_TOKEN_
and set the variable accordingly in your local machine. 

With these settings done you could open Allas connection for rclone with commands:

```text
allas_conf.cmd
set OS_AUTH_TOKEN=string-copied-from-puhti
```
Now you should be able to check your buckets with command:
```text
rclone lsd allas:
```







 
