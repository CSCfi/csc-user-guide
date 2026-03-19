# SBOM Generation

SBOM (Software Bill of Materials) generation in Satama provides users with a clear inventory of the components, libraries, and dependencies included in a container image. 

SBOM generation helps improve software transparency and supply chain security by showing exactly what software is included inside an image.

### Benefits of SBOM

* Better visibility into image contents
* Faster vulnerability investigation
* Compliance with security standards
* Improved supply chain security

### Automatically generate SBOM

You can enable automatic SBOM generation of images on push. 

* Inside the project, navigate to **Configuration** tab.
* Locate the **SBOM generation** section.
* Check box in front of **Automatically generate SBOM on push**

When SBOM generation is enabled, Satama automatically analyzes images after they are pushed to a project, producing a structured list of components that can be viewed directly from the image details page. If disabled, user can maually trigger SBOM generation, click on the repository and select the image. Now you can start scanning by clicking the botton 'generate SBOM'.