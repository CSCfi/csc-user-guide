---
tags:
  - Free
system:
  - www-puhti
---

# CloudCompare

[CloudCompare](http://cloudcompare.org/) is an open source tool for editing and processing dense 3D point clouds (such as those acquired with laser scanners).

The main purpose of CloudCompare on Puhti is to serve as a tool for visualizing point cloud data.

## Available

The following versions of CloudCompare are available in **Puhti**:

- CloudCompare 2.12.4 for GPU partitions. Plugins: qEDL, qPDALIO, qAnimation and qPCV.
- CloudCompare 2.10.3 for CPU partitions with more plugins than the GPU version.

GPU version is faster, but consumes also a lot more billing units. Also queues to GPU partitions may be longer.

## Usage
Both versions of CloudCompare are available in [Puhti web interface](https://puhti.csc.fi).

### GPU-accelerated CloudCompare
GPU-accelerated CloudCompare is available with [Accelerated visualization app](../computing/webinterface/accelerated-visualization.md)
   
### Basic CloudCompare
Basic CloudCompare is available via [Desktop app](../computing/webinterface/desktop.md). After launching the remote desktop, double-click CloudCompare icon OR open `Terminal` (Desktop icon) and start CloudCompare:

```
module load cloudcompare
CloudCompare
```

## License 

CloudCompare is published under the [GNU General Public License](https://github.com/CloudCompare/CloudCompare/blob/master/license.txt).

You are free to use CloudCompare for any purpose, including commercially or for education. 


## Citation


`CloudCompare (version 2.10.3) [GPL software]. (2021). Retrieved from http://www.cloudcompare.org.`

If you used a [CloudCompare plugin](http://www.cloudcompare.org/doc/wiki/index.php?title=Plugins), also cite the plugin authors.

## Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports. As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

## Installation

CloudCompare was installed to Puhti with Apptainer. The basic version was installed using this [CloudCompare Apptainer definition file](https://github.com/CSCfi/singularity-recipes/blob/main/cloudcompare/cloudcompare.def).

## References

* [CloudCompare homepage](http://cloudcompare.org/)
* [CloudCompare on github](https://github.com/cloudcompare/cloudcompare)
* [CloudCompare forum](http://cloudcompare.org/forum/)

