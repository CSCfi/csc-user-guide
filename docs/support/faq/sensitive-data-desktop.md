# SD Desktop 

## Can I access/analyze encrypted data stored in SD Connect using SD Desktop?
Yes. Encrypted data stored in SD Connect can be accessed via data streaming (in read-only format ) in SD Desktop. You can store up to TB of data in SD Connect and directly analyze it in your private Desktop without creating a full copy of it. 

## Can I edit/annotate data using SD Desktop?
Yes. You can edit or annotate data in SD Desktop. However, you need to make a full copy of it in the Desktop environment. If your data is larger than  280 GB, contact us at servicedesk@csc.fi. We can provide additional external disk pace (the default space in SD Desktop is about 280 GB). 

## Does CSC provide SD Desktop operating system, software, and security updates?
Yes, every SD Desktop is built on a predefined virtual machine defined by our team. CSC provides the operating system, software, and updates. CSC also takes care of the security of all the service components and network connections.

## What are the technical specifications of the service?

* Accessible directly from a modern web browser (e.g., Google Chrome, Firefox). from any computer /laptop (Windows, Mac, or Linux).

* Disk space: 80GB (possibility to add an external disk up to 200GB)

* Computing environment provided via web browser: currently only Linux OS.

* Copy-paste function disabled for security reasons.

* Default pre-installed software (additional software can be installed by importing singularity containers).

* The computing environment is isolated from the Internet.

* Data import only via SD Connect.

* Only the CSC project manager can export files outside SD Desktop.

If you need help choosing a suitable computing environment, don't hesitate to contact us at servicedesk@csc.fi (email subject: Sensitive Data). 

## What type of file can I analyze using SD Desktop?
Any type: text, video, audio, images, genetic data, questionnaires.

## What software is available on SD Desktop?

We currently provide only Linux Ubuntu22 computing environments with a limited amount of open-source software installed, including Libre Office (with LibreOffice Calc, a spreadsheet program similar to Microsoft Excel, and LibreOffice Writer,  a word processor similar to Microsoft Word), R Studio and Python. We are not providing proprietary software, but we could help you install on your private desktop an open-source version. 
For further information and for desktop customisation see: [Default programs available on SD Desktop](../../data/sensitive-data/sd-desktop-software.md).  
Don't hesitate to get in touch with us at servicedesk@csc.fi for specific technical support.

## Who can access my private computing environment in SD Desktop?
Only your CSC project members can directly access the private Desktop. Furthermore, as the computing environment is isolated from the Internet, no one can export files from SD Desktop without CSC project manager approval. 

## What is the difference between SD Desktop and ePouta?
SD Desktop is a web-user interface that allows you to connect to your virtual computing environment securely. CSC manages SD Desktop: we manage the connection, access, and security. 
SD Desktop is suitable for collaborative projects across Finnish organizations and provides the computational capability to research organizations that do not have an ePouta tenant. 

ePouta is an infrastructure provided to research organizations, and the organization's own IT unit manages its access and network. ePouta works on extending an academic organization infrastructure and provides all the flexibility and requirements decided by the organization. 

## Can I have root or sudo access to a virtual machine running in SD Desktop?
No. Your account has only normal user level priviledges. Providing sudo rights to a user would compromise the secutity of you SD Desktop environmenyt. 

## Why do I see the word guacamole in the URL next to sd-desktop.csc.fi?
Yes, this is a very frequent question! Guacamole is a technical component (Open source)  of the services and allows you to access SD Desktop via a web browser. Especially if you are using a Windows laptop, the term may appear in your URL while accessing the service as in this example: https://sd-desktop.csc.fi/guacamole/#/


   



