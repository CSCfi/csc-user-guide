## SD Connect and SD Desktop major service upgrade, 28 September 2026

A new version of SD Connect and SD Desktop is now available. The upgrade introduces significant improvements, but some changes require users to take action to continue using certain features.

Please review the following information:

- [1. Important dates and support](#1-important-dates-and-support)
- [2. CSC Project- Academic type: video overview and required actions](#2-csc-project-academic-type-video-overview-and-required-actions)
- [3. CSC Project- Secondary use type: register data](#3-csc-project-secondary-use-type-register-data)
- [4. Known issues](#4-known-issues)
- [5. Materials](#5-materials)



### 1. Important dates and support

- **Mondays at 12:00 and Thursdays at 10:00**: online support sessions with step-by-step guidance and opportunities to ask questions about the upgrade. Registration available via this link in [English](https://ssl.eventilla.com/event/Gl0Wb/EN) or [Finnish](https://ssl.eventilla.com/event/Gl0Wb/FI).
  
- **30 September at 14:00**: Webinar at the [CSC Research Support Coffee](https://csc.fi/en/training-calendar/csc-research-support-coffee-every-wednesday-at-1400-finnish-time-2-2/)introducing the upgrade, key changes and required actions.



### 2. CSC Project-Academic type: video overview and required actions

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/s4yPO45j608" title="CSC Academic project type: SD Connect and SD Desktop major upgrade" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/ClH2FroTMA8" title="Sensitive Data (SD) -palveluiden päivitys" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

- **SD Connect**: Access to files stored in SD Connect may be interrupted if the main folder (bucket) name contains spaces, special characters or exceeds 63 characters. Access can be restored after the upgrade by following the step-by-step instructions available [here](sd-connect-conversion.md)

- **SD Desktop**: The import and export functionality needs to be restored.

1. **If you did not complete the preparation steps before the upgrade [follow these instructions](sd-desktop-major-upgrade.md)
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

You can now access again SD Desktop for analysis. Importing and exporting data or adding software is temporarily unavailable. We will provide new information soon. 


### 4. Known issues

#### 4.1 SD Connect: white page 

When accessing SD Connect, you may see a **blank white page**. Clear your browser history and cookies, restart the browser and access SD Connect again.


#### 4.2 SD Desktop: black screen when accessing the virtual desktop

When accessing the **virtual desktop in your browser**, you may see a black screen for up to one minute while the virtual desktop loads.

If the virtual desktop does not appear and you see an **X on the black screen**:

1. Move your mouse pointer to the **left side of the black screen**.
2. Click anywhere in that area.
3. This should wake up the display, and the **virtual desktop should become visible in your browser**.


### 4.3 SD Desktop: Data Gateway connection needs to be refreshed

If you see a message indicating that the Data Gateway connection needs to be refreshed, follow these steps:
   
   1. Log out from the virtual desktop: click **Power icon** in top right corner of the desktop and select **Log Out**.
   2. In the new window, select **Home** to return to SD Desktop home page. There, on the top right corner next to your username, log out form the service.
   3. Wait a few minutes.
   4. Log in to SD Desktop service again and access your virtual desktop. The **New Data Gateway** icon should now work.



### 4.4 SD Desktop: SD Apply access from Data Gateway not working

Accessing **SD Apply from Data Gateway** is currently not working. You may see an **empty folder** instead of the expected content, with no error message displayed.



### 5. Materials
- [SD Connect: New features](../../data/sensitive-data/releases-sd-connect.md)
- [SD Desktop: New features](../../data/sensitive-data/releases-sd-desktop.md)
  

