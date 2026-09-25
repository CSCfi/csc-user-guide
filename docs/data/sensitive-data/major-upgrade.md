## SD Connect and SD Desktop major service upgrade, 28.09.2026

A new version of SD Connect and SD Desktop is now available. The upgrade introduces significant improvements but also includes changes that are not compatible with the previous version of the services.

Please review the following information:

- [1. Important dates and support](#important-dates-and-support)
- [1. CSC Project- Academic type: video overview and required actions](#csc-project-academic-type-video-overview-and-required-actions)
- [2. CSC Project- Secondary use type: if you are processing register data]

- [4. Materials and instructions](#materials-and-instructions)


### Important dates and support

- **Mondays at 12:00 and Thursdays at 10:00**: online support sessions with step-by-step guidance and opportunities to ask questions about the upgrade. Registration available via this link in [English](https://ssl.eventilla.com/event/Gl0Wb/EN) or [Finnish](https://ssl.eventilla.com/event/Gl0Wb/FI)
  
- **30 September at 14:00**: Webinar introducing the upgrade, key changes and required actions at the [CSC Research Support Coffee](https://csc.fi/en/training-calendar/csc-research-support-coffee-every-wednesday-at-1400-finnish-time-2-2/)



### CSC Project-Academic type: video overview and required actions

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/s4yPO45j608" title="CSC Academic project type: SD Connect and SD Desktop major upgrade" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/ClH2FroTMA8" title="Sensitive Data (SD) -palveluiden päivitys" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

- **SD Connect**: access to files stored in SD Connect may be interrupted if the main folder (bucket) name contains spaces, special characters, or exceeds 63 characters. Access can be restored after the upgrade by following the step-by-step instructions available [here](sd-connect-conversion.md)

- **SD Desktop**: import and export functionality need to be restored.

1. if you have not done any preparation, please follow [these instructions](sd-desktop-major-upgrade.md)
2. If you followed the preparation instructions sent by email before September 21, complete the following steps:

    1. Log in to the service and access your virtual desktop.
    2. Right-click and select **Open in Terminal**.
    3. In the terminal, enter:
       ```
       csc-update-ubuntu22.04
       ```
       Press **Enter**. The script installs the **New Data Gateway** icon.
    4. Log out from the virtual desktop: Click Power icon in top right corner of the desktop and select Log Out.
       In the new window, select Home to return to SD Desktop home page. There, on the top right corner next to your username, log out form the service. 
    5. Log in to SD Desktop again and access your virtual desktop. The **New Data Gateway** icon should now work.
 

### CSC Project- Secondary use type: if you are processing register data

You can now access again SD Desktop for analysis. Importing and exporting data or adding software is temporarily unavailable. We will provide new information soon. 


### Materials:
- [SD Connect: New features](../../data/sensitive-data/releases-sd-connect.md)
- [SD Desktop: New features](../../data/sensitive-data/releases-sd-desktop.md)


