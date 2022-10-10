---
tags:
  - Free
---

# PCL

[PCL](https://pointclouds.org/) (Point Cloud Library) is a standalone, large scale, open project for 2D/3D image and point cloud processing.

[PCLpy](https://github.com/davidcaron/pclpy) adds Python bindings to PCL.

## Available

__PCL__ is available in Puhti with following versions:

* 1.12.1 without PCLpy
* 1.9.1 with PCLpy version 0.12.0 with Python 3.8.

 
All included Python packages can be seen by using the command `list-packages`.

## Usage

PCL is included in the __pcl__ module and can be loaded with

`module load pcl`

You can see all available binaries with the command depending on the version:

```
ls /appl/soft/geo/pcl/1.12.1/bin
``` 
or 
```
ls /appl/soft/geo/pcl/1.9.1/bin
```

Note, that PCL/1.9.1 includes less PCL modules.

## License and acknowledgement

PCL is released under the terms of the BSD license, and thus free for commercial and research use.

[PCL citation](https://pointclouds.org/about/)

Please acknowdlege CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

### References

* [PCL homepage](https://pointclouds.org/)
* [PCL Documentation and tutorials](https://pcl.readthedocs.io)


