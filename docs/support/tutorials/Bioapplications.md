This tutorial page  explains how bioapplications can be run as singularity containers in Puhti using selected applications  as explained below:

   - [DeepVariant pipeline](#deepvariant-pipeline)
   - ...

### DeepVariant pipeline  ###

DeepVariant pipeline (Poplin et al., Nature biotechnology, 2018) is used  to perform variant calling on WGS and WES data sets. More information about the deepvariant programmes can be found [here](https://github.com/google/deepvariant) 

One needs to get DeepVariant docker image, models and test data in order to run the pipeline. Additionally, other prerequisites for running deepvariant method includes 1) obtaining A reference genome in [FASTA](https://en.wikipedia.org/wiki/FASTA_format) format and its corresponding index file (.fai). 2) An aligned reads file in [BAM](http://genome.sph.umich.edu/wiki/BAM) format and its corresponding index file (.bai).

#### Convert docker image to singularity image on your local machine ####

One way to build a singularity image is to download the deepvariant docker image to local registry and convert it to singularity image to avoid any possible erros with docker images pulled directly with singularity from google registry. Please note that one has to do these image conversions in local machines as Puhti does not grant root access to users.

Pull the DeepVariant image and push it to local registry as below:

```
sudo docker pull gcr.io/deepvariant-docker/deepvariant:0.8.0
sudo docker tag gcr.io/deepvariant-docker/deepvariant:0.8.0 localhost:5000/deepvariant:latest
sudo docker run -d -p 5000:5000 --restart=always --name registry registry:2
sudo docker push localhost:5000/deepvariant:latest
```

then create a definition file (deffile) as follows:

```
Bootstrap: docker
Registry: http://localhost:5000
Namespace:
From:deepvariant:latest
```
and finally create a singularity image as below:

```
sudo SINGULARITY_NOHTTPS=1 singularity build deepvariant.simg  deffile
```
Alternatively, one can download already converted images and test data from **allas** object storage as below:

```
wget https://a3s.csc.fi/pilot_projects/Deepvariant_singulairty.zip
```


### Prepare slurm batch scripts to run it on Puhti (file: deepvariant_puhti.sh)

```
#!/bin/bash
#SBATCH --time=00:05:00
#SBATCH --partition=test
#SBATCH --account=project_xxx

export TMPDIR=$PWD 

singularity -s exec -B $PWD:/data  \
deepvariant.simg \
/opt/deepvariant/bin/run_deepvariant \
--model_type=WGS \
--ref=/data/testdata/ucsc.hg19.chr20.unittest.fasta \
--reads=/data/testdata/NA12878_S1.chr20.10_10p1mb.bam \
--regions "chr20:10,000,000-10,010,000" \
--output_vcf=output.vcf.gz  \
--output_gvcf=output.g.vcf.gz
```

### Submit job using sbatch command

```
sbatch  deepvariant_puhti.sh
```

Please **note** that one can use gpu version of deepvariant with the following sbatch script 

```
#!/bin/bash
#SBATCH --time=00:05:00
#SBATCH --partition=gputest
#SBATCH --gres=gpu:v100:1
#SBATCH --account=project_xxx

export TMPDIR=$PWD

singularity -s exec --nv -B $PWD:/data \
deepvariant_gpu.simg \
/opt/deepvariant/bin/run_deepvariant \
--model_type=WGS \
--ref=/data/testdata/ucsc.hg19.chr20.unittest.fasta \
--reads=/data/testdata/NA12878_S1.chr20.10_10p1mb.bam  \
--regions "chr20:10,000,000-10,010,000" \
--output_vcf=output.vcf.gz  \
--output_gvcf=output.g.vcf.gz
```
