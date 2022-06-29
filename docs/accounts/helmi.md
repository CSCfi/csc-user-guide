# Specific instructions for the LUMI Helmi partition


The LUMI Helmi partition is currently only available for FiQCI users in projects that have been granted access. In addition to running jobs on Helmia via LUMI, users can also use the general LUMI system and software stack including using simulators. 



## LUMI Helmi projects vs. regular LUMI projects

When applying for a new project in MyCSC for the Helmi partition, under "Select LUMI **access mode**", select the "Quantum" option. 


* [Creating a new project in MyCSC](../how-to-create-new-project)
* [How to create Finnish LUMI projects](../how-to-create-new-project/#how-to-create-finnish-lumi-projects)


<!-- ===
* Can a Quantum project use the Helmi partition AND LUMI-C partition for example?
* What about other LUMI Partitions? E.g they want to use Jupyter-notebook LUMI-D?
* Integration with Kvasi or just mention Kvasi?  -->



## LUMI Helmi partition

The LUMI Helmi partition consists of a single LUMI-C node with 256 GiB of memory that is directly connected to Helmi for submitting jobs through. [This is described in more detail on the LUMI-C page](https://docs.lumi-supercomputer.eu/computing/systems/lumic/). 
<!-- 
* Can this node make use of Classical HPC pre processing or just for submitting jobs to Helmi?  -->

There are currently only two queues in the Helmi partition correspodning to FiQCI projects: `q_fiqci`, `q_fiqcitest`. The maximum job size for both queues is **1 node**. For `q_fiqci` the maximum runtime is **ENTER MAX RUNTIME** and for `q_fiqcitest` the maximum runtime is **ENTER MAX RUNTIME**. 

<!-- * `q_fiqci` for submitting jobs to Helmi on the actual QC
* `q_fiqcitest` for submitting jobs to simulator?
* Or normal test queue rules i.e `q_fiqci` for actual QPU and simulator but user specifys QPU through our software stack? (Future work?) -->

## Storage areas

Helmi partition users can access the `/helmi/` folder in LUMI. This folder has a global quota of **XXX**. Project folders of Helmi project are located in `/helmi/projappl/<projectname>` and `/helmi/scratch/<projectname>`. 

<!-- * Is there going to be a global quota? Add here if yes
* Cleaning of unsued files policy on LUMI? Add here relevant info
* LUMI-P? -->

## Usage

<!-- * Will helmi users have specific LUMI login nodes? If yes add here -->

LUMI Helmi works similarly to the regular LUMI system, the main difference being that 

1. FiQCI projects use the `q_fiqci` and `q_fiqcitest` partitions instead of the regular LUMI-C, LUMI-G partitions. 


Helmi specific support can be reached either via the regular CSC user support [servicedesk@csc.fi](mailto:servicedesk@csc.fi) or through the very active Helmi RocketChat channel #helmi-computing (**WIP link to channel**) on [chat.csc.fi](https://chat.csc.fi). LUMI specific support such as connecting or storage is available from the [LUMI user support team (LUST)](https://lumi-supercomputer.eu/user-support/need-help/account/).

## Billing 

