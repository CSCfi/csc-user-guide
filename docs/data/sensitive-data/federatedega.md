# Federated European Genome-phenome Archive (FEGA)

Federated European Genome-phenome Archive (FEGA) is a service for storing and sharing human -omics data consented for research. The service is based on a European network of local repositories. CSC hosts Finnish FEGA. 

You can use FEGA either to submit or apply access to biomedical datasets. The service allows you to store sensitive research data under controlled access in Finland. At the same time, the public information (metadata) is made internationally available in central [European Genome-phenome Archive](https://ega-archive.org/studies) (EGA). Each dataset is associated with a Data Access Committee (DAC), which evaluates data access applications and can grant or deny data access for re-use. If the application is approved, the requester can directly access and analyse the sensitive data in a secure and private cloud workspace using CSC Sensitive Data Services for research. 

!!! note
    For more information, check Federated EGA [service description](https://research.csc.fi/-/fega) in CSC service catalog and [CSC sensitive Data Services for research webpage](https://research.csc.fi/sensitive-data-services-for-research).

The following is a step-by-step guide to Finnish FEGA that illustrates:

- **[Data submission](https://github.com/CSCfi/csc-user-guide/edit/wip-at-fega/docs/data/sensitive-data/federatedega.md#data-submission)**
- Data access application
  - For Data Requesters
  - For Data Access Committee

## Useful terminology

- **Central EGA**. Central European Genome-phenome Archive. When submitting data to FEGA, the metadata is made internationally available in central EGA. 
- **Data Access Committee (DAC)**. Individual or group of individuals who are controllers for a dataset stored at FEGA and are responsible for approving and rejecting access requests to that dataset.
- **Data Requester**. Individual who applies access to sensitive data or metadata that has been stored at FEGA.
- **Data Submitter**. Individual who uploads data, metadata, and other information to FEGA for re-use under controlled access. 
- **Finnish FEGA**. A national repository for biomedical data consented for research. CSC hosts Finnish FEGA. The research data uploaded to Finnish FEGA will remain under controlled access in Finland.

## Data submission
### Step 1: Application form
To begin the submission process, please fill in the [application form](https://docs.csc.fi/data/sensitive-data/fega-application.docx) with contact information, details about the type of data submission, and information about the data controller. Send the filled form via email to servicedesk@csc.fi (subject: Federated EGA). You will receive further instructions.

!!! note
    Data submission might take up to a month or more. Therefore, please get in touch with us well in advance (before submitting your manuscript to a scientific journal). In this way, we can offer proper support and guide you during the entire process.
    
### Step 2: Legal agreements 
Each user must provide a series of legal agreements to confirm that they have the authority and permission to deposit data in FEGA. Download the necessary documentation below and share the agreements concerning the data controller with the legal service of your home organisation. Please note that your organisation may already have some required agreements in place with CSC. We will provide additional support if additional agreements are needed. Send the finalised documents via email to servicedesk@csc.fi by replying to the previous email of the CSC helpdesk. 

!!! note
    The required legal documents state the roles of a data processor and a data controller, which are defined in the General Data Protection Regulation (GDPR). CSC acts always as a data processor. In most research projects, the data controller is an academic organisation or other legal entity. 

Here’s a list of the required documents:

- **[Data Processing Agreement](https://research.csc.fi/data-processing-agreement)** (DPA). A data processing agreement (DPA) is a contract between the Data Controller and the Data Processor. It regulates the particularities of data processing – such as its scope and purpose – as well as the rights and duties between the controller and the processor. 
- **[CSC General terms of use](https://research.csc.fi/general-terms-of-use)**.
- **[Description of the data processing activities](https://docs.csc.fi/data/sensitive-data/data-processing-form.docx)**.
- **Data Protection Impact Assessment (DPIA)**. In case you need to draft a DPIA, you can find the technical and organisational security measures for the protection of sensitive data in CSC Sensitive Data Services available for download here <br/><br/>
- **Data Access Agreement (DAA)**. In addition to the legal documents concerning the data controller, you should provide a DAA which is a contract between the Data Access Committee ([DAC](https://ega-archive.org/submission/data_access_committee)) and an requester. The DAA includes all the policies regulating data re-use (e.g., data use, publication, download, or access) and it will be linked to each submitted dataset in the central EGA submitter portal. Your academic organisation might provide a template for the DAA or give you information and assistance. In specific cases, the document needs to be drafted by a legal representative. A copy of the agreement can be returned to servicedesk@csc.fi (subject Federated EGA). For more info and examples, check [DAC and policy documentation](https://ega-archive.org/submission/dac/documentation) and [Data Use Conditions](https://ega-archive.org/data-use-conditions) on EGA webpage. 
- **Names and contact information of the Data Access Committee**.

### Step 3: Credentials
Once the legal agreements between the data controller and CSC are finalised, you can request the central EGA credentials by sending an email to central EGA helpdesk at helpdesk@ega-archive.org. You will receive the credentials via email. 

!!! note
    Central EGA credentials, including a username (format: ega-box-NNN) and a password, are required for the encryption and data upload to Finnish FEGA and for the metadata submission to the submitter portal of central EGA.
    
### Step 4: Data formats
Before uploading the data to FEGA, you must prepare the datasets and verify the data formats. Some examples of the accepted formats are listed below.

!!! note
    A dataset is usually defined as a set of files belonging to the same experiment and data type. One study can be linked to multiple datasets. Your study may include both sensitive (e.g. human genetic or phenotypic information) and non-sensitive data (e.g. viral sequences, metabolites). Only the sensitive data can be submitted to FEGA. The non-sensitive data can be published openly in appropriate repositories. In this case, the sample accessions generated at the repository should be referenced in the FEGA submission.
    
**Sensitive Data**:

- **sequence data**: CRAM, BAM, FASTq, VCF formats
- **array data**: Data from all types of array-based technologies, such as genotypes, gene expression, methylations, etc. is accepted. Central EGA also recommends submitting raw data (IDATs, CELs, final reports) and any analysis files.
- **metagenomics**: EGA has adopted the suite of [Minimum Information about any (x) Sequence (MIxS)](https://press3.mcs.anl.gov/gensc/projects/mixs-gsc-project/) standards to describe data of this type.
- **phenotypic information**: No specific format. Where possible, we recommend using the Experimental Factor Ontologies. To search for the correct ontology terms and describe your phenotypic data, check the [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols/ontologies/efo) developed by EMBL-EBI.
- **linking files**: If non-sensitive datasets belonging to the same study have been submitted to a specific repository, the samples can be linked to sensitive information submitted to Federated EGA for the same sample. The datasets should have different anonymised sample IDs in each archive. The IDs obtained in the appropriate archive can then be referenced in the FEGA submission. For example, the sample ID can be linked in an additional .txt file that can be added to one of the sensitive datasets above.

**Non-sensitive data**:

Non-sensitive data (or open data) needs to be submitted in appropriate archives. For example, sequences to the ENA [European Nucleotide Archive](https://www.ebi.ac.uk/ena/browser/home), variants to EVA [European Variation Archive](https://www.ebi.ac.uk/eva/), array-based to [ArrayExpress – functional genomics data](https://www.ebi.ac.uk/arrayexpress/), phenotypes to [Biosamples BioSamples](https://www.ebi.ac.uk/biosamples/) and GWAS summary statistics to the [GWAS Catalog](https://www.ebi.ac.uk/gwas/).

!!! note
    For more information about data types and formats, check [Central EGA webpage](https://ega-archive.org/submission/sequence) or contact us at servicedesk@csc.fi (subject Federated EGA).

### Step 5: Data encryption and upload 
Next, you can upload the data to Finnish FEGA. Each file uploaded to Finnish FEGA needs to be encrypted. 

!!! note
    The data is encrypted with a FEGA public encryption key using crypt4gh, a tool designed to encrypt and share human genetic data according to the Global Alliance for Genomics and Health (GA4GH) standard.
    
You can carry out the encryption and upload steps using:

- **Fi-FEGA upload tool**. The Fi-FEGA upload tool (graphical user interface) can be used to encrypt and upload files or folders automatically to Finnish FEGA.

or

- **Command-line interface**. Data encryption with crypt4gh CLI and data upload with sftp CLI. If you prefer to use the command-line interface, you can find information on the encryption and upload step below. 

**Fi-FEGA upload tool**

1. You can download the application specific to your operating system from the GitHub repository: Linux, Mac or Windows. After downloading and unzipping the file, you can find the SDA application in your download folder. When you open the application, you might encounter an error message. In this case, click on More info and verify that the publisher is CSC-IT Center for Science (or in Finnish CSC-Tieteen tietotekniikan keskus Oy) and click on Run anyway. 
2. Next, download the Finnish FEGA public encryption key. 
3. Open the FEGA submission tool and click on Load Recipient Public Key. This opens a file browser that you can use to select the Finnish FEGA public encryption key (example_ega.key). Next, click on Open.
4. Click on Select file to Upload or Select Directory to upload to upload a single file or an entire folder. 
5. Next, you need to fill in the SFTP (or secure connection) credentials, which correspond to your Central EGA account username. In SFTP Username, write your EGA username (ega-box-NNN). In SFTP Server, write the following: test.sd.csc.fi:9002. Loading an SFPT key is not required for data uploads to FEGA.
6. Click on Encrypt and upload files. The tool will ask the SFTP Passphrase, which corresponds to your Central EGA account password. After clicking on OK, the SDA toll will start the data encryption and upload. 
7. The application is not provided with a progress bar. Data encryption and upload can take minutes or up to several hours, depending on the size of the dataset. Data upload is successfully finished when the activity log in the SDA tools visualises the following message: Disconnecting SFPT. SFPT has been disconnected.
8. Please inform the Finnish FEGA helpdesk via email (servicedesk@csc.fi) when you have completed the data encryption and upload to Finnish FEGA. You will receive further instructions for the metadata submission.


