# Under construction

<div class="grid cards" markdown>

- :material-alert:{ .lg .middle } **Page is under construction**
  { .csc-grid-card-warning }

    ---
    
    This page and content is under construction and development.

</div>

# SD Connect Conversion guide

SD Connect has been upgraded to a new version. Existing buckets must be converted to maintain access and functionality.

## Step 1: Check bucket tag

### 🔴 Urgent (fully incopatible name, file can not be accessed)

The bucket name is not compatible with the new SD Connect version, and the bucket content is no longer accessible.

- Files cannot be accessed and sharing permissions are not visible.
- Conversion is required to regain access. 

During the conversion, a new bucket is created and all files are copied to it. Make sure your CSC project has enough free quota to temporarily store both copies of the data.

### 🟡 By End of 2026 (fully comapatible bucket name, files can be accessed)

The bucket content is still accessible, however bucket size is showed as zero and sharing prmissions are not visible. 

- Files can still be accessed and downloaded.  Sharing permissions are not be visible and bucket size is zero. 
- Conversion is optional, but it is recommended to restore bucket size information and sharing permissions.

During the conversion, no new bucket is created. The tool will represtinate the correct bucket size and repristinae sharing permssions. 


### 🟡 By End of 2026 (includes incompatible capital letters and underscor, files can be accessed). 

The bucket content is still accessible, however bucket size is showed as zero and sharing prmissions are not visible. 

- Files can still be accessed and downloaded.  Sharing permissions are not be visible and bucket size is zero. 
- Conversion is optional, but it is recommended to restore bucket size information and sharing permissions.

During the conversion, a new bucket is created and all files are copied to it. Make sure your CSC project has enough free quota to temporarily store both copies of the data.

### Multiple tags

If your project contains buckets with different tags, convert all **Urgent** buckets first and then proceed with the remaining buckets.

---

## Step 2: Choose the appropriate conversion method

| Tag | Data Size | Recommended Action | User Guide |
|-------|------------|-------------------|------------|
| Urgent | Up to 1 TB | Use the SD Connect Conversion Tool user interface on your local computer. | [Link](sd-connect-conversion-tool-ui.md)|
| Urgent | 1–4 TB | Use the SD Connect Conversion CLI on Rhoihu. | Link |
| Urgent | 4–50 TB | Verify that sufficient quota is available to create a copy of the bucket with comaptible name.  Use the CLI on Rhoihu and convert a few buckets at a time. | Link |
| Urgent | More than 50 TB | Contant CSC support to plan the conversion. | Contact us |
| By End of 2026  | Up to 1 TB | Use the SD Connect Conversion Tool user inetrface on your local computer. | Link |
| By End of 2026  | More than 1 TB | Use the SD Connect Conversion CLI on Rhoihu.| Link |
| By End of 2026 (name includes capital letters and underscores)| Any size |Contant CSC support to plan the conversion.| Link |

---

## Bucket name requirements

Bucket names must:

- Start and end with a lowercase letter or a number.
- Be between 3 and 63 characters long.
- Contain only lowercase letters (`a-z`), numbers (`0-9`), and hyphens (`-`).

Bucket names cannot contain:

- Uppercase letters (`A-Z`)
- Underscores (`_`)
- Accented or special characters such as `å`, `ä`, `ö`, or `é`
