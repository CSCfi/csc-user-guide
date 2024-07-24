# Tools for client side encryption for Allas

Allas is not certified as high level security storage platform and thus you should not use it to store sensitive data in readable format.
However, sensitive data can be stored on Allas if it is properly encrypted before transfer to the object storage.

For sensitive data we generally recommend the [SD Connect service](../sensitive-data/sd_connect.md) that provides Web and command line interfaces 
that automatically encrypt the data when it is stored to Allas. 

If you for some reason don't want to use SD Connect, below you can find some alternative approaches for storing your sensitive data to Allas. When you use Allas with these encryption tools, remember that:
   
   1. You can store encrypted sensitive data in Allas, but are allowed to decrypt it only in environments with a high enough security level. For example, the CSC HPC environment (i.e. Puhti, Mahti, LUMI) is **not** secure enough for sensitive data.
   
   2. You should use strong enough encryption passwords and keep them safe.  
   
   3. If you forget the encryption password, the data is lost. CSC can't provide you a new password to read your data as the password was set by you, not CSC.
   
   
## 1. Encrypting a single file or directory with `a-put`
  
If you install [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils/) to the machine you are using, you can use `a-put` with option _--encrypt_ to encrypt the file or directory you want to upload to Allas. You can use either symmetric (i.e. password) encryption with [**gpg**](https://gnupg.org/) or asymmetric key based encryption with [**crypt4gh**](https://crypt4gh.readthedocs.io/en/latest/). Gpg is available in most linux systems while crypt4gh is not so widely used so you may need to install it to your local system if you wish to use asymmetric encryption.

Note, that by default `a-put` creates an additional metadata object that contains information about the uploaded files. When _--encrypt_ option is used, the actual data content will be encrypted, but the metadata objects (the _\_ameta_ files) will not be encrypted. In cases where the file names should not be stored in readable format, you should turn off the metadata object creation by using `a-put` with option _--no-ameta_.


### Symmetric gpg encryption

Symmetric gpg encryption can be executed with command:
 
```text
a-put --encrypt gpg data_dir -b my_allas_bucket
``` 
When option _--encrypt gpg_ is in use the data is encrypted with `gpg` command using _AES256_ encryption algorithm, that generally considered good enough for sensitive data. When you launch the command it will ask for encryption password, and password confirmation. In this approach only the content of the file or directory is encrypted. Object name and metadata remain in human readable format. 

When you retrieve the data with `a-get`, you will be asked for the encryption password so that the object can be decrypted after download.

```text
a-get my_allas_bucket/data_dir.tar.zst.gpg
```

### Asymmetric crypt4gh encryption

If you want to use asymmetric `crypt4gh` encryption, you need to have a public key file for encryption and a secret key file for decryption.
In Puhti, you first need to make `crypt4gh` available with the command:
```text
module load allas
```
Now you can create keys with a command like: 
```text
crypt4gh-keygen --sk allaskey.sec --pk allaskey.pub
```
Data can now be uploaded to Allas with command:
```text
a-put --encrypt c4gh --pk allaskey.pub data_dir -b my_allas_bucket
```
The command above first encrypts the data using `crypt4gh` and the public key and then uploads the encrypted data to Allas. Note, that you don't need the secret key for encryption. You can deliver the public key to a another server (and to another user) so that data can be securely uploaded to Allas from an external secure location. Secret key is needed only in the environment where to data is downloaded to from Allas:
```text
a-get --sk allaskey.sec my_allas_bucket/data_dir.tar.zst.c4gh
```
The command above will download the encrypted object from Allas, ask for the password of the secret key and the unpack then data into readable files. 


## 2. Creating encrypted repository with rclone
 
`rclone` has a client side encryption feature that allows you create an encrypted data repository to Allas. In this approach, you need to once define an encrypted `rclone` connection to Allas, and when this connection is used, all the transported data will be automatically encrypted. The automatic encryption of `rclone` is based on the _Salsa20_ stream cipher. Salsa20 is not as widely used as AES256, but it is one of the encryption tools that were recommended by the European [eSTREAM](https://www.ecrypt.eu.org/stream/) project.

In the example here, we assume that you are using a server where you have [rclone](https://rclone.org/) and [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils/) installed. First, you have to configure a normal, un-encrypted swift-connection to Allas. This can be done with the `allas-conf` script that is included in _allas-cli-utils_ package:
```text
source allas-cli-utils/allas_conf -u your-csc-username -p your-csc-project-name
```

Once you have configured a normal swift connection to Allas, you can configure an encrypted bucket to your Allas area. To start the configuration process, run command `rclone config`. 

The `allas-conf` script has already created an `rclone` configuration file with `rclone remote` named as _allas_.

As the first step, choose option: _n_ to create a _new remote_.
The configuration process will ask for a name for the new rclone _remote_.
In this case, the new remote is named as named as _allas-crypt_.

<pre>
[kkayttaj@puhti-login11 ~]$ <b>rclone config</b>
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
In the next step you need to define the Allas bucket, that will be used for encrypted data. When defining the bucket, note that you 
have to define both the bucket and the site (i.e. rclone remote connection name) where the bucket locates. 
In the case of Allas, the remote name is _allas:_. The actual bucket name should be unique among all Allas users. 
In this case we use definition _allas:2001659-crypt_ that defines that the encrypted data will be stored to Allas to bucket _2001659-crypt_.
<pre>
Remote to encrypt/decrypt.
Normally should contain a ':' and a path, eg "myremote:path/to/dir",
"myremote:bucket" or maybe "myremote:" (not recommended).
Enter a string value. Press Enter for the default ("").
remote> <b>allas:2001659-crypt</b>
</pre>
Next, the configuration process asks if the object and directory names are encrypted. In this case we will encrypt the names, so you choose _1_ for both cases.

After that, you need to define two passwords: a main password and a so called _salt password_. This password pair will be used for the encryption. You can define these passwords yourself or you can let the configuration process to create them. In any case, store securely the passwords you have used. Other users and servers may need to use them, too. Now the setup is ready and there is now a new rclone remote called _allas-crypt_ defined. You can now exit the configuration process.

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
[kkayttaj@puhti-login11 ~]$ <b>ls job_6</b>
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

The `allas-crypt remote` translates the data from the encrypted bucket (allas:2001659-crypt) automatically into readable format. However, if you study the content of the encrypted bucket directly, you can see that the object names, as well as the stored data, are in encrypted format:

<pre>[kkayttaj@puhti-login11 ~]$ <b>rclone ls allas:2001659-crypt</b>
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
Would download and un-encrypted file _hello.xrsl_ from Allas to the local disk.

The configuration of the Allas connections is by default stored to the rclone configuration file in `$HOME/.config/rclone/rclone.conf`

In this case the _allas-crypt_ defining part in the configuration file could look like:
```text
[allas-crypt]
type = crypt
remote = allas:2001659-crypt
filename_encryption = standard
directory_name_encryption = true
password = A_JhQdTOEIx0ajyWb1gCvD2z0gBrEVzy41s
password2 = UgmByNqlnb8vCZrFgpaBtUaQrgJkx30
```
The configuration as such is not linked to any specific server or user account. The connection to the encrypted bucket could be opened by anyone who has 1) access to the Allas project and 2) has the same settings (including the passwords) in their own rclone configuration file. This is handy in cases where you need an encrypted data storage that can used by several trusted persons and sites. However, this causes potential security concerns as the same passwords are used by several users. Further, in the configuration file the passwords are only _obscured_ but not encrypted.

To enhance security, the `rclone` configuration file can be encrypted. This can be done by running `rclone conf` command again.
In this case select _s_ to go to _Set configuration password_ and then _a_ to add a password. Setting the password has two effects:

  1. The `rclone` configuration file is converted to an encrypted format
  2. Each time you execute an `rclone` command, you must give the configuration file password, so that `rclone` can read the settings.

The second feature can be quite annoying, especially if you mostly use the normal, non-encrypted Allas connection. Because of this, it can be more reasonable to create a separate rclone configuration file for the encrypted Allas usage and then, when encryption is needed, define the usage of encrypted configuration file with rclone option _--config_.

For example:

Make a copy of the existing `rclone` configuration file (before you define the encrypted connection described above).

```text
cp $HOME/.config/rclone/rclone.conf $HOME/rc-encrypt.conf
```
Then run the `rclone config` command to add the information of the encrypted Allas bucket and then to encrypt the configuration file. You can do the both two steps in one `rclone config` session.
```text
rclone config --config $HOME/rc-encrypt.conf
```
The configuration file encryption key can and should be personal. 

Now you can use your protected configuration file with `rclone` command. For example:

```text
rclone copy --config $HOME/rc-encrypt.conf job_6 allas-crypt:job_6
```


## Restic - Backup tool that includes encryption

[Restic](https://restic.net/) is a backup program that can use Allas as storage space for the backuped data. In stead of importing the data directly, `restic` stores the data as a collection hash. This feature enables effective storage of datasets that include small changes. Thus, different versions of a dataset can be stored so that in the case of a new dataset version, only the changes compared to the previous version needs to be stored. This approach also enables retrieving not just the latest version, also earlier versions of the backuped data. 

In addition to hashing, `restic` encrypts the data using AES256 cipher. The Allas specific backup tool, `allas-backup` (available in Puhti and Mahti) is based on `restic` but it uses a fixed pre-defined encryption password and thus it should not be used, if high security level is required. In those cases you can use `restic` directly.

To use Allas as the storage place for `restic`, first open a connection to Allas. When you start using `restic` for the first time, you must set up a `restic` repository.
The repository definition includes a protocol (`swift` in this case), location that is the bucket name in the case of Allas, and a prefix for the stored data objects. For example: 
<pre><b>restic init --repo swift:123_restic:/backup</b>
enter password for new repository: <b>************</b>
enter password again: <b>************</b>

created restic repository a70df2ced1 at swift:123_restic:/backup

Please note that knowledge of your password is required to access
the repository. Losing your password means that your data is
irrecoverably lost.
</pre>

The initialization process asks for an encryption password for the repository. 

Now, you can backup a file or directory to the Restic repository in Allas. In the example below a directory _my_data_ is backuped.

<pre> <b>restic backup --repo swift:123_restic:/backup my_data/</b>
enter password for repository: <b>************</b>
repository a70df2ce opened successfully, password is correct
created new cache in /users/kkayttaj/.cache/restic

Files:         258 new,     0 changed,     0 unmodified
Dirs:            0 new,     0 changed,     0 unmodified
Added to the repo: 2.018 MiB

processed 258 files, 2.027 MiB in 0:00
snapshot a706c054 saved
</pre>

After modifying one file in _my_data_ directory we do a second backup:
<pre><b>restic backup --repo swift:123_restic:/backup my_data/</b>
enter password for repository: <b>************</b>
repository a70df2ce opened successfully, password is correct

Files:           0 new,     1 changed,   257 unmodified
Dirs:            0 new,     0 changed,     0 unmodified
Added to the repo: 1.154 KiB

processed 258 files, 2.027 MiB in 0:00
snapshot e3b46fe2 saved
</pre>

With command `restic sanpshots` we can see that we have two versions of my_data in the backup repository:

<pre><b>restic snapshots --repo swift:123_restic:/backup</b> 
enter password for repository: <b>************</b>
repository a70df2ce opened successfully, password is correct
ID        Time                 Host          Tags        Paths
-------------------------------------------------------------------------------------------
a706c054  2021-02-12 14:43:03  r07c52.bullx              /run/nvme/job_4891841/data/my_data
e3b46fe2  2021-02-12 14:47:18  r07c52.bullx              /run/nvme/job_4891841/data/my_data
-------------------------------------------------------------------------------------------
2 snapshots
</pre>

If we would like to get back the first version, we could download it with snapshot id and command `restic restore`.

<pre><b>restic restore --repo swift:123_restic:/backup a706c054 --target ./ </b>
enter password for repository: <b>************</b>
repository a70df2ce opened successfully, password is correct
found 3 old cache directories in /users/kkmattil/.cache/restic, run `restic cache --cleanup` to remove them
restoring <Snapshot a706c054 of [/run/nvme/job_4891841/data/my_data] at 2021-02-12 14:43:03.215110283 +0200 EET by kkayttaj@r07c52.bullx> to ./
</pre>

The actual data is stored as encrypted hash objects that are usable for other Allas tools. For example, the data that was stored by `restic` to bucket
_123_restic_ in the example above loos like below, when listed with `rclone`:
```
rclone ls allas:123_restic
      155 backup/config
     1349 backup/data/26/263a8a412486d0fe6278ec1992c3b2dc64352041ca4236de0ddab07a30e7f725
  2133179 backup/data/46/4643d0d98ef90363629561828a3c113c2ca1acbdefcd3ef0f548724501c1e8f3
   108646 backup/data/77/77f36c6b6f7b346010d76e6709c8e3e4a61a7bc25dce4ffee726fe2a9b208e48
      895 backup/data/b7/b757b4f8b370a3f7199d717128f8bcb90139c589b761d2d6e683cbb3943c32e9
      550 backup/index/3b824311bf222eb9131e83dc22b76ee1686a41deff8db73912a6ec4b58ec7c9c
    32326 backup/index/9e7e8858bc9e8cdcd96f7020ad9f1246629e3a80b2008c1debec30ac21c2b717
      458 backup/keys/9f47c0adcdaa29d1e89eab4763fbcf9269c834b6590b45fd9a0ac079e2ee483e
      272 backup/snapshots/a706c054a77edba31337669ebd851c80f34dfbc3ca92255dee1ff0c0cad8cedf
      348 backup/snapshots/e3b46fe293fae187a53296f8cde25f7aec9f896e4586d96ac4df78ba27cdd911
```



