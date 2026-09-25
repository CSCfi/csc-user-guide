## SD Connect and SD Desktop major service upgrade, 28.09.2026

A new version of SD Connect and SD Desktop is now available. The upgrade introduces significant improvements but also includes changes that are not compatible with the previous version of the services.

Please review the following information:

- [1. CSC Project- Academic type: video overview and required preliminary actions](#csc-project-academic-type-video-overview-and-required-preliminary-actions)
- [2. CSC Project- Secondary use type](#important-dates-and-support)
- [3. Important dates and support](#important-dates-and-support)
- [4. Materials and instructions](#materials-and-instructions)


### CSC Project-Academic type: video overview of changes

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/s4yPO45j608" title="CSC Academic project type: SD Connect and SD Desktop major upgrade" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/ClH2FroTMA8" title="Sensitive Data (SD) -palveluiden päivitys" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

- **SD Connect**: access to files stored in SD Connect may be interrupted if the main folder (bucket) name contains spaces, special characters, or exceeds 63 characters. Access can be restored after the upgrade by following the step-by-step instructions available [here](sd-connect-conversion.md)

- **SD Desktop**: import and export functionality need to be restored.

  1. If you have followed the instructions provided before the 21st of September, please follow these steps:

  - login to your virtual desktop
  - right click, open the terminal, write csc-update-ubuntu2024 pres enter. This will install the icon called: new data gateway. 
  - log out from the virtual desktop, log out from the SD Desktop service.
  - When you log in again, the New Data Gateway icon will work.
 
  2. if you have not done any preparation, please follow [these instructions](sd-desktop-major-upgrade.md)
 
  




### CSC Project- Secondary use type

- **SD Desktop**: Import and export functionality from virtual desktops will be temporarily unavailable after the upgrade. No action is currently required. Instructions for restoring the functionality will be available from 28 September.

### Important dates and support

- **21.9.2026 09:00 – 25.9.2026 17:00 EEST**: Service break. SD services will not be available during this period.

- **Mondays at 12:00 and Thursdays at 10:00**: online support sessions with step-by-step guidance and opportunities to ask questions about the upgrade. Registration available from September 28 via this link in [English](https://ssl.eventilla.com/event/Gl0Wb/EN) or [Finnish](https://ssl.eventilla.com/event/Gl0Wb/FI)
  
- **30 September at 14:00**: Webinar introducing the upgrade, key changes and required actions at the [CSC Research Support Coffee](https://csc.fi/en/training-calendar/csc-research-support-coffee-every-wednesday-at-1400-finnish-time-2-2/)
  

### Materials and instructions:
- [SD Connect: New features](../../data/sensitive-data/releases-sd-connect.md)
- [SD Desktop: New features](../../data/sensitive-data/releases-sd-desktop.md)
- Step-by-step instructions for actions required after 28 September, link soon available here

