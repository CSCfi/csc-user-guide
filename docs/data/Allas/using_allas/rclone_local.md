# Local Rclone configuration for Allas

Rclone can be installed in any operating system and thus it provides an effective way 
to use Allas from any computer. You can download a copy of Rclone to your own computer 
from the link below.

* [Rclone download site](https://rclone.org/downloads/)

Once you have Rclone installed you still need to configure the connection to Allas. Rclone is a 
command-line application so both configuration and actual usage is normally done in a command 
line: _Terminal_ in Mac and Linux, _Command prompt_ or _Powershell_ in Windows.

## Configuring Allas connection in Mac and Linux (Swift and S3)

If you are using Rclone in a local **Linux** or **Mac machine**, you can download 
the `allas_conf` script to set up the connection to your Allas project.

```bash
wget https://raw.githubusercontent.com/CSCfi/allas-cli-utils/master/allas_conf
source allas_conf -u your-csc-username -p your-csc-project-name
```

Note that you should use the `-u` option to define your CSC username and `-p` to 
define the CSC project you want to use. For example:

```bash
source allas_conf -u kkayttaj -p project_2001234
```

The command above defines a connection that uses Swift protocol and is valid in the current
terminal session for 8 hours. The Rclone _remote_ site name is in this case _allas_. After 
configuration you can for example list your buckets in Allas with command:

```bash
rclone lsd allas:
```

If you want to use S3 protocol instead of Swift, add option `-m S3` to the configuration command. 

```bash
source allas_conf -u kkayttaj -p project_2001234 -m S3
```

Note that in order to run the command above you must have _OpenStack_ client installed in your local machine. After configuring S3 connection to Allas, you can use it through Rclone remote called _s3allas:_. For example:

```bash
rclone lsd s3allas:
```

S3 connection is active until you explicitly delete it with command:

```bash
source allas_conf -u csc-user-name -p csc-project-name --s3remove
```

!!! Note
    Remember to be careful and security-aware when configuring S3 connection to Allas. The S3 keys are stored in a readable format in your home directory and anyone who can read your keys can access Allas until the keys are expilicitly revoked from Allas. Removing the keys from your own computer is not enough to deactivate them.

## Configuring Allas connection in Windows 

In Windows machines you can't use `allas_conf` script. So for Windows some connection-specific variables need to be checked up in parallel from a Linux/Mac supporting `allas_conf` script. Easiest could be Puhti, if you use it otherwise. One option is also to use Windows Linux Subsystem and then the instructions above can be followed.

Configure the Allas connection with command:

```bash
rclone config
```

You can use this command also in other machines where `allas_conf` is not available.
The command above launches a configuration process that you can use to define new Rclone 
connection. In Rclone these defined connections are called _remotes_. 

Below we describe how to create Swift and S3 connections to Allas.

#### Configuring Swift connection in Windows

Start the process by opening PowerShell and executing command:

```bash
.\rclone.exe config
```

In the interactive configuration process, do following selections:

1. Select **n** to create a _New remote_
2. Name the remote as: **allas**
3. From the list of storage protocols, select the number that defines:
_OpenStack Swift (Rackspace Cloud Files, Memset Memstore, OVH)_
4. Select authentication option **2**: _Get swift credentials from environment vars._
5. After that select the default _blank_ setting for all the remaining settings until you are back in the starting menu of the configuration process. 
6. Finally, choose **q** to stop the configuration process.
 
In the case of Swift you need to do this configuration only once. In the configuration 
it is now defined that in case of _allas_, all data for the connection is read from environment variables.

If you have access to Puhti, then the easiest way to check the values of the variables needed is to open a terminal connection to it and activate there a connection to the Allas project you wish to use. Another option is to use a utility program [allas-get-swift-token-win.zip](https://github.com/CSCfi/allas-get-swift-token/releases/download/v1.0.0/allas-get-swift-token-win.zip). If you choose to use the utility program, you (or your local IT-support) may have to configure your anti-virus etc. software to allow running it.

If you use Puhti for setting Swift access variables, activate the Allas environment in Puhti with commands:

```bash
module load allas
allas-conf --show-powershell
```

When the configuration process in Puhti is ready, copy the last four lines, starting with `$Env:`, to the local PowerShell and execute them. Then test the Rclone connection with command:

```bash
  .\rclone.exe lsd allas:
```

Note that also in this case the connection will work only for the next 8 hours.

#### Configuring S3 connection in Windows

!!! Note
    Remember that you need to be careful and security-aware when configuring S3 connection to Allas. The S3 keys are stored in a readable format in your home directory and anyone who can read your keys can access Allas until the keys are expilicitly revoked from Allas. Removing the keys from your own computer is not enough to deactivate them.

To check your S3 keys, open a connection to Puhti (or some other machine that can run `allas_conf` tool). If you don't yet have S3 connection to your Allas project activated, open it with commands:

```
module load allas
allas-conf -m S3
```

This creates a local configuration file that we will later on use to check some values.

Then switch to your Windows _Command Prompt_ and start the Rclone configuration process by executing command:

```bash
rclone config
```

And do following selections:

   1. Select **n** to create a _New remote_
   2. Name the remote as: **s3allas**
   3. From the list of storage protocols, select the number that defines: _Amazon S3 Compliant Storage Providers including AWS, Alibaba, Ceph, Digital Ocean, Dreamhost, IBM COS, Minio, and Tencent COS_
   4. Next you are asked to Choose your S3 provider. Select option that provides _Any other S3 compatible provider_
   5. Then select that you _Enter AWS credentials in the next step_ 
   6. Give the _AWS access key_. You can check this in Puhti with command: 
   `grep access_key $HOME/.s3cfg  | cut -d " " -f3`
   7. Give the _AWS secret access key_. You can check this in Puhti with command: 
   `grep secret_key $HOME/.s3cfg  | cut -d " " -f3`
   8. Region: **1**
   9. Endpoint: **a3s.fi**
   10. Location constant: (blank, just press Enter)
   11. acl: **1**
   12. Edit advanced config: **n**
   13. Remote config: **y** (yes, this is ok)
   14. **q**, quit config
 
After this you can access your Allas project using Rclone remote _s3allas_. For example:

```bash
rclone.exe lsd s3allas:
```

This connection stays active in your laptop until you delete it.
