# WhiteboxTools

[WhiteboxTools](https://jblindsay.github.io/ghrg/WhiteboxTools/index.html) is an advanced geospatial data analysis platform which includes more than 420 tools. 

## Available

WhiteboxTools is available in Puhti with following versions:

* 0.15.0

## Usage

WhiteboxTools is available in the __WhiteboxTools__ module and can be loaded with

`module load whiteboxtools`

WhiteboxTools usage in Puhti happens through a container system called [Singularity](https://sylabs.io/docs/) which is very similar as Docker. CSC provides a [__singularity_wrapper__](../computing/containers/run-existing.md) command that makes running these containers simpler for the user. 

After loading the WhiteboxTools module you can run normal WhiteboxTools commands on the computing nodes with the following way:

```
srun singularity_wrapper exec <whiteboxtools command>
```

!!! note
    For now, the Graphical user interface (Whitebox GAT) and the Python interface are not available on Puhti

Here is an example of calculating Hillshade for a 2m DEM. 

```
singularity_wrapper exec whitebox_tools -r=Hillshade -v --wd="<INPUT-DATA-FOLDER>" -i=T4323D.tif -o=test_hillshade.tif --azimuth=315.0 --altitude=30.0
```

!!! note
    The --wd (working directory) parameter requires quotation marks __" "__ around the path

## Example batch job script

```
#!/bin/bash
#SBATCH --account=<YOUR-PROJECT>
#SBATCH --cpus-per-task=1
#SBATCH --partition=small
#SBATCH --time=00:10:00
#SBATCH --mem=2G

module load whiteboxtools
singularity_wrapper exec whitebox_tools -r=Hillshade -v --wd="<INPUT-DATA-FOLDER>" -i=T4323D.tif -o=test_hillshade.tif --azimuth=315.0 --altitude=30.0
```

## License and acknowledgement

The WhiteboxTools project has been developed using a permissive MIT license, which allows for the tools to be readily incorporated into other GIS software. [Full license here](https://github.com/jblindsay/whitebox-tools/blob/master/LICENSE.txt)

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

### References

* [WhiteboxTools homepage](https://jblindsay.github.io/ghrg/WhiteboxTools/index.html)
* [WhiteboxTools Github](https://github.com/jblindsay/whitebox-tools)
* [WhiteboxTools User Manual](https://jblindsay.github.io/wbt_book/intro.html)
* [Singularity containers in CSC](../computing/containers/run-existing.md)



