# 1.1 Grid certificates

FGCI, like most of the middleware based grid environments, uses personal
X.509 certificates for user authentication. In this approach the users
doesn't need a personal user accounts in the cluster they are using.
This means also that CSC user account is not necessary for FGCI usage.

Certificate requests need to be signed by a Certification Authority (CA)
which acts as a trusted third party. CSC is using [GÉANT Trusted
Certificate Service (TCS)] as the authority to provide Finnish academic
grid users with personal e-science grid user certificates. The
certificates will be requested through the [DigiCert SSO portal], which
automatically installs in the certificate to users web browser. The
certificates are valid for one year at a time.

The user logs on to the DigiCert SSO portal using their HAKA credentials
(username and password in most cases). To be able to log in, your
Identity Provider ( i.e. home university or institute) most must be
compatible with [eduGAIN] service. If the name of your home institute is
not recognized by the DigiCert SSO portal (Finnish, Swedish and English
institute names should be recognized) that means that your home
institute is not compatible with the eduGAIN service. In this case you
can still request a personal certificate from Nordugrid: [Personal
Nordugrid certificate].

 

# 1.1.1 Obtaining a grid certificate from GEANT

**Please ONLY use your personal computer for obtaining your grid
certificate**<span style="font-weight: normal"> as your grid certificate
will be stored into the browser you are using for obtaining the
certificate. </span> **Chrome is not compatible with the Digicert
service** so you should use Firefox or Explorer to get a
certificate.Here are the step-by-step instructions for obtaining your
own certificate:

1.  <span lang="en-IE">Go to </span><https://www.digicert.com/sso><span
    lang="en-IE">  </span>

2.  Enter the name of your home institute (Finnish, Swedish and English
    institute names are recognized) and press "Start single sign-on"

3.  Login using your **HAKA username and password** (a HAKA account is
    created by your home organization, not by CSC. Typically this is the
    user account you use to log in to local university network)

4.  In the "Request  Product" page, choose product: **Grid Premium**,
    check your information and press "**Request Certificate"**

Now you have your certificate in the keystore of your browser, signed by
DigiCert and ready for use.

 

# 1.1.2 Exporting the certificate from the browser

After obtaining the certificate from TERENA, the certificate is
initially stored only in the certificate repository of the web browser
that was used for the certificate generation process. To use your
certificate for grid jobs you need to export your certificate to a
certificate file. The location of the certificate repository and
commands that export the certificate to a file vary between browsers
(even between different versions of the same browser). Your browser may
contain several certificates, many of which are used to verify other web
service providers. Normally you can recognize your personal TERENA
certificate based on the certificate name that should contain your name
or e-mail address.

Below are instructions for exporting the certificate from a few commonly
used browsers.

**Firefox:**

1.  Select: *Edit -&gt; Preferences* (in Linux) or *Tools -&gt; Options*
    (in Windows) or *Firefox -&gt; Preferences* ( In Mac)

2.  Go to *Advanced -&gt; Encryption -&gt; View Certificates*

3.  Select your certificate and click *Backup*

4.  Save the certificate as "**usercert.p12**". The browser will ask you
    for your password, along with an export password. <span
    style="font-weight: normal">You MUST have a password here, you may
    not backup the certificate without a password!</span>

**Opera:**

1.  Select *Menu -&gt; Settings -&gt; Preferences*

2.  Go to *Advanced -&gt; Security -&gt; Manage Certificates*

3.  Select your certificate and click *Export*

4.  Choose the "**PKCS \#12 (with private key)**" file type, and save
    the certificate as "**usercert.p12**". The browser will ask you for
    your password, along with an export password. You MUST have a
    password here, you may not export the certificate without a
    password!  
     

 

# 1.1.3 Installing certificate

Browsers normally store the certificates using the PKCS12 format.
However, for the ARC middleware uses PEM as the default certificate
format. The following commands do PKCS12-PEM  conversion on Linux
machines. If you will use the grid tools on a different machine than
that which your browser is on, you can transfer the *usercert.p12* file
to that machine, and run the following commands there. It's suggested
that you use a secure tool like [*scp*] to do this. Optionally, you can
use the *My Certificates* tool, introduced in section 1.1.4, to do the
conversion and transport.

The PEM formatted certificate consists of two files: private key file
(*userkey.pem*) and certificate file (*usercert.pem*). The certificate
private key is created with the command:

    openssl pkcs12 -nocerts -in usercert.p12 -out userkey.pem

When executed, this command will ask for the old and the new key
passwords (they can be the same). The user certificate file is created
with the command :

    openssl pkcs12 -clcerts -nokeys -in usercert.p12 -out usercert.pem

The commands above should have created two files, *usercert.pem* and
*userkey.pem*. To use the ARC middleware these two files should be moved
into a *.globus* sub-directory under the user's home directory (note the
dot as the first character of the directory name). If the *.globus*
directory does not exist, it can be created with the command:

    mkdir ~/.globus/

After this, the certificate files can be moved to the *.globus*
directory with the commands:

    cp usercert.pem ~/.globus/
    cp userkey.pem ~/.globus/

Finally, make sure that the access permissions of the *userkey.pem* file
are set up correctly. The command to ensure this is:

    chmod 400 ~/.globus/userkey.pem

# 1.1.4 Managing certificates in the Scientist's User Interface

CSC's *Scientist's User Interface* (SUI) service contains a *My
Certificates* tool that can be used to manage X.509 certificates. The
*My Certificates* tool provides a machine independent certificate
repository that can be used for backing up and copying certificates from
one machine to another. *My Certificates* can also do conversions
between different certificate formats. The *My Certificates* tool can be
found at

   <span
lang="en-IE"><https://sui.csc.fi/group/sui/my-certificates></span>

When you use this service for the first time you need to set up a
password that this certificate repository will use. This is done by
right-clicking the repository and selecting:*<span
style="font-weight: normal"> Security Settings</span>* from the pop-up
menu. This repository password is not linked technically to other
passwords like CSC, SUI or certificate passwords.

Once the repository password has been defined, certificates can be
imported to the repository. This is done by right clicking the empty
certificate menu and selecting: *Upload.* <span
style="font-style: normal">The</span> *My Certificate*s tool can read in
certificates in PEM and PKCS12 formats. For example to import the
*usercet.p12* file, created with the commands used in [chapter 1.1.2],
the *Select file format* setting must be changed to *PKCS12*. The import
process is then started by clicking *OK*. Clicking on the *Upload*
button opens a file browser that can be used to select the certificate
file (*usercert.p12*).

When the certificate file is imported, SUI will ask for the certificate
password. This is the password that has been assigned to the certificate
in the TERENA certificate portal (not the certificate repository
password or the CSC password). After providing the password, check the
certificate information and click *<span
style="font-weight: normal">"Save"</span>*. The certificate should then
be visible as one row in the *Stored Certificates* table.

Once the certificate is stored to the *My Certificates* repository, it
can easily be exported to the computer you are currently working by
logging in to the service and using the *Download* command.

  
You can also use this command to store the certificate in PEM format to
the *.globus* directory of the CSC server Taito. This is necessary to be
able to submit grid jobs from Taito.

1.  Select the certificate from the list.

2.  <span lang="en-IE">Right-click and select:  </span><span
    lang="en-IE">**Download**</span>

3.  <span lang="en-IE">Then select:  
              Download Destination:  </span><span lang="en-IE">**Globus
    directory ($HOME/.globus)**</span>  
    <span lang="en-IE">          File format: </span><span
    lang="en-IE">**PEM**</span>  
     

<span lang="en-IE">After entering the certificate password for the PEM
certificate files, they will be stored to the </span><span
lang="en-IE">*.globus*</span><span lang="en-IE"> directory of your CSC
home directory. This is the default location for the certificates that
grid tools at CSC will use.</span>

  
![]

#### Figure 1. The My Certificates tool in the Scientists User Interface.

 

 

  [GÉANT Trusted Certificate Service (TCS)]: http://www.geant.org/TCS/Pages/default.aspx
  [DigiCert SSO portal]: https://www.digicert.com/sso%E2%80%8B
  [eduGAIN]: http://services.geant.net/edugain/Pages/Home.aspx
  [Personal Nordugrid certificate]: https://research.csc.fi/nordugrid-certificate
  [*scp*]: https://research.csc.fi/csc-guide-copying-files-from-linux-and-mac-osx-machines-with-scp
  [chapter 1.1.2]: https://research.csc.fi/fgi-grid-certificates#1.1.2
  []: https://research.csc.fi/documents/48467/84606/FGI-guide_image1.jpg/8346b997-2596-43fc-acc7-0d1730bfc67e?t=1383829146000
