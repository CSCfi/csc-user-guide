
# Web client - OpenStack Horizon Dashboard

This chapter includes instructions for using Allas with the user-friendly _OpenStack Horizon Dashboard_. The OpenStack documentation on managing buckets over the web interface can be found from: [https://docs.openstack.org/horizon/latest/user/manage-containers.html](https://docs.openstack.org/horizon/latest/user/manage-containers.html)

The OpenStack dashboard has a small subset of object storage functionalities. The available operations are:

| Function |
| :--- |
| _Create_ a new bucket |
| _Upload_ an object |
| _View_ objects and buckets |
| _Download_ an object |
| _Remove_ objects and buckets |
| Make buckets _public_ or _private_ |

&nbsp;


## Create a bucket

1\. Go to [pouta.csc.fi](https://pouta.csc.fi/) and login

2\. On the left bar menu, navigate to **Project | Object Store | Containers**  
(Container equals to a bucket)  

!["Creating a container"](img/allas_screenshot_create_container.png)  
**Figure** Creating a container

3\. Press the **+Container** button and name the bucket (see [Checklist for naming a bucket](../introduction.md#naming-buckets)). If you choose to make the bucket *Public*, the content of the bucket can be [viewed via Internet](#view-objects-via-internet).
 
&nbsp;


## Upload an object

1\. Choose the desired bucket and press the **upload symbol** on the right

!["Upload object"](img/Allas_screenshot_upload.png)  
**Figure** Uploading an object

2\. Choose the object from your computer and name it. **Note:** Do <u>not</u> use Scandinavian letters (&auml;, &ouml;, etc.) in the name  

3\. Upload the object and it will appear to your container. You can also create pseudofolders for the objects with the **+Folder** button next to the upload symbol, for example, in need to organize objects into folders.
 
&nbsp;


## View objects via Internet

If the bucket including the objects is set to be _public_, the objects can be viewed via Internet by anyone who knows the URL. This setting can be changed from [pouta.csc.fi/dashboard/project/containers](https://pouta.csc.fi/dashboard/project/containers/) by choosing the container and selecting the **Public Access** setting:

!["Making object public or private"](img/Allas_screenshot_public.png)

**Figure** Making an object public or private

A public object called _my_fish_ belonging to a container called _my_fishbucket_ can be viewed from an URL: _object.pouta.csc.fi/my_fishbucket/my_fish_

&nbsp;


## Download an object

Downloading an object can be done from the **Download** button on the right side of the object's name.

&nbsp;


## Remove objects and buckets

Objects can be removed by expanding the drop-down menu on the right next to the _Download_ button. There will be an option **Delete**.

Buckets can be removed only when they are empty. Hence all the objects in a bucket must be removed or moved somewhere else before the bucket can be deleted. Removing a bucket can be done from the **trashcan symbol** next to the buckets name. 

!["Removing object or container"](img/Allas_screenshot_delete.png)

**Figure** Removing an object or a bucket

Alternatively, and especially if you want to remove several objects at once, you can choose the wanted objects by selecting the small boxes on the left side of the objects names and then choose the **trashcan symbol** on the red background on the upper right corner.
  
