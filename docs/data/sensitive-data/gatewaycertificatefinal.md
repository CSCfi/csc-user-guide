#  Data Gateway error

Virtual desktops created before **November 5, 2025** may display the following error:

**Initializing Data Gateway failed**

To resolve this issue, a one-time workaround is available. Each user must apply it by following the steps below.


## Step-by-Step Instructions

1. **Connect to your virtual desktop**, right-click and select **Open in Terminal**.

2. Test if another project member has already added the fixing tool. Type the following command and press Enter:

    ```bash
    dg-fix
    ```

3. If the terminal responds with `command not found`, continue with the steps below.

4. Type the following command and press Enter:

    ```bash
    gedit dg-fix
    ```

5. This opens the **Gedit text editor**. Make sure the editor view is active by clicking inside it.

6. Press **Ctrl + Alt + Shift** to activate the copy-paste function inthe vrtual desktop. Choose **Text Input**. A new input field will appear at the bottom of the screen.

7. Copy and paste the following script into the input field:

```bash
-----script-starts-here-this-line-is-not-part-of-script------------------

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
 
-----script-ends-here-this-line-is-not-part-of-script------------------ 
```


8. The script will appear in the Gedit document.

9. Close the Clipboard dashboard by selecting **Input method: None**.

10. Click **Save** in the top-right corner of Gedit, then close the editor. A file named `dg-fix` will appear on your desktop.

11. In the terminal, type or copy the following command:

    ```bash
    chmod a+rwx dg-fix
    ./dg-fix
    ```

12. *(Optional)* If you're using the SD software installer, you can make the tool available to other users:

    ```bash
    cp dg-fix /shared-directory/sd-tools/bin/
    ```

    Other users can then run the fix by typing:

    ```bash
    dg-fix
    ```

13. **Log out** from the virtual desktop. After logging back in, the Data Gateway application will open automatically and the error will no longer be displayed.



!!! Note
    If you encounter any difficulties with these steps, feel free to contact us at **servicedesk@csc.fi (sunbject: SD Services)**. We’re happy to assist you via an online meeting.



