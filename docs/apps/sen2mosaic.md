# Sen2mosaic

[Sen2mosaic](https://sen2mosaic.readthedocs.io/en/latest/) is a tool to download, preprocess and mosaic [Sentinel-2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2) data.

## Availability

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

For `s2m_preprocess` and `s2m_mosaic` you can use the argument `--n_processes` to set the number of available CPU cores to the number of CPU cores you applied for with your job.

## License and citation

Sen2mosaic is published under the [GNU,GPL v3](https://github.com/smfm-project/sen2mosaic/blob/master/LICENSE.md) license.

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [Sen2mosaic user manual](https://sen2mosaic.readthedocs.io/en/latest/)
* [Sen2mosaic github](https://github.com/smfm-project/sen2mosaic)
