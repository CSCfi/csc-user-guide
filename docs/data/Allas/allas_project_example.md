# Using Allas to host a data set for a research group #


### Roles of the play ###

**Saara**:   A professor coordinating an inspiring research project.

**Pekka**:  Researcher that takes care of the data management of the project.

**Mats**:    Technician working in Analysis Service Center.

**Xi and Laura**:   Researchers working in the research project. 
 

## Act 1. Professor Saara opens CSC projects. ##

Professor Saara is running a large research project called HiaNo in a Finnish university. 
The project has just send a set of samples to the Analysis Service Center to be processed and analyzed. 
The analysis takes some weeks and produce 80 Tb of data that the research group will use for the actual research.

To store and make this data available for the research project Saara and Pekka, who is taking care of the data management, decide to use the Allas service of CSC. Data is not sensitive human data so using Allas in OK. 
As a first step Saara and Pekka login to [MyCSC portal](https://my.csc.fi) and [register themselves as CSC users](../../accounts/how-to-create-new-user-account.md).

Then Saara [creates two research projects](../../accounts/how-to-create-new-project.md) at CSC. One called _Data management of HiaNo project_ that gets project ID: project_2000444  another called _HiaNo research project_ that gets project DI: project_2000333.

Once the CSC projects are established, Saara [activates Allas, Puhti and cPouta services](../../accounts/how-to-add-service-access-for-project.md) for both projects. As Saara knows that the default storage space of Allas (10 Tb) will not be enough for the coming data set, she sends a request for 90 TB Allas quota for the project “Data management of HiaNo project” to servicedesk@csc.fi.

Finally, Saara [adds Pekka to both CSC projects](../../how-to-add-member-to-project.md)
, and asks him to take care of the details of the coming data.  

## Act 2. Data arrives ##

Mats from the Analysis Service Center contacts Pekka and tells that the results are now available and asks how he should deliver the data. Mats has an account at CSC ( _msundber_ in project _project_2000111_) with Allas enabled, so Pekka proposes that data is uploaded to Allas. For that purpose Pekka creates a bucket to Allas and sets is so, that Mats is able to use it.

To do this Pekka logs in to Puhti 
```text
ssh puhti.csc.fi   
```
and open connection to the data management project in Allas:
```text
module load allas
allas-conf 2000444
```
Then he creates a new bucket in Allas. There is many ways to do this, but this time, Pekka does this by importing a new file to Allas with _a-put_.

```text
echo “This bucket is used to host the original data of HiaNo project sample1” > README.txt
a-put --nc -b hiano-project-sample1 README.txt
a-list hiano-project-sample1 
```
Pekka included the project name in the bucket name (_hiano-project-sample1_) to make sure that the bucket name is unique through the whole Allas service. _a-list_ command shows that the bucket was successfully created.

Next Pekka uses _swift post_ command to [modify the access rights of the new bucket](./using_allas/swift_client.md#giving-another-project-read-and-write-access-to-a-bucket) so that Mats (user _msundber_ from Allas _project_2000111_) is able so use it .
```text
swift post hiano-project-sample1 -r "project_2000111:msundber"
swift post hiano-project-sample1 -w "project_2000111:msundber"
swift stat hiano-project-sample1
```
Then Pekka needs to send the name of the bucket to Mats as normal Allas listing commands don’t show the name for Mats who is not member in the project that owns the bucket.

Mats has [Allas tools](https://github.com/CSCfi/allas-cli-utils) installed in the front end server of the measurement device in Analysis Service Center. Thus he can upload the data directly from the front end server to the _hiano-project-sample1_ bucket in Allas. For example:
```text
rclone copy sample1/cannel43/aa_3278830.dat  allas:hiano-project-sample1/sample1/cannel43/aa_3278830.dat
```
As there is a large amount of data to be transported the upload takes few days and it needs to be done as several batches. When Mats tells that he is ready with the data uploads, Pekka closes the shared bucket with commands
```text
swift post hiano-project-sample1 -r ""
swift post hiano-project-sample1 -w ""
swift stat hiano-project-sample1
```

## Act 3. Using data for research ##

Once the data is available the actual analysis work starts. There will be several users using the data set during the research project. Pekka knows that if all the users would use the data with full access rights (read and write) there is a danger that somebody accidentally deletes of overwrites the some part of the data. Because of that it is agreed that while the data is hosted by the data management project (project_2000444), the researchers access the data through the _HiaNo research project _ (project_2000333).

To enable that Pekka gives read access to the _hiano-project-sample1_ bucket for project _project_2000333_, but not write access.
```text
module load allas
allas-conf 2000444
swift post hiano-project-sample1 -r "project_2000333:*"
```
Xi and Laura can now start working with the data. They register themselves to CSC  using the MyCSC portal, after which Saara, who is the Principal Investigator, adds them only to CSC project “HiaNo research project ” (project_2000333).

Xi and Laura need to re-visist MyCSC again and accept the services if the research project. After that thy can download that  research data they need to any machine that is able to connect allas: Puhti, a vitual machine in cPouta or their own laptop. As new researchers come along to the project Saara adds them to project_2000333 so that they can access the data.

