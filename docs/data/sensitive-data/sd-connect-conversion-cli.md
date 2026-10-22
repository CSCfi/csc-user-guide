# SD Connect Conversion command line tool

## On This page: 

[Step 1: Verify that you have enough quota](#step-1-verify-that-you-have-enough-quota)
[Step 2: Migrating SD Connect buckets in Roihu](#step-2-migrating-sd-connect-buckets-in-roihu)

Please note: the bucket name Conversion Tool  CLI can be run locally (recommended for smaller datasets) or on the Roihu supercomputer. While Roihu is not suitable for processing sensitive data, it can be used to run the Conversion Tool, providing faster conversions through CSC's network.


## Step 1: Verify that you have enough quota

You will need enough storage quota to complete the conversion. First you need to know the amount of data you have in Urgent buckets per project.

1. Log into SD Connect and select a project.
2. Add the sizes with **Urgent** label you have in your project together. Repeat for other projects.

You will need twice this amount of quota to complete the conversion. Check the amount you have and apply for more if needed by following instructions below. Repeat for other projects.

1. Log in to [MyCSC](https://my.csc.fi).
2. Go to **Projects** page (menu on the left or hamburger icon) and navigate to your project's view.
3. Scroll down to **Services** window.
4. Click **Allas**. You can see storage quota  under **Usage** at the bottom of the window. By default amount of quota is 10 TB.
![Storage Quota limit in MyCSC](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_Quota.png)
5. Then scroll down service list and click **SD Connect**. You can see how much storage quota  you are using under **Usage** at the bottom of the window. For example if you have 10 TB of storage quota and you've used 4 TB, your project has 6 TB of quota available.
![Storage Quota used in MyCSC](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_QuotaUsed.png)
5. If you have less quota available than is needed, apply for more:

    * Send email to Service Desk (subject line: Increase Allas quota). It takes few days to process your application.
    * You will receive email when your quota is available.


## Step 2: Migrating SD Connect buckets in Roihu

The SD Connect migration tool is available in Roihu supercomputer. The tool can be installed to your local computer too, but in many cases Roihu provides fester connection to SD Connect and thus quicker migration.

Open terminal connection to Roihu using either locally installed terminal program or the [Roihu Web interface](https://www.roihu.csc.fi).  In the web interface select tool: 

   * **Login node shell (Roihu-CPU)**

This tool provides you a terminal session running in one of the login nodes of Roihu.

Next check your available disk areas with command:

```text
  csc-workspaces
```

The command above lists the _/projappl_ and _/scratch_ disk areas that you can use and the current usage of these disk areas. In some cases the conversion process may need to download the whole content of the bucket temporarily to Roihu, so you should do then conversion in a directory where you have enough free space for the temporary copy of the bucket to be migrated. Note that the scratch directory you use don’t need to belong to the same project than the SD Connect bucket to be migrated.

Move to a scratch disk area of a project where you have enough free storage capacity available with command:

```text
   cd /scratch/project_your-project-number
```

Then, load the Allas tools:

```text
   module load allas
```

Next you can start the conversion process with command

```text
   sd-connect-s3-migrate convert
```

The command will first ask for your CSC user account and password. Note that HAKA password can't be used here.

After that accept the default values for authentication API address and SD Connect API Address by pressing **Enter**.

After these selections, the tool shows a list of your SD Connect projects.
Choose the project to be used from the list. Use the arrow keys to move up and down in project list and press **Space** to select a project and continue by pressing **Enter**.

Next, the tool asks for the API key for the project you selected. Follow instructions below:

1. Log in to [SD Connect](https://sd-connect.csc.fi).
2. Select project you want to convert from dropdown. The API keys are project specific. In the web interface, check that the active project is the same that you have selected in the Conversion tool.
3. In the top right corner of the web interface, click on **Support**, then select **Create API Token** from the dropdown menu.
![API key](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SDConnect_CreateAPI.png)
4. In the new dialog, **enter a name** for your API key. Avoid using special characters in the name. The name can be anything as it is actually not used in any step of the migration process. Click **Create key**. 
![API key 2](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SDConnect_CreateAPI2.png)  
5. The API key will be displayed only once. Once you see the key, copy it by clicking button on the right side of the key.
![API key 3](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SDConnect_CreateAPI3.png)  
6. Paste API key to the field in Conversion tool. The token will be valid for 7 days and will be automatically deleted after this period. If your conversion takes longer than 7 days you need to create a new API key.
    

When API key has been inserted to the terminal, the tool displays a list of all buckets of your SD Connect project.

Note that the list does not contain information about which buckets need to be converted.  You will need to check this information from the SD Connect web interface. **Use the arrow keys to move up and down in the bucket list and press “Space” to select a bucket or buckets and start conversion process by pressing “Enter”**.



  
