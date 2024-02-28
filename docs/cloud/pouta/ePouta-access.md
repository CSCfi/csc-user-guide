# Applying for ePouta access

Asking for ePouta access is not a self service process. ePouta is a cloud designed to hold and process sensitive data. Because if that the architecture that ensures the security of the platform and the data contained in it, requires a VPN connection between ePouta and the local network of the user of the VM. In other words, before using ePouta it is necessary to have a VPN configured. This network setup is a manual step that involves several teams in CSC and the institution of the user of the VMs.

1. The first step is to be sure that ePouta is the platform for the use case. ePouta is designed to store and process sensitive data. If the use case does not deal with sensitive data, cPouta might be a better service for the use case.

1. Once the suitability of ePouta has been validated, it is necessary to check if there is already a project created in ePouta that can hold this use case. Some institutions have what is called an "umbrella project", or other kind of pre-created or pre-allocated pool of network connections. Please contact your institution's IT team to check this.

1. If nothing is already available, you must create a ticket by sending an email to <servicedesk@csc.fi> explaining you use case. Please make sure to mention this information:

    * Use case description and why it needs to be hosted in ePouta.
    * Explanation on why the existing resources cannot be used and a new one must be created.
    * Estimation of resources needed and for how long. You can check the [VM flavors and billing](vm-flavors-and-billing.md#epouta-flavors) page to see what VMs are available.
    * IPs of the administration computers that will need to create, modify and delete VMs.

1. Once the ticket has been created, it is necessary to wait. CSC will contact the necessary network teams to setup the infrastruture. You will be only contacted upon completion, or if any questions arises.
