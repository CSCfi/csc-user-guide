# Finnish Federated EGA Node

The Federated European Genome-phenome Archive (FEGA) is a European network of local repositories that facilitates storing and sharing human -omics data. CSC hosts the Finnish Federated EGA. After completing the submission process, your sensitive research data is stored under controlled access in Finland. At the same time, the public information is available for discovery internationally through the [European Genome-phenome Archive](https://ega-archive.org/studies). Each dataset is associated with a Data Access Committee, which manages it, evaluating external requests and granting or denying data access for re-use. Using CSC Sensitive Data Services for research, the requestor can then directly analyze (via data streaming) the sensitive data stored in Federated EGA using a private and secure cloud workspace.

For more information, check Federated EGA [service description](https://research.csc.fi/-/fega) in CSC service catalog and [CSC sensitive Data Services for research webpage](https://research.csc.fi/sensitive-data-services-for-research).

The following is a step-by-step guide to Federated EGA Finland that illustrates:

- [Data submission process](https://csc-guide-preview.rahtiapp.fi/origin/fm-wip-sensitive-data-piloting/data/sensitive-data/federatedega/#submission-process-overview)
- [Data access for applicants](https://csc-guide-preview.rahtiapp.fi/origin/fm-wip-sensitive-data-piloting/data/sensitive-data/federatedega/#data-access-for-applicants)
- Data access approval for DACs


## Submission process overview


![Artboard 1](https://user-images.githubusercontent.com/83574067/148032149-1d58b8f2-6bc7-4f82-805b-a2840cb6dbd1.png)


## Application form

To begin the submission process, please fill in the [application form](./fega-application.docx) with contact information, details about the type of data submission, and information about the data controller. Then, you can send the form via email to servicedesk@csc.fi (subject: Federated EGA). You will receive further instructions.


!!! note
    Data submission might take up to a month or more. Therefore, please get in touch with us well in advance (before submitting your manuscript to a scientific journal). In this way, we can offer proper support and guide you during the entire process.



## Legal agreements

Each user must confirm that they have the authority and permission to deposit data in Federated EGA, providing a series of legal agreements.

Listed below are the documents that define CSC's roles (as the service provider) and the Data Controller according to the General Data Protection Regulation. In most research projects, the data controller is a legal entity (academic organization). 

You can share the following documents with your organization's legal service and return them via email to servicedesk@csc.fi (subject: Federated EGA). We will provide additional support if specific agreements are needed.


- **Data Processing Agreement (DPA)**. A data processing agreement (DPA) is a contract between the Data Controller and the Data Processor. It regulates the particularities of data processing – such as its scope and purpose – as well as the relationship between the controller and the processor: [CSC General terms of use](https://research.csc.fi/general-terms-of-use) and [CSC Data Processing Agreement](https://research.csc.fi/data-processing-agreement).

- **Description of the data processing activities**: available for download [here](./data-processing-form.docx)

- **Pilot or service agreement for Federated EGA**. A pilot or service agreement is a contract that defines the terms and conditions for service between an academic organization and CSC. If needed, the contract will be drafted with the help of CSC customer support.

- In case you need to draft a **Data Protection Impact Assessment (DPIA)**, you can find the technical and organizational security measures for the protection of
sensitive data in CSC Sensitive Data service available for download [here](./technical-organisational-sec-measures.pdf)

In addition, the legal document provided by academic organizations: **Data Access Agreement (DAA)**. The DAA is a contract **between the Data Access Committee [DAC](https://ega-archive.org/submission/data_access_committee) and an applicant** which includes all the policies regulating data re-use (e.g., data use, publication, download, or access). Your academic organization might provide a template or give you information/assistance. In specific cases, the document needs to be drafted by a legal representative. The Data Access Agreement will be linked to each submitted dataset using the EGA submitter portal interface. A copy can be returned to servicedesk@csc.fi (subject Federated EGA). For more info and examples, check [DAC and policy documentation](https://ega-archive.org/submission/dac/documentation) and [Data Use Conditions](https://ega-archive.org/data-use-conditions) on EGA webpage. 


## Credentials

Central EGA credentials (username: ega-box-NNN and password) are required:
- for data upload  to the Finnish Federated EGA node;
- for metadata submission to Central EGA using the submitter portal.

You will obtain the credentials via email only when the legal agreements between the Data Controller (your home organization) and CSC (or the Finnish Federated Node) have been finalized.


## Data formats

Each dataset is usually defined as a set of files belonging to the same experiment and data type. One study can be linked to multiple datasets.
Your study may include managed sensitive data (e.g., human genetic or phenotypic information), which can be submitted to Federated EGA, and non-sensitive data (e.g., viral sequences, metabolites), which can be published openly appropriate repositories. In this case, the sample accessions generated at the repository can be referenced in the Federated EGA submission in a linking file.

**Sensitive Data** :

- **sequence data**: CRAM, BAM, FASTq, VCF formats;

- **array data**: data from all types of array-based technologies, such as genotypes, gene expression, methylations, etc. Central EGA also recommends submitting raw data (IDATs, CELs, final reports) and any analysis files.

- **metagenomics**:  EGA has adopted the suite of [Minimum Information about any (x) Sequence (MIxS](https://press3.mcs.anl.gov/gensc/projects/mixs-gsc-project/) standards to describe data of this type.

- **phenotypic information**: no specific format. Where possible, we recommend using the Experimental Factor Ontologies.
  To search for the correct ontology terms and describe your phenotypic data check the [Ontology Lookup Service (OLS)](https://www.ebi.ac.uk/ols/ontologies/efo ) developed by EMBL-EBI.
 
 - **linking files**: if non-sensitive datasets belonging to the same study have been submitted to a specific repository, the samples can be linked to sensitive information submitted to Federated EGA for the same sample. The datasets should have different anonymized sample IDs in each archive. The IDs obtained in the appropriate archive can then be referenced in the Federated EGA Submission; for example, the samples ID can be linked in an additional .txt file that can be added to one of the sensitive datasets above.

**Non-sensitive data**:

Non-sensitive data (or open data) needs to be submitted in appropriate archives: for example sequences to the ENA [European Nucleotide Archive](https://www.ebi.ac.uk/ena/browser/home), variants to EVA [European Variation Archive](https://www.ebi.ac.uk/eva/), array-based to [ArrayExpress – functional genomics data](https://www.ebi.ac.uk/arrayexpress/),  phenotypes to [Biosamples BioSamples](https://www.ebi.ac.uk/biosamples/) and GWAS summary statistics to the [GWAS Catalog](https://www.ebi.ac.uk/gwas/).

For more information about data types and formats, check [Central EGA webpage](https://ega-archive.org/submission) or contact us at servicedesk@csc.fi (subject Federated EGA).


## Data encryption and upload to the Finnish Node

Before data upload, each file needs to be encrypted with Federated EGA public encryption key using crypt4gh, a tool designed to encrypt and share human genetic data according to the Global Alliance for Genomics and Health (GA4GH) standard. You can carry out the encryption and upload steps using:

-**SDA application**: the Sensitive Data Access (SDA) graphical user interface can be used to  encrypt and automatically upload files or folders to the Finnish Federated EGA node;

-**command-line interface**: data encryption with crypt4gh CLI and data upload with sftp CLI.


Each file belonging to a submission needs to be encrypted with Federated EGA public encryption key and crypt4gh before data upload to the Finnish Federeted EGA node, hosted by CSC. To facilitate this step, we have developed the SDA tool (Sensitive Data Access tool, a graphical user interface), which can be used to automatically encrypt and upload data. If you prefer to use the command-line user interface, you can find information on the encryption and upload step below. 

### **SDA graphical user interface**

1. You can download the application specific to your operating system from the [GitHub repository](https://github.com/CSCfi/sda-uploader): [Linux](https://github.com/CSCfi/sda-uploader/releases/download/v0.5.3/sdagui-python3.7-linux-amd64.zip), [Mac](https://github.com/CSCfi/sda-uploader/releases/download/v0.5.3/sdagui-python3.7-macos-amd64.zip) or [Windows](https://github.com/CSCfi/sda-uploader/releases/download/v0.5.3/sdagui-python3.7-windows-amd64.zip). Verify that the program has been digitally signed by CSC - IT Center for Science. After downloading and unzipping the file, you can find the SDA application in your download folder. When you open the application, you might encounter an error message. In this case, click on *More info* and verify that the publisher is CSC-IT Center for Science (or in Finnish CSC-Tieteen tietotekniikan keskus Oy) and then click on *Run anyway*. 

2. Next, download the [Finnish Federated EGA public encryption key](https://a3s.fi/swift/v1/AUTH_5e26ea3590b94423aea712aad7a289d4/fega-public-keys/fega-demo-key.c4gh.pub) 

3. Open the SDA application and click on *Load Recipient Public Key*. This opens a file browser that you can use to select the Finnish Federated EGA public encryption key (example_ega.key). Next, click on *Open*.

4. Click on *Select file to Upload* or *Select Directory to upload* to upload a single file or an entire folder. 

5. Next, you need to fill in the SFTP (or secure connection) credentials, which correspond to your Central EGA account username:

      in *SFTP Usarname* write your EGA usarname (ega-box-NNN)
      
      in *SFTP Server* write the follwing: test.sd.csc.fi:9002. Note: loading an SFPT key is not required for data uploads to Federated EGA.

6. When you click on *Encrypt and upload files*, the tool will ask the *SFTP Passphrase*, which corresponds to your Central EGA account password. After clicking on *OK*, the SDA toll will start data encryption and upload. 

7. The tool is not provided with a progress bar. Depending on the dataset size, data encryption and upload can take minutes or up to several hours. Data upload is successfully finished when the SFTP disconnects, and the activity log in the SDA tools visualizes this message: *Disconnecting SFPT. SFPT has been disconnected.*




### **Command line interface**

Data encryption with crypt4gh CLI:

1. **Python 3.6+ is required** to use the Crypt4GH encryption utility. If you need help installing Python, please follow [these instructions](https://www.python.org/downloads/release/python-3810/).

2. Open a terminal and install Crypt4GH directly with pip tool:

"`bash
pip install crypt4gh     
```

3. To encrypt a file with the [Finnish Federated EGA public encryption key](https://a3s.fi/swift/v1/AUTH_5e26ea3590b94423aea712aad7a289d4/fega-public-keys/fega-demo-key.c4gh.pub) use `crypt4gh encrypt` command:

```bash
$ crypt4gh encrypt  --recipient_pk finnishfega.pub < example_file.txt > example_file.txt.c4gh
```

Where the syntax:
- -- recipient_pk  defines the public key used to encrypt the data, in this case, Finnish Federated EGA public key
- <example_file.txt >example_file.txt.c4gh  defines the input file and output encrypted file. 


Data upload with sfpt CLI (default in Linux and Mac OS):

4. Open a terminal and transfer the encrypted files or directory with the following syntax:

```bash
sftp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -P 9002 <ega_user>@test.sd.csc.fi
```
 where ega_user is the EGA credentials username: ega-box-8903






## Metadata submission using Central EGA submitter portal

After data upload to the Finnish Node, you can describe all the information (or metadata objects) related to your study using Central [EGA submitter portal](https://test.ega-archive.org/submitter-portal/#/login) or programmatically (https://ega-archive.org/submission/sequence/programmatic_submissions). This information will then be published on the EGA website to facilitate data discovery and re-use.

You can log in to the submitter portal using the same EGA credentials (username: ega-box-NNN and password)  obtained when applying for the Finnish Federated EGA account.
Specific guidance on EGA submitter portal can be found on EGA website: [user guide and video tutorials](https://ega-archive.org/submission/tools/submitter-portal).

Briefly, using the interface, you can register the following metadata objects:

- Study: information about the sequencing study

- Samples: Information about the sequencing samples

- Experiments: Information about the sequencing methods, protocols, and machines
    
- Runs: Samples, experiments, and files are linked through runs - appropriate objects for FASTQ and BAM/CRAM submissions

- Analysis: References the analysis (BAM) files; associated with samples and study

- DAC: contains information about the Data Access Committee (DAC)

- Policy: contains the Data Access Agreement (DAA); associated with DAC 

- Dataset: contains the collection of runs/analysis data files to be subject to controlled access; associated with Policy.
    
    
After data release, each of these objects will be assigned with a permanent identifier or unique accession number.


Note:

- Study, samples, DAC, and Policy metadata can all be registered before uploading files, while run and analysis objects cannot be registered **until at least 24 hours** after the files have been uploaded to the Finnish node.

- If you are performing **Array-based submission(s)**, the Submitter Portal should only be used to register the Study, Samples, Data Access Committee (DAC), and Policy metadata objects. In contrast, the other metadata objects need to be registered using an [excel template](https://ega-archive.org/submission/array_based/metadata).




## Data release

To finalize your submission, write to servicedesk@csc.fi (subject: Federated EGA) to confirm that the submission can be released and add the following information (from the submitter portal):

- **Name of the submission** (as on the submitter portal);

- **Dataset Accession number (EGAD)**;

- appropriate **Data Use Ontology codes (DUO)** : more info in [Data Use Conditions](https://ega-archive.org/data-use-conditions) (EGA webpage). 

CSC help-desk and Central EGA help-desk will work together to complete the release process.





## Data Access 



### Data Access for applicants overview


1. To access a specific dataset hosted in the Finnish Federated EGA Node, go to the [EGA webpage](https://ega-archive.org/studies) and *search* for a particular study, dataset, or DAC. Then, in the *Study view*, click on the *Dataset ID (EGADNNNN)*. In the Dataset view, under **Who controls access to this dataset**, you can click on the link that will allow you to access the application form using SD Apply, one of the CSC services for sensitive data.

2. In the **application form** you can accept the Data Access Agreement, specify the purpose of your request and add your research plan. The Data Access Committee will evaluate your application, accepting or denying data access.

3. Once the application is approved, you will receive a confirmation email. Briefly, you can access the data logging into [ SD Desktop](https://anvil-test.sd.csc.fi/guacamole/#/), a private workspace part of CSC Sensitive Data Services.  

4. Log in to SD Desktop is possible using CSC login, HAKA or ELIXIR login. Next, enter the authentication code received via the mobile app.


5. Once you have accessed the computing environment, you can open the terminal (right-click) and input the following command:

 "`go-fuse -enable SD-Submit ```
 
 Note: as SD Desktop complies with high-security measures, it is not possible to use the copy-paste function.
 
 
6. Next, open the **Project folder** that will appear on the Desktop. Open the SD Connect folder: the dataset will be available in the subfolder called Project NNNN.






Step1:

EGA webpage

![final EGA page](https://user-images.githubusercontent.com/83574067/149823106-67a1cfe0-a639-45c4-9875-b5391a933853.png)

Step2:

Application form

![SD Apply applicant view](https://user-images.githubusercontent.com/83574067/149817377-4d223858-3b3d-4e51-b978-92eaf5a562b3.jpg)

Step 4:

Login and authentication
![MFA FEGA demo](https://user-images.githubusercontent.com/83574067/149823080-723ad1b1-8523-4262-abc6-e228a55325b3.png)

Step 6:

Project access
![SD SUbmit fuse](https://user-images.githubusercontent.com/83574067/149823223-957d5bcf-95a4-49c0-8b22-30f485ef67e4.png)









