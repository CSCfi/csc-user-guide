# Under construction

<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **Page is under construction**
  { .csc-grid-card-warning }

    ---
    
    This page and content is under construction and development.

</div>



# Overview

The SD Connect service has been upgraded to a new version with changes that are not fully backward compatible. This guide explains how to regain access to your files or convert them to the new format using the SD Connect Conversion Tool.

## Step 1: Check the tags visible in the SD Connect user interface


- **Urgent**: The bucket name contains incompatible characters, so you no longer have access to your files and sharing permissions are not visible. Use the Conversion Tool to regain access. **The tool will create a new bucket with a compatible name (including the suffix “-conv”) and copy all files there**. Because this involves creating a full duplicate of your data, the process may take time and use significant network and storage resources. Before starting,we need to consider the available storage quota for yoru CSC project, where the Conversion Tool will be installed, and the potential impact on network performance during the process. At the end of the conversion, the oroginal bucket needs to be deleted. Please refer to the table below to find the relevant step by step guide.


- **By the end of 2026**: The bucket name contains compatible characters, so you can still access and download your files; however, file sizes may appear as zero and sharing permissions are no longer visible. Use the Conversion Tool to improve usability, update the file format, restore the correct file sizes and sharign perssmions. 
In this case, the conversion process is faster because no data is duplicated—only the format and metadata are updated—resulting in fewer constraints. Please refer to the table below to find the relevant guide.


- **Both tags are present**: Your project contains both types of buckets. In this case, you can the buckets marked as urgent first, and in a second steo al the remianing one. 


Step 2: Choose the correct option and step by step guide

| Tag | Bucket or CSC project size | Next steps | Link to the user guide |
|-----|----------------------------|------------|------------------------|
| Urgent | Up to 1 TB | Download the SD Connect Conversion Tool application to your laptop | [SD Connect Conversion tool application](sd-connect-conversion-tool-ui.md) |
|  | Up to 4 TB | Use the SD Connect Conversion CLI installed on Rhoihu | Link |
|  | Up to 50 TB | Verify that your CSC project has enough quota to create a copy of your files during the conversion. Plan the process so that single buckets are converted at a time. Use the SD Connect Conversion CLI installed on Rhoihu | Add link here |
|  | More than  50 TB| Contact us to plan teh comevrsion with our support |
| By end of 2026 | Up to 1 TB | Download the SD Connect Conversion Tool application to your laptop and schedule conversion before the end of 2026 | Add link here |
|  | More than 1 TB | Plan and schedule the conversion well ahead of the deadline | Add link here |
