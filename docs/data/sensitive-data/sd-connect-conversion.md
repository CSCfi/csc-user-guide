# SD Connect: bucket names conversion


Existing buckets need to be converted to work correctly with the updated version of SD Connect available from September 2026.. The SD Connect Conversion Tool, available via graphical user interface or command line, converts buckets names while preserving the data and restoring their functionality.

The action you need to take depends on the label displayed in the SD Connect user interface next to your bucket:

- Urgent: convert the bucket as soon as possible to restore data access.
- By the end of 2026: the data remains accessible, but the bucket name and file format should be converted by the end of 2026.

If your project contains both types of buckets, convert the Urgent buckets first.


## On this page:

- Before you start





## 1. Before you start

Plan the conversion with the other members of your CSC project.

- Agree on when the conversion will take place.
- Do not upload new files while the conversion is in progress.
- If possible, delete files and buckets that you no longer need before starting the conversion.
- Check the labels and sizes of the buckets that need to be converted.

!!! warning "Projects with more than 5 TB" If your project contains more than 5 TB of data in Urgent buckets, contact the CSC Service Desk before starting the conversion. Converting these buckets is network intensive and may require additional planning.


## 2. Check bucket label

### 2.1 Urgent

Buckets labelled Urgent should be converted as soon as possible.

Before conversion:

- Files in the bucket cannot be accessed.
- Sharing permissions are not visible.

The conversion creates a new bucket with compatible name adding the suffix -conv and copies the files to it. It also restores the bucket size and sharing permissions.

This is a network-intensive operation. Large conversions should be planned in advance to avoid overloading CSC storage infrastructure. If your project's data size exceeds 5 TB**, please contact us for support before starting the conversion. Buckets labelled **Urgent** are given priority in Helpdesk support queues. 

https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD_Connect_Urgent.png

## 2.2 By the end of 2026

Buckets labelled By the end of 2026 must be converted by the end of 2026.

Before conversion:

- Files can still be accessed and downloaded.
- Sharing permissions are not visible.
- The bucket and file size are displayed as zero.

The conversion might create a new bucket with compatible name adding the suffix -conv in case the name contained capital letters and underscore, otherwise the bucket name remains unchanged. The conversion is not network intensive.

https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD_Connect_Bytheend2026.png


## 3. Choose the appropriate conversion method

Choose the method based on bucket's tag and size. The SD Connect Conversion tool is available for download via graphical user interface (for files up to 10 GB), or as poart of the SD Command lien tools on Roihu for large conversions. 

| Bucket Tag | Data Size | Recommended Action | User Guide |
|-------|------------|-------------------|------------|
| Urgent | Up to 1 TB | Use the SD Connect Conversion Tool user interface on your local computer. This is a network-intensive operation. On a standard home internet connection, converting 25 GB may take around 2 hours. | [Link](sd-connect-conversion-tool-ui.md) |
| Urgent | 1–4 TB | Use the SD Connect Conversion CLI on Roihu. | [Link](sd-connect-conversion-cli.md) |
| Urgent | 4–50 TB | Verify that sufficient quota is available to create a copy of the bucket with compatible name.  Use th SD Connect Conversion CLI on Roihu and convert a few buckets at a time.This is a network-intensive operation. Larger projects require advance planning to avoid overloading CSC storage infrastructure and to ensure a smooth conversion.  | Link |
| Urgent | More than 50 TB | Contact CSC support to plan the conversion. | Contact us |
| By End of 2026 | Up to 1 TB | Use the SD Connect Conversion Tool user interface on your local computer. | Link |
| By End of 2026 | More than 1 TB | Use the SD Connect Conversion CLI on Roihu.| Link |



## 4. Convert bucket names


During conversion, the tool makes bucket names compatible with the current SD Connect naming requirements.

Depending on the bucket name, the tool may:

- convert uppercase letters to lowercase and add teh suffic -conv
- replace spaces with hyphens (`-`) and add teh suffix -conv
- replace underscores (`_`) with hyphens (`-`) and add he suffic -conv
- add a unique string if the resulting bucket name already exists.














Follow the instructions for the conversion method you selected. 

Depending on the bucket type and name, the conversion may create a new bucket with a compatible name and copy the files to it.
Bucket name changes

If a new bucket is required, its name is automatically converted to a compatible format. For example:
Before conversion	After conversion
Non-compatible name	non-compatible-name-conv
non_compatible_name	non-compatible-name-conv

The conversion tool can:

    convert uppercase letters to lowercase;
    replace spaces with hyphens (-);
    replace underscores (_) with hyphens (-);
    add the suffix -conv when a new bucket is created.

If the resulting bucket name already exists, the tool adds a unique identifier to the name.


# SD Connect bucket name conversion guide

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
| `compatible-name` → `compatible-name` | No changes in the bucket name. |
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



