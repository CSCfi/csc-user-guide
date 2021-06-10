# SD Connect (Sensitive Data Connect)








## Login 

To access SD Connect you need:

* **a CSC account**
* **a CSC project**
* **Service access to Allas** (CSC cloud storage solution)

Login to SD Connect is possible with user identity federation systems (Haka, Virtu and Elixir AAI) or with a CSC account at https://sd-connect.csc.fi/ using any modern web browser.


!!! note
    Sensitive data need to be encrypted before upload to SD Connect. Check the previous paragraph for more informations about encryption with Crypt4GH.


!!! note
    Currently, users may not process any personal data granted for the purposes of the Act on the Secondary Use of Health and Social Data (552/2019) by ***Findata.***








## SD Connect User Interface

Once you Login in SD Connect you access the default front-page: **Browser**.

In this page you can :

* view all **the containers (or buckets) available in your CSC project**, in which you can store encrypted sensitive data. The containers can be created, downloaded, deleted or shared, using the appropriate icons;

!!! note
    

*  **list and select your CSC project** from the drop down menu bar (top left corner) to visualize container or data belonging to a specific project;

*  open any container (double click) and view  thi contents (uploaded files or folders). Any file can be downloaded from the container or shared using the download link. From this view, you can also download the entire container, delete file or upload new files and folders.


<img width="544" alt="Screenshot 2021-06-10 165847" src="https://user-images.githubusercontent.com/83574067/121538121-335c3a80-ca0d-11eb-89eb-55c9e0d8fb94.png">

<img width="569" alt="Screenshot 2021-06-10 172357" src="https://user-images.githubusercontent.com/83574067/121542307-b7fc8800-ca10-11eb-9125-150bfb5fa0ed.png">  







In the  **User information** page you can:

* in Currently Consumes view statistics about the selected CSC project resource usage: billing unit consumption and the total project storage usage (defount storage 10TiB);

* in **Project usage** you can view the **SD Connect Account, an ID associated your CSC project**. This ID is required when you want to share containers with other CSC projects using SD Connect user interface.

* access the **Token icon** through which you can generate a temporary token (necessary for data upload programmatically, using Swift client. For more info check below).



<img width="515" alt="Screenshot 2021-06-10 184144" src="https://user-images.githubusercontent.com/83574067/121555306-905eed00-ca1b-11eb-991d-7bc53e719a3c.png">




In the **Shared** page:


* in **Shared to the project** you can view the **containers or bukets that other CSC projects (belonging to your colligues or collaborators) shared with you**. With double click you can access the container and view the content (if you have reading access) or add files to the container (if you have edits rights). 

!!! note 
    All the container listed here, are own by another users, that can decide when revoke your access. You will not be able to access the file from SD Dekstop untill you make a copy of the container. 


* in **Shared with the project** you can view the containers or bukets which  **you shared with other CSC projects**. In this case you own the shared containers or bukets and you can decide when revoke access. 



![](img/SDConScreenshot_6.png)




Naming: 





# Drag and Drop data upload (limits)


# Data Download


# Data Sharing  from your project to  other CSC users's project



# Data Sharing from other CSC users to your project


# Container deletion



# Data upload using CLI for SD Connect


## Linux enviroment


## Windowns enviroment


## MacoS





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

















