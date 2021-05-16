# Gaussian

Gaussian is a versatile program package providing various capabilities for electronic structure modeling.

[TOC]

## Available
- Puhti: G16RevC.01 (two versions)

## License
CSC has acquired a full commercial license for Gaussian. Gaussian is available for use by all approved account holders, subject to some license restrictions.To be able to use Gaussian at CSC your user-id has to be added to Gaussian users group. Send a request to CSC Service Desk, servicedesk@csc.fi .

## Usage

Initialise the Gaussian environment:

```bash
module load gaussian/G16RevC.01
```
Standard jobs are then conveniently submitted by using the subg16 script:
```text
subg16 time jobname <billing project id>
``` 
(run the plain subg16 command for details)
For optimal performance of Gaussian jobs on CSC's servers it is beneficial to make some efficiency considerations.
Some hints on how to estimate memory and disk requirements can be found [here](http://gaussian.com/running/?tabid=3).

## References

* [How to cite Gaussian](http://gaussian.com/citation_b01/) in your publications.

## More information

* [Online Gaussian user reference](http://gaussian.com/man/)
* [Using Gabedit as GUI for Gaussian jobs on Puhti](https://docs.csc.fi/support/tutorials/gabedit_gaussian/)
* [Using GREASY for running multiple Gaussian jobs on Puhti](https://csc-training.github.io/csc-env-eff/hands-on/throughput/gaussian_greasy.html)


