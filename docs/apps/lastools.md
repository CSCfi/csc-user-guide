# LAStools

[LAStools](https://rapidlasso.com/lastools) is a collection of tools for LiDAR data processing. 

## Usage

### Using LAStools

LAStools is included in the [geoconda](../apps/geoconda.md) and [lidarconda](../apps/lidarconda.md) modules and can be loaded with

`module load geoconda` (or lidarconda)

You can test LAStools loaded successfully with

`lasinfo -h`

### LAStools commands

Puhti installation includes only the open source tools of LAStools

* laszip - compresses the LAS files in a completely lossless manner
* lasinfo - prints out a quick overview of the contents of a LAS file
* lasindex - creates a spatial index LAX file for fast spatial queries
* las2las - extracts last returns, clips, subsamples, translates, etc ...
* lasmerge - merges several LAS or LAZ files into a single LAS or LAZ file
* txt2las - converts LIDAR data from ASCII text to binary LAS format
* las2txt - turns LAS into human-readable and easy-to-parse ASCII
* lasprecision - analyses the actual precision of the LIDAR points

!!! note
    For now, Puhti does not support running __.exe__ files so if you need to install/run the closed source tools, use the Taito cluster. [Taito & LAStools documentation](https://research.csc.fi/-/lastools)


## License and citing

For information on the legal use and licensing of LAStools, please read the [LAStools LICENSE](http://lastools.org/LICENSE.txt).

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [LAStools homepage](https://rapidlasso.com/lastools/)
* [LAStools Github](https://github.com/LAStools/LAStools)
* [LAStools examples and tutorials](https://rapidlasso.com/category/tutorials/)
