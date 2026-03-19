# Deployment Security
 
 This section controls image verification and vulnerability enforcement.
 
 Administrators can enforce security policies such as:
 
### Allowing only signed images
 
 Two image signature verification mechanisms are there, cosign and Notation. If enabled, only signed images can be deployed. It ensures image integrity and authenticity. 

### Preventing the use of vulnerable images
 
 If 'Prevent vulnerable images from running' is enabled, Satama blocks deployment of images that contain vulnerabilities above a selected severity level. 
 
 You can adjust severity threshold from dropdown. If 'Low' vulnerability severity is selected, that means if any vulnerability (Low, Medium, High, Critical) exists, deployment can be blocked.
