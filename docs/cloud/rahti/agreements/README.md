#  Rahti service agreement documents

This directory contains the canonical versions of the Rahti service level agreement and terms of use documents, in addition to supplementary files for PDF creation.

  * logo.png, footer.png: images for the PDF documents
  * pdf_metadata.yml: Metadata for PDF creation using pandoc
 
## Making PDF versions of the document

## Install required software

```
yum install pandoc pandoc-pdf
```
## Create a PDF of a file

```
pandoc  sla.md pdf_metadata.yml -o /tmp/rahti-sla.pdf
```

