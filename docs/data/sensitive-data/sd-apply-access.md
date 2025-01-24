# Data access for Data Applicant

## Step 1: Apply for access

To access a specific dataset hosted in Finnish FEGA, navigate to the [EGA webpage](https://ega-archive.org/studies) and search for a particular study, dataset, or DAC using the search field at the top of the page. Then, in the Study view, click on the Dataset ID (EGADNNNN). In the Dataset view, under “Who controls access to this dataset”, click on the link that allows you to access the application form using SD Apply. SD Apply is a service for applying access rights to sensitive datasets stored at CSC. 

[![EGA webpage study and dataset view](images/fega/fega_search.png)](images/fega/fega_search.png)

!!! note
    In the EGA webpage, you can also find datasets that are hosted outside Finland, in central EGA or other FEGA nodes. However, this workflow is specific for datasets that are hosted in Finnish FEGA. 

Alternatively, if you know the dataset ID you can search for it from [SD Apply Catalogue](https://sd-apply.csc.fi/catalogue) page under FEGA category. Note that you have to login to apply for access.

## Step 2: Login to SD Apply

Login to [SD Apply](https://sd-apply.csc.fi) by using your identity provider (Haka, Virtu and ELIXIR login) or with CSC account credentials. The interface is compatible with all modern web browsers.

!!! note
    Always use the same identity provider (e.g. Haka, CSC) when you log in to SD Apply because all your actions are connected to your login identity. You also have to use this same login method in the SD Desktop service to get access to the SD Apply data.

[![SD Apply login page](images/apply/apply_login.png)](images/apply/apply_login.png)

## Step 3: Fill application

After login, you will access the SD Apply Catalogue page. On this page, you can search for a specific dataset and start the application process. 

Start a new application by clicking on *Add to cart* next to the name of the dataset. You can select multiple datasets, and they will all appear in your cart under the "Catalogue" title. By clicking on *Apply*, you will be redirected to the application form.

[![SD Apply "Catalogue" page](images/apply/apply_catalogue.png)](images/apply/apply_catalogue.png)

## Step 4: Submit the application

Follow the instructions on the application form and fill in the required fields. Access to a dataset is granted for a single, designated purpose only. 

**Inviting members to application**:

Everyone who processes or has direct or indirect access to the data is considered as a research group member and must be named in the Applicants field. 

- Add your research group members to the application by clicking *Invite member* and providing their name and email address. The invited research group members will receive an email and by following the invitation link in the email, they can log in to SD Apply and join the application. In SD Apply they have to accept the terms of use and Data Access Agreement the data controller has defined. 
- When the application has been approved, all members of the application will be granted access to the same dataset(s) after they have accepted the agreements and terms of use in SD Apply.

**Terms of use**: 

The terms of use and agreements the data controller has defined for data access and re-use (e.g., Data Access Agreement) are all listed under Terms of use. After you have read and understood the terms click *Accept terms of use*.

Before sending the application, ensure:

- You are applying access to the right datasets. These are showns in the resources field.
- You have added all the research group members to the applicant field.
- You have filled in all necessary information to the application form. 

To submit your application, select **Send application** under **Actions** (top right). 

 - After sending, you can't edit or delete the application, but you can still remove members. If you want to edit the application, please ask the data controller to return the application to you for editing. 
 - To use your past application as a template for a new application, select **Copy as new application** under **Actions** (top right). Attachments from the old application will also be copied.

[![SD Apply application form](images/apply/apply_application.png)](images/apply/apply_application.png)

## Step 5: Wait for approval

After you have sent the application, it will be forwarded to the Data Access Committee (DAC), who evaluate your application and either grant or deny access to the dataset. You will receive an email notification about DAC's decision. You can follow the approval process and read the possible comments from the "State" section on top of the application form. 

If the data controller needs additional information regarding your application, they can return your application to you. To edit the application, follow the link in the email or log in to SD Apply, navigate to the application, and select *View*. You can see the comments of the Data Access Committee in the State section. After you have made the necessary changes select *Send application*.

You can find all your applications and see their state from the "Applications" tab in SD Apply. You will receive an email notification whenever the state of your application changes.

[![SD Apply Applications tab](images/apply/apply_state.png)](images/apply/apply_state.png)

## Step 6: Project members join the application

If you have invited members in the application, they will receive an invitation email.

To access the data all members should:

1. Click the link in the email and sign in to SD Apply. They will land on the application page.
3. Scroll down to Term of use section.
4. Read terms of use and then click **Accept terms of use**.

![SD Apply terms of use](https://a3s.fi/docs-files/sensitive-data/SD_Apply/SD-Apply_Termsofuse.png)


## Step 7: Access SD Desktop

Once your application has been approved, you will receive a notification and further instructions via email. You can now access the data in SD Desktop, a private cloud computing environment. 

Read more how to create a CSC project and access SD Desktop:

* [Access SD Desktop](./sd-access.md)

## Step 8: Access the data

Once you sign in to your virtual desktop, you can access the data using Data Gateway application. Follow these steps:

* [Create virtual desktop](./sd-desktop-create.md)
* [Import data to virtual desktop](./sd-desktop-access.md) Use SD Apply option in Data Gateway
* [Working with virtual desktop](./sd-desktop-working.md)

When you login to SD Desktop, remember to use same login method you used to log in to SD Apply. 

## Step 9: Export your results

Once your analysis is completed, you can export the results from the computing environment. After that, the data access will be discontinued. To get access to the same dataset, you need to start a new application process. Follow these steps:

* [Export data from virtual deskotop](./sd-desktop-export.md)

## Support

If you have questions about using SD Apply, please contact [CSC Service Desk](../../support/contact.md) (subject: SD Apply).

If you have questions regarding the application form or the dataset you are applying for access, please contact the data controller or the Data Access Committee.
