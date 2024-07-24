# Using Allas to host a data set for a research project #

An example scenario of an Allas use case.

### Roles of the play ###

**Saara**:   A professor coordinating an inspiring research project.

**Pekka**:  A researcher that takes care of the data management of the project.

**Mats**:    A technician working at Analysis Service Center.

**Xi and Laura**:   Researchers working in the research project. 
 

## Act 1. Professor Saara opens CSC projects ##

Professor Saara is running a large research project called _HiaNo_ in a Finnish university. 
The project has just sent a set of samples to Analysis Service Center to be processed and analyzed. 
The analysis takes some weeks and produces 80 TB of data that the research group will use in the actual research.

Saara and Pekka, who is taking care of the data management, study the [storage options provided by CSC](https://research.csc.fi/data-management). They decide to use the Allas service for storing and sharing the data during the research project. The data is not sensitive personal data, so Allas is suitable.

As a first step, Saara and Pekka login to the [MyCSC portal](https://my.csc.fi) and [register as CSC users](../../accounts/how-to-create-new-user-account.md).

Then Saara [creates two research projects](../../accounts/how-to-create-new-project.md) at CSC: one called _Data management of the HiaNo project_ (project ID: project_2000444) and another called _HiaNo research project_ (project ID: project_2000333).

Once the CSC projects are established, Saara [activates the Allas, Puhti and cPouta services](../../accounts/how-to-add-service-access-for-project.md) for both projects. As Saara knows that the default storage space of Allas (10 TB) will not be enough for the incoming data set, she sends a request for 90 TB of Allas quota for the project _Data management of the HiaNo project_ to servicedesk@csc.fi.

Finally, Saara [adds Pekka to both CSC projects](../../accounts/how-to-add-members-to-project.md) and asks him to take care of the details of the incoming data.  

## Act 2. Creating a shared bucket ##

Mats from Analysis Service Center contacts Pekka and tells that the results are available, and asks how he should deliver the data. Mats has an account at CSC (_msundber_ in the project _project_2000111_) with Allas enabled, so Pekka proposes that data be uploaded to Allas. For that purpose, Pekka creates a bucket in Allas and allows Mats to use it.

Pekka logs in to Puhti
```text
ssh puhti.csc.fi   
```
and opens a connection to the data management project in Allas:
```text
module load allas
allas-conf project_2000444
```
Then he creates a new bucket in Allas. There are many ways to do this but this time, Pekka does this by importing a new file to Allas with _a-put_:
```text
echo “This bucket is used to host the original data of HiaNo project sample1” > README.txt
a-put -b hiano-project-sample001 README.txt
a-list hiano-project-sample001 
```
Pekka included the project name in the bucket name (_hiano-project-sample001_) to make sure that the bucket name is unique in the whole Allas service. The _a-list_ command shows that the bucket was successfully created.

Next Pekka uses the _a-access_ command to [modify the access rights of the new bucket](./using_allas/swift_client.md#giving-another-project-read-and-write-access-to-a-bucket) so that Mats (user _msundber_ from Allas _project_2000111_) is able so use it.
```text
a-access +rw project_2000111 hiano-project-sample001
```
Pekka still needs to send the name of the shared bucket to Mats, as normal Allas listing commands do not display the name for Mats who is not a member in the project that owns the bucket.

## Act 3. Uploading data

Mats has [Allas tools](https://github.com/CSCfi/allas-cli-utils) installed in the front-end server of the measurement device at Analysis Service Center. Thus he can upload the data directly from the front-end server to the _hiano-project-sample1_ bucket in Allas:
```text
rclone copy sample1/cannel43/aa_3278830.dat  allas:hiano-project-sample001/sample1/cannel43/aa_3278830.dat
```
As there is a large amount of data to be transported, the upload takes few days and needs to be done in several batches. When Mats tells that he is ready with the data uploads, Pekka closes the shared bucket:
```text
a-access -rw project_2000111 hiano-project-sample001
```

## Act 4. Using the data in research ##

Once the data is available, the actual analysis work begins. There will be several users using the data set during the research project. Pekka knows that if all users use the data with full access rights (read and write), there is a danger that somebody accidentally deletes or overwrites some part of the data. Thus, it is agreed that while the data is hosted by the data management project (project_2000444), the researchers access the data through the _HiaNo research project_ (project_2000333).

Pekka gives read access to the _hiano-project-sample001_ bucket for the project _project_2000333_ but no write access.
```text
module load allas
allas-conf project_2000444
a-access +r project_2000333 hiano-project-sample001
```
Xi and Laura can now start working with the data. They register using the MyCSC portal, after which Saara, who is the Principal Investigator, adds them to the CSC project _HiaNo research project_ (project_2000333).

Xi and Laura need to revisit MyCSC and accept the services of the research project. After that, they can download the research data they need to any environment that is able to connect to Allas: Puhti, a virtual machine in cPouta, or their own laptop. As new researchers join the project, Saara adds them in project_2000333, so that they can access the data.

Because storing data in Allas consumes billing units, Saara needs to check the saldo in MyCSC from time to time, and if needed, [apply for more billing units](../../accounts/how-to-apply-for-billing-units.md) (80 TB consumes 700 800 Bu in year). Fortunately, HiaNo is an academic research project, so Saara does not need to pay for the billing units.

Allas storage is only for research project's duration, but Saara thinks it would be beneficial to have the preliminary data made publicly available and easier to be found. This is supported by the [Fairdata Services](https://www.fairdata.fi/en/) produced by CSC.

Pekka creates a new bucket with public access and uploads the data to the bucket. Command _a-publish_ creates the bucket and uploads the selected files into it. Parameter `-b` is used to define the name for the bucket, in this case `hiano-project-public001`.
```text
a-publish -b hiano-project-public001 zz_364872.dat zz_242165.dat
```
Next, Pekka creates a basic description of the data using the [Fairdata Qvain Tool](https://www.fairdata.fi/en/qvain/) and provides the two URLs (one for each file in Allas) as a Remote Resource in Qvain. After this, the data can be published as a dataset with a landing page and a persistent identifier. This way the preliminary data can be shared among colleagues using the persistent identifier. The dataset can also be explored via [Fairdata Etsin Service](https://www.fairdata.fi/en/etsin/) with structured information and direct access to download the files in Allas.


## Act 5. The end ##

After four years of intensive research that has expanded to several institutes in Finland and abroad, the HiaNo project has produced a few theses and many high quality publications (all acknowledging the use of CSC resources).  

The data is no longer actively used presently. A part of the data that was imported to Allas has been published in international research databases. Some datasets have been moved to [IDA](https://ida.fairdata.fi), so that a DOI identifier and metadata can be linked to the data to make it reusable by other researchers. These datasets can also be explored via [Fairdata Etsin](https://www.fairdata.fi/en/etsin/). Some data can now be deleted and some remaining parts be moved to the buckets of the new _HiaNo2_ project.

At this stage, Pekka cleans the remaining data objects from Allas, after which Saara informs CSC that the project can be closed.
