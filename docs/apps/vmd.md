# VMD

VMD (Visual Molecular Dynamics) is a molecular visualization program for displaying, animating, and analyzing large biomolecular systems using 3-D graphics and built-in scripting.

## Available

-   Puhti: 1.9.3
-   Mahti-rhel7: 1.9.3

## License

-  The use of the software is restricted to non-commercial research. [Detailed license description.](https://www.ks.uiuc.edu/Research/vmd/current/LICENSE.html)    

## Usage

Initialize with:

```bash
module load vmd/1.9.3 
```

Note, that you need remote graphics to work with VMD. Due to the heavy graphics required by VMD we recommend to use it through [NoMachine](nomachine.md).
Please don't run VMD on the Puhti login nodes, but e.g. via the [sinteractive](../computing/running/interactive-usage.md)
command on a compute node (one core will be available without queueing).

## References

 The authors request that all published work which utilizes VMD include the primary VMD citation at a minimum:

```
    Humphrey, W., Dalke, A. and Schulten, K., "VMD - Visual Molecular Dynamics", 
    J. Molec. Graphics, 1996, vol. 14, pp. 33-38. 
```

Consult ["How to cite VMD"](https://www.ks.uiuc.edu/Research/vmd/allversions/cite.html), for further details.

## More information
-   [VMD home page](http://www.ks.uiuc.edu/Research/vmd/)
-   [VMD Tutorials](http://www.ks.uiuc.edu/Research/vmd/current/docs.html#tutorials)
-   [VMD Manuals](http://www.ks.uiuc.edu/Research/vmd/current/docs.html)  

