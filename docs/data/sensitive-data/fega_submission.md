# Data submission

!!! Note 
    We will process submissions in the order we have received the support requests. In addition to the legal agreements listed on this page, there needs to be a service agreement between CSC and the data controller specific for FEGA service. Make sure before starting submitting any data that all these legal agreements are in place.

## Submission process overview 
[![FEGA submission process overview](images/fega/fega_submission_overview.png)](images/fega/fega_submission_overview.png)

## Step 1: Basic information of the submission

Submission to the Finnish FEGA service starts with contacting the Finnish FEGA helpdesk and providing the basic information of the submission.

To begin the submission process, please fill in the [basic information form](./fega-basic-information.docx) with contact information, details about the data submission type and information about the data controller, or provide the same information in an email message. Send the required information via email to servicedesk@csc.fi (subject: Federated EGA). You will receive further instructions.

!!! note

    - This workflow is specific for submitting datasets to Finnish FEGA. Central EGA and other FEGA nodes have different data submission processes.
    
    - Data submission might take up to a month or more. Therefore, please get in touch with us well in advance (before submitting your manuscript to a scientific journal). In this way, we can offer proper support and guide you during the entire process.
    
    - Please use the same email thread throughout the whole submission process.
    
## Step 2: Legal agreements 

The data deposition to FEGA requires a series of legal agreements. The necessary documentation is introduced below. The agreements concerning the data controller need to be discussed with the legal service of your home organisation. Please note that your organisation may already have some required agreements in place with CSC. We will provide support if additional agreements are needed. Please confirm that all the necessary agreements are in place before starting the submission by replying to the previous email you received from the CSC helpdesk (servicedesk@csc.fi).

!!! note
    The required legal documents state the roles of a data processor and a data controller, which are defined in the General Data Protection Regulation (GDPR). CSC acts always as a data processor. In most research projects, the data controller is an academic organisation or other legal entity. The ownership of the data does not change by using this service.

The Data Controller must have a **service agreement** specific to FEGA service with CSC before the data can be transferred. The service agreement includes the **Data Processing Agreement (DPA)**, which regulates the particularities of data processing – such as its scope and purpose – as well as the rights and duties between the controller and the processor. [CSC’s general DPA](https://research.csc.fi/data-processing-agreement) is available on the CSC website. Also, **[CSC General terms of use](https://research.csc.fi/general-terms-of-use)** and **[Description of the data processing activities](./data-processing-form.docx)** are included in the service agreement.

In addition to the legal agreements between the Data Controller and Data Processor, you need a **Data Access Agreement (DAA)**. The DAA is a contract between the Data Access Committee ([DAC]([https://ega-archive.org/submission/data_access_committee](https://ega-archive.org/access/data-access-committee/what-is-dac/))) and an applicant applying access to the data. With the DAA, you can define conditions and restrictions for the data reuse. The document includes all the policies regulating data reuse (e.g. data use, publication, download, or access) and it will be linked to each submitted dataset. It might also include a data transfer agreement (needed when researcher from non-EU/non-EEA are accessing the data via SD Desktop). For more information, contact the legal services of your home organisation.

## Step 3: Credentials

Once the legal agreements between the data controller and CSC are finalised, you can register on the [EGA webpage](https://ega-archive.org/register/) to create central EGA credentials. You will receive an activation link via email after your registration has been approved by central EGA. After activating your credentials, contact servicedesk@csc.fi in order to be added as a Finnish FEGA submitter.

!!! note
    Central EGA credentials, including a username (usually this is your email address) and a password, are required for the encryption and data upload to Finnish FEGA and for metadata submission with the submitter portal.

## Step 4: Data formats
Before uploading the data to FEGA, you must prepare the datasets and verify the data formats. Some examples of the accepted formats are listed below.

!!! note
    A dataset is usually defined as a set of files belonging to the same experiment and data type. One study can be linked to multiple datasets. Your study may include both sensitive (e.g. human genetic or phenotypic information) and non-sensitive data (e.g. viral sequences, metabolites). Only the sensitive data can be submitted to FEGA. The non-sensitive data can be published openly in appropriate repositories. In this case, the sample accessions generated at the repository should be referenced in the FEGA submission.
    
**Sensitive Data**:

- **sequence data**: CRAM, BAM, FASTQ, VCF formats

- **array data**: Data from all types of array-based technologies, such as genotypes, gene expression, methylations etc. is accepted. Central EGA also recommends submitting raw data (IDATs, CELs, final reports) and any analysis files.

- **metagenomics**: EGA has adopted the suite of [Minimum Information about any (x) Sequence (MIxS)](https://www.gensc.org/pages/projects/mixs-gsc-project.html) standards to describe data of this type.

- **phenotypic information**: No specific format. Where possible, we recommend using the Experimental Factor Ontologies. To search for the correct ontology terms and to describe your phenotypic data, check the [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols/ontologies/efo) developed by EMBL-EBI.

- **linking files**: If non-sensitive datasets belonging to the same study have been submitted to a specific repository, the samples can be linked to sensitive information submitted to FEGA for the same sample. The datasets should have different anonymised sample IDs in each archive. The IDs obtained in the appropriate archive can then be referenced in the FEGA submission. For example, the sample ID can be linked in an additional .txt file that can be added to one of the sensitive datasets above.

**Non-sensitive data**:

Non-sensitive data (or open data) needs to be submitted in appropriate archives. For example, sequences to the ENA [European Nucleotide Archive](https://www.ebi.ac.uk/ena/browser/home), variants to EVA [European Variation Archive](https://www.ebi.ac.uk/eva/), array-based to [ArrayExpress – functional genomics data](https://www.ebi.ac.uk/arrayexpress/), phenotypes to [BioSamples](https://www.ebi.ac.uk/biosamples/) and GWAS summary statistics to the [GWAS Catalog](https://www.ebi.ac.uk/gwas/).

!!! note
    For more information about data types and formats, check [Central EGA webpage](https://ega-archive.org/submission/sequence) or contact us at servicedesk@csc.fi (subject: Federated EGA).

## Step 5: Data encryption and upload 
Next, you can upload the data to Finnish FEGA. Each file uploaded to Finnish FEGA needs to be encrypted. 

!!! note
    The data is encrypted with a FEGA public encryption key using crypt4gh, a tool designed to encrypt and share human genetic data according to the Global Alliance for Genomics and Health (GA4GH) standard.
    
You can carry out the encryption and upload steps using:

- **Option 1 - Fi-FEGA upload application**. The Fi-FEGA upload application (graphical user interface, GUI) can be used to encrypt and upload files or folders automatically to Finnish FEGA.

or

- **Option 2 - Command-line interface**. Data encryption with crypt4gh CLI and data upload with sftp CLI. If you prefer to use the command-line interface, you can find information on the encryption and upload steps below. 

### Option 1 - Fi-FEGA upload application

1. You can download the Fi-FEGA upload application specific to your operating system from the [GitHub repository](https://github.com/CSCfi/sda-uploader/releases): Linux, Mac or Windows (release v0.7.0), select from the sdagui options. After downloading and unzipping the file, you can find the application in your download folder. When you open the application, you might encounter an error message. In this case, click on *More info* and verify that the publisher is CSC-IT Center for Science (or in Finnish: CSC-Tieteen tietotekniikan keskus Oy) and click on *Run anyway*. 

2. Next, download the [Finnish FEGA public encryption key](https://a3s.fi/fega-public-keys/fega-pubkey-c4gh.pub). 

3. Open the upload application and click on *Load recipient public key*. This opens a file browser that you can use to select the Finnish FEGA public encryption key (fega-pubkey-c4gh.pub). Next, click on *Open*.

4. Click on *Select file to upload* or *Select directory to upload* to upload a single file or an entire folder. 

5. Next, you need to fill in the SFTP (or secure connection) credentials, which correspond to your Central EGA account username. In SFTP Username, write your EGA username (usually this is your email address). In SFTP Server, write the following: admin.sd.csc.fi:50529. Loading an SFPT key is not required for data uploads to FEGA.

6. Click on *Encrypt and upload files*. The tool will ask the SFTP Passphrase, which corresponds to your Central EGA account password. After clicking on OK, the application will start the data encryption and upload. 

7. The application is not provided with a progress bar. Data encryption and upload can take minutes or up to several hours, depending on the size of the dataset. Data upload is successfully finished when the activity log in the application visualises the following message: Disconnecting SFTP. SFTP has been disconnected.

8. Please inform the Finnish FEGA helpdesk via email (servicedesk@csc.fi) when you have completed the data encryption and upload to Finnish FEGA. You will receive further instructions for the metadata submission.

[![Fi-FEGA upload application](images/fega/fega_upload.png)](images/fega/fega_upload.png)

### Option 2 - Command line interface
**Data encryption with crypt4gh CLI**:

1.	Python 3.6+ is required to use the Crypt4GH encryption utility. If you need help with installing Python, please follow [these instructions](https://www.python.org/downloads/release/python-3810/).

2.	Open a terminal and install Crypt4GH directly with pip tool:
```
pip install crypt4gh
```

3.	To encrypt a file with the [Finnish FEGA public encryption key](https://a3s.fi/fega-public-keys/fega-pubkey-c4gh.pub) use ```crypt4gh encrypt``` command:
 
```
$ crypt4gh encrypt  --recipient_pk fega-pubkey-c4gh.pub <example_file.txt> example_file.txt.c4gh
```

Where the syntax *--recipient_pk* defines the public key used to encrypt the data. In this case, Finnish FEGA public key. *example_file.txt.c4gh* defines the input file and output encrypted file. 

**Data upload with sfpt CLI (default in Linux and Mac OS)**:

1. Open a terminal and transfer the encrypted files or directory with the following syntax, where <ega_user> is the EGA credentials username (usually this is your email address):

```
sftp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -P 50529 <ega_user>@admin.sd.csc.fi
```

2. For the password, use your Central EGA account password. Data upload can take minutes or up to several hours, depending on the size of the dataset

3. Please inform the Finnish FEGA helpdesk via email (servicedesk@csc.fi) when you have completed the data encryption and upload to Finnish FEGA. You will receive further instructions for the metadata submission.

## Step 6: Data Access Committee and Policy registration

Data Access Committee (DAC) and Policy are created by CSC service desk separately from other metadata. DAC and policy must be finalised before they can be added to the metadata submission.

To register DAC and Policy for your dataset, contact servicedesk@csc.fi. For registration, you will need

1. names and email addresses of all the Data Access Committee members;
2. Data Access Agreement;
3. other necessary information defining the conditions of data reuse, e.g. DUO codes; and
4. data application link for each dataset (provided by CSC helpdesk).

### Dataset application link

After uploading the data to Finnish FEGA, you will receive a dataset application link for each dataset via email from the CSC helpdesk.

!!! note
    If someone wants to apply access to your dataset stored in Finnish FEGA, they must click the dataset application link on the EGA website. The link will direct the user to the application form in SD Apply. SD Apply is a service for applying access rights to sensitive datasets stored at CSC. There is a separate [guide](./fega_application.md) for applying data access.

## Step 7: Metadata submission

Next, you can describe all the information related to your study, i.e. metadata, using the [Finnish FEGA submitter portal](https://submission.finland.ega-archive.org/) or programmatically. The public metadata will be published on the EGA website to facilitate data discovery and re-use.

You can get an introduction to the submitter portal from the video below or by taking the tour available in the portal by clicking the yellow book icon in the top right corner while you are logged in.

<iframe width="280" height="155" srcdoc="https://www.youtube-nocookie.com/embed/eDTNIE8Ex0g?si=yTW0Cs0-dDPhoyKo&amp;start=134" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Log in to the submitter portal using the EGA credentials (username: usually your email address, and password).

Using the submitter portal, you can register the following metadata objects:

- **Study**. Information about the sequencing study.

- **Samples**. Information about the sequencing samples. You can also do a batch upload for samples.

- **Experiments**. Information about the sequencing methods, protocols, and machines.

- **Runs**. Samples, experiments, and files are linked through runs. Appropriate objects for FASTQ and BAM/CRAM submissions. You can also do a batch upload for runs.

- **Analysis**. References the analysis (BAM) files. Associated with samples and study. Analysis should be only be used for BAM/BAI pair, VCF and phenotype linkage to samples. The analysis is an EGA specific metadata object that links Samples, to Files.

- **Dataset**. Contains the collection of runs/analysis data files to be subject to controlled access. Associated with Policy, which is created by CSC helpdesk.

After data release, each of these objects will be assigned with a permanent identifier or unique accession number.

!!! note
    
    - **Data Access Committee (DAC)** and **Policy** need to be created by CSC helpdesk before they can be added to the metadata in the submitter portal. DAC is always associated with a Policy, and by selecting a Policy for a dataset in the metadata submitter portal, you also select the DAC linked to that specific Policy.
    
    - **Study**, **Samples**, and **Experiment** metadata can be registered before uploading files, while **Run** and **Analysis** objects cannot be registered before the files have been uploaded to Finnish FEGA. You can choose **Policy** for your submission only after you have registered all the other metadata, when you are registering **Dataset** metadata.
    
    - If you are performing *array-based submission(s)*, the submitter portal should only be used to register the Study, Samples, and Dataset metadata objects. In contrast, the other metadata objects need to be registered using an excel template.
    
## Step 8: Data release
To finalise your submission, write to servicedesk@csc.fi to confirm that the submission can be released and add the following information from the submitter portal:

- Name of the submission (as on the submitter portal)

- Study Accession number (EGAS)

- Dataset Accession number (EGAD)

- Appropriate Data Use Ontology codes (DUO). You can find more information in Data Use Conditions on [EGA webpage](https://ega-archive.org/access/data-access-committee/data-use-ontology/). 

CSC helpdesk will complete the release process. You will receive confirmation of successful submission and accessions suitable for publication, grants, etc. from the CSC helpdesk.
