## 4.4.6 Accessing the object storage from Taito

  
The usage will strongly depend on what  you will do with the data. The
"swift", "s3" and "s3cmd" command  line tools are already installed on
Taito.

<table> <colgroup> <col style="width:  50%" /> <col style="width: 50%"
/>  </colgroup>  <tbody>  <tr  class="odd">  <td><strong>Command  line
tool</strong></td>  <td><strong>Requirements</strong></td>  </tr>  <tr
class="even">  <td>swift</td>  <td>Computing  project  openrc.sh  file
downloaded                           from                           <a
href="https://pouta.csc.fi">https://pouta.csc.fi</a> &amp;  sourced to
shell.</td>  </tr>   <tr  class="odd">   <td>s3</td>  <td><p>Following
environment    variables    present     in    environment:</p>    <ul>
<li>S3_ACCESS_KEY_ID</li>                <li>S3_SECRET_ACCESS_KEY</li>
<li>S3_HOSTNAME</li>        </ul>        <p>More        info        <a
href="https://research.csc.fi/pouta-using-object-storage#s3-client">here</a>.</p></td>
</tr> <tr  class="even"> <td>s3cmd</td> <td>Configuration  file .s3cfg
populated                 (more                info                 <a
href="https://research.csc.fi/pouta-using-object-storage">here</a>).</td>
</tr> </tbody> </table>

  
You can  use any  of the  commands to stage  in the  data you  need to
process  to the  project/scratch disk  and process  the data  like you
would process
any other data.  
  
For S3 use cases, you can also store the ec2 credentials with the job.
This is the  recommended way of accessing objects from  a compute job.
When you don't need the credentials anymore you can delete them with:

    $ openstack credential delete

Please note that ec2 credentials do not work against other Openstack
services.  
  
There is also the possibility to  create temp URLs for the objects you
need to  access, and use  those URLs to  access the data  from compute
jobs from Taito. One benefit of using temp URLs is that no credentials
need
to be stored in Taito for retrieving the object.  
 

|                    | | | | |
|--------------------|-----|----------------|-----|----------------|
| [Previous chapter] |     | [One level up] |     | [Next chapter] |

  [Previous chapter]: https://research.csc.fi/pouta-using-object-storage
  [One level up]: https://research.csc.fi/pouta-object-storage
  [Next chapter]: https://research.csc.fi/pouta-object-storage-common-error-messages
