---
tags:
  - Free
catalog:
  name: Avogadro2
  description: Molecular editor and visualizer
  license_type: Free
  disciplines:
    - Chemistry
  available_on:
    - Roihu
---

# Avogadro2

[Avogadro2](https://two.avogadro.cc/) is a graphical molecular editor and analysis tool. It is used to build molecular structures, to generate input files for quantum chemistry programs, and to visualize results, for example the molecular orbitals and vibrational modes of an ORCA calculation.

## Available

- Roihu-CPU: 2.0.0

Avogadro2 is available in the Desktop app of the Roihu web interface at [www.roihu.csc.fi](https://www.roihu.csc.fi). It runs in a container with software rendering (CPU).

## License

Avogadro2 is free and open source software, distributed under the [BSD 3-clause license](https://github.com/OpenChemistry/avogadroapp/blob/master/LICENSE).

## Usage

Avogadro2 is a graphical program. Use it in the [Desktop app](../computing/webinterface/desktop.md) of the Roihu web interface.

1. Log in to the [Roihu web interface](https://www.roihu.csc.fi).
2. Select **Apps → Desktop**.
3. Select your **Project** and the **Partition** `interactive`. Set **Memory (GiB)** to 4. Click **Launch**.
4. In **My Interactive Sessions**, wait until the Desktop session is **Running**, then click **Launch Desktop**.
5. In the desktop, double-click the **Avogadro 2** icon, or select **Applications → Chemistry → Avogadro 2**.

!!! note
    Avogadro2 is used for preparing structures and inputs, and for viewing results. Run the calculations as batch jobs, see the pages of the programs, for example [ORCA](orca.md) and [Gaussian](gaussian.md).

### Importing a structure

The simplest way to get a start structure is the fragment library. No file is needed.

1. Select **Build → Insert → Fragment...**.
2. Type a name in the **Filter** field, or expand a category (for example `aromatics` or `amino_acids`). The preview shows the selected molecule.
3. Click **Insert** once. The **Files** panel shows the formula (for benzene `C6H6`).

To use your own structure file:

1. Upload the structure file to Roihu with the **Files** web interface app: select the directory (for example `/scratch/<project>`) and click **Upload**.
2. In Avogadro2, select **File → Open** and select the file. Many formats (`.xyz`, `.mol2`, `.pdb`, `.cif`, etc.) are read through Open Babel.

### Building a structure

1. Draw a structure with the draw tool, or import one (see above).
2. Optimize the geometry with **Extensions → Open Babel → Optimize Geometry**. This force-field pre-optimization gives a reasonable start geometry for the quantum chemistry calculation. Select the force field with **Extensions → Open Babel → Configure Force Field...**.
3. Export the coordinates with **File → Export Molecule** (or the **Export Molecule...** button in the toolbar), for example as `mymolecule.xyz`. Save the file in your project directory, for example in `/scratch/<project>`.

### Generating an input file

The structure in the Avogadro2 window is used as the coordinates of the input file.

1. Select **Input → ORCA...** to open the **ORCA Input Generator**. The **Input** menu has generators for several programs, for example Gaussian, NWChem, MOLPRO and Psi. The generators only write input files, and the program itself must be available on Roihu.
2. Set the options in the tabs (**Basic**, **SCF**, **Basis**, **Electric Properties**). On the **Basic** tab you can set, for example, the calculation type, the theory, the charge and the multiplicity.
3. Set **Processor Cores** and **Memory** (total memory in GiB). The preview window (`job.inp`) shows the result. The number of cores gives `%pal nprocs`, which must be equal to the number of MPI tasks in the batch script (`--nodes` × `--ntasks-per-node`). The memory gives `%MaxCore`, the memory per MPI process in MB. For example, 4 cores and 6 GiB give `%MaxCore 1536`. In the batch script, `--mem-per-cpu` must have the same value as `%MaxCore`. See the [ORCA](orca.md) page.
4. To view orbitals later, select **Print Molecular Orbitals**. This adds the keywords `PrintMOs PrintBasis` to the input.
5. Click **Save Input...**. In the file dialog, select your project directory and the file name, for example `/scratch/<project>/benzene/job.inp`, and click **Save**. Use a separate directory for each calculation.
6. Create a batch script and submit the calculation, see below.

### Running the calculation

ORCA is not installed centrally at CSC. Each user installs a private copy, see the [ORCA](orca.md) page. Jobs must be submitted from the CPU login node (`roihu-cpu`).

Create a batch script `job.sh` in the same directory as `job.inp`. If you saved the input with another name, use that name in the script. The values below match the example above (4 cores, 6 GiB, `%MaxCore 1536`). Replace the text in angle brackets (`<...>`) with your own values:

```bash
#!/bin/bash
#SBATCH --partition=small
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4       # same as %pal nprocs
#SBATCH --mem-per-cpu=1536        # MB, same as %MaxCore
#SBATCH --account=<project>
#SBATCH --time=01:00:00

export ORCADIR=/projappl/<project>/<user>/orca/<orca-directory>
module purge
module load orca/6.1.1

${ORCADIR}/orca job.inp > job.out
```

Submit the job from the login node:

```bash
cd /scratch/<project>/benzene
sbatch job.sh
```

When the job has finished, the end of `job.out` shows `ORCA TERMINATED NORMALLY`. Then open `job.out` in Avogadro2 to view the results, see below. For the available partitions and other options, see the [Roihu batch job partitions](../computing/running/batch-job-partitions.md) page.

### Analysing ORCA output

1. Open the ORCA output file with **File → Open** and select the `.out` file.
2. Molecular orbitals: select **Analyze → Molecular Orbitals...**. The window lists the orbitals with their energies (eV) and occupations. Select an orbital, for example `HOMO` or `LUMO`, set the **Quality** and click **Render**. This requires `PrintMOs PrintBasis` in the ORCA input. The option **Print Molecular Orbitals** of the input generator adds them.
3. Vibrational modes: select **Analyze → Vibrational Modes...**. The window lists the frequencies (cm⁻¹) and the IR intensities (km/mol). Select a mode to animate it, change the **Amplitude** with the slider, and click **Stop Animation** to stop. The first six frequencies of a non-linear molecule are zero: they are the translations and rotations. This requires a frequency calculation (**Calculation Type** `Freq`).
4. IR spectrum: select **Analyze → Plot Spectra...**. The **Vibrational Spectra** window shows the transmission against the wavenumber (cm⁻¹), with a smoothed and a raw curve. The drop-down list under the plot shows the spectrum type (**Infrared**), and **Options...** opens the plot settings.

### Tips

- Avogadro2 runs inside the Desktop session. Keep the session open while you use it.
- A terminal window opens together with Avogadro2 and closes when you quit Avogadro2.
- Copy-paste between your local computer and the desktop works via the noVNC clipboard. Open the **Clipboard** menu from the tab on the left edge of the desktop window, paste your text there, and then paste normally inside the desktop.
- If a **Version Update** dialog appears, select **Ignore**.
- The file dialog may open in another directory. Type the full path of the file in the **File name** field to go there directly.
- Open Babel is included, so many structure file formats can be read and written.

## References

The Avogadro project plans a separate Avogadro2 paper. Until it appears, cite the original Avogadro paper and the version of Avogadro2 that you used:

- Hanwell, M. D. et al. Avogadro: an advanced semantic chemical editor, visualization, and analysis platform. J. Cheminform., 4:17, 2012. doi:[10.1186/1758-2946-4-17](https://doi.org/10.1186/1758-2946-4-17).
- Hanwell, M. D. and Hutchison, G. R. Avogadro2 (version 2.0), 2026. doi:[10.5281/zenodo.19369545](https://doi.org/10.5281/zenodo.19369545).

## More information

- [Avogadro2 project page](https://two.avogadro.cc/)
- [Avogadro2 documentation](https://avogadro.cc/docs/)
