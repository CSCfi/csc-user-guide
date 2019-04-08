## Turbomole

### Description

TURBOMOLE is a program package for electronic structure calculations.
Methods include DFT, HF, MP2 and CC2. Properties both for ground and
excited states can be obtained. TURBOMOLE has been designed for
efficient study of large systems.

------------------------------------------------------------------------

### Available

##### Version on CSC's Servers

-   Puhti: 7.3

[New features and improvements for 7.3]

------------------------------------------------------------------------

### Usage

In order to set the interactive TURBOMOLE environment  issue the 
command:

`module load turbomole/7.3 `


For other ways of using it, see our [TmoleX pages]

**OpenBabel** supports the TURBOMOLE coord format.  The babel
environment is set by

`module load openbabel`

and  the program is called by 'babel'.  Do ' babel -H' for more
information.

**Parallel runs**

Most of the TURBOMOLE modules are parallelized either by MPI or SMP. MPI
versions can be run over several nodes whereas the SMP parallized rely
on a shared memory environment and hence must be executed within a
single node.** At present the modules aoforce, escf and egrad can only
be run parallel in SMP mode.** For more information, please read the
section ["Parallel Runs"] in the manual.

**Taito**

Sample job script  [job-tm73-taito.job] for running an MPI-parallel job
**Taito.**

Sample job script  [job-tm73-taito\_smp.job] for running an SMP-parallel
job **Taito.**  
  
Submit the job with:

`sbatch job-tm73-taito.job (job-tm73-taito_smp.job )`

For disk I/O intensive jobs it's recommended to use the local disks
on **Taito** for scratch. 

**Parallel NumForce runs**

To obtain numerical vibrational spectra efficiently with the NumForce
program, you can run the program in parallel. There is a slight
difference to normal parallel runs, however, as you want to start many
parallel *single*-CPU calculations. The following example scripts 
for  **Taito ** starts a parallel jobex calculation followed by a
parallel NumForce calculation:

-   jobex + NumForce job file [job-tm73-taitoNF.job]

------------------------------------------------------------------------

### Discipline

Chemistry  

------------------------------------------------------------------------

### References

Please quote the usage of the program package under consideration of the
version number:

<table>
<tbody>
<tr class="odd">
<td><hr /></td>
</tr>
<tr class="even">
<td>TURBOMOLE V7.3 2018, a development of University of Karlsruhe and</td>
</tr>
<tr class="odd">
<td>Forschungszentrum Karlsruhe GmbH, 1989-2007,</td>
</tr>
<tr class="even">
<td>TURBOMOLE GmbH, since 2007; available from</td>
</tr>
<tr class="odd">
<td><span class="ectt-1095">http://www.turbomole.com. </span></td>
</tr>
<tr class="even">
<td><hr /></td>
</tr>
<tr class="odd">
<td> </td>
</tr>
</tbody>
</table>

Scientific publications require proper citation of methods and
procedures employed. The output headers of TURBOMOLE modules include the
relevant papers. [See the on-line documentation for further
instructions.]

------------------------------------------------------------------------

### Support

------------------------------------------------------------------------

### Manual

The manual is available in different formats:

-   [PDF format]
-   [HTML format][See the on-line documentation for further
    instructions.]

#### More information

-   Additional information can be found at the [TURBOMOLE homepage]
-   [Manuals and Tutorials]

<!-- -->

-   **A tutorial** is available:
    -   [Tutorial (PDF)]
-   **Notes **from the course "[*Molecular electronic excitations with
    Turbomole*]"
    -   [PDF]

<!-- -->

-   **Notes** from the course "Introduction to TURBOMOLE" are also
    available: The notes also give an introduction in how to visualize
    results using [gOpenMol].
    -   [PDF][1]
    -   [Postscript].
-   [TURBOMOLE 5.8 ja uudet ominaisuudet] (PDF). From [@CSC, 1/2006].
-   **Users forum **is available for discussion:
    -   [TURBOMOLE Forum]

#### Licensing restrictions

-   You may use the Software exclusively for non-profit research
    purposes.
-   Only users from academic (i.e. degree-granting) institutes are
    allowed to use the Software

------------------------------------------------------------------------

  [New features and improvements for 7.3]: http://www.turbomole-gmbh.com/release-notes.html
  [TmoleX pages]: https://research.csc.fi/-/tmolex
  ["Parallel Runs"]: http://www.turbomole-gmbh.com/manuals/version_7_3/DOK/DOKse9.html#x16-220003.2
  [job-tm73-taito.job]: https://extras.csc.fi/chem/progs/turbomole/job-tm73-taito.job
  [job-tm73-taito\_smp.job]: https://extras.csc.fi/chem/progs/turbomole/job-tm73-taito_smp.job
  [job-tm73-taitoNF.job]: http://extras.csc.fi/chem/progs/turbomole/job-tm73-taitoNF.job
  [See the on-line documentation for further instructions.]: http://www.turbomole-gmbh.com/manuals/version_7_3/DOK/DOK.html
  [PDF format]: http://www.cosmologic-services.de/downloads/TM73-documentation/TM73-documentation.pdf
  [TURBOMOLE homepage]: http://www.cosmologic.de/turbomole.html
  [Manuals and Tutorials]: http://www.cosmologic.de/turbomole/support-download/documentation-how-to.html
  [Tutorial (PDF)]: http://www.turbomole-gmbh.com/manuals/version_6_6/Turbomole_Tutorial_6-6.pdf
  {.generated}
  [*Molecular electronic excitations with Turbomole*]: http://www.csc.fi/english/csc/courses/archive/tm-10
  [PDF]: http://extras.csc.fi/chem/courses/tm-2010/CSC_course_140110.pdf
  [gOpenMol]: http://www.csc.fi/gopenmol
  [1]: http://extras.csc.fi/chem/progs/turbomole/turbocourse.pdf
  [Postscript]: http://extras.csc.fi/chem/progs/turbomole/turbocourse.ps
  [TURBOMOLE 5.8 ja uudet ominaisuudet]: http://extras.csc.fi/chem/progs/turbomole/atCSC-0106-7-10.pdf
  [@CSC, 1/2006]: http://www.csc.fi/csc/julkaisut/atcsc/edelliset_numerot/atcs
