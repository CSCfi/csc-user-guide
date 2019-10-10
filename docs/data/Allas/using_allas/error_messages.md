# Common error messages

### HTTP status code 409 

A bucket with that name already exists:
```bash
Conflict
```

### HTTP status code 404

The bucket does not exist:
```bash
NoSuchBucket
```

### HTTP status code 403

Your credentials are not allowed to view the bucket:
```bash
AccessDenied
```

### HTTP status code 403

You have reached a quota limit. Contact `servicedesk@csc.fi` and request a quota increase. Please specify the project name, bucket name and size of the file in the request.
```bash
QuotaExceeded
```

### HTTP status code 400

THe file is too large. See [Swift client - Files larger than 5 GB](./swift_client.md#files-larger-than-5-gb).
```bash
EntityTooLarge
```
