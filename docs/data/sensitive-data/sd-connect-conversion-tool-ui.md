# SD Connect Conversion tool

<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **Page is under construction**
  { .csc-grid-card-warning }

    ---
    
    This page and content is under construction and development.

</div>



This guide helps you to install and use SD Connect Conversion tool.


___


## 1. Download and install SD Connect Conversion tool


??? info "Installation guide for macOS"

    1. Download the SD Connect Conversion Tool.

    3. Open a new **Finder** window. In Finder window open your **Home folder** (marked with Home icon) from left sidebar. Then select **Applications**.
    
    If **Home folder** is not visible, click **Finder** at top left and select **Settings** from dropdown menu. A new window opens. In this Settings window select **Sidebar** tab and select **Home folder** to make it visible in the sidebar.

    4. Launch the downloaded file. A new window named **sd_connect_s3_migrate_gui** will open. Drag and drop **sd_connect_s3_migrate_gui** file (black icon) to Applications folder.

    3. On your desktop, find the icon named **SD_Connect_s3_migrate_gui**. Right-click it and select **Eject SD_Connect_s3_migrate_gui**.

    4. Press **Command (⌘) + Space** to open Spotlight Search.

    5. Type **Terminal** and press **Enter**.

    6. A Terminal window will open. Copy and paste command below into the terminal and press **Enter**:

        ```bash 
        cd /Applications
        ```

    7. Copy and paste command below into the terminal and press **Enter**:

        ```bash 
        xattr -cr sd_connect_s3_migrate_gui.app
        ```

    8. Copy and paste command below into the terminal and press **Enter**:

        ```bash 
        logout
        ```


    10. Double-click **SD Connect Conversion Tool** icon to start the application.


??? info "Installation guide for Linux"



??? info "Installation guide for Windows"

    1. Download the SD Connect Conversion Tool.

    2. Open your **Downloads** folder and extract the folder you just downloaded.

    3. Drag the extracted folder to your Desktop.

    4. Open the folder and locate file **sd_connect_s3_migrate_gui.exe**.

    5. Launch the file. A new window appears **Windows protected your PC**. In this window, click **More info**, then **Run anyway** button.

    6. Conversion tool should start after a while.

___

## 2. Using SD Connect Converter tool

### 2.1 Login to Converter tool

- Launch SD Connect Conversion tool and login with your CSC credentials.

![Login to Conversion tool](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD_Connect_Conversion_login.png)


### 2.2 Select project

- Conversion tool allows you to convert buckets from one project at a time. 
- Select first project you will convert and click **Continue**.

![Select project](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD_Connect_Conversion_Select.png)


### 2.3 Add project's temporary API key

- Next Converter tool will ask to add project's temporary API key. Follow instructions below.

??? info "How to retrieve to API key"

    1. Log in to [SD Connect](https://sd-connect.csc.fi).
    2. Select project you want to convert from dropdown.
    3. In the top right corner of the web interface, click on **Support**, then select **Create API Token** from the dropdown menu.
    ![API key](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SDConnect_CreateAPI.png)

    4. In the new dialog, **enter a name** for your API key. Avoid using special characters in the name. Click **Create key**. 
    ![API key 2](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SDConnect_CreateAPI2.png)  

    5. The API key will be displayed only once. Once you see the key, copy it by clicking button on the right side of the key.
    ![API key 3](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SDConnect_CreateAPI3.png)  

    6. Paste API key to the field in Conversion tool. The token will be valid for 7 days and will be automatically deleted after this period. If your conversion takes longer than 7 days you need to create a new API key.

![Add API key](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD_Connect_Conversion_API_key.png)


### 2.4 Select buckets to convert

- Next select buckets you want to convert by clicking checkboxes on the left side of bucket names. 
- If the estimated conversion time is very long we recommend using command-line version of the conversion tool. 
- Converter tool tells you the amount of quota that is needed to complete the conversion. Please check the amount you have available from MyCSC and apply for more if needed. Follow instructions below.

??? info "How to check quota from my.csc.fi"

    1. Log in to [MyCSC](https://my.csc.fi).
    2. Go to **Projects** page (menu on the left or hamburger icon) and navigate to your project's view.
    3. Scroll down to **Services** window.
    4. Click **Allas**. You can see storage quota usage under **Usage** at the bottom of the window (for example 6 TB/10 TB would mean your project has 4 TB of quota available).
    ![Storage Quota in MyCSC](https://a3s.fi/docs-files/sensitive-data/MyCSC/MyCSC_Quota.png)
    5. If you have less quota available than is needed, apply for more:
        * Send email to Service Desk (subject line: Increase Allas quota). It takes few days to process your application.
        * You will receive email when your quota is available.

![Select buckets](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD_Connect_Conversion_buckets.png)


### 2.5 During conversion

- After selecting buckets you can start process by clicking **Start conversion**. 
- We recommend that you don't upload files to buckets being converted during conversion. 
- You can follow the progress from Conversion tool. 

![Conversion in process](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD_Connect_Conversion_in_process.png)


### 2.6 If conversion is interrupted

Conversion pauses if your laptop runs out of power or loses internet connection. You can continue conversion easily.

1. Launch SD Connect Conversion tool and login with your CSC credentials.
2. Converter tool will show you that conversion has been interrupted.
    - If a new API key is needed, it will be shown in the tool. Follow these [instructions](#33-add-projects-temporary-api-key).
3. Continue by clicking **Continue conversion**.

![Conversion paused](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD_Connect_Conversion_pause.png)

### 2.7 Finish conversion

After conversion is complete Conversion tool will ask you if you want delete original incompatible buckets. 

![Deleting incombatible buckets](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD_Connect_Conversion_delete.png)
