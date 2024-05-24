# Shape based molecular screening using GPU

This tutorial will show how to use the 
[Schrödinger Maestro Shape](https://www.schrodinger.com/Shape-Screening/)
tool to quickly screen the 
[Molport molecular database](https://molport.com/shop/screeening-compound-database)
with 16 million structures (160 million conformations) on a GPU in Puhti.

_Preparing_ the Molport database for GPU screening takes two weeks,
but since the prepared _shape file_ is already available on Puhti the actual
screening of your molecule takes only 5-20 minutes on a GPU.


## HOW-TO

* Install Maestro on your local computer. Detailed instructions can
  be found on [our Maestro page](../../apps/maestro.md).
* Draw / import the molecule you want to find similar molecules of
* Run the [Maestro LigPrep](https://www.schrodinger.com/LigPrep/) tool on it
* Export the prepared molecule in the native Maestro format (mae), e.g. as `target.mae`
* Copy the file to Puhti in your scratch area ([Tips for copying files](../../data/moving/index.md))
* Copy (and edit if necessary) the following _script_ as `gpushape.bash` (don't copy the 139GB shape-file)
  to the same folder
    * This script will request 60 minutes of time on one GPU, use the _shape file_ from
      `/appl/data/bio/molport-shape/MP_SHAPE.bin`, use `target.mae` as the search
      molecule, and put the results in `shape_test-out.maegz`
```
$SCHRODINGER/shape_screen_gpu run -shape_data_treatment remote \
      -shape target.mae -HOST quick-gpu -JOBNAME shape_test \
      -screen /appl/data/bio/molport-shape/MP_SHAPE.bin
```
* Initialize the default Maestro installation with
```
module load maestro
```
* ...and submit the job (note, without `sbatch`!)
```
bash gpushape.bash
```
* Copy the results to your local computer for analysis
