---
tags:
  - Free
---

# Seismic Unix

[Seismic Unix](https://wiki.seismic-unix.org/start) is a seismic processing package. It aims first at delivering a robust and efficient seismic reflection software package, dedicated to education, and to permit the processing of moderate size 2D seismic or GPR data sets.


## Available

__Seismic Unix__ is available in Puhti with following versions:

* 44R28


## Usage

Seismic Unix is available in the __seismic-unix__ module:

```
module load seismic-unix
<commands>
```
Seismic Unix can be used in Puhti with command-line or graphical interface, as interactive job or with batch system. In any case reserve suitable amount of computing resources: cores and memory. 

### Seismic Unix with Graphical User Interface

Seismic Unix Graphical User Interface (GUI) can be started in Puhti web interface:

1. Log in to [Puhti web interface](https://puhti.csc.fi).
2. Open [Desktop app](../computing/webinterface/desktop.md)
3. After launching the Desktop, open Terminal

```
module load seismic-unix
cd /scratch/project_200xxxx/<location_of_your_data>
<commands>
```

### Working with Seismic Unix interactively
For relatively short analysis jobs, it is possible to use Seismic Unix in [interactive session](../computing/running/interactive-usage.md).

```
sinteractive -i
cd /scratch/project_200xxxx/<location_of_your_data>
module load seismic-unix
<commands>
```

### Using Seismic Unix with batch job
For longer analysis jobs, Puhti batch system should be used.

```
#!/bin/bash
#SBATCH --account=project_200xxxx
#SBATCH --cpus-per-task=1
#SBATCH --partition=small
#SBATCH --time=00:15:00
#SBATCH --mem=4G

module load seismic-unix
cd /scratch/project_200xxxx/<location_of_your_data>
<commands>
```

## License 

Seismic Unix is distributed under following license:

```
Copyright ▒ 2008, Colorado School of Mines,
All rights reserved.


Redistribution and use in source and binary forms, with or
without modification, are permitted provided that the following
conditions are met:

    *  Redistributions of source code must retain the above copyright
       notice, this list of conditions and the following disclaimer.
    *  Redistributions in binary form must reproduce the above
       copyright notice, this list of conditions and the following
       disclaimer in the documentation and/or other materials provided
       with the distribution.
    *  Neither the name of the Colorado School of Mines nor the names of
       its contributors may be used to endorse or promote products
       derived from this software without specific prior written permission.

Warranty Disclaimer:
THIS SOFTWARE IS PROVIDED BY THE COLORADO SCHOOL OF MINES AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COLORADO SCHOOL OF MINES OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
```


## Citation

`Cohen, J. K. and Stockwell, Jr. J. W., (202x), CWP/SU: Seismic Un*x Release No. 44R28: an open source software  package for seismic research and processing, Center for Wave Phenomena, Colorado School of Mines.
`


## Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".


## Installation

Seismic Unix was installed to Puhti with Apptainer using commands listed in [Seismic Unix Apptainer definition file written by CSC](https://github.com/CSCfi/singularity-recipes/blob/main/seismic-unix/44R28.def). 
Because the `make install` asks a few questions, that need to be answered interactively, the container was first created in [sandbox mode](https://apptainer.org/docs/user/main/build_a_container.html#creating-writable-sandbox-directories) 
and then converted to normal Apptainer container.

The container was finally wrapped with [Tykky's wrap-container functionality](../computing/containers/tykky.md#container-based-installations): `wrap-container -w /usr/local/cwp/bin su.sif --prefix 44R28`

Additionally `common.sh` of Tykky created files was edited to add 2 required environment variables:
* Edit the end: `export SINGULARITYENV_DEFAULT_PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/cwp/bin/"`
* Add new row: `export SINGULARITYENV_CWPROOT="/usr/local/cwp"`
