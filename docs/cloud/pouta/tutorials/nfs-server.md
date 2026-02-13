In this section, we will learn how to set up a NFS server on cPouta.

We will demonstrate a simple tutorial on how to create your NFS server with two services:

- [NFS Kernel Server](https://documentation.ubuntu.com/server/how-to/networking/install-nfs/#)
- [NFS Ganesha](https://github.com/nfs-ganesha/nfs-ganesha)

## NFS Kernel Server

### Server side

!!! Note  
    The following commands were executed on Ubuntu 24.04 and AlmaLinux 9.

1. [Create and attach a volume on your machine](../persistent-volumes.md#creating-and-attaching-a-volume-in-the-pouta-web-interface), then [use the volume into your machine](../persistent-volumes.md#using-attached-volumes). For our example, the mount point will be named `/srv/nfs4`

1. Update the system and install the `nfs-kernel-server` package. For Ubuntu, run

    ```
    sudo apt update && sudo apt upgrade -y
    sudo apt install nfs-kernel-server -y
    ```

    For AlmaLinux, run

    ```
    sudo dnf install -y nfs-utils
    ```

1. Enable the service

    ```
    sudo systemctl enable --now nfs-server
    ```

1. Edit `/etc/exports` and add this line:

    ```
    /srv/nfs4 192.168.1.0/24(rw,fsid=0,no_subtree_check,crossmnt)
    ```

    - `rw`: allow read and write
    - `fsid=0`: designate the exported root (mandatory for NFSv4).
    - `no_subtree_check`: disable the verification of the exported subtree (recommended)
    - `crossmnt`: allow the NFS server to include the nested mount points within the exported directory, so clients can access the mounted file systems inside the exported path.

1. Save and exit. Apply the configuration:

    ```
    sudo exportfs -ra # or sudo systemctl restart nfs-server
    ```

1. Verify the exports

    ```
    sudo exportfs -v
    ```

### Client side

1. Update the system and install the `nfs-common` package. For Ubuntu, run

    ```
    sudo apt update && sudo apt upgrade -y
    sudo apt install nfs-common -y
    ```

    For AlmaLinux, run

    ```
    sudo dnf install nfs-utils
    ```

1. Create the mount point

    ```
    sudo mkdir -p /mnt/nfs/share # For example
    ```

1. Mount manually

    ```
    sudo mount <server_ip_adress>:/srv/nfs4 /mnt/nfs/share
    ```

    a. You can mount with some optimised parameters

    ```
    sudo mount -o rsize=1048576,wsize=1048576,nconnect=4,noatime <server_ip_adress>:/srv/nfs4 /mnt/nfs/share/
    ```

    - `rsize=1048576`: set the read block size to 1 MB (to be tested depending on bandwidth)
    - `wsize=1048576`: same but the write block
    - `nconnect=4`: open 4 parallels TCP connections for transfer (useful on low-latency networks)
    - `noatime`: remove the update of the access date with each read, reducing disk writes

1. You can test the Read/Write performance
   
    ```
    dd if=/dev/zero of=/mnt/nfs/share/testfile bs=1M count=100 oflag=direct
    ```

    The recommended way is to add the mount point in the `/etc/fstab` file:

    ```
    <server_ip_address>:/ /srv/nfs4 nfs4 defaults,noatime,tcp,rsize=1048576,wsize=1048576,nconnect=4 0 0
    ```

    If your client reboot, it will be automatically mounted


## NFS Ganesha

### Server side

!!! Note  
    The following commands were executed on Ubuntu 24.04 and AlmaLinux 9.
    
1. [Create and attach a volume on your machine](../persistent-volumes.md#creating-and-attaching-a-volume-in-the-pouta-web-interface), then [use the volume into your machine](../persistent-volumes.md#using-attached-volumes). For our example, the mount point will be named `/srv/nfs4`

1. Update the system and install the `nfs-ganesha` and `nfs-ganesha-vfs` packages. For Ubuntu, run

    ```
    sudo apt update && sudo apt upgrade -y
    sudo apt install -y nfs-ganesha nfs-ganesha-vfs
    ```

    For AlmaLinux, run

    ```
    sudo dnf install -y centos-release-nfs-ganesha4
    sudo dnf install -y nfs-ganesha nfs-ganesha-vfs
    ```

1. Make a copy of the default config

    ```
    sudo cp /etc/ganesha/ganesha.conf /etc/ganesha/ganesha.conf.ORI
    ```

1. Edit the configuration file

    ```
    sudo vi /etc/ganesha/ganesha.conf
   
    ## These are core parameters that affect Ganesha as a whole.
    NFS_CORE_PARAM {
            ## Allow NFSv3 to mount paths with the Pseudo path, the same as NFSv4,
            ## instead of using the physical paths.
            mount_path_pseudo = true;
    }
    
    ## Configure an export for some file tree
    EXPORT
    {
            ## Export Id (mandatory, each EXPORT must have a unique Export_Id)
            Export_Id = 1;
    
            ## Exported path (mandatory)
            Path = /srv/nfs4;
    
            ## Pseudo Path (required for NFSv4 or if mount_path_pseudo = true)
            Pseudo = /nfs;
    
            ## Restrict the protocols that may use this export.  This cannot allow
            ## access that is denied in NFS_CORE_PARAM.
            Protocols = 3,4;
    
            ## Access type for clients.  Default is None, so some access must be
            ## given. It can be here, in the EXPORT_DEFAULTS, or in a CLIENT block
            Access_Type = RW;
    
            ## Whether to squash various users.
            Squash = root_squash;
    
            ## Allowed security types for this export
            Sectype = sys;
    
            ## Exporting FSAL
            FSAL {
                    Name = VFS;
            }
    
            ## You can make custom rules for certain clients (R, W, RW)
            CLIENT {
                    Clients = 192.168.1.0/24;
                    Access_Type = RW;
            }
    }
    
    ## Configure logging.  Default is to log to Syslog.  Basic logging can also be
    ## configured from the command line
    LOG {
            ## Default log level for all components
            Default_Log_Level = WARN;
    }
    ```
   
    This is a basic configuration. You can browse through the configuration file and customise it to your liking.

1. **On AlmaLinux**, the repository only provides the repo-configuration package, not the actual Ganesha service unit or daemon. You need to create it

    ```
    sudo vi /etc/systemd/system/ganesha.service
   
    [Unit]
    Description=NFS-Ganesha NFS server
    After=network.target
    
    [Service]
    Type=forking
    PIDFile=/run/ganesha/ganesha.pid
    ExecStart=/usr/bin/ganesha.nfsd -f /etc/ganesha/ganesha.conf -L /var/log/ganesha/ganesha.log -p /run/ganesha/ganesha.pid
    ExecReload=/bin/kill -HUP $MAINPID
    Restart=on-failure
    
    [Install]
    WantedBy=multi-user.target
    ```

    Save, exit and reload

    ```
    sudo systemctl daemon-reload
    sudo systemctl enable —-now ganesha
    ```

1. Verify the exports

    ```
    showmount -e localhost
    ```

### Client side

1. Update the system and install the `nfs-common` package. For Ubuntu, run

    ```
    sudo apt update && sudo apt upgrade -y
    sudo apt install nfs-common -y
    ```

    For AlmaLinux, run

    ```
    sudo dnf install nfs-utils
    ```

1. Create the mount point

    ```
    sudo mkdir -p /mnt/nfs/share # For example
    ```

1. Mount manually. Since we are using `mount_path_pseudo = true` in the ganesha server, you must mount the share using the mount pseudo (`nfs`)

    ```
    sudo mount <server_ip_adress>:/nfs /mnt/nfs/share
    ```

    a. You can mount with some optimised parameters

    ```
    sudo mount -o rsize=1048576,wsize=1048576,nconnect=4,noatime <server_ip_adress>:/nfs /mnt/nfs/share/
    ```

    - `rsize=1048576`: set the read block size to 1 MB (to be tested depending on bandwidth)
    - `wsize=1048576`: same but the write block
    - `nconnect=4`: open 4 parallels TCP connections for transfer (useful on low-latency networks)
    - `noatime`: remove the update of the access date with each read, reducing disk writes

1. You can test the Read/Write performance
   
    ```
    dd if=/dev/zero of=/mnt/nfs/share/testfile bs=1M count=100 oflag=direct
    ```

    The recommended way is to add the mount point in the `/etc/fstab` file:

    ```
    <server_ip_address>:/ /nfs nfs4 defaults,noatime,tcp,rsize=1048576,wsize=1048576,nconnect=4 0 0
    ```

    If your client reboot, it will be automatically mounted
