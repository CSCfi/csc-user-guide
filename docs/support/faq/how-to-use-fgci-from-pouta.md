# How to use FGCI grid form Pouta

cPouta environment allows you to set up your personalized computing environment at CSC. However, in cPouta you typically have only limited computing capacity available and thus cluster-like computing is not possible.

One option to mitigate the limited computing resources is to use FGCI grid for heavier computing tasks. FGCI grid provides free computing resources for Finnish academic research. The usage FGCI grid is described more in detail in the FGCI user guide.

FGCI grid is used through ARC middleware that you can install to your Virtual Machine in cPouta (or any linux or Mac OSX). Below we describe the steps for installing ARC middlieware to a Centos7 based VM running in cPouta and configuring it to use FGCI environment.

The installation process is described more in detail in the ARC middelware web site.

First thing to do is to install Grid CA certificates. For that you must add EGI-turustanchors repository to your repository list:

    cd /etc/yum.repos.d/
    sudo wget http://repository.egi.eu/sw/production/cas/1/current/repo-files/EGI-trustanchors.repo
After that the Gird CA Certificates can be installed with command:

    sudo yum install ca-policy-egi-core
Now you can install the nordugrid ARC client and its dependencies with command:

    sudo yum install nordugrid-arc-client nordugrid-arc-plugins-needed nordugrid-arc-plugins-globus ca-policy-igtf-classic ca-policy-igtf-mics ca-policy-igtf-slcs fetch-crl
Finally you must edit the ARC configuration file in: /etc/arc/client.conf so that it can locate the FGCI cluster names.

    sudo vi /etc/arc/client.conf
The content of the client.conf should look like:

**FGCI configuration:**

    [registry/index1]
    url=ldap://giis1.fgi.csc.fi:2135/Mds-Vo-name=Finland,o=grid
    registryinterface=org.nordugrid.ldapegiis
    default=yes
    [registry/index2]
    url=ldap://giis2.fgi.csc.fi:2135/Mds-Vo-name=Finland,o=grid
    registryinterface=org.nordugrid.ldapegiis
    default=yes
Now the ARC middleware client is installed and configured.

The ceritificate revocation list (CRL) needs to be updated after few days. The update is done by running command:

    sudo fetch-crl
You can add the above command to a suitable crontab process to keep the revocation list up to date automatically.

To be able to create a proxy certificate, that is needed to access FGCI environment, you must import your personal Grid Certificate the directory $HOME/.globus and set the access permissions for the certificate file correctly.

    mkdir $HOME/.globus
    cd $HOME/.globus/
    vi usercert.pem
    vi userkey.pem
    chmod 644 usercert.pem
    chmod 400 userkey.pem
In the case of FGCI grid you should also add a vomses file, describing the fgi.csc.fi Virtual Organization,to your $HOME/.arc  dierectory:

    mkdir $HOME/.arc
    echo '"fgi.csc.fi" "voms.fgi.csc.fi" "15003" "/O=Grid/O=NorduGrid/CN=host/voms.fgi.csc.fi" "fgi.csc.fi"' > $HOME/.arc/vomses
    After this you can use arcproxy command to create a proxy certificate:

    arcproxy -S fgi.csc.fi

And now you can use the ARC-client commands to use FGCI.

    arcsync -T
    arcsub fgci_job.xrsl
    arcstat -a
    arcget your_job_id
    For more effective FGCI usage, you can install arcrunner to your VM to help your with submitting and managing large amounts of FGCI jobs.




