# Troubleshooting

<table>
<tr>
<th>Problem</th>
<th>Description</th>
<th>Solution</th>
</tr>
<tr>
<td>Service Access</td>
<td>I can not access SD Connect</td>
<td>1) Verify in the MyCSC portal if your CSC project has service access to SD Connect and accepted CSC’s terms of use. 2) Link your Haka account to your CSC account 3) SD Connect is not supported during private browsing with Firefox (incognito mode).</td>
</tr>
<tr>
<td>

</td>
<td>I can not access SD Connect, an error tells me that it was not possible to perform elevation /authentication</td>
<td>

Activate multifactor authentication (MFA) on your csc profile in the Mycsc.fi portal (necessary since October 2024). https://docs.csc.fi/accounts/mfa/
</td>
</tr>
<tr>
<td>

</td>
<td>I need to log in twice to be able to access the service</td>
<td>Currently, the login steps require you to login twice to the service. We apologise for the inconvenience, this problem should be solved by November 2024.</td>
</tr>
<tr>
<td>

</td>
<td>I end up in a loop of login requests</td>
<td>We suggest you to use Chrome as better supported browser. If you are using Firefox, login will be again successful if you clear history and cookies.</td>
</tr>
<tr>
<td>Data Access</td>
<td>I can not see files uploaded via an older version of SD Connect</td>
<td>Unencrypted files are no longer visible using SD Connect 2.0 since October 2024</td>
</tr>
<tr>
<td>

</td>
<td>I can not access files stored in SD Connect using SD Desktop</td>
<td>Unencrypted files are not accessible via the SD Desktop service (you can use a Allas user interfaces for managing non encrypted data). Only files encrypted using the SD service encryption key are visible in the secure computing environment (or encrypted using SD Connect default option). Refresh the Data Gateway application. </td>
</tr>
<tr>
<td>Folder creation</td>
<td>I can not create a new folder.</td>
<td>Try using a unique folder name that doesn’t contain special characters. Select the correct CSC project in the SD Connect user interface</td>
</tr>
<tr>
<td>Folder not visible</td>
<td>I cannot find my folder.</td>
<td>Check if the folder is stored under a different project. If someone has shared the folder with you, you can find it under the Shared to section and copy it. If someone shared the folder with you, they could have revoked the sharing permissions.</td>
</tr>
<tr>
<td>Folder deletion</td>
<td>I can not delete an empty folder</td>
<td>

If the folder has been created in November or December 2022, contact us at servicedesk@csc.fi (subject: sensitive data)
</td>
</tr>
<tr>
<td>Manual decryption  with Crypt4gh</td>
<td>Cannot open or decrypt files downloaded from SD Connect.</td>
<td>

1) You can not decrypt files that have been encrypted with the SD Connect user interface and default option before October 2024. In this case, the files have been encrypted with the service-specific encryption key and are automatically decrypted when accessed using the SD Desktop service. Please contact us at servciedesk@csc.fi for support.
2) Add the extension .c4gh to the downloaded files if it is missing and decrypt it using your private encryption key.
</td>
</tr>
<tr>
<td>Data upload</td>
<td>I am trying to upload a big file/folder with the user interface, and the upload is not responding.</td>
<td>Files or folders larger than 100 GB should be uploaded programmatically. SD Connect user interface supports only data uploads that last up to 8 hours.</td>
</tr>
<tr>
<td>Data upload</td>
<td>I cannot upload data into my folder</td>
<td>Check if your CSC project has storage space left and apply for more quota (more info available in the first chapter of this guide under Accounts).</td>
</tr>
<tr>
<td>Data upload</td>
<td>Low upload speed (programmatically)</td>
<td>


Uplaod and download speed depends on the local network. 
</td>
</tr>
<tr>
<td>Shared folder</td>
<td>I cannot upload data into a shared folder</td>
<td>Only folders shared with 'collect' permissions allow data uploads.</td>
</tr>
<tr>
<td>

</td>
<td>I cannot download the content of a shared folder.</td>
<td>Only folders shared with 'transfer' or 'collect' permissions allows you to download a copy of the content. </td>
</tr>
</table>