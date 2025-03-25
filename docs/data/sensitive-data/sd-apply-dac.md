 

# Enabling reuse of FEGA data

Access to data that are stored at CSC and published under controlled access are managed by the data controller or their representatives in the SD Apply service. To enable reuse of datasets stored in Finnish Federated EGA (FEGA) you need to add the datasets your organisation offers to the catalogue in SD Apply. Please note, when you use SD Apply to manage access to datasets stored in FEGA, your organization needs to have a service agreement with CSC in place. Read more about [FEGA legal agreements](./fega-submission.md#step-1-legal-agreements-data-access-committee-and-policies).

As a data controller in SD Apply, you are responsible for:

* Adding your datasets to catalogue in SD Apply together with an application form and policies.
* Designating representatives (a Data Access Committee, DAC) who manage the data access requests to your organization’s datasets.
* Defining data access policies for data reuse.

## Forming a Data Access Committee (DAC)

Before you start adding information in SD Apply, we recommend discussing inside your organization about the possibility of forming a general Data Access Committee (DAC) that manages access to all datasets your organization is the data controller of. 

DAC is responsible for:

- **Coordinating and approving new FEGA submissions inside their organisation**: Reviewing the datasets that will be submitted in the Federated EGA under their organization and controllership.
- **Managing access to organization's datasets**: Evaluating data access requests for datasets managed by the DAC to ensure compliance with defined policies, regulations, and ethical guidelines.

## Adding a dataset to catalogue in SD Apply

![SD Apply Infograph](https://a3s.fi/docs-files/sensitive-data/SD_Apply/SD_Apply_infographic.png)

Adding datasets to SD Apply for the first time is made in close collaboration with CSC Service Desk as the process can be a bit complicated. Please reserve time for the process and prepare to discuss with your legal team about the agreements needed for data reuse. Below are general instructions to guide you through the process.

## Step by step guide

### 1. Request for organization profile

Before you can add information to SD Apply, CSC service desk needs to create an organization profile and set you as the organization administrator. 

1. Send an email to servicedesk@csc.fi with the subject "SD services" to request profile creation.
2. Log in to [SD Apply service](https://sd-apply.csc.fi/).
3. Inform the service desk that you have logged in. Service desk will add you to right organization.
4. The service desk will inform you when you can start adding datasets to SD Apply. 

!!! note
    Always use the same identity provider (Haka/Virtu or CSC login) when logging into SD Apply because your role and datasets you manage are connected to your login identity.

### 2. Add dataset as catalogue item

Cataloque item enables applicant to apply for access for your dataset. When you add datasets to be applied via SD Apply, you have to first create:

* **Form:** applicants use the application form to apply for access rights.
* **Policy (optional):** Data access agreements which describe how applicants can re-use data.
* **DAC:** Data Access Committee process applications.
* **Identifier:** a technical identifier for the dataset, for example a DOI.

Then you combine these items together by creating a catalogue item. You can also reuse existing items. 

!!! note
    You have to create form, policy, DAC and identifier items **before** creating a catalogue item.

### 2.1. Create an application form

The data controller specifies what information the applicant must provide in the application form to access the data.

1. Log in to SD Apply and navigate to Administration > Forms.
2. Select **Create form**.
3. Give the form a descriptive name. The name will show in the form list view to help you find it but it is not shown to the applicant.
4. Give the form a title. This is shown to the applicant. 
5. Add the fields you want to have in the application. The preview on the right side shows how an applicant would see the application form. The form field options are explained in more detail below.
6. Select **Save** when you are finished with the form.

!!! note
    You can only edit the form as long as it has not been connected to a catalogue item.

It's recommended to include the parts of the agreements that need to be filled in directly in the application form in SD Apply. The rest of the agreement content can be provided as a PDF attachment and added as policy in SD Apply, allowing applicants to review and accept the terms electronically when requesting access to the dataset. This way, applicants can complete the necessary sections within SD Apply and accept the terms of use without needing to manually sign documents. Please discuss with your organization's legal team about this possibility.

#### Form fields explained

- **Application title**: Use this field if you want the applicants to provide a name for their application.
- **Option list**: Use option list if you want the applicant to choose one of the given options. ID-code is the identifier for the option. It is shown, for example in the reports, but the applicant will only see the label fields. For example: You can put “Y” as an ID-code for Yes-option and “N” for No-option.
- **Multi-select list**: Use a multi-select list if you want the applicant to choose one or more of the given options.
- **Table**: Provide a set of columns for the table. The applicant can add as many rows as they wish. All columns are required for each row. You can require the applicant to fill in at least one row.
- **Email address**: Email address field will validate the email the applicant has provided.
- **Attachment**: Applicant can add one or multiple attachments.
- **Label**: Use labels as descriptive texts if you want to give the applicant additional information, such as instructions, regarding some field.
- **Header**: Consider using headers if you want to divide the application form into sections.
- **Phone number**: A phone number in an international format (E.164), e.g. +14155552671.
- **IP address**: IP address field will validate the IP address the applicant has provided in IPv4 or IPv6 forms. IP address must not be within the known private range.

#### Creating conditional fields 

If needed, you can create fields that are hidden or shown to the applicant depending on their answers.

For example, you can create an option list “Do you want to add attachments?” Yes - No. If the applicant chooses “Yes” the attachment field is shown to the applicant. If they choose “No” they will not see the attachment field.

!!! note
    Conditional fields only work with Option list and Multiselect fields.

1. Create an **Option list** and fill in the options
2. Create another field of any field type.
3. In the field you just created, select Additional settings>Visible>Only if
4. Field: Locate the Option list you created earlier from the drop-down list
5. Has one of the values: Select when you want the list to be shown. In this example, Field 2 "Add one or multiple attachments" is shown if the applicant chooses the "Yes" option in Field 1, "Do you want to add attachments?".

You can test how the fields work in the Preview section on the right of the page.

### 2.2. Create a policy 

Policies define the agreements and terms of use that the applicant has to accept to be able to use the data. Policies are shown as part of the application form and every research group member who applies for access has to accept the policies before they are able to access the data.

You can create three types of policies:

- **External link**: Provide a link to an external page with terms of use. Use links, for example, when you want to license your resources using standardised licenses, such as [Creative Commons](https://creativecommons.org/choose/?lang=en).
- **Inline text**: Write the terms of use in the application form. The applicant will see it as normal text in the application form.
- **Attachment**: Upload a file that the applicant can download and accept when they fill in the application form. We recommend using PDF format. We recommend drafting the policy attachments in the way that allows the applicant to agree to them by accepting the terms of use electronically in SD Apply.

#### Data Access Policies in the Finnish Federated EGA

Data deposition to the Finnish Federated EGA requires a series of legal agreements: a Service Agreement for Federated EGA and a Data Access Agreement including a Data Transfer Agreement. 

**Data Access Agreement**: The Data Access Agreement (DAA) is a contract between the Data Access Committee (DAC) and an applicant seeking access to the data for reuse. Through the DAA, the data controller can define conditions and restrictions for data reuse, including policies governing data use, publication, download, and access. The DAA should also include a Data Transfer Agreement (DTA), necessary when researchers from non-EU/non-EEA regions access the data via SD Desktop. DAA and DTA will be included in the Polcies in SD Apply. For further information, please contact your home organization's legal services. You can [download an example template](https://ega-archive.org/assets/files/Example_DAA.doc) provided by the EGA.

Consult your organization's legal experts to define data access policies that are appropriate for this purpose.  

Policies are optional. You cannot edit the policy after you have created and saved it.

### 2.3. Create a DAC

By creating a DAC, you assign a Data Access Committee (DAC) members as application handlers. They approve or reject data access requests for your organization's datasets and receive email notifications of new applications.

You can choose between two different processes: A dynamic process and a decider process. Choose the one which suits your organisation best. Remember to give your DAC a descriptive name so it will be easier for you to find it later.

- **A default process**: DAC members are in full charge of approving or rejecting applications. In addition, there can be reviewers and deciders. Only one DAC member has to approve the application. 

- **A decider process**: Restricted version of the default process. The DAC members do not have the authority to approve or reject applications. They have to request a separate decider user to approve or reject the application. 

#### Assign DAC members

Add DAC members as application handlers by searching the user by their username or locating them from the drop-down list. We recommend **assigning more than one handler to a DAC** to make sure there are enough handlers to process all the applications. 

!!! note
    You can **only find handlers that have previously logged in to SD Apply**. If you cannot find the handler you were looking for, please ask them to log in and try again.

If you want to hide the names of the application handlers (DAC, reviewers, deciders) from the applicant, select the checkbox *Anonymized handling*.

DAC members do not get notified when they have been assigned as a handler, but they receive emails about new applications.

#### Add a form to a DAC

If you know all the datasets your organization manages in SD Apply will use the same application form, you can connect the form you created to a DAC by selecting the form from the dropdown menu.  

If you want to ask dataset specific questions from the applicant, you can create two application forms and connect the form with general questions to the DAC, and another form with dataset specific questions to the catalogue item. In this case, the applicant will see the application forms two parts and will fill in both forms. 

#### Add a policy to a DAC

If you know all the datasets your organization manages in SD Apply will have the same terms of use and agreements, you can connect the policies you created to a DAC  by selecting them from the dropdown menu.

Unfortunately, we currently have a technical limitation of 1 MB for PDF attachments. **Please optimise your PDF file before adding it to SD Apply**.  

This way these polcies will be added automatically to all catalogue items that use the same DAC. You can also add dataset specific terms of use by connecting a policy to a identifier. 

### 2.4. Create a identifier

When a researcher submits data to Federated EGA, they receive a unique identifier for their dataset, for example EGAD12345. To make the dataset available for reuse through SD Apply, the FEGA Submitter should send this identifier to the data controller so that it can be added to SD Apply. 

1. Add the identifier the FEGA submitter provided to you in the identifier field. 
2. Select the policies you want to connect to your identifier by choosing the policies you have created from the drop-down list. Policies are optional.

!!! note
    You cannot edit the identifier after you have created and saved it. If you want to change something after you have created an identifier, you should create a new identifier and archive the old one.

### 2.5. Create a catalogue item

Catalogue item connects the items you have created into a single dataset to which the applicant can apply for access. 

1. In the title field, provide a descriptive name for the dataset. It will make it easier for the applicants to recognise which dataset they want to apply access to.
2. If there is more information about the dataset on another website, you can add a link to the More info field.
3. Select the DAC you have created from the DAC drop-down.
4. Select the identifier for the dataset you want to add to SD Apply from identifier drop-down.
5. If you didn't connect the form to the DAC, select the application form you have created from the drop-down list.
6. Select FEGA as category.
7. **Enable the catalogue item to show it to applicants**. The catalogue item is disabled at first so no one will be able to apply access to it before it is enabled. After you enable the catalogue item, it will show as a dataset on the Catalogue page.

#### Editing catalogue items

You can edit the catalogue item’s name, organization and links to additional information by selecting edit.

!!! note
    After saving, you cannot edit form, DAC or identifier connected to the catalogue item. Editing is also not possible when some part of the catalogue item is disabled.

If you want to change the application form and/or the DAC of one or multiple catalogue items, select the catalogue items you want to edit by clicking the checkbox and then **Update catalogue item**.

This will **disable and archive the old catalogue item** and create a new updated catalogue item. This means that the applicants cannot see or apply for access to the old catalogue item anymore.

## Adding more datasets under your organisation

When you have created a form, necessary policies, and a DAC once, you can reuse these items for future dataset submissions, if the datasets have the same DAC.

Add a new dataset to SD Apply catalogue with the same DAC:

1. Create a new **identifier**. The FEGA submitter should provide you the unique identifier for their dataset. 
2. Create a **catalogue item** by combining the items you previously created (identifier, form, DAC)
3. Enable the catalogue item so it shows for the applicants.

Make sure that necessary agreements are either combined with the DAC you use or every new identifier you add to SD Apply. 

## Disabling, and archiving items

You can disable and archive all the items. Deleting is not possible because we want to offer a full history of events for information security reasons.

### Disabling items

When you disable an item, for example a form, it **cannot be used in any new catalogue items anymore**. Disabled items will be hidden from the drop-down lists.

**If you disable a catalogue item**, the applicant will not be able to apply for access to it anymore. However, if they have applied for access to the catalogue item before disabling, the handler can still complete the application process and approve or reject the application.

You can re-enable disabled items.

### Archiving

Archiving **hides the item from the administration view and from the applicants**. If you want to view archived items select **Display archived**. We recommend archiving old items that are not in use anymore.

You can unarchive archived items.

Handlers are warned if the catalogue item the applicant has applied for access, has been disabled or archived. 

## Support

If you have questions about using SD Apply, please contact [CSC Service Desk](../../support/contact.md) (subject: SD Apply).
