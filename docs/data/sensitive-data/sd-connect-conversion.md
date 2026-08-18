# Under construction

<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **Page is under construction**
  { .csc-grid-card-warning }

    ---
    
    This page and content is under construction and development.

</div>

# SD Connect Conversion guide

SD Connect has been upgraded to a new version. To continue using your existing buckets, they must be converted by using **SD Connect Conversion Tool**. The conversion upgrades your existing buckets to the new SD Connect version while preserving their data, access, and functionality.

## Step 1. Review CSC project's buckets in SD Connect

Review your project's buckets together with your (possible) team. We recommend [deleting](sd-connect-delete.md) unneeded files and buckets from SD Connect before starting conversion as this shortens conversion time. It also saves resources for other research projects. Team should agree together on the schedule of the conversion. 

### Buckets with label Urgent

These buckets seem empty, files cannot be accessed and sharing permissions are not visible. **Prioritize converting these buckets** to regain access to the files.

During the conversion, a new bucket is created and all files are copied to it. 

After conversion these buckets will have new compatible names with a suffix "-conv" at the end of the bucket name. 

Note !!!
This is a network-intensive operation. Larger projects require advance planning to avoid overloading CSC storage infrastructure and to ensure a smooth conversion. If your project exceeds 5 TB, please contact us for migration planning and support. 


![Urgent buckets in SD Connect](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD_Connect_Urgent.png)


### Buckets with label By the end of 2026

In these buckets sharing permissions are not be visible and bucket size is zero. Files can still be accessed and downloaded. Please convert these buckets or create a new bucket before uploading new files. 

**Conversion must be done by the end of 2026.** During the conversion, a new bucket is created only when there are capital letters and underscores in the bucket name. The tool will restore the correct bucket size and  sharing permissions. 

![By the end of 2026 buckets in SD Connect](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD_Connect_Bytheend2026.png)


### If your project contains both Urgent and By the end of 2026 buckets

Convert all **Urgent** buckets first and then proceed with the remaining buckets by end of 2026. 


---

## Step 2: Choose the appropriate conversion method

Choose the method based on bucket's tag and size.

| Bucket Tag | Data Size | Recommended Action | User Guide |
|-------|------------|-------------------|------------|
| Urgent | Up to 1 TB | Use the SD Connect Conversion Tool user interface on your local computer. This is a network-intensive operation. On a standard home internet connection, transferring 25 GB may take around 2 hours. | [Link](sd-connect-conversion-tool-ui.md)|
| Urgent | 1–4 TB | Use the SD Connect Conversion CLI on Roihu. | Link |
| Urgent | 4–50 TB | Verify that sufficient quota is available to create a copy of the bucket with compatible name.  Use th SD Connect Conversion CLI on Roihu and convert a few buckets at a time.This is a network-intensive operation. Larger projects require advance planning to avoid overloading CSC storage infrastructure and to ensure a smooth conversion. Please contact us for migration planning and support.  | Link |
| Urgent | More than 50 TB | Contact CSC support to plan the conversion. | Contact us |
| By End of 2026 | Up to 1 TB | Use the SD Connect Conversion Tool user interface on your local computer. | Link |
| By End of 2026 | More than 1 TB | Use the SD Connect Conversion CLI on Roihu.| Link |



