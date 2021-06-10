
# SD Connect (Sensitive Data Connect)








## Login 

To access SD Connect you need:

* **a CSC account**
* **a CSC project**
* **Service access to Allas** (CSC cloud storage solution)

Login to SD Connect is possible with user identity federation systems (Haka, Virtu and Elixir AAI) or with a CSC account at https:https://sd-connect.csc.fi/ using any modern web browser.


!!! note
    Sensitive data uploaded to SD Connect need to be encrypted. Check the previous paragraph for more informations about encryption with Crypt4GH.


!!! note
    Users may not process any personal data granted for the purposes of the Act on the Secondary Use of Health and Social Data (552/2019) by ***Findata.***








## SD Connect User Interface

Once you Login in SD Connect you access the default front-page: **Browser**. This page shows the containers (or bukets) available in your CSC project, as well as general information about them. 








<img width="959" alt="Screenshot 2021-06-10 134145" src="https://user-images.githubusercontent.com/83574067/121511795-b4a5d400-c9f1-11eb-9ad9-2b0b362ee387.png">










Any container can be opened, and the contents (uploaed files or folders) viewed. The object page shows information on the objects, e.g.
The object name, A download link for the object, Content type, Last date of modification.






<img width="959" alt="Screenshot 2021-06-10 134412" src="https://user-images.githubusercontent.com/83574067/121512161-19612e80-c9f2-11eb-8c6d-9e342f7804c1.png">










On the top left corner of the browser page, you can **list your CSC project** from the drop down menu bar. 






<img width="959" alt="Screenshot 2021-06-10 134657" src="https://user-images.githubusercontent.com/83574067/121512458-66dd9b80-c9f2-11eb-8a91-8dc6b6bcdc70.png">










If you click on the **User information** button in the front page, you will access thea page that displays:

statistics about the current resource usage (billing unit consumption, amount of containers and objects (files or folders) present in each CSC project, the total project data usage. 




  <img width="958" alt="Screenshot 2021-06-10 135303" src="https://user-images.githubusercontent.com/83574067/121513216-46621100-c9f3-11eb-8274-4b60047cdf7e.png">      









   
Morever, the page displays also the SD Connect Account. You can give this 





<img width="959" alt="Screenshot 2021-06-10 135501" src="https://user-images.githubusercontent.com/83574067/121513399-7c9f9080-c9f3-11eb-8199-b3caddc180df.png">





And the token icon. From here you can generale a token necessary to upload data to SD Connect programmatically. For more info, check the ...below.


<img width="959" alt="Screenshot 2021-06-10 135501" src="https://user-images.githubusercontent.com/83574067/121513769-e5870880-c9f3-11eb-8b50-2b1bc43399c9.png">
<img width="960" alt="Screenshot 2021-06-10 135637" src="https://user-images.githubusercontent.com/83574067/121513758-e0c25480-c9f3-11eb-8d1e-c6a9b0c83ef8.png">




## Shared

In the **Shared** page you can:


* in **Shared to the project** visualize the containers or bukets that other CSC users shared with you: 

From this view the shared access can be revoked, a new share initiated, or existing access synchronized to the sharing back-end, thus enabling it to be queried from the back-end in the future. (?)


![](img/SDConScreenshot_5.png)

* in **Shater with the project** visualize the containers or bukets that you shared with other CSC users: 

From this view the granted access can be viewed, and any container can be opened just like when using the normal container browsing view. All features available in the ordinary container view work, such as downloading, uploading (if write access is granted to the container) and copying the container.


![](img/SDConScreenshot_6.png)

# Buket or Container creation in SD Connect


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
























