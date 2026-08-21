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

Plan the conversion in advanced with the other CSC project members. All the project members should agree together on the schedule and no new files should be uploaded during the conversion.

 When possible, we recommend [deleting](sd-connect-delete.md) unnecessary files and buckets from SD Connect before starting, as this reduces conversion time and frees up resources for other research projects. 

____

### Buckets with label Urgent

![Urgent bucket](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD_Connect_Urgent.png)

#### Before conversion

Buckets with **Urgent** label appear empty, files in them cannot be accessed and sharing permissions are not visible. Prioritize converting these buckets to restore access to the data.


<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **When your project size exceeds 5 TB**
  { .csc-grid-card-warning }

    ___

    This is a network-intensive operation. Large conversions should be planned in advance to avoid overloading CSC storage infrastructure. **If your project's data size exceeds 5 TB**, please contact us for support before starting the conversion. Buckets labelled **Urgent** are given priority in Helpdesk support queues. 

</div>


____

#### During conversion

Select buckets you want to convert via SD Converter tool. The tool will create new buckets with the suffix "-conv" and all files are copied to them. The tool will restore the correct bucket size and sharing permissions. 

#### Example of new bucket names

| Example (Old name -> New name) | Changes |
|----------|----------|
| `Non-compatible name` → `non-compatible-name-conv` | Capital letters are converted to lowercase. Spaces are replaced with hyphens (`-`). Suffix `-conv`is added to the end. |
| `non-compatible name` → `non-compatible-name-conv` | Spaces are replaced with hyphens (`-`). Suffix `-conv`is added to the end. |
| `non_compatible name` → `non-compatible-name-conv` | Underscores (`_`) are replaced with hyphens (`-`). Spaces are replaplaced with hyphens (`-`). Suffix `-conv`is added to the end. |
| In case of similar bucket names, for example: `Non-compatible name` and `non-compatible name` → `non-compatible-name-conv` and `non-compatible-name-234-conv` | Two buckets can't have the same name. Tool adds random string to other's bucket name. |

____

#### After conversion

Verify that the converted data is complete and accessible using the tool, then delete the original bucket. Keeping both buckets (old and new ones) consumes significant CSC storage resources. Deleting a bucket permanently removes all data it contains.

____

### Buckets with label By the end of 2026

![By the end of 2026 bucket](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD_Connect_Bytheend2026.png)

#### Before conversion

In buckets with **By the end of 2026** files can still be accessed and downloaded, however buckets sharing permissions are not be visible and bucket size is zero. **Conversion must be done by the end of 2026.** 

____

#### During conversion

Select buckets you want to convert via SD Converter tool. The tool will create new buckets with the suffix "-conv" when there are capital letters and underscores in the bucket name and all files are copied to them. The tool will restore the correct bucket size and sharing permissions. 

Unlike the conversion of **Urgent** buckets, this process is not network intensive.  

#### Examples of new buckets names:

| Examples (Old name -> New name) | Changes |
|----------|----------|
| `compatible-name` → `compatible-name` | No changes in bucket name. |
| `NONcompatible-name` → `noncompatible-name-conv` | Capital letters are converted to lowercase. Suffix `-conv`is added to the end. |
| `non_compatible_name` → `non-compatible-name-conv` | Underscores (`_`) are replaced with hyphens (`-`). Suffix `-conv`is added to the end. |
| In case of similar bucket names, for example: `Non-compatible_name` and `non-compatible_name` → `non-compatible-name-conv` and `non-compatible-name-234-conv` | Two buckets can't have the same name. Tool adds random string to other's bucket name. |

____


#### After conversion

Verify that the converted data is complete and accessible using the tool, then delete the original bucket. Keeping both buckets (old and new ones) consumes significant CSC storage resources. Deleting a bucket permanently removes all data it contains.

____

### If your project contains both Urgent and By the end of 2026 buckets

Convert all **Urgent** buckets first and then proceed with the remaining buckets by end of 2026. 


---

## Step 2: Choose the appropriate conversion method

Choose the method based on bucket's tag and size.

| Bucket Tag | Data Size | Recommended Action | User Guide |
|-------|------------|-------------------|------------|
| Urgent | Up to 1 TB | Use the SD Connect Conversion Tool user interface on your local computer. This is a network-intensive operation. On a standard home internet connection, converting 25 GB may take around 2 hours. | [Link](sd-connect-conversion-tool-ui.md) |
| Urgent | 1–4 TB | Use the SD Connect Conversion CLI on Roihu. | [Link](sd-connect-conversion-cli.md) |
| Urgent | 4–50 TB | Verify that sufficient quota is available to create a copy of the bucket with compatible name.  Use th SD Connect Conversion CLI on Roihu and convert a few buckets at a time.This is a network-intensive operation. Larger projects require advance planning to avoid overloading CSC storage infrastructure and to ensure a smooth conversion.  | Link |
| Urgent | More than 50 TB | Contact CSC support to plan the conversion. | Contact us |
| By End of 2026 | Up to 1 TB | Use the SD Connect Conversion Tool user interface on your local computer. | Link |
| By End of 2026 | More than 1 TB | Use the SD Connect Conversion CLI on Roihu.| Link |



