### Creating your virtual desktop


<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/t6xXKPTB6H0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Once you can access the service, you can create your virtual computer (desktop), choosing between three pre-built options. This operation can be carried out with a few simple steps and does not require any technical expertise. The services will automatically start your virtual desktop (or, in technical terms: launch a virtual machine) and create a secure connection between CSC and your browser. After this operation, your virtual desktop will be directly available whenever you log in to the service and will consume billing units (or resources) from your CSC project until paused or deleted.

Each CSC project supports the launch of 3 virtual Desktops. In addition, each desktop supports the simultaneous connection of 10 project members. Therefore, all project members can connect to the virtual desktop and access the data stored in your project. Furthermore, all the desktops are provided with the same open-source software (pre-installed and managed by CSC). The complete and updated list can be found in the following paragraph.


To start your virtual desktop, log in to the services and on the _Connection_ page, click on _Go To SD Desktop Management_. 

Here you can specify several parameters:

1. _Select CSC project, operating system and desktop name_.
Possible operating systems are Linux CentOS 7 and Linux Ubuntu 22. Assigning a descriptive name for a Desktop so that all project members can quickly identify it later on, is a good practice.

2. _Select a desktop from the pre-built options_. Based on the computing needs, choose one of the pre-built options (Small, Medium, or Heavy computation).

3. _Add external volume (optional)_. Each desktop's default disk (or storage) space is 80 GB. With this option, you can extend the disk space up to 200 GB, adding an external volume where you can save your files. You can add a new volume by selecting the  _Volume size_  and add a name in the field _Volume name_. **It is a good practice to save a copy of your analysis or important file on the volume that can also have a backup function in case the virtual desktop becomes unresponsive.** Note: you can't extend the disk space after you have created the virtual desktop. Additional disk space can be requested by writing to servicedesk@csc.fi (subject: Sensitive data). 
You can detach and attach a volume from your virtual desktop. This operation corresponds to connecting or disconnecting a hard drive to your laptop and is availale only on desktops created after February 2023. For more informations see: [Managing volume and desktops](./sd_desktop.md#managing-volumes-and-virtual-desktops).

4. Finally, press on _Create desktop_. The operation is entirely automated and can take up to 30 minutes. If you try accessing the virtual desktop during this process, an error message will be displayed asking you to return later.


You can choose between three different pre-built virtual desktop options:

* **Small computation**. Technical specifications: _Core:6; memory 15 GiB; Root disk: 80 GB; Correspondent Pouta Flavour: standard.xlarge; Billing Units: 5.2 units/h_. This option is ideal for analyzing sensitive data using office software (for example: similar to simple statistical analysis with Excel, watching videos, listening to audio files, and working on text files). You can compare this desktop to your laptop. 

* **Medium computation**. Technical specifications:_Core:8; memory 30 GiB; Root disk: 80 GB; Correspondent Pouta Flavour: standard.xxlarge; Billing Units: 10.4 units/h**_. This option is ideal for running complex statistical or genome analysis (for example: using the command line to run specific scripts). You can compare this desktop to a powerful laptop provided by your organization's  IT unit. 

* **Heavy computation**: Technical specifications: _Core:32; memory 116 GiB; Root disk: 80 GB; Correspondent Pouta Flavour: hpc.5.32core; Billing Units: 52 units/h_. This option is ideal for running non-interactive programmatic analysis (machine learning) that requires heavy computation. Please do not choose this option for simple analysis, as it consumes considerable resources. 



!!! Note
    For support in choosing the correct desktop option for your needs, don't hesitate to contact us at servicedesk@csc.fi (email subject: Sensitive data). 


!!! Note
    As each virtual desktop consumes resources, it's advisable to delete your desktop when it's no longer necessary (for instance, after testing the SD Desktop service or completing the analysis phase). All project members will receive email notifications if a desktop remains unused for at least 14 days. Before deletion, make sure to export all essential results and disconnect any volumes containing important files for future use and notifying the other CSC project members. For further details, refer to [Managing volumes and desktops](./sd_desktop.md#managing-volumes-and-virtual-desktops).
    


The following paragraphs will discuss how to work with your virtual desktop, which software is available, and how to customize your workspace.

[![Launch](images/desktop/desktop_launch.png)](images/desktop/desktop_launch.png)


