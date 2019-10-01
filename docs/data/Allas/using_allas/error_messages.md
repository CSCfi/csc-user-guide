
# Common Error Messages

HTTP status code 409 - There is already a bucket with that name:
```bash
Conflict
```
HTTP status code 404 - Bucket does not exist:
```bash
NoSuchBucket
```
HTTP status code 403 - Your credentials are not allowed to view bucket:
```bash
AccessDenied
```
HTTP status code 403 - You have reached a quota limit. Contact servicedesk@csc.fi and ask to have the quota increased. Include the project, bucket and size of the file.
```bash
QuotaExceeded
```
HTTP status code 400 - Your file is much too large. See [Swift client - Files larger than 5 GB](./swift_client.md#files-larger-than-5-gb){:target="_blank}.
```bash
EntityTooLarge
```
