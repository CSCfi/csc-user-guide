# Using Avogadro2 with Gaussian and ORCA on Roihu

Avogadro2 is a molecular editor. On Roihu it runs in the Desktop app of the web interface, so you can build a molecule, create an input file, and open the result in one place. In this tutorial you build ethanol, optimize it, and run a B3LYP geometry optimization with Gaussian or ORCA.

For all options, see the [Avogadro2](../../apps/avogadro2.md), [Gaussian](../../apps/gaussian.md) and [ORCA](../../apps/orca.md) pages.

## 1. Start Avogadro2

1. In the [Roihu web interface](https://www.roihu.csc.fi), select **Apps → Desktop**.
2. Select your **Project** and the **Partition** `interactive`, set **Memory (GiB)** to 4, and click **Launch**.
3. In **My Interactive Sessions**, click **Launch Desktop** when the session is **Running**.
4. In the desktop, double-click **Avogadro 2**. If a **Version Update** window appears, select **Ignore**.

See the [Desktop](../../computing/webinterface/desktop.md) page for more.

## 2. Build ethanol

Select **Build → Insert → Molecule...**, type `ethanol` in the **Filter** field, and click **Insert**. <!-- VERIFY: ethanol is in the fragment library -->

To draw it instead, use the draw tool: two carbon atoms and one oxygen atom in a chain. Avogadro2 adds the hydrogen atoms. <!-- VERIFY: hydrogens are added automatically; else Build → Add Hydrogens -->

![Ethanol in Avogadro2](../../img/avogadro2-ethanol-build.png)
<!-- SCREENSHOT 1: avogadro2-ethanol-build.png (1-2 arrows maximum) -->

## 3. Optimize with a force field

Select **Extensions → Open Babel → Optimize Geometry**. This gives a reasonable start geometry. To change the force field, use **Extensions → Open Babel → Configure Force Field...**.

## 4. Create the input file

Open the generator from the **Input** menu. Use the same values for both programs: 4 processor cores and 6 GiB memory.

=== "Gaussian"

    Select **Input → Gaussian...**. <!-- VERIFY: menu entry and setting names -->

    | Setting | Value |
    |---|---|
    | Calculation type | Equilibrium Geometry |
    | Theory | B3LYP |
    | Basis | 6-31G(d) |
    | Charge / Multiplicity | 0 / 1 |
    | Processor Cores | 4 |
    | Memory | 6 GiB |

    Click **Save Input...** and save the file as `/scratch/<project>/ethanol_opt/ethanol.com`.

    ![Gaussian input dialog](../../img/avogadro2-gaussian-dialog.png)
    <!-- SCREENSHOT 2a: avogadro2-gaussian-dialog.png -->

=== "ORCA"

    Select **Input → ORCA...**.

    | Setting (tab) | Value |
    |---|---|
    | Calculation type (Basic) | Equilibrium Geometry |
    | Theory (Basic) | B3LYP |
    | Basis (Basis) | def2-SVP |
    | Charge / Multiplicity (Basic) | 0 / 1 |
    | Processor Cores | 4 |
    | Memory | 6 GiB |

    The input has `%pal nprocs 4` and `%MaxCore 1536` (MB per process). Click **Save Input...** and save the file as `/scratch/<project>/ethanol_opt/ethanol.inp`.

    ![ORCA input dialog](../../img/avogadro2-orca-dialog.png)
    <!-- SCREENSHOT 2b: avogadro2-orca-dialog.png -->

Use a separate directory for each calculation. The generators only write the input file. The program must be available on Roihu.

## 5. Run the calculation

Run the calculation as a batch job. Submit it from the Roihu CPU login node.

=== "Gaussian"

    ```bash
    cd /scratch/<project>/ethanol_opt
    module load gaussian
    subg16 ethanol.com
    ```
    <!-- VERIFY: module name, subg16 syntax, and how cores and memory are given, against gaussian.md -->

=== "ORCA"

    ORCA is not installed centrally at CSC. Install a private copy first, see the [ORCA](../../apps/orca.md) page.

    Create `job.sh` in the same directory as `ethanol.inp`:

    ```bash
    #!/bin/bash
    #SBATCH --partition=small
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=4       # same as %pal nprocs
    #SBATCH --mem-per-cpu=1536        # MB, same as %MaxCore
    #SBATCH --account=<project>
    #SBATCH --time=00:30:00

    export ORCADIR=/projappl/<project>/<user>/orca/<orca-directory>
    module purge
    module load orca/6.1.1

    ${ORCADIR}/orca ethanol.inp > ethanol.out
    ```

    ```bash
    cd /scratch/<project>/ethanol_opt
    sbatch job.sh
    ```

The job is small and should finish in a few minutes.

## 6. Check the result

=== "Gaussian"

    ```bash
    tail -f ethanol.log
    ```

    The optimization is finished when the file contains `Optimization completed` and ends with `Normal termination`.

=== "ORCA"

    ```bash
    tail -f ethanol.out
    ```

    The optimization is finished when the file contains `OPTIMIZATION RUN DONE` and ends with `ORCA TERMINATED NORMALLY`.

Press `Ctrl+C` to stop `tail`.

## 7. View the optimized structure

In Avogadro2, select **File → Open** and open the output file: `ethanol.log` (Gaussian) or `ethanol.out` (ORCA). <!-- VERIFY: Avogadro2 shows the final geometry from both files -->

Compare the structure with the start geometry, for example the C–O bond length.

![Optimized ethanol](../../img/avogadro2-optimized-ethanol.png)
<!-- SCREENSHOT 3: avogadro2-optimized-ethanol.png -->

## 8. Frequency calculation

A frequency calculation confirms that the optimized structure is a minimum. Add `Freq` to the job line of the input file:

=== "Gaussian"

    ```text
    # B3LYP/6-31G(d) Opt Freq
    ```

=== "ORCA"

    ```text
    ! B3LYP def2-SVP Opt Freq
    ```

A minimum has no imaginary frequencies. An imaginary frequency is printed as a negative number. One imaginary frequency means a transition state, or a structure that needs more optimization.

Open the output in Avogadro2 and select **Analyze → Vibrational Modes...** to animate the modes, or **Analyze → Plot Spectra...** for the IR spectrum.

## Common problems

- **SCF does not converge:** check the charge, the multiplicity and the start geometry.
- **Job stops at the time limit:** increase `--time` and start again from the last geometry.

See the [Gaussian](../../apps/gaussian.md) and [ORCA](../../apps/orca.md) pages for more.
