# Using Allas and Lumi-O object storage services in Roihu


Object storage related tools are initialized in Roihu with command:

```text
module load allas
```
The allas module enables command:

```text
allas-conf    
```

that is used to configure connections to [Allas](../../data/Allas/index.md) and [Lumi-O](https://docs.lumi-supercomputer.eu/storage/lumio/) object storage services. 

In addition this module brings available a set of command line tools that can be used to operate with Allas and Lumi-O object storage services. These tools include:

    [a-commands]  (https://docs.csc.fi/data/Allas/using_allas/a_commands/)
    Rclone (https://docs.csc.fi/data/Allas/using_allas/rclone/)
    s3cmd  (https://docs.csc.fi/data/Allas/using_allas/s3_client/)
    s5cmd
    aws s3 (https://docs.aws.amazon.com/cli/latest/reference/s3/)
    swift (https://docs.csc.fi/data/Allas/using_allas/swift_client/)
    allas-backup and restic  (https://docs.csc.fi/data/Allas/using_allas/a_backup/)


Configuring connections with allas-conf

allas-conf can be used to configure S3 based connections to Lumi-O and Allas and swift based connections to Allas. Note that  in  Roihu allas-conf now by default configures an S3 based connection to Allas, unlike to Puhti and Mahti where swift is used by default.


S3 connection to Allas

You can define a new S3 connection to Allas with command:

    allas-conf  project_proj-number

or

    allas-conf

First allas-conf asks you to give your CSC password.  After that, if target project is not given as an argument, it lists all available Allas projects and asks user to pick one.  ( Note that allas-conf has often problems with passwords that have characters that have special meaning in bash shell.  For example space, *,  ;  and different quotation marks can cause allas-conf to fail).

The project specific access key pair is stored to to the configuration files of aws, s3cmd a rclone in your home directory. Due to this the configuration is not session specific, but applies to all  sessions that utilize aws, s3cmd, rclone and a-commands. S3 keys are permanent so you need to run allas-conf command again only when you wish to set a new default S3 connection in use. Thus, in case of S3 based Allas usage, you normally need just to load the Allas module and then start using Allas.  

In case of aws and s3cmd, only one connection is defined and running allas-conf overwrites the old default connections.  

In case of rclone, two endpoints are defined s3allas: and s3allas_project-proj-number. Both endpoints refer to the same Allas project. When a new project is defined with allas-conf, a3allas: endpoint is changed to refer to the new project, but the older project specific endpoint is preserved in addition to the new project specific endpoint that gets generated. 

For example after  commands

    allas-conf project_200111
    allas-conf project_200222
    
Following connections are in use:

a-commands, aws and s3cmd			project_200222
rclone s3allas:  				project_200222
rclone a3allas_project_200111:  		project_200111
rclone a3allas_project_200222:  		project_200222



Swift connection to Allas

In Puhti and Mahti a-commands, rclone and allas-backup used by default swift based connections. In Roihu you can define swift based Allas connection with command: 
    allas-conf --swift
This connection is session specific and valid only for 8 hours. After the connection is activated, rclone endpoint allas: provides swift based connection to Allas.
A-commands need extra option  --swift to use swift based Allas connection

    a-list --swift
Note that in a terminal session, S3 based a-list and Swift based a-list --swift may refer to different Allas projects.

Swift configuration has no effect on aws and s3cmd commands as they use only S3 protocol. 

S3 connections to Lumi-O

Connections to Lumi-O are defined with command:

    allas-conf --lumi

The configuration process asks you to login  to https://auth.lumidata.eu  where you can create an access key pair for your Lumi-project. You can the copy the project name, access key and secret key to the configuration process in Roihu.

Lumi connections use always S3 protocol and this configuration process changes aws and s3cmd commands to use the Lumi-O project as the default project.  In case of a-commands you can add option --lumi  to the command in order to make use Lumi-o. For example:

   a-list --lumi

In the case of rclone four new endpoints are created. 
    • lumi-o: and  lumi-proj-number-private: refer to the non-public area of the Lumi-O project
    • lumi-pub: and  lumi-proj-number-public: to the public are of the Lumi-O project.
In the same way as in the case of S3 connections to Allas, executing Lumi-O configuration to a new project, changes the target project of a-commands, aws, s3cmd as well as lumi-o: and lumi-pub: endpoints but preserves the long endpoint names that include the project numbers.

Note that the Lumi-O keys have a validity time, defined in the authentication interface. Thus you may need to update the connection configuration every now and then.



