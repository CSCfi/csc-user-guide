## SD Connect and SD Desktop major service upgrade, 28 September 2026

On September 28, 2026, a new version of SD Connect and SD Desktop was released. While the upgrade brings [several improvements](https://www.youtube.com/embed/s4yPO45j608), some changes require existing users to take action to maintain access to certain features. **If you started using the service after September 28, 2026, you can skip this section**.

Please review the following information:

- [1. Support](#1-support)
- [2. CSC Project- Academic type: video overview and required actions](#2-csc-project-academic-type-video-overview-and-required-actions)
- [3. CSC Project- Secondary use type: register data](#3-csc-project-secondary-use-type-register-data)
- [4. Known issues](#4-known-issues)
- [5. Materials and release pages](#5-materials-and-release-pages)



### 1. Support

- **Mondays at 12:00 and Thursdays at 10:00**: online support sessions with step-by-step guidance and opportunities to ask questions about the upgrade. Registration available via this link in [English](https://ssl.eventilla.com/event/Gl0Wb/EN) or [Finnish](https://ssl.eventilla.com/event/Gl0Wb/FI).
  

### 2. CSC Project-Academic type: video overview and required actions

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/s4yPO45j608" title="CSC Academic project type: SD Connect and SD Desktop major upgrade" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/ClH2FroTMA8" title="Sensitive Data (SD) -palveluiden päivitys" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

- **SD Connect**: Access to files stored in SD Connect may be interrupted if the main folder (bucket) name contains spaces, special characters or exceeds 63 characters.

- **SD Desktop**: The import and export functionality needs to be restored.

1. **If you did not complete the preparation steps before the upgrade** [follow these instructions](sd-desktop-major-upgrade.md)
2. **If you followed the preparation instructions sent by email before September 21**, complete the following steps:

    1. Log in to the service and access your virtual desktop.
    2. Right-click and select **Open in Terminal**.
    3. In the terminal, enter:
       ```
       csc-update-ubuntu22.04
       ```
       Press **Enter**. The script installs the **New Data Gateway** icon.
    4. Log out from the virtual desktop: click **Power icon** in top right corner of the desktop and select **Log Out**.
    5. In the new window, select **Home** to return to SD Desktop home page. There, on the top right corner next to your username, log out form the service. 
    6. Log in to SD Desktop again and access your virtual desktop. The **New Data Gateway** icon should now work.
 

### 3. CSC Project-Secondary use type: register data

- **SD Desktop**: To gain access to the import and export functionality, [follow these instructions](secondary-use-major-upgrade.md).

- **SD Connect**: In order to restore access to the register dataset, [follow these instructions](sd-use-case-secondary-use-project.md#7-retrieve-your-projects-share-id-from-sd-connect) to retrieve the Share ID of your project from SD Connect and deliver it to [CSC Service Desk](../../support/contact.md) (subject: Sensitive Data).

- Get familiar with the [new features](secondarydata-access.md) for secondary use projects, and [export instructions](sd-desktop-secondary-export.md) for all project members.

You can also join the **[CSC Research Support Coffee](https://csc.fi/en/training-calendar/csc-research-support-coffee-every-wednesday-at-1400-finnish-time-2-2/) on Wednesday, November 4th**, to learn more and dicuss the updates on CSC SD services for Secondary Use, or register for the online support sessions mentioned [above](#1-support).



### 4. Known Issues

| Issue | Description | Resolution |
|-------|-------------|------------|
| **SD Connect: white page** | When accessing SD Connect, you may see a blank white page. | **Google Chrome is currently the only supported browser**. Clear your browser history and cookies, restart the browser, and access SD Connect again. |
| **SD Connect: bucket empty** | Some buckets containing files uploaded before 28 September 2026 and labelled **"By the End of 2026"** may appear empty. | Uploading a small file to the bucket will restore visibility of its contents. |
| **SD Connect: download fails shortly after starting** | Data uploaded by sequencing facilities to your CSC project before 28 September 2026, and visible in buckets labelled **"By the End of 2026"**, may currently be inaccessible or downloads may fail shortly after starting. | This issue can be resolved by converting the bucket with the Conversion Tool. Alternatively, a workaround is available; please contact us for support. |
| **SD Desktop: black screen when accessing the virtual desktop** | When accessing the virtual desktop in your browser, you may see a black screen for up to one minute while the virtual desktop loads. If the virtual desktop does not appear and you see an **X** on the black screen, the display may be asleep. | Move your mouse pointer to the **left side of the black screen**, click anywhere in that area, and the display should wake up. |
| **SD Desktop: Data Gateway connection needs to be refreshed** | You may see a message indicating that the Data Gateway connection needs to be refreshed. | Log out from the virtual desktop and SD Desktop, wait a few minutes, then sign in again. |
| **SD Desktop: SD Apply access from Data Gateway not working** | Accessing **SD Apply** from Data Gateway is currently not working. You may see an empty folder instead of the expected content. | No workaround is currently available. |
| **SD Desktop: backup server is currently unavailable** | Data export is available only through the Data Gateway (web interface or CLI). | Exported files can be downloaded via SD Connect by any project member. |
| **SD Desktop: Byobu terminal stops** | Long-running jobs using Byobu stop when logging out of the virtual desktop. | As a temporary workaround, close the browser window instead. |
| **SD Desktop: executable not running** | Executable stored on external volumes may not run as expected. | A simple workaround is available, and a permanent fix is being developed. |


### 5. Materials and release pages

You can find a complete overview of the changes and improvements on the release page: 
  
- [SD Connect: New features](../../data/sensitive-data/releases-sd-connect.md)
- [SD Desktop: New features](../../data/sensitive-data/releases-sd-desktop.md)
  
- [SD Desktop: updated virtual desktop creation guide](../../data/sensitive-data/sd-desktop-create.md)
- [SD Desktop: updated virtual desktop management guide](../../data/sensitive-data/sd-desktop-manage.md)
- [SD Desktop: updated virtual desktop export guide](../../data/sensitive-data/sd-desktop-export.md)
