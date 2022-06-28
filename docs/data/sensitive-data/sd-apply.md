# SD Apply
Sensitive Data Apply (SD Apply) is a service for applying access rights to sensitive datasets stored at CSC. In practice, it’s a simple web user interface that guides you during the application process.

Each sensitive dataset that is published under controlled access is associated with a Data Access Committee (DAC). The DAC is a body of one or more named individuals who are responsible for granting data access to external applicants (or requesters) based on specific policies. SD Apply facilitates the communication between a data applicant and the DAC by automating the application process, ensuring the availability of the necessary information and providing a record of the application history. Once the application has been reviewed and approved, the data applicant can directly analyse the datasets in SD Desktop – a cloud computing environment part of [CSC Sensitive Data Services for research](https://research.csc.fi/sensitive-data-services-for-research).

The following is a step-by-step guide to SD Apply that illustrates: 

- **[Data access for Data Applicant](https://github.com/CSCfi/csc-user-guide/edit/wip-at-fega/docs/data/sensitive-data/sd-apply.md#data-access-for-data-applicant)**
- **Data approval for Data Access Committee (DAC)**

## Data access for Data Applicant
### Step 1: Login
Login to SD Apply is possible with user identity federation systems (Haka, Virtu and Elixir login) or with CSC login at https://sd-apply.csc.fi. The interface is compatible with all modern web browsers.

!!! note
    If you own several user accounts, please always use the same login method to access SD Apply from multiple identities provided.

### Step 2: Apply for access
After login, you will access the SD Apply Catalogue page. On this page, you can search for a specific dataset and start the application process. Start a new application by clicking on *Add to cart* button next to the name of the dataset. You can select multiple datasets, and they will all appear in your cart under the Catalogue title. By clicking on *Apply*, you will be redirected to the application form.

### Step 3: Submit the application
Follow the instructions on the application form and fill in the required fields:

- **State**. Contains basic details like title and state of your application.
- **Applicants**. Everyone who processes or has direct or indirect access to the data is considered as a research group member and must be named in the Applicants field. Members can be added, changed, or removed without re-applying. You can invite other people to join the data access application by selecting Invite member and providing their names and email addresses. They will then get an invitation email. By following the invitation link, they can log in to SD Apply and accept the terms of use and Data Access Agreement. When the application is approved, all the applicants will be granted access to the same dataset(s).
- **Resources**. Shows all the datasets you are applying for
- **Terms of use**. Lists all the licenses defining the terms and conditions for data access and re-use (e.g. Data Access Agreement). To access, click on Accept terms of use.
- **Application**. Access to a dataset is granted for a single, designated purpose only. Add the necessary information about your research: research/study name, research plan abstract, Data access start date and Data access end date.

To submit your Application, select *Send application* under Actions. Unfortunately, editing or deleting the application is no more possible after sending the application. However, removing members is still possible. If you want to use the application as a template for a new application, select *Copy as new application*. Note that the attachments (e.g. research plan) of your old application will also be copied.

### Step 4: Wait for approval
After you have sent the Application, it will be forwarded to the Data Access Committee, which evaluates it and grants the access rights.

During the approval process, a Data Access Committee can:
- approve or reject your application.
- return the application asking for additional information.
- close your application and cancel the application process.
- add comments to your application.

You can follow the approval process and read the possible comments from the Application events section. In addition, you can find all your applications and see their state from the Applications tab:

- **Draft**. Your application is still a draft and cannot be seen by the Data Access Committee. You can continue working on your application or delete it entirely from the system.
- **Submitted**. The application has been sent to the Data Access Committee and cannot be edited anymore unless specifically requested.
- **Approved**. The application has been approved, and you have been granted access rights.
- **Rejected**. To see why your application was rejected, navigate the application and select View. Data Access Committee comments will be shown in the Events section.
- **Returned**. If the data owner needs additional information regarding your application, they can return your application to you. To edit the application, follow the link in the email or log in to SD Apply, navigate to the application, and select View. You can see the comments of the Data Access Committee in the Events section. Then, make the changes and select Send application.
- **Revoked**. Your Application, and thus your access rights, have been revoked by the Data Access Committee.

You will receive an email notification whenever the state of your application changes.

### Step 5: Set up your Desktop
Once your Application has been approved, you will receive a notification and further instructions. You can now access the data in SD Desktop, a private cloud computing environment. When logging in to SD Desktop, use the same user account/identity provider (HAKA, VIRTU, CSC login, or ELXIR login) you have used for SD Apply log in. To set up your workspace, you need a CSC account, a CSC project, and service access to SD Desktop. 

!!! note
    If you are a new CSC user, please check these instructions on CSC [accounts](https://docs.csc.fi/accounts/). Check also the [SD Desktop user guide](https://docs.csc.fi/data/sensitive-data/sd_desktop/) and [CSC Sensitive Data Services for Research webpage](https://research.csc.fi/sensitive-data-services-for-research) for more information. 

### Step 6: Export your results
Once your analysis is completed, you can export the results from the computing environment. After that, data access will be revoked. To get access to the same dataset, you need to start a new application process.

