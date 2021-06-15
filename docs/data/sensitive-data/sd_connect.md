# SD Connect (Sensitive Data Connect)


## Step1: Login 

To access SD Connect you need:

* **a CSC account**
* **a CSC project**
* **Service access to Allas** (CSC cloud storage solution)

Login to SD Connect is possible with user identity federation systems (Haka, Virtu and Elixir AAI) or with a CSC account at https://sd-connect.csc.fi/ using any modern web browser.


!!! note
    Sensitive data need to be encrypted before upload to SD Connect. Check the previous paragraph for more informations about encryption with Crypt4GH.


!!! note
    SD Connect is not suiteble for permanet data storage. Make regular backups of important datasets.

!!! note
    Users may not process any personal data granted for the purposes of the Act on the Secondary Use of Health and Social Data (552/2019) by ***Findata.***



## Step 2: User Interface

Once you Login in SD Connect you access the default front-page: **Browser**.

In this page you can :

* view all **the  buckets (or containers) available in your CSC project**, in which you can store encrypted sensitive data. The bukects can be created, downloaded, deleted or shared, using the appropriate icons;
   
*  **list and select your CSC project** from the drop down menu bar (top left corner) to visualize container or data belonging to a specific project;

*  open any bucket (double click) and view its content (uploaded files or folders). Any file can be downloaded or shared using the download link. From this view, you can also download the entire bucket, delete file or upload new files and folders.

<img width="956" alt="SD-Connect-1copy" src="https://user-images.githubusercontent.com/83574067/122087350-4906a100-ce0d-11eb-91ac-c39df3dedb23.png">



In the  **User information** page you can:

* in **Currently Consumes** view statistics about the selected CSC project resource usage: billing unit consumption and the total project storage usage (defoult storage 10 TiB);

* in **Project usage** you can view the **SD Connect Account, an ID associated your CSC project**. This ID is required when you want to share containers with other CSC projects using SD Connect user interface. It does not containe sensitive information, thus it can be sharer with your colleagues or collaborators via email.

* access the **Token icon** through which you can generate a temporary token (necessary for data upload programmatically, using Swift client. For more info check below).


<img width="925" alt="SD-Connect-2" src="https://user-images.githubusercontent.com/83574067/122087374-4dcb5500-ce0d-11eb-9835-15f96f152df8.png">



In the **Shared** page:

* in **Shared to the project** you can view the **bukets that other CSC projects (belonging to your colligues or collaborators) shared with you**. Next to the bucket name, under **Containeor Owner**,  it is displayed the ID associated to CSC project to which the bucket belongs to (also called SD Account). With double click you can access the bucket and view the content (if you have reading access) or add files to the container (if you have edits rights). 

!!! note 
    All the container listed here are own by another users that can decide when revoke your access. You will not be able to access the file from SD Dekstop untill you make a copy of the container. 

* in **Shared with the project** you can view the bukets which  **you shared with other CSC projects**. In this case you own the shared bukets and you can decide when revoke access. 

<img width="959" alt="SD-Connect-3" src="https://user-images.githubusercontent.com/83574067/122087777-c7fbd980-ce0d-11eb-9ccb-c98fdb897e02.png">


## Step3: Data upload 

To upload encrypted data in SD Connect it is suffiecint to use the **drag and drop function** (files or datasets less then 100 GB) in the browser page. Once the upload has started, a progress bar will visulize the status of the upload. For bigger datasets or files, you can upload files programmatically  or folders use the clients described later.

If you did not create a buket yet, the user interface will automatically create a buket named: upload-nnnnnnnnnnnnn. Note that **it is not possible to rename buckets**.

If you create a new buket use the following **suggestions to name it**:

* Bucket **names must be unique** across all existing bucket in CSC storage solution
    
* Bucket names must **not contain uppercase characters or underscores or non-ASCII (ä, ö etc.) characters**
    
* All bucket **names are public**, so please do not include any confidential information in the bucket names
 
Example: ns-123456-raw-data-ddmmyy
  




# Data Sharing  from your project to  other CSC users's project



# Data upload using CLI for SD Connect





Questions:

- DO we mention Chromes, works better?
- Objects: in the defilition?
- all the actiosn can be done just with files but now with folders.
- some discrepancies in SD Connect nomenclature
- Account is missleading. because if you change project it changes. It should be name project ID, could this one day become a link? (like MyCSC)?
-links to cloud (can they be links to user guide)
- could we add the public key here?
- how do they find the ID linked to the project? there is a way
- shared to the project (can they access that from SD Desktop or do they need to copy it?)

















