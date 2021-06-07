
# SD Connect (Sensitive Data Connect)

## Login 

To access SD COnnect you need:

* **a CSC account**
* **a CSC project**
* **Service access to Allas** (CSC cloud storage solution)

Login to SD Connect is possible with user identity federation systems (Haka, Virtu and Elixir AAI) or with a CSC account at https:https://sd-connect.csc.fi/
using any modern web browser.

!!!Note: Users may not process any personal data granted for the purposes of the Act on the Secondary Use of Health and Social Data (552/2019) by ***Findata.***


## SD Connect User Interface

# Browser

Once you Login in SD Connect you access the default front-page: **Browser**. 

SD Connect Browser page shows the containers available in your CSC project, as well as general information about them. 

![](img/SDConScreenshot_1.png)

The container can be opened with a double-click, or if the table row is active, enter.
Any container can be opened, and the contents (uploaed files or folders) viewed. The object page shows information on the objects, e.g.

        The object name

        The object ETag  ??

        A download link for the object

        Content type

        Last date of modification


![](img/SDConScreenshot_2.png)


On the top left corner, you can *select your CSC project* from the drop down menu bar. 


![](img/SDConScreenshot_2.png)

# User Information

Behind the **User information** button in the front page, a user information dashboard is displayed. The dashboard displays statistics about the current resource usage, e.g.

        Current billing unit consumption

        Amount of containers and objects in a project

        Total project data usage.
        
        SD Connect account ( also defined as project ID when using the command line tool)

Additional information on different billing details is also provided, in the links contained in the dashboard bottom tile.

# Shared

In the **Shared** page you can:

* in **Shared to the project** visualize the containers or bukets that other CSC users shared with you: From this view the shared access can be revoked, a new share initiated, or existing access synchronized to the sharing back-end, thus enabling it to be queried from the back-end in the future. (?)

* in **Shater with the project** visualize the containers or bukets that you shared with other CSC users: From this view the granted access can be viewed, and any container can be opened just like when using the normal container browsing view. All features available in the ordinary container view work, such as downloading, uploading (if write access is granted to the container) and copying the container.











