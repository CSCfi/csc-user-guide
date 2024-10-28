# QEMU virtual images in cPouta

[QEMU](https://www.qemu.org/docs/master/about/index.html) is a robust open-source machine emulator and virtualizer. It enables the running of operating systems and applications intended for one machine on an entirely different platform. This tool is integral to various virtualization frameworks. Notably, it's implemented within the OpenStack cloud infrastructure.

## 1. Downloading a backup or snapshot

Downloading a backup or snapshot image from cPouta to your local PC. To accomplish this, you need to have the OpenStack command-line client (`openstack`). Source your openrc script file to configure the necessary environment variables for authentication. If you don't have this file, you can download it from the web [UI](https://pouta.csc.fi/). For more information see [Installing the client tools using pip](install-client.md) and [Configure your terminal environment for OpenStack](install-client.md).

For example, on a Debian/Ubuntu-based system, you can install these with:

```bash
sudo apt-get install python3-openstackclient 
```
And  source openrc script file:

```bash
source <project_name_here>-openrc.sh
```

You will be prompted to enter your password. See [Install OpenStack client](install-client.md) for other Operating Systems.

List the images/snapshots including the disk format that are available in your OpenStack project:

```bash
openstack image list --long
```

Note down the ID of the image you want to download.

Now, download the image to your local machine:

```bash
openstack image save --file LOCAL_IMAGE_FILENAME.qcow2 IMAGE_ID
```

Replace `LOCAL_IMAGE_FILENAME.qcow2` with your desired local filename, disk format  and `IMAGE_ID` with the ID.

## 2. Understanding file formats of the downloaded backup or snapshot

When you download a backup or snapshot of your virtual machine (VM) from cPouta, the file format of the downloaded image could be raw or qcow2. The QEMU emulator supports several disk formats including raw, vdi, and qcow2. See [OpenStack Disk and Container Formats](https://docs.openstack.org/glance/stein/user/formats.html) for more information.

- **QCOW2 (QEMU Copy On Write)**: This is the default and most common format for OpenStack images, especially when QEMU is used.
- **RAW**: A raw disk image format. It's generally larger in size than QCOW2 images.
- **VDI (Virtual Disk Image)**: This format is mainly associated with VirtualBox but can also be used with OpenStack.

The following command tell you the format of the image, providede that you have the `qemu-img` tool installed. See [QEMU installation](https://www.qemu.org/download/#linux) for more information.

```bash
qemu-img info /path/to/your/image
```

## 3. Converting VM image disk formats to QCOW2 with QEMU

If you do not have a QCOW2 image but have a VM disk in another format, you can convert it to QCOW2 using QEMU's `qemu-img` tool. The following command 
converts  your VM disk to QCOW2 format:

```bash
qemu-img convert -f [source_format] -O qcow2 [source_image] [destination_image.qcow2]
```    

Where:

- `[source_format]`: The format of the source image (e.g., `raw`, `vdi`, `vmdk`, `vhdx`).
- `[source_image]`: The path to the source VM disk.
- `[destination_image.qcow2]`: The path where you want to save the converted QCOW2 image.

For example, to convert the `testCentOS.raw` downloaded image to QCOW2 image using QEMU, first get image info and then convert it as following:

```bash
qemu-img info testCentOS.raw 

image: testCentOS.raw
file format: raw
virtual size: 2.97 GiB (3184721920 bytes)
disk size: 2.97 GiB
```

```bash
qemu-img convert -f raw -O qcow2 testCentOS.raw testCentOS.qcow2
```

After the conversion process completes, you can check the details of the converted image using:

```bash
qemu-img info testCentOS.qcow2
```

## 4. Running downloaded backup or snapshot images locally with QEMU

The downloaded backup or snapshot image from cPouta, which is typically in the `raw` format. Before executing it with QEMU, it's essential to convert this image to the `qcow2` format. Please refer to the previous section for steps on format conversion and verification. Before running the virtual machine locally, ensure that `cloud-utils` and `qemu-kvm` packages are installed. A step-by-step guide as follows:

!!! Warning  
    The image you downloaded from cPouta needs cloud-init and requires modification to function properly locally. The image downloaded may require configuration change on the networking setup locally.

- Install necessary packages.
    
    For RHEL or CentOS 8 system:

    ```bash
    sudo dnf install cloud-utils
    ```

    On a Debian/Ubuntu-based system:

    ```bash
    sudo apt-get install cloud-image-utils
    ```

- Prepare the cloud-init configuration.

    Create a file named `cloud-config.yaml` with the following content:

    ```yaml
    #cloud-config
    ssh_authorized_keys:
    - YOUR_SSH_PUBLIC_KEY
    ```

    Replace `YOUR_SSH_PUBLIC_KEY` with the content of your SSH public key (`~/.ssh/id_rsa.pub`). For example:

    ```yaml
    #cloud-config
    ssh_authorized_keys:
    - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQ... your.email@example.com
    ```

- Generate a cloud-init ISO with your configuration

    Using the `cloud-localds` utility, convert the YAML file to a cloud-init ISO:

    ```bash
    cloud-localds user-data.iso cloud-config.yaml
    ```

-  Boot the VM with the cloud-init ISO.
  
    Using QEMU, you'd boot the image as follows:

    ```bash
    qemu-kvm  -enable-kvm -m 2048 -hda test100snapshot-v2.qcow2  -cdrom user-data.iso -net nic -net user,hostfwd=tcp::2222-:22
    ```

    The command will output `VNC server running on ::1:5900`.

    The output `VNC server running on ::1:5900` indicates that QEMU started the virtual machine and is providing a graphical console via a VNC server. You can connect to this VNC server to see the VM's display and interact with it. We will try to onnect it using SSH.

    The given QEMU command does a few things:

    1. `-enable-kvm`: Enables KVM 
    2. `-m 2048`: Assigns 2048MB (or 2GB) of RAM to the virtual machine.
    3. `-hda test100snapshot-v2.qcow2`: Sets the primary hard drive of the VM to the `test100snapshot-v2.qcow2` image.
    4. `-cdrom user-data.iso`: Mounts `user-data.iso` as a CD-ROM in the VM.
    5. `-net nic`: Creates a virtual NIC (Network Interface Card) for the VM.
    6. `-net user,hostfwd=tcp::2222-:22`: Sets up user-mode networking and forwards port 2222 on the host to port 22 on the VM. 

- Once the VM has booted and fully initialized, you can SSH into this image locally(the snapshot used here is an Ubuntu 22.04 flavor as an example):

    ```bash
    ssh -i ~/.ssh/id_rsa -p 2222 ubuntu@localhost
    ```
## 5. Uploading a VM image to cPouta

Uploading a VM image to cPouta can be done using either the Horizon web interface (WEB UI) or the OpenStack CLI. See more on [Adding Images](adding-images.md).

- using OpenStack CLI, assuming you have sourced the OpenStack credentials as shown above.

    Use the `openstack image create` command to upload the image as follows:

    ```bash
    openstack image create "testCentOS" \
    --file  testCentOS.qcow2 \
    --disk-format qcow2 \
    --container-format bare \
    --private
    ```

    Check the created image is in the list of images that are available in your OpenStack project:

    ```bash
    openstack image list --long
    ```

- Using Web UI, first log in to web dashboard using your credentials.

    - **Navigate to image management**: Under the `Project` tab, go to `Compute` -> `Images`.
    -  **Upload the Image**: Click on the `+ Create Image` button and fill in the details:
        - **Image Name**: Provide a name for the image.
        - **Image Description**: (Optional) Add a brief description.
        - **Image Source**: Choose `File Browse` and select your QCOW2 image.
        - **Format**: Select `QCOW2 - QEMU Emulator` or `raw`.
        - **Architecture**: (Optional) Specify the architecture (e.g., x86_64).
        - **Image Sharing **: `Protected` `Yes`.
        - Click `Create Image`.
  
After the command runs or web ui upload successfully, the image will be available for use.
