# VisIt

VisIt is an open source, versatile software for scientific visualization. VisIt is available on Puhti and we recommend [the Puhti web interface remote desktop](../computing/webinterface/desktop.md) for running the GUI. [NoMachine](nomachine.md) can be used as a fallback option.

## License

VisIt is free also for commercial use and has been released under [BSD Open Source License](https://github.com/visit-dav/visit/blob/develop/LICENSE)

## Parallel use

VisIt can be run interactively in parallel configuration, using several processors. Login to Puhti and submit the following, to launch VisIt on compute node

```
module load visit/3.0.2
visit -l srun -np 2 -p test -t 00:10:00 -la --mem-per-cpu=2G -la --account=<your project>
```

The job reservation parameters are: -np *number of cores*, -p *queue*, -t *time* (hours:minutes:seconds), -la --mem-per-cpu *memory per processor* (in GB), -la --account *the billing project for the job*. Note that running VisIt with many processors does not necessarily bring speed benefits. It will depend on VisIt's particular data reader, if (and to what extent) the data can be distributed between the processors.


## Using host profile of local VisIt installation

VisIt client can be run on your local desktop computer while having VisIt components, that process the data remotely, on Puhti. Local VisIt host profiles can be used to launch jobs on Puhti compute nodes. Local and remote VisIt versions have to match.

An example of a working host profile is screen captured in links below. Note that job reservation parameters, that are not directly available as profile options, should be given as *Advanced/Launcher arguments*, see the last screen capture.

![Puhti screen capture 1](../img/host_profile_1.png)

![Puhti screen capture 2](../img/host_profile_2.png)

![Puhti screen capture 3](../img/host_profile_3.png)

![Puhti screen capture 4](../img/host_profile_4.png)


## More Information

*  [VisIt homepage (source code, binaries, manuals and tutorials, example data files)](https://wci.llnl.gov/simulation/computer-codes/visit/)
*  [User community web site](http://visitusers.org)
