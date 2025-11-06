# Fix

Virtual desktops created before November 5 2025 display an error that blocks Data Gateway application: Initializing Data Gateway failed.

To resolve this issue, a one time workaround is available. It must be applied per by each user by following these steps:


1. connect to your virtual desktop, right click and click on open in terminal.

2. Next, we need to test if another project member has already added the fixing tool. Type the following command in the terminal and press enter:

dg-fix

3. If the terminal says that command is not found, continue with the following steps:

4. type this command and press enter:

gedit dg-fix

5. This opens a new user-friendly interface called Gedit text editor. Make sure that the editor view is active by clkiing in it.

    
6.  Press Ctrl + Alt + Shift to activate copy-paste function. Choose Text Input. A new input filed will appear in the loewr part of the screem. Copy the script below to your local clipboard and paste it to the SD Desktop input field.

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


7. The script will soon appear to the Gedit document too.

8. Close the Clipboard dashboard by selecting Input method: None

7. Then press on save in Gedit top right cornet and then close the text editor. This will create a file callled  dg-fix that will appear on the desktop. 

8. Now type or copy this command in the terminal: 

chmod a+rwx dg-fix./dg-fix

9. (optonal) If you have been using SD software installer, you can make the dg-fix tool available for other users wiht thi command: 

cp dg-fix /shared-directory/sd-tools/bin/

After that command can be launched by other users by just by opening the terminal, typing the following commanda dn pressinf enter: 

dg-fix

10. Now log out from the virtual desktop. After logging back in, the Data Gateway application will open automatically and the error will no longer be displayed.

!!! Note
    If you encounter any difficulties with these steps, feel free to contact us at servicedesk@csc.fi.  We are happy to assist you via an online meeting.
