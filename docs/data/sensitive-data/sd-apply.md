# SD Apply


Sensitive Data Apply (SD Apply) is a simple web-user interface that guides you during the application for data access rights. 

Sensitive data published under controlled access are linked to a Data Access Committee: a body of one or more named individuals who are responsible for granting data access to external applicants (or requestors) based on specific policies. 

SD Apply facilitates the communication between an applicant and a DAC, automating the application process, 
ensuring the availability of all the necessary information and providing a record of the application's history. 

Once the application has been reviewed and approved, the applicant can directly analyze the datasets SD Desktop, a cloud computing environment part [CSC Sensitive Data Services for research](https://research.csc.fi/sensitive-data-services-for-research).

- Data access for applicants
- Data approval for data owners

## Data access for applicants: overview

![SD Applyv1](https://user-images.githubusercontent.com/83574067/148039341-24feb45e-06b4-4f48-bc04-c3816041ee7b.png)


### Login

Login to SD Apply is possible with user identity federation systems (Haka, Virtu and [Elixir Login](https://elixir-europe.org/register)) or with  [CSC login](./accounts/how-to-create-new-user-account/) at

[https://sd-apply.csc.fi](https://sd-apply.csc.fi)

The interface is compatible with all modern web browsers. 

!!! Note
    If you own several user accounts, please always use the same login method to access SD Apply from multiple identities provided. 



### Apply for access

After login, you will access SD Apply catalog Page. On this page, you can search for a specific dataset and start the application process by clicking on **Add to cart**. You can select multiple datasets, and they will then appear in your cart. By clicking on **Apply**, you will be redirected to the **Application form**.




### Submit the application form

Follow the instructions on the application form and fill in the required fields:

- State: you can visualize all the details about the Application

- **Applicants**: Every person processing or having direct or indirect access to the data is considered a member of the research group and must be named. Members can be added, changed, or removed without re-applying. You can invite other people to join your Application by selecting **Invite member** providing their names and email addresses. They will then get an invitation email and, following the link, log in to SD Apply and accept the license terms and Data Acess Agreement. When the Application is approved, they will also be granted access to the same dataset(s).

- Resources: visualized all the datasets you are applying for

- **Terms of use**: lists all the licenses defining the terms and conditions for data access and re-use (e.g., Data Access Agreement). To access, click on **Accept terms of use**

- **Application**: Access to a dataset is granted for a single, designated purpose only. Add the necessary information about your research: research/study name, research plan abstract, Data access start date, Data access end date.

Select the type of submission: FEGA or SDA?

To submit your Application, select **Send Application**. Unfortunately, it is no more possible to edit or delete the Application; however, it is possible to remove members.
If you want to use one of the old applications as a template for a new application, select Copy as new. Note that if your old Application has attachments (e.g. research plan), they will also be copied.


### Wait for approval

After you have sent the Application, it will be forwarded to the Data Acess Committee,  which evaluates it, granting the access rights. 

During the approval process, a Data Acess Committee can:

- approve or reject your Application
- return the Application asking for additional information
- close your Application and cancel the application process
- add comments to your Application

You can follow the approval process and read the possible comments from the Application's Events section. In addition, you can find all your applications and see their state from the Applications tab:

- Draft: Your Application is still a draft and can't be seen by the Data Acess Committee. You can continue working on your Application or delete it entirely from the system.

- Submitted: The Application has been sent to the Dat Acess Committee and can not be edited anymore unless specifically requested.

- Approved: The Application has been approved, and you have been granted access rights.

- Rejected: To see why your Application was rejected, navigate the Application and select View. Data Acess Committee comments will be shown in the Events section.

- Returned: If the data owner needs additional information regarding your Application, they can return your Application to you. To edit the Application, follow the link in the email or log in to SD Apply, navigate to the Application, and select View. You can see the Data Access Committee's comments in the Events section. Then, make the changes select Send application.

- Revoked: Your Application, and thus your access rights, have been revoked by the Data Access Committee.


**You will receive an email notification whenever the state of your application changes.**



### Set up your Desktop

Once your Application has been approved, you will receive a notification and further instructions. Briefly, you can now access the data in SD Desktop, a private cloud computing environment. When logging in, use the same user account/identity provider you have used for SD Apply log in: HAKA, VIRTU, CSC login, or ELXIR login.
To set up your workspace, you need a CSC account, a CSC project, and service access to SD Desktop. 
Check the SD Desktop user guide for more information and CSC Sensitive Data Services for the Research web page.


### Export your results
Once your analysis is completed, you can export the results from the computing environment. After that, however, data access will be revoked, and to re-grain access o the same dataset, you need to start a new application.



## Data approval for data owners (DACs)
