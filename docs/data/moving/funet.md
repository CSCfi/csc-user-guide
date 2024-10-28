# Sharing and transporting files using Funet FileSender

Funet FileSender is a browser-based service for sending large files to
colleagues. It is provided as an alternative to email attachments, but it can
also be used for moving files to CSC environment. The service allows you to
upload and send files up to 300 GB size. The service is **not** intended for
long-term storage, as the files are deleted automatically after the
preservation time is exceeded. The maximum preservation time is 21 days.

Funet FileSender is available for all Haka-enabled organizations without any
additional measures. For example, a CSC user account is not needed to use the
service. Both sending and receiving are possible without installing any
additional programs.

You can use Funet FileSender to share your files with anybody. The receiver
doesn't need any authentication for downloading the file from FileSender. If
you don't belong to Haka, you need a colleague who can send you an
_upload voucher_. The voucher is a one-time permit to use the service for
sending a file.

## Uploading data to FileSender

First, [login to the service with your browser](https://filesender.funet.fi).
You should login to the system with your Haka credentials; first select your
home organization and use your institutional username and password to log in
(not CSC username and password).

After this you can specify the email address of the recipient, or alternatively
get a shareable link. Use the _Select files_ button to choose the files you
want to send. After the temporary storage time has been defined
(_Expiry date:_) and the usage terms are accepted, press the _Send_ button to
upload the files. Once the files have been uploaded, the recipient will get an
email notification.

It is possible to administer your files while they are waiting for the pick-up.
Click the _My Transfers_ button to do this.

![Funet FileSender upload page](/img/funet_upload.png 'Funet FileSender upload page')

!!! Note
    As data is uploaded to Funet FileSender through a web browser, it may be
    difficult to use it for data located on CSC supercomputers. In this case,
    you can alternatively use
    [Allas commands](../Allas/using_allas/a_commands.md) `a-flip` or
    `a-publish` for sharing data. Yet another alternative is to
    [use the FileSender command-line client](#using-filesender-from-the-command-line).

## Download data from FileSender

The recipient will get an email that contains a URL to the download page of
the submitted files. The shareable link will also point to the download page.
You can start the download by pressing the _Download_ button.

![Funet FileSender download page](/img/funet_download.png)

You can also right click the download button and select _Copy Link_ to
get the download URL to the file. The URL can then be used to download the file
using another tool, for example [`wget`](wget.md):

```bash
wget "https://filesender.funet.fi/download.php?token=4da0-b98e-3290c6471469&files_ids=36805" -O data_from_FS
```

!!! note "Note"
    When downloading data from Funet FileSender with `wget` you must enclose
    the download link with quotation marks and use option `-O` to define a file
    name that will be used for the downloaded data.

## Using FileSender from the command-line

FileSender can also be used from the command-line using a Python 3 utility
script. These instructions have been adapted from the
[AARNet Knowledge Base](https://support.aarnet.edu.au/hc/en-us/articles/5276533711887-Use-FileSender-from-the-command-line).

Assuming you are on a Linux server (e.g. Puhti or Mahti):

1. Download the `filesender.py` Python tool:

    ```bash
    wget "https://filesender.aarnet.edu.au/clidownload.php" -O filesender.py
    ```

2. Create a new folder `~/.filesender` in your home directory and download a
   client configuration file there:

    ```bash
    mkdir -p ~/.filesender
    wget "https://filesender.aarnet.edu.au/clidownload.php?config=1" -O ~/.filesender/filesender.py.ini
    ```

3. Edit the `~/.filesender/filesender.py.ini` files as follows (decrease the
   preservation time if needed):

    ```ini
    [system]
    base_url = https://filesender.funet.fi/rest.php
    default_transfer_days_valid = 21

    [user]
    username = <your username>
    apikey = <api secret>
    ```

    Your username (_Identifiant_) and API key (_Secret_) can be found/generated
    on the _My profile_ page of the
    [Funet FileSender website](https://filesender.funet.fi/) (requires logging
    in first). Treat the API key as any password – keep it secret! Note that
    the username in this case is **not** the same as your CSC account username.

4. Now you may send a file (e.g. `data.tgz`) to a recipient (e.g.
   `recipient@example.com`) with:

    ```bash
    python3 filesender.py -r recipient@example.com data.tar.gz
    ```
