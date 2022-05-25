# CloudCompare

[CloudCompare](http://cloudcompare.org/) is an open source tool for editing and processing dense 3D point clouds (such as those acquired with laser scanners).

The main purpose of CloudCompare on Puhti is to serve as a tool for visualizing point cloud data.

## Availability

The following versions of CloudCompare are available in **Puhti**:

- Cloudcompare 2.10.3

## Usage

### Puhti web interface

The easiest option for using CloudCompare is to open it in [Puhti web interface as Desktop app](../computing/webinterface/desktop.md).

1. Log in to [Puhti web interface](https://puhti.csc.fi). 
2. Start CloudCompare: Apps -> Desktop, choose Desktop: 'single application' and App: 'CloudCompare'
3. CloudCompare is started automatically when the Desktop is launched. 


Alternatively, especially if you want to use CloudCompare together with some other Graphical User Interface (GUI) tool or want to use data from Allas, CloudCompare can be started in Puhti web interface with remote desktop:

1. Log in to [Puhti web interface](https://puhti.csc.fi).
2. Open Remote desktop: Apps -> Desktop, choose Desktop: `mate` or `xfce`. 
3. After launcing the remote desktop open `Host Terminal` (Desktop icon) and start CloudCompare:

```
module load cloudcompare
CloudCompare
```

## License 

CloudCompare is published under the [GNU General Public License](https://github.com/CloudCompare/CloudCompare/blob/master/license.txt).

You are free to use CloudCompare for any purpose, including commercially or for education. 



## Citation

```
CloudCompare (version 2.10.3) [GPL software]. (2021). Retrieved from <a href="http://www.cloudcompare.org/" aria-label="CloudCompare homepage">CloudCompare</a>
```

Also cite the plugin authors, if you used a [plugin](http://www.cloudcompare.org/doc/wiki/index.php?title=Plugins).

In your publications please acknowledge also Geoportti and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”


## References

* [CloudCompare homepage](http://cloudcompare.org/)
* [CloudCompare on github](https://github.com/cloudcompare/cloudcompare)
* [CloudCompare forum](http://cloudcompare.org/forum/)

