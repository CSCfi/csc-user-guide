
# SD Connect (Sensitive Data Connect)

## Login 

To access SD Connect you need:

* **a CSC account**
* **a CSC project**
* **Service access to Allas** (CSC cloud storage solution)

Login to SD Connect is possible with user identity federation systems (Haka, Virtu and Elixir AAI) or with a CSC account at https:https://sd-connect.csc.fi/ using any modern web browser.

---
**NOTE**

It works with almost all markdown flavours (the below blank line matters).

---


---
header-includes:
    - \usepackage[most]{tcolorbox}
    - \definecolor{light-yellow}{rgb}{1, 0.95, 0.7}
    - \newtcolorbox{myquote}{colback=light-yellow,grow to right by=-10mm,grow to left by=-10mm, boxrule=0pt,boxsep=0pt,breakable}
    - \newcommand{\todo}[1]{\begin{myquote} \textbf{TODO:} \emph{#1} \end{myquote}}
---

blah blah

\todo{something}

blah


---
title: "Get Started"
output: flexdashboard::flex_dashboard
---

```{r setup, include=FALSE}
library(flexdashboard)
```

Column 1
--------------------------------------------------

### Chart A

```{r}
```

Column 2
--------------------------------------------------

### Chart B

```{r}
```

### Chart C

```{r}
```







!!! Note
    Sensitive data uploaded to SD Connect need to be encrypted. Check the previous paragraph for more informations about encryption.


!!! Note
    Users may not process any personal data granted for the purposes of the Act on the Secondary Use of Health and Social Data (552/2019) by ***Findata.***


# SD Connect User Interface

## Browser

Once you Login in SD Connect you access the default front-page: **Browser**. 
<img width="641" alt="SDDkSreenshot_3" src="https://user-images.githubusercontent.com/83574067/121243305-3f79b800-c8a6-11eb-891b-08a9e09ff536.png">
SD Connect Browser page shows the containers available in your CSC project, as well as general information about them. 


Any container can be opened, and the contents (uploaed files or folders) viewed. The object page shows information on the objects, e.g.
The object name, The object ETag  ??, A download link for the object, Content type, Last date of modification.

<img width="607" alt="SDDkSreenshot_1" src="https://user-images.githubusercontent.com/83574067/121242837-af3b7300-c8a5-11eb-9752-7bd4f3f21a77.png">
![](img/SDConScreenshot_1.png)


![](img/SDConScreenshot_2.png)


On the top left corner, you can *select one of your CSC project* from the drop down menu bar. 


![](img/SDConScreenshot_3.png)


## User Information ( this should be changed to Project information before the 22th)

Behind the **User information** button in the front page, a user information dashboard is displayed. The dashboard displays statistics about the current resource usage, e.g.

        Current billing unit consumption

        Amount of containers and objects in a project

        Total project data usage.
        
        SD Connect account ( also defined as project ID when using the command line tool)


![](img/SDConScreenshot_4.png)

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
























