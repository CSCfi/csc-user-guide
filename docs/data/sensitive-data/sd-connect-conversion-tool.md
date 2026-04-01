# SD Connect Conversion tool

<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **If your project has more than 4 TB of data**
  { .csc-grid-card-warning }

    ---
    
    If your project has more than 4 TB of data, contact **servicedesk@csc.fi** with topic "Sensitive Data". We plan conversion process together with you. 

</div>


## 1. Prepare for conversion

Review your project's buckets together with the team. We recommend [deleting](sd-connect-delete.md) unneeded files and buckets from SD Connect before starting conversion as this shortens conversion time. It also saves resources for other research projects. Agree together on schedule of the conversion. 

### Buckets with incompatible names (Urgent)

In SD Connect UI you will see buckets marked with **Urgent** label. This bucket seems empty because bucket’s name is incombatible with new version of SD Connect. It must be converted to regain access to the files. We recommend that you don’t upload files to this bucket to ensure smooth conversion process.

### Buckets with files uploaded with previous versions of SD Connect

Buckets containing files uploaded with a previous version of SD Connect now show those file sizes as zero. Please convert this bucket or create a new bucket before uploading new files.


## 2. Download and install SD Connect Conversion tool

- Links 
- Installation guide


## 3. Start conversion 

- Launch SD Connect Conversion tool and login with your CSC credentials.
- SD Connect Conversion tool allows you to convert buckets from one project at a time. Select first project you will convert.

## 4. Retrieve project's API key
- Log in to [SD Connect service](https://sd-connect.csc.fi).
- Select project you want to convert from dropdown.
- In the top right corner of the web interface, click on **Support**, then select **Create API Token** from the dropdown menu.
- In the new dialog, **enter a name** for your API key. Avoid using special characters in the name.
- Click **Create key**. The API key will be displayed only once. Once you see the key, copy it (click the icon to the left of the token). Important: make sure to store it securely, as it will not be retrievable later.

    ![API key](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SDConnect_APItoken.png)

- The token will be valid for 7 days and will be automatically deleted after this period.
- Paste API key to the field in Conversion tool.



## 4. Select buckets to convert

- Guide about possible changes in bucket names
- If user has slow connections, what to do next (Pouta VM and CLI?). Instructions on internet connections speeds, amount of data and impact on time that conversion would take.
- If user needs more quota, what to next. Guide about applying for more Allas quota.
    - Where quota is in MyCSC
    - Send email
    - wait for few days
    - user receives email when quota is raised
- Some reminder about billing units? IF they don't delete buckets at the end, they will consume double.

## 5. During conversion

- No uploads.
- UI in SD Connect


## 6. If conversion is interrupted

- Guide to continue conversion, possible reasons.
- Add new API key guide.

## 7. Delete old buckets

- User should delete old incombatible buckets.
