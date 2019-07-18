----------------------

## Web client - OpenStack Horizon Dashboard

This section includes instructions for using the user friendly **OpenStack Horizon Dashboard**.

The OpenStack documentation on managing buckets over the web interface can be found here:

[https://docs.openstack.org/horizon/latest/user/manage-containers.html](https://docs.openstack.org/horizon/latest/user/manage-containers.html){:target="_blank"}

The OpenStack dashboard has a small subset of the Object Storage functionalities. The available operations are:

* _Create_ a new bucket
* _Upload_ an object to a bucket
* _View_ objects and buckets
* _Download_ an object
* _Remove_ objects and buckets
* And in addition, you can make buckets _public_ or _private_

&nbsp;


### Creating a bucket

1\. Go to [pouta.csc.fi](https://pouta.csc.fi/){:target="_blank"} and login

2\. Choose **Project** on the left bar menu

3\. Navigate to **Object Store** on the left bar menu, expand it and choose **Containers** (Container equals to a bucket)  

!["Creating a container"](/img/allas_screenshot_create_container.png)  
**Figure** Creating a container

4\. Press the **+Container** button and name the bucket (Do not use Scandinavian letters in the name). If you choose to make the bucket _Public_, the content of the bucket can be [viewed via Internet](#viewing-objects-via-internet).
 
&nbsp;


### Adding an object to a bucket

1\. Choose the desired bucket and press the **upload symbol** on the right

!["Upload object"](/img/Allas_screenshot_upload.png)  
**Figure** Uploading an object

2\. Choose the object from your computer and name it (Do not use Scandinavian letters in the name)  

3\. Upload the object and it will appear to the container. You can also create folders for the objects with the **+Folder** button next to the upload symbol, for example, in need to organize objects into folders
 
&nbsp;

<a name="web_public"></a>

### Viewing objects via Internet

If the bucket including the objects is set to be _public_, the objects can be viewed via Internet by anyone who knows the URL. This setting can be changed from [pouta.csc.fi/dashboard/project/containers](https://pouta.csc.fi/dashboard/project/containers/){:target="_blank"} by choosing the container and selecting the **Public Access** setting:

!["Making object public or private"](/img/Allas_screenshot_public.png)

**Figure** Making an object public or private

A public object named _my_fish_ belonging to a container named _my_fishbucket_ can be viewed from an URL: _object.pouta.csc.fi/my_fishbucket/my_fish_

&nbsp;


### Downloading an object

Downloading an object happens from the **Download** button on the right side of the object's name.

&nbsp;


### Removing objects and buckets

Objects can be removed by clicking the drop-down menu on the right next to the _Download_ button. There will be an option **Delete**.

Buckets can be removed only when they are empty. In other words, all the objects in a bucket must be removed or moved somewhere else before the bucket can be deleted. Removing a bucket happens from the **trashcan symbol** next to the buckets name. 

!["Removing object or container"](/img/Allas_screenshot_delete.png)

**Figure** Removing an object or a container

Alternatively, and especially if you want to remove several objects at once, you can choose the wanted objects by selecting the small boxes on the left side of the objects names and then choose the **trashcan symbol** on the red background on the upper right corner.
  