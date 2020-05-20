## Grid certificates

FGCI, like most of the middleware based grid environments, uses personal
X.509 certificates for user authentication. In this approach the users
doesn't need a personal user accounts in the cluster they are using.
This means also that CSC user account is not necessary for FGCI usage.

Certificate requests need to be signed by a Certification Authority (CA)
which acts as a trusted third party. CSC is using [GÉANT Trusted
Certificate Service (TCS)] as the authority to provide X.509 certificates for Finnish academic
grid users. The certificates are requested through the [Sertigo portal](https://cert-manager.com/customer/funet/idp/clientgeant
), generates and downloads the certificate to your local computer. The
certificates are valid for one year at a time.

Users log in to the Sertigo portal using their HAKA credentials
(username and password in most cases). To be able to log in, your
Identity Provider ( i.e. home university or institute) most must be
compatible with [eduGAIN] service. If the name of your home institute is
not recognized by the Sertoigo portal (English
institute names are recognized) that means that your home
institute is not compatible with the eduGAIN service. In this case you
can still request a personal certificate from Nordugrid: [Personal
Nordugrid certificate].

## Obtaining a grid certificate from GEANT

**Please ONLY use your personal computer for obtaining your grid
certificate**<span style="font-weight: normal"> as your grid certificate
will be stored the default download folder of the computer you are using for obtaining the
certificate. 
    
Here are step-by-step instructions for obtaining your own certificate:

1.  Go to [https://cert-manager.com/customer/funet/idp/clientgeant](https://cert-manager.com/customer/funet/idp/clientgeant)

2.  Enter the name of your home institute (English
    institute names are recognized) and select it from the list below the text field.
    
3.  Login using your **HAKA username and password**. HAKA account is
    created by your home organization, not by CSC. Typically this is the
    user account you use to log in to local university network. 
    
    If you get error message saying  _You are not allowed to self enroll_, then your home organization is not yet compatible with the Sertigo portal and you should contact local network management to fix this issue.
    

4.  In the Digital certificate enrollment page, check that your personal infromation is corret.
In the**Certificate Profile** selection, choose: **GÉANT IGTF-MICS Personal** and Use **Generate RSA** option for the Private Key selection.   
Finally define and verify a **password** for your certificate and press **submit** button.

The PKCS12 formatted certificate id now exported to the download folder of your browser. Default name for the ceritficate is **certs.p12**

## Installing certificate for FGCI use

Browsers are normally able to use PKCS12 certificates, but the ARC middleware 
uses PEM as the default certificate format. The following commands do PKCS12 to PEM  
conversion on Linux machines. If you will use the grid tools on a different machine than
that which your browser is on, you can transfer the *certs.p12* file
to that machine, and run the following commands there. It's suggested
that you use a secure tool like [*scp*] to do this. 

The PEM formatted certificate consists of two files: private key file
(*userkey.pem*) and certificate file (*usercert.pem*). The certificate
_private key_ is created with the command:

    openssl pkcs12 -nocerts -in certs.p12 -out userkey.pem

When executed, this command will first asks password for the _cetrs.p12_ file (the one you defined in the Sertigo portal) and then a password that will be assigned for the PEM formatted certificate (they can be the same). The user certificate file is created with the command :

    openssl pkcs12 -clcerts -nokeys -in certs.p12 -out usercert.pem

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





  [GÉANT Trusted Certificate Service (TCS)]: http://www.geant.org/TCS/Pages/default.aspx
  [DigiCert SSO portal]: https://www.digicert.com/sso%E2%80%8B
  [eduGAIN]: http://services.geant.net/edugain/Pages/Home.aspx
  [Personal Nordugrid certificate]: https://research.csc.fi/nordugrid-certificate
  [*scp*]: /data/moving/scp.md
