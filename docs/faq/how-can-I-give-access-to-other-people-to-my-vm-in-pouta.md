# How can I give access to other people to my VM in Pouta?

When a [new VM is created](/cloud/pouta/launch-vm-from-web-gui/), a single default user is created automatically. And a single SSH key pair has given access to that default user in that VM. This gives access to that VM to a single person, the one that created the VM and the one that owns the SSH **private** key. See the Wikipedia [Secure Shell](https://en.wikipedia.org/wiki/Secure_Shell) article for more information about SSH keys and the protocol in general.

It is a common use case (and a good practice for production services) that more than one person has access to the VM. The following procedure is one of the several options to accomplish that. We will create a new user and give access to that user to a single person.

## Create a new user

1. [Connect to the VM](/cloud/pouta/connecting-to-vm/) as the default user. This user has superuser privileges (`sudo`).

1. Create the new user, see the [adduser](https://linux.die.net/man/8/adduser) manual for more information.

	```sh
	sudo adduser -m <user>
	```

!!! info "Substitute `<user>` by the username you want to create"

The user has been created in the VM, but nobody has access to it. To give access to this user, we need to configure the **Authorized Keys** for this account.

## Configure Authorized keys

Before you start, you will need a **public** ssh key. This public key must have been created by the new person that will be given access to this VM. When an SSH key pair is created, two keys are created, the **public** SSH key and the **private** key. The public one can be publicly published to the whole world, for example, GitHub publishes the keys of all its users. On the other hand, the **private** key must never be shared with anyone, and should not leave the computer where it was created.

### Create SSH key pair

It is recommended to create a new ssh key pair per user and service, this way if the **private** key is leaked, the damage is limited to that user in that service. If you use the same key for every VM, every one of them will be potentially compromised and will have to be recreated. In Linux and Mac you can create a new private/public key pair by doing:

```sh
$ ssh-keygen 
Generating public/private rsa key pair.
Enter file in which to save the key (/home/ubuntu/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/ubuntu/.ssh/id_rsa
Your public key has been saved in /home/ubuntu/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:9MKfQAUs+b2tmpXjqsa0DinzFbW+9qdpFAPYKh4P1i8 ubuntu@ab-tests
The key's randomart image is:
+---[RSA 3072]----+
|       =...      |
|      + +.       |
|     . ++o       |
|    = o=.o+      |
|   o =..S .=     |
|    ..Eo.+oo.    |
|  o oo.o..*.     |
|   + o+ .=oo.    |
|    .ooo===o     |
+----[SHA256]-----+
```

The example above created two files: `id_rsa` the **private** key, and `id_rsa.pub` the **public** key. For reference, a **public** ssh key looks like this:


```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCoQ9S7V+CufAgwoehnf2TqsJ9LTsu8pUA3FgpS2mdVwcMcTs++8P5sQcXHLtDmNLpWN4k7NQgxaY1oXy5e25x/4VhXaJXWEt3luSw+Phv/PB2+aGLvqCUirsLTAD2r7ieMhd/pcVf/HlhNUQgnO1mupdbDyqZoGD/uCcJiYav8i/V7nJWJouHA8yq31XS2yqXp9m3VC7UZZHzUsVJA9Us5YqF0hKYeaGruIHR2bwoDF9ZFMss5t6/pzxMljU/ccYwvvRDdI7WX4o4+zLuZ6RWvsU6LGbbb0pQdB72tlV41fSefwFsk4JRdKbyV3Xjf25pV4IXOTcqhy+4JTB/jXxrF
```

!!! info "The key above is [Linus Torvarld](https://github.com/torvalds.keys)'s public ssh key in github"

### Adding keys to `authorized_keys`

Once the new person has sent you the public key, you need to copy it to the server and add it to the `authorized_keys` "database" file:

1. Upload the public key file to the server, from a Linux or Mac machine you can use `SCP` (Secure copy protocol):

       ```sh
       scp id_rsa.pub <default_user>@<floating_ip>:
       ```

       Note: The `<default_user>` is still the one found in the [image documentation](/cloud/pouta/images/#images)

1. Make sure that the special SSH configuration directory exists:

	```sh
	mkdir -p ~<user>/.ssh
	```

	Again, substitute `<user>` with the username you just created. For example, for the user `pepe` the command would be: `mkdir -p ~pepe/.ssh`.

1. make a backup of the `authorized_keys` file (this is optional but recommended):

	```sh
	cp ~<user>/.ssh/authorized_keys ~<user>/.ssh/authorized_keys.$(date +%s)
	```

1. Add the public key to the `authorized_keys` file:

	```sh
	cat id_rs.pub >> ~<user>/.ssh/authorized_keys
	```
1. Make sure the permissions are right:

	```sh
	chmod 700 ~<user>/.ssh
	chmod 600 ~<user>/.ssh/authorized_keys
	```

1. Finally, check that the `authorized_keys` file looks like it should, with one public key per line.

The new person can now follow the [connecting to a VM](/cloud/pouta/connecting-to-vm/) article. The command (in Linux and Mac) should be something like the following:

```sh
ssh -i id_rsa <user>@<floating_ip>
```

## Give access to the same user to several public keys

It could be a good practice to give access to the same user at the same VM to more than one SSH key pair. For example, if the same person has different devices, each device will have a different private key, and if one of the devices gets lost, only one of the keys has to be deleted from `authorized_keys`. For this use case, it is possible to use the [ssh-copy-id](https://linux.die.net/man/1/ssh-copy-id) tool. This tool will only work if you already have access to that user at that VM.

```sh
ssh-copy-id -i ~/.ssh/id_rsa.pub <user>@<floating_ip>
```

The file `~/.ssh/id_rsa.pub` is the new SSH key to add.

!!! warning "Do not give access to the same user name to different people"
    It is not a good practice to give access to different people to the same user. This is because it makes it almost impossible to audit who and when connected to the VM.

