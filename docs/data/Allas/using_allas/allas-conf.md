# Allas connection configuration

The easiest general option to set up Allas connection configuration is to use `allas-conf` tool:

* Sets up connection configuration for many different tools
* Swift or S3 connection
* Is itself a command-line tool. 
* Available on CSC supercomputers
* Can be installed to Linux and Mac, but not Windows.
* Suits well, if only one CSC project at a time in use for Allas.

Alternatively, one can use [Roihu web interface](../../../computing/webinterface/file-browser.md#accessing-allas-and-lumi-o):

* Sets up connection configuration for web interface file section and `rclone`, but not other Allas clients.
* Swift or S3 connection
* Available in web-interface, so no installations needed for using it, but the CSC project must have Roihu service enabled.


## `allas-conf` availability

Available on CSC supercomputers with **allas** module. Can be (installed)[allas-conf-installation] to Linux and Mac, but not Windows.

```text
module load allas
```
When you load the Allas module in Roihu, it lists you the status of currently configured Allas and Lumi-O connections.
You can check this information later on with command:

```text
check-allas-connections
```

## Using `allas-conf` to configure connections to Allas, SD-Connect and Lumi-O

### S3 connection to Allas

To enable S3 based connection to Allas in Roihu, use command `allas-conf`.  

```text
allas-conf 
```

In Puhti and Mahti you must add option `-m S3`
```text
allas-conf -m S3
```

The authentication process asks you to give the password of your CSC account. Note that the Haka password or password related to you ssh key 
are not valid in this authentication step.

Once S3 connection is configured, same authentication is used for all login sessions and it does not have an expiration time.

`allas-conf` generates configuration files in S3 mode for: 
* `rclone`: `.config/rclone/rclone.conf`
* `s3cmd`: `~/.s3cfg`
* `aws`: credentials and S3 region in `~/.aws/credentials` and S3 endpoint in `~/.aws/config` files.

Additionally, Python 'boto3' and R 'aws.s3' libraries use 'aws' configuration files.

If you use these keys in other services, your should make sure that the keys always remain private. Any person who has access to these two keys, can access and modify all the data that the project has in Allas.

If needed, you can deactivate an S3 key pair with command:

```
allas-conf --s3remove
```

!!! Note
    Remember to be careful and security-aware when configuring S3 connection to Allas. The S3 keys are stored in a readable format in your home directory and anyone who can read your keys can access Allas until the keys are expilicitly revoked from Allas. Removing the keys from your own computer is not enough to deactivate them.



### SWIFT connection to Allas

Swift connection is valid for up to **eight hours**

Configure Allas access using Swift protocol:
```text
allas-conf --swift 
```
The `allas-conf` command prompts for your CSC password (University/Haka password will not work here). It lists your Allas projects and asks you to define a project (if not already defined as an argument). 

By default, `allas-conf` lists your projects that have access to Allas, but if you know the name of the project, you
can also give it as an argument:
```text
allas-conf project_201234
```

`allas-conf --swift` enables you to use only one Allas project at a time in one session. You can switch to another project by running `allas-conf` again.

Note that the Allas project does not need to be the same as the project you are using in Roihu.

`allas-conf --swift` generates Swift configuration files for : `a-tools, `rclone` and `swift`.

The authentication information is stored in the `OS_AUTH_TOKEN` and `OS_STORAGE_URL` environment variables. However, you can refresh the authentication at any time by running `allas-conf` again. The environment variables are set only for the current login session, so you need to configure authentication individually for each shell with which you wish to access Allas.

If you are running big, multistep processes (e.g. batch jobs), it may be that your data management pipeline takes more than eight hours. In those cases you can add option `-k` to the `allas-conf` command.
```text
allas-conf -k
```
With this option on, the password is stored into environment variable OS_PASSWORD. A-commands recognize this environment variable and when executed, automatically refresh the current Allas connection.

### S3 connection to Lumi-O

You can configure Lumi-O connection with command:

```text
allas-conf --lumi
```
The configuration process asks you to retrieve your Lumi project number and keys from [Lumi-O Credentioals Management Service Page](https://auth.lumidata.eu/). Note that configuring Lumi-O connection this way overwrites the configuration files that `aws s3` and `s3cmd` commands use.
In the case of `rclone` previosly defined Allas connections remain still active.

### Connection to SD Connect service

You can configure SD Connect connection with command:

```text
allas-conf --sdc
```

The authentication process asks you to give the password of your CSC account. Note that the Haka password or password related to you ssh key 
are not valid in this authentication step. Once you have selected the SD Connect project you wish to use, the configuration process asks you to copy an API-token from [SD Connect web interface](https://sd-connect.csc.fi). Not that in SD Connerct, you must create the API-token using the same project that you seleted in the beginning of this configuration process.




## `allas-conf` installation 

`allas-conf` can be installed only to Linux or Mac. 

1. Download the `allas_conf` script to set up the connection to your Allas project: `wget https://raw.githubusercontent.com/CSCfi/allas-cli-utils/master/allas_conf`
2. Install Rclone for Swift connection OR [OpenStack client](https://pypi.org/project/python-openstackclient/) for S3 connection

If running `allas_conf` locally, you should modify all of the commands above with:

* Add `source` the beginning
* Use `--user` option to define your CSC username .

For example:

```bash
source allas_conf --user your-csc-username -p your-csc-project-name
source allas_conf --user your-csc-username -p your-csc-project-name -m S3
source allas_conf --user your-csc-username -p csc-project-name --s3remove
source allas_conf --user your-csc-username --lumi
source allas_conf --user your-csc-username --sdc
```

## S3 connection details

To use Allas with S3 on a machine where `allas-conf` is not available or with tools not directly supported, usually the following information is needed:

* S3 credentials: access key and secret key
* S3 endpoint: `a3s.fi` or `https://a3s.fi`
* S3 region: sometimes no settings needed, sometimes leave empty (````)

The easiest way to get the S3 credentials is by configuring an [S3 connection](#s3-connection-to-allas) on a CSC supercomputer (or some other machine that can run `allas_conf` tool) and see the keys from the printout of the command. 

```
module load allas
allas-conf -m S3
```

Later the keys can be found for example with: `less ~/.aws/credentials`

If you wish to access Allas from a personal laptop or some other server with `s3cmd` or `aws` command-line tools, you can also copy the setting files as such. [Use any file transfer tool](../../moving/index.md), for example `scp`.

* `aws`: copy the `~/.aws`-folder to your home directory to `C:\Users\username\.aws` on Windows or `~/.aws/` on Mac and Linux.
* `s3cmd`: copy the `~/.s3cfg`-file to your home directory on Mac and Linux.

