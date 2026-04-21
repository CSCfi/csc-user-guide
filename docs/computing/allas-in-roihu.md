# Using Allas and Lumi-O object storage services in Roihu


Object storage related tools are initialized in Roihu with command:

```text
module load allas
```
The allas module enables command: **allas-conf** that is used to configure **S3* connections to [Allas](../data/Allas/index.md) and [Lumi-O](https://docs.lumi-supercomputer.eu/storage/lumio/) object storage services and *Swift* based connections to Allas. Note that in Roihu _allas-conf: by default configures an S3 based connection to Allas, unlike to Puhti and Mahti where swift is used by default.

In addition this module brings available a set of command line tools that can be used to operate with Allas and Lumi-O object storage services. These tools include:

   * [a-commands](../data/Allas/using_allas/a_commands.md)
   * [Rclone](../data/Allas/using_allas/rclone.md)
   * [s3cmd](../data/Allas/using_allas/s3_client.md)
   * [aws s3](https://docs.aws.amazon.com/cli/latest/reference/s3/)
   * [swift](../data/Allas/using_allas/swift_client/)
   * [allas-backup](../data/Allas/using_allas/a_backup/) and restic

You can check current object storage connections with command:

```text
check-allas-connections
```

### S3 connection to Allas

You can define a new S3 connection to Allas with command:

```text
allas-conf  project_proj-number
```
or

```text
allas-conf
```

First allas-conf asks you to give your CSC password (Haka-password can't be used here).  After that, if target project is not given as an argument, it lists all available Allas projects and asks user to pick one. ( Note that allas-conf has often problems with passwords that have characters that have special meaning in bash shell.  For example space, *,  ;  and different quotation marks can cause allas-conf to fail).

The project specific access key pair is stored to to the configuration files of *aws*, *s3cmd* a *rclone* in your home directory. Due to this the configuration is not session specific, but applies to all sessions that utilize aws, s3cmd, rclone and a-commands. S3 keys are permanent so you need to run allas-conf command again only when you wish to set a new default S3 connection in use. Thus, in case of S3 based Allas usage, you normally need just to load the Allas module and then start using Allas.  

In case of **aws** and **s3cmd**, only one connection is defined and running allas-conf overwrites the old default connections.  

In case of **rclone**, two endpoints are defined **s3allas:** and **s3allas-project-_proj-number_**. Both endpoints refer to the same Allas project. When a new project is defined with allas-conf, a3allas: endpoint is changed to refer to the new project, but the older project specific endpoint is preserved in addition to the new project specific endpoint that gets generated. 

For example after commands:

```text
allas-conf project_200111
allas-conf project_200222
```

Following connections are in use:

| Tool                           | Target project |
|--------------------------------|----------------|
| a-commands, aws and s3cmd	     | project_200222 |
| rclone s3allas:                | project_200222 |
| rclone a3allas-project200111:  | project_200111 |
| rclone a3allas-project_200222: | project_200222 |

And with these settings all the commands below list the Allas buckets of project 200222.

```txt
a-list
rclone lsd s3allas:
rclone lsd a3allas-project_200222:
s3cmd ls s3://
aws s3 ls
```

### Swift connection to Allas

In Puhti and Mahti a-commands, rclone and allas-backup used by default swift based connections. In Roihu you can define Swift based Allas connection with command:

```text
allas-conf --swift
```

This connection is session specific and valid only for 8 hours. After the connection is activated, rclone endpoint **allas:** provides Swift based connection to Allas. For example:

```text
rclone lsd allas:
```

A-commands need extra option `--swift` to use Swift based Allas connection. For example:

```text
a-list --swift
```

Note that in a terminal session, S3 based `a-list` and Swift based `a-list --swift` may refer to different Allas projects.

Swift configuration has no effect on aws and s3cmd commands as they use only S3 protocol. 


### S3 connections to Lumi-O

Connections to Lumi-O are defined with command:

```text
allas-conf --lumi
```

The configuration process asks you to login to [https://auth.lumidata.eu](https://auth.lumidata.eu)  where you can create an access key pair for your Lumi-project. You can then copy the _project name_, _access key_ and _secret key_ to the configuration process in Roihu.

Lumi-O connections use always S3 protocol and this configuration process changes *aws* and *s3cmd* commands to use the Lumi-O project as the default project.  In case of *a-commands* you can add option `--lumi`  to the command in order to make use Lumi-o. For example:

```text
a-list --lumi
```

In the case of rclone four new endpoints are created. 

   * **lumi-o:** and  **lumi-_proj-number_-private:** refer to the non-public area of the Lumi-O project
   * **lumi-pub:** and  **lumi-_proj-number_-public:** to the public are of the Lumi-O project.
     
In the same way as in the case of S3 connections to Allas, executing Lumi-O configuration to a new project, changes the target project of a-commands, aws, s3cmd as well as lumi-o: and lumi-pub: endpoints but preserves the long endpoint names that include the project numbers.

Note that the Lumi-O keys have a validity time, defined in the authentication interface. Thus you may need to update the connection configuration every now and then.



