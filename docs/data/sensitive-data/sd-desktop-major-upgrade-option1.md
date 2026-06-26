
# Option 1: Virtual desktop has a volume and you don't need new features of SD Desktop

Choose this if your analysis is short-term or almost finished, and you prefer to avoid the effort of migrating. Before you begin, make sure you read the instructions carefully and agree on the approach with your colleagues.

## Step-by-step

### Step 1: Access desktop

1. [Login](./sd-desktop-login.md) to SD Desktop. Select the correct CSC project in the top left corner. Now you can see all desktops in this project.

2. Make sure the virtual desktop you want to access is running. If it is paused, you need to [unpause](sd-desktop-manage.md#unpausing-a-virtual-desktop) it before you can access it.
  
3. Access virtual desktop by clicking **Access desktop** on right side of the desktop name.

When you open the connection, a virtual desktop will open in your browser in a new window. 

![Access virtual desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_AccessVM2.png)


### Step 2: Save all important data to the volume

All project members should save data they want to keep to the volume. 

* Open **Volume**.
* Save data you want to keep to the volume. 

![Open volume](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_Volume.png)


### Step 3: Update Data Gateway application

All project members who **plan to import data** to SD Connect need to update Data Gateway application.

Project manager needs to update update Data Gateway application to **export data**.


* Open terminal.

![Open terminal](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_Clipboard1.png)


* Copy this command:


* Press **Ctrl + Alt + Shift** to open the **Clipboard panel.** Select **Text input** to enable copy-paste. Clipboard panel will close automatically. Do not close the Clipboard panel with Ctrl + Alt + Shift, as this may disable copy-paste.

![Open Clipboardß](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_Clipboard2.png)

*  Move your mouse over the black bar in the bottom of the screen.
    * Right-click and **Paste** the command you copied. 
    * Command will appear in the terminal. Presss **Enter**. Update will start.

![Use Clipboardß](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-Desktop_Clipboard3.png)

* When update is finished, an icon called **New Data Gateway** will appear on your desktop. Use this icon to launch Data Gateway.





