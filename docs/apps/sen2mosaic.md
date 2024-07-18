---
tags:
  - Free
---

# Sen2mosaic

[Sen2mosaic](https://sen2mosaic.readthedocs.io/en/latest/) is a tool to download, preprocess and mosaic [Sentinel-2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2) data.

## Available

__Sen2mosaic__ is available in Puhti with following versions:

* 0.2

## Dependencies

The __sen2mosaic__ module depends on [__geoconda/3.8.8__](./geoconda.md) and [__sen2cor/2.9__](./sen2cor.md) modules which are loaded automatically.

## Usage

Sen2mosaic is included in the __sen2mosaic__ module and can be loaded with

`module load sen2mosaic`

On Puhti, you run the tools with
```
s2m_download <arguments>
s2m_preprocess <arguments>
s2m_mosaic <arguments>
```

More information on the available arguments for each tool can be displayed with

`s2m_mosaic --help`

or from the [sen2mosaic user manual](https://sen2mosaic.readthedocs.io/en/latest/command_line.html). (Note the `_` in tool names on Puhti!)

For `s2m_preprocess` and `s2m_mosaic` you can use the argument `--n_processes` to set the number of available CPU cores to the number of computing cores of your job.

### Advanced usage

Further configuration of `s2m_preprocess` can be done via the `L2A_GIPP.xml` file (part of [Sen2cor](./sen2cor.md)). 
You can find the default GIPP file in `/appl/soft/geo/sen2cor/2.9/Sen2Cor-02.09.00-Linux64/lib/python2.7/site-packages/sen2cor/cfg/L2A_GIPP.xml`. 
Copy it to your `$HOME` directory, adjust it to your needs and add it to the call: `s2m_preprocess --gipp $HOME/L2A_GIPP.xml <other arguments>`

## License

Sen2mosaic is published under the [GNU,GPL v3](https://github.com/smfm-project/sen2mosaic/blob/master/LICENSE.md) license.


## Citation

Sen2mosaic does not provide any preferred citation information.

```Samuel Bowers: Sen2mosaic v.0.2. https://github.com/smfm-project/sen2mosaic , last accessed on {date}.```


## Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".


## Installation

Almost all dependencies for Sen2mosaic are available from the [sen2cor](./sen2cor.md) and [geoconda](./geoconda.md) modules, so Sen2mosaic was installed on top of them using `pip install --user opencv-python git+https://github.com/smfm-project/sen2mosaic.git`, while both modules were loaded (remember to set the installation directory first with `export PYTHONUSERBASE=/path/to/sen2mosaic/install/directory`. For shorter command line calls, the commands `s2m_download` ,`s2m_preprocess` and `s2m_mosaic` were created to shorten the original `python3 /path/to/sen2mosaic/cli/download.py` commands. This last step is not necessary for usability.  


## References

* [Sen2mosaic user manual](https://sen2mosaic.readthedocs.io/en/latest/)
* [Sen2mosaic github](https://github.com/smfm-project/sen2mosaic)
