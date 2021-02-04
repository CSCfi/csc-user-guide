# Tools for client side encryption for Allas

Allas is not certified as high level security storage platform and thus you should not use it to store sensitive data in readable format.
Howerver, sensitive data can be stored to Allas if it is properly encrypted before data is transported to Allas

This document describes some password based (symmetric) encryption tools that help you to move your sensitive data to Allas so that data gets encrypted before it leaves your local environment. When you use Allas with these encryption tools, remember that:
   1. You can only store the encrypted data in Allas, but not open it there or in the HPC environment of CSC. 
   2. You should use strong enough passwords and keep them safe
   3. If your forget the encryption password, the data is lost. CSC can't provide you a new password to read your data as the password is set by the users, not CSC.
   
   
  ## 1. Encrypting single file or directory with a-put
  
In you install [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils/) to the machine you are using, you can use a-put with option _--encrypt_ to encrypt the file or directory you want to upload to Allas. For example:
 
```text
a-put --encrypt data_dir -b my_allas_bucket
``` 
With the _--encrypt_ option on the data is encrypted with _gpg_ command using _AES256_ encryption algorithm. When you launch the command it will ask for encryption password, and password confirmation. In this approach only the content of the file or directory is encrypted. Object name and metadata remain in human readable format. 

When you retrieve the data with _a-get_ command, you will be asked for the encryption password so that the object can be decrypted after download.

 ## 2. Creating encrypted reposoitury with rclone
 
Rclone has client side encryption feature, that allows you create an encrypted data repository to Allas. In this approach you need to once define an encrypted rclone connection to Allas and when this connection is used, all the transported data will be automatically encrypted.

In the exaple here, we assume that you are using a server where you have [rclone](https://rclone.org/) and [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils/) installed. First you have to configure a normal, un-encrypted swift-connection to Allas. This can be done with the _allas_conf_ script that is included in _allas-cli-utils_ package:
<pre>
source allas-cli-utils/allas_conf -u <i>your-csc-username</i> -p <i>your-csc-project-name</i>
</pre>

Once you have configured a normal swift connection to Allas, you can configue an encrypted bucket to your Allas area. To start the configuration process, run command _rclone config_. 

The _allas_conf_ script has already created an rclone configuration file with _rclone remote_ named as _allas_.

As first step, choose opion: _n_ to create a _new remote_.
The configuration process will ask for a name for the new rclone _remote_.
In this case, the new remote is named as named as _allas-crypt_.

<pre>
[kkayttaj@puhti-login1 ~]$ <b>rclone config</b>
Current remotes:

Name                 Type
====                 ====
allas                swift

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q> <b>n</b>
name> <b>allas-crypt</b>
</pre>
Next the configuration process asks you to configure storage type.
Choose option 10 _Encrypt/Decrypt a remote_.
<pre>
Storage> <b>10</b>
</pre>
In the next step you need to define the bucket that will be used for encrypted data. 
Note that the bucket name should be unique among all Allas users. This case we use bucket name _allas:2001659-crypt_
<pre>
Remote to encrypt/decrypt.
Normally should contain a ':' and a path, eg "myremote:path/to/dir",
"myremote:bucket" or maybe "myremote:" (not recommended).
Enter a string value. Press Enter for the default ("").
remote> <b>allas:2001659-crypt</b>
</pre>
Next, the configuration process asks if the object and directory names are encrypted. In this case we will encrypt the names so you choose _1_ for both cases.

After that you need to define two passwords, a main password and a so called _salt password_. This password pair will be used for the encryption. You can define these passwords yourself or you can let the configuration process to create them. In any case, store seucurely the passwords you have used. Other users and servewrs may need to use them too. Now the setup is ready an there is now a new rclone remote called _allas-crypt_ defined. You can now exit the configuration process.

Current remotes:
<pre>
Name                 Type
====                 ====
allas                swift
allas-crypt          crypt

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q><b>q</b>
</pre>
 
Now the repository is ready to be used. Say, you have a directory called _job_6_ containing some files and directories:
<pre>
[kkayttaj@puhti-login1 ~]$ <b>ls job_6</b>
hello.xrsl  results  results.1601291937.71  runhello.sh
</pre>

You can now upload the content of this directory to the encrypted bucket.
```text
rclone copy job_6 allas-crypt:job_6
```
The data has now been copied to Allas and you can check the uploaded files with command:
<pre><b>rclone ls allas-crypt:job_6</b>
       77 runhello.sh
       11 results.1601291937.71/std.out
       86 results.1601291937.71/std.err
      117 hello.xrsl
       11 results/std.out
       86 results/std.err
 </pre>

The allas-crypt remote translates the edata from the encrypted bucket (allas:2001659-crypt) automatically into readable format. However if you study the content of the encrypted bucket directly, you can see that the object names, as well as the stored data, are in encrypted format:

<pre>[kkayttaj@puhti-login3 ~]$ <b>rclone ls allas:2001659-crypt</b>
      125 4lpbj55pc5v8t119q0tp2o6k58/36sb832och3tde30k9nlks3dpo
       59 4lpbj55pc5v8t119q0tp2o6k58/90alcaodph3386197agf252t5b97f144n88e99m9ire5tcpqu380/flqitnrsrc8iloggbc4ouagukg
      134 4lpbj55pc5v8t119q0tp2o6k58/90alcaodph3386197agf252t5b97f144n88e99m9ire5tcpqu380/gvie6dv3s50v32qptl30960me4
      405 4lpbj55pc5v8t119q0tp2o6k58/a6rlk2hr489roehagfu6iest38
      165 4lpbj55pc5v8t119q0tp2o6k58/kmqnruv14agevg6okod0io2fl0
       59 4lpbj55pc5v8t119q0tp2o6k58/o515vd0l1bp270v7gdc7m3tpbo/flqitnrsrc8iloggbc4ouagukg
      134 4lpbj55pc5v8t119q0tp2o6k58/o515vd0l1bp270v7gdc7m3tpbo/gvie6dv3s50v32qptl30960me4
      352 4lpbj55pc5v8t119q0tp2o6k58/p87n5ins7g0hvfh06r6o6a91n0
</pre>

Similarly, command:
```text
rclone copy allas-crypt:job_6/hello.xrsl ./
``` 
Would download and un-encrypt file _hello.xrsl_ from Allas to the local disk.

The configuration of the Allas connections is by default stored to the rclone configuration file in $HOME/.config/rclone/rclone.conf

In this case the :allas-crypt_ defining part in the configuration file could look like following:
```text
[allas-crypt]
type = crypt
remote = allas:2001659-crypt
filename_encryption = standard
directory_name_encryption = true
password = A_JhQdTOEIx0ajyWb1gCvD2z0gBrEVzy41s
password2 = UgmByNqlnb8vCZrFgpaBtUaQrgJkx30
```
The configuration as such is not linked to any specific server or user account. The connection to the encrypted bucket could be opened by anyone who has 1) access to the Allas project and 2) has the same settings (including the passwords) in their own rclone configuration file. This is handy in cases were you need an encrypted data storage that can used by several trusted persons and sites. However, this causes potential security concern as the same passwords are used by several users. Further, in the configuration file the passwords are only _obscured_ but not encrypted.

To enhance the security the rclone configuration file can be encrypted. This can be done by running _rclone_conf_ command again.
In this case select _s_ to go to _Set configuration password_ and then _a_ to add a password. Setting the password has two effects:

  1. the rclone configuration file is converted to an encrypted format
  2. each time you execute an rclone command, you must give the configuration file password, so that rclone can read the settings.

The second feature can be quite annoying, especially if you mostly use the normal, non-encrypted Allas connection. Because or that it can be more reasonable to create a separate rclone configuration file for the encrypted Allas usage and then, when encryption is needed, define the usage of encrypted configuration file with rclone option _--config_.

For example:

Make a copy of existing rclone cofiguration file (before you define the encrypted connection described above).

```text
cp $HOME/.config/rclone/rclone.conf $HOME/rc-encrypt.conf
```
Then run the _rclone config_ command to add the information of the encrypted Allas bucket and then to encrypt the configuration file. You can do the both two steps in one _rclone config_ session.
```text
rclone config --config $HOME/rc-encrypt.conf
```
The configuration file encryption key can and should be personal. 

Now you can use your protected configuration file with rclone command. For example:

```text
rclone copy --config $HOME/rc-encrypt.conf job_6 allas-crypt:job_6
```





