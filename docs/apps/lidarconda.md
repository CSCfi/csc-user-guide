# Lidarconda

Lidarconda is a collection of LiDAR data related Python packages and stand-alone tools

## Available

The `lidarconda` module is available in Puhti:

* 3.7 (version number is the same as Python version)

### Installed libraries

* pdal (2.0.1)
* lastools (20171231) - stand-alone tool
* laspy (1.6.0)
* laxpy (0.1.9)
* laszip (3.4.1)
* gdal (3.0.1)
* pandas (0.25.1)
* rasterio (1.0.28)
* scikit-learn (0.21.3)
* + additional minor libraries

If you think that some important GIS packages are missing from here, you can ask for installation from __servicedesk@csc.fi__

## Usage

### Using lidarconda

For using Python packages and other tools listed above, you can initialize them with

`module load lidarconda`

You can list all installed packages with

`list-packages`

### Adding more Python packages to Lidarconda

You can add more Python packages to Lidarconda for your own use with `pip`, for example

`pip install [newPythonPackageName] --user --target=/projappl/[yourProject]/python3.7/site-packages/`

If you do not give the installation folder as target, the packages are by default installed to your home directory under

`.local/lib/python3.7/site-packages`

## License and citing

All packages are licenced under various free and open source licences (FOSS), see the linked pages above for exact details.
In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [pdal](https://pdal.io/)
* [lastools](https://rapidlasso.com/lastools/)
* [laspy](https://pythonhosted.org/laspy/tut_part_1.html)
* [laxpy](https://github.com/brycefrank/laxpy)
* [laszip](https://laszip.org/)
* [gdal](https://gdal.org/)
* [pandas](https://pandas.pydata.org/)
* [rasterio](https://rasterio.readthedocs.io/en/stable)
* [scikit-learn](https://scikit-learn.org/stable/)