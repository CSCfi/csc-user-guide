# Gaussian

Gaussian is a versatile program package providing various capabilities for electronic structure modeling.

[TOC]

## Available
- Puhti: G16RevC.01

## License
CSC has acquired a full commercial license for Gaussian. Gaussian is available for use by all approved account holders, subject to some license restrictions.To be able to use Gaussian at CSC your user-id has to be added to Gaussian users group. Send a request to CSC Service Desk , servicedesk@csc.fi .

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


