---
tags:
  - Free
catalog:
  name: CloudCompare
  description: for visualizing, editing and processing point clouds
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - web_interfaces:
        - Puhti
        - Roihu
    - Puhti
    - Roihu
---

# CloudCompare

[CloudCompare](http://cloudcompare.org/) is an open source tool for editing and processing dense 3D point clouds (such as those acquired with laser scanners).

The main purpose of CloudCompare on Puhti is to serve as a tool for visualizing point cloud data.

## Available

The following versions of CloudCompare are available:


- CloudCompare 2.14 for CPU. Plugins: Core I/O, LAS I/O **In Roihu**. 
- CloudCompare 2.13.1 for GPU **In Roihu**. 
- CloudCompare 2.12.4 for GPU. Plugins: qEDL, qPDALIO, qAnimation and qPCV. **In Puhti**.
- CloudCompare 2.10.3 for CPU with more plugins than the GPU version. **In Puhti**.

GPU version is faster, but consumes GPU Billing Units instead of CPU Billing Units (see [Billing](../computing/hpc-billing.md) for details). Also queues to GPU partitions may be longer.

## Usage
CloudCompare is available in web interface: [Puhti](https://puhti.csc.fi) or [Roihu](https://roihu.csc.fi).

* **Basic CloudCompare is available** via [Desktop app](../computing/webinterface/desktop.md). 
* **GPU-accelerated CloudCompare** via [Accelerated visualization app](../computing/webinterface/accelerated-visualization.md)

After launching the remote desktop, start CloudCompare or ccViewer from `Applications` (upper left corner) -> `Geosciences`.

Alternatively, open terminal from `Applications` -> `Terminal emulator`:

```
module load cloudcompare
CloudCompare
```

## License 

CloudCompare is published under the [GNU General Public License](https://github.com/CloudCompare/CloudCompare/blob/master/license.txt).


## Citation

`CloudCompare (version 2.X.Y) [GPL software]. (2026). Retrieved from http://www.cloudcompare.org.`

If you used a [CloudCompare plugin](http://www.cloudcompare.org/doc/wiki/index.php?title=Plugins), also cite the plugin authors.

## Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports. As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

## Installation

CloudCompare was installed to Puhti with Apptainer. The CPU-versions were installed using [Apptainer](https://github.com/CSCfi/singularity-recipes/tree/main/cloudcompare) and wrapped with Tykky

```
wrap-container -w /usr/bin/CloudCompare,/usr/bin/ccViewer cc.sif --prefix 2.14
```

## References

* [CloudCompare homepage](http://cloudcompare.org/)
* [CloudCompare on github](https://github.com/cloudcompare/cloudcompare)
* [CloudCompare forum](http://cloudcompare.org/forum/)

