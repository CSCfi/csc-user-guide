#  Data Gateway error

The Data Gateway application can no longer be opened on all virtual desktops created **before November 5, 2025** and shows the error: "Initializing Data Gateway failed." 

![Gateway doesn't open](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Gateway-fix-1.png)

**A one time workaround is available and must be applied by each virtual desktop user**. 

* If you **have** previously used the SD Software Installer in the virtual desktop, **one project member** completes [the full process](#full-process) but others only need to perform [the final step](#final-steps-for-project-members).

* If you **haven't** previously used the SD Software Installer in the virtual desktop, **all project members** need to complete [the full process](#full-process).





## Step-by-Step Instructions

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/3pgpG2Kosb4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


### Full process

1. **Connect to your virtual desktop**, right-click and select **Open in Terminal**.

![Open in terminal](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Gateway-fix-2.png)

2. Test if another project member has already added the fixing tool. Type the following command and press Enter:

    ```bash
    dg-fix
    ```
![Type in terminal](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Gateway-fix-3.png)

3. If the terminal responds with `command not found`, continue with the steps below. 

![Command not found](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Gateway-fix-4.png)

4. Type the following command and press Enter:

    ```bash
    gedit dg-fix
    ```

5. This opens the **Gedit text editor**. Make sure the editor view is active by clicking inside it.

![Open Gedit text editor](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Gateway-fix-5.png)

6. Press **Ctrl + Alt + Shift** to activate the copy-paste function in the virtual desktop. Choose **Text Input**. A new input field will appear at the bottom of the screen.

![Choose text input](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Gateway-fix-6.png)

7. Copy and paste the following script into the input field:

![Copy and paste into the inout field](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Gateway-fix-7.png)

```bash
#!/bin/bash
# Run this script if DataGateway does not work 

echo "export FS_CERTS=/shared-directory/.certs/ca.crt" >> $HOME/.profile

if [[ ! -e /shared-directory/.certs/ca.crt ]]; then
mkdir -p /shared-directory/.certs
cp /usr/local/share/ca-certificates/ca.crt /shared-directory/.certs/
fi 

check1=$(grep -c "CooV2DCfiEJlIsKz" /shared-directory/.certs/ca.crt )
check2=$(grep -c "TGAl5j07G7ZIuK3Q" /shared-directory/.certs/ca.crt )

if [[ $check1 -eq 1 && $check2 -eq 1 ]]; then
echo "Certificates have already been updated"
else

if [[ $check1 -eq 0 ]]; then
openssl s_client -showcerts -verify 5 -connect aai.sd.csc.fi:443 < /dev/null | \
awk '/-----BEGIN CERTIFICATE-----/{c++} c==3{print}/-----END CERTIFICATE-----/&&c==3{exit}' \
>> /shared-directory/.certs/ca.crt
fi

if [[ $check2 -eq 0 ]]; then
openssl s_client -showcerts -verify 5 -connect terminal.sd.csc.fi:8443 < /dev/null | \
awk '/-----BEGIN CERTIFICATE-----/{c++} c==3{print}/-----END CERTIFICATE-----/&&c==3{exit}' \
>> /shared-directory/.certs/ca.crt
fi
fi

echo "Logout and start a new session to take the updated certificates in use." 
```

8. The script will appear in the Gedit document.


9. Close the Clipboard dashboard by selecting **Input method: None**.

10. Click **Save** in the top-right corner of Gedit, then close the editor. A file named `dg-fix` will appear on your desktop.

![Gedit](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Gateway-fix-8.png)

![dg-fix file](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Gateway-fix-9.png)

11. In the terminal, type or copy the following command:

    ```bash
    chmod a+rwx dg-fix
    ./dg-fix
    ```

You've now completed all required steps. Log out of the virtual desktop and relaunch it. 

![In terminal](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Gateway-fix-10.png)

12. *(Optional)* If you have previously used the SD software installer, you can make the tool available to other users of the same virtual desktop by copying this commands in the terminal:

    ```bash
    cp dg-fix /shared-directory/sd-tools/bin/
    ```


13. **Log out** from the virtual desktop. After logging back in, the Data Gateway application will now open and the error will no longer be displayed.


!!! Note
    If you encounter any difficulties with these steps, feel free to contact us at **servicedesk@csc.fi (subject: SD Services)**. We’re happy to assist you via an online meeting.


## Final steps for project members

If you have been using the SD Software Installer and one of the member of the project has completed the process above, you can simply:

1.. **Connect to your virtual desktop**, right-click and select **Open in Terminal**.

2. Type the folloging command and press enter:

    ```bash
    dg-fix
    ```

13. **Log out** from the virtual desktop. After logging back in, the Data Gateway application will now open and the error will no longer be displayed.
