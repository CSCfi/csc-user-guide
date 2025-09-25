---
tags:
  - Academic
catalog:
  name: AMS
  description: Modelling suite providing engines like ADF, BAND, DFTB and MOPAC
  description_fi: Mallinnuspaketti, joka tarjoaa moottoreita kuten ADF, BAND, DFTB ja MOPAC
  license_type: Academic
  disciplines:
    - Chemistry
  available_on:
    - Puhti
    - Mahti
---

# AMS { #ams }

Amsterdam Modeling Suite (AMS) on kattava laskennallisen kemian ohjelmistopaketti. Siihen kuuluu graafinen käyttöliittymä, [AMS-GUI](ams-gui.md), joka tarjoaa intuitiivisen tavan simulaatioiden määrittämiseen, ajamiseen ja analysointiin.

## Saatavilla { #available }

-   Puhti: ADF, versio 2024.102
-   Mahti: ADF, versio 2024.102

## Lisenssi { #license }
-  Lisenssi oikeuttaa ohjelmiston käyttöön kenen tahansa akateemisen tutkijan tai akateemiseen oppilaitokseen kuuluvan opiskelijan toimesta, missä "Academic" tarkoittaa "tutkintoja myöntävään oppilaitokseen kuuluvaa". 
-  Lisenssi ei sisällä oikeutta käyttää ohjelmistoa valtion laboratorioiden tai muiden ei-akateemisten voittoa tavoittelemattomien tutkimuslaitosten työntekijöille. 
-  Lisenssi sallii ainoastaan voittoa tavoittelemattoman, ei-kaupallisen käytön. 
-  Lisenssi sulkee pois kaikki sopimustutkimuksen muodot, rojaltituloja tuottavat toiminnot sekä muut taloudelliseen hyötyyn johtavat toiminnot.
-  Tutkimusryhmät, jotka tarvitsevat AMS-paketin muita moduuleja, voivat hankkia itselleen lisenssin ohjelmien ajamiseen CSC:n tietokoneilla. 

## Käyttö { #usage }

Alusta AMS:

```bash
module load ams/2024.102
```

### Esimerkkieräajojen skriptit { #example-batch-scripts }

!!! warning "Huomio"
    Erityisesti jotkin ominaisuuslaskut voivat olla hyvin levy-I/O-intensiivisiä. Tällaiset työt hyötyvät [nopean paikallisen tallennustilan (NVMe)](../computing/running/creating-job-scripts-puhti.md#local-storage) käytöstä Puhtissa. Paikallisen levyn käyttö tällaisissa töissä vähentää myös Lustre-rinnakkaistiedostojärjestelmän kuormitusta.
 

=== "Puhti"
    
    ```bash
    #!/bin/bash
    #SBATCH --partition=test
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=40      # MPI tasks per node
    #SBATCH --account=yourproject     # insert here the project to be billed 
    #SBATCH --time=00:15:00           # time as `hh:mm:ss`
    #SBATCH --mem-per-cpu=1500        # requested memory per process in MB
    module purge
    module load ams/2024.102
    export SCM_TMPDIR=$PWD/$SLURM_JOB_ID
    mkdir -p $SCM_TMPDIR
    # Create an example input file from the examples 
    sed '1,4d;$d;/Print/,/End/d' $AMSHOME/examples/Benchmarks/ADF/Si35_TZ2P/Si35_TZ2P.run  > ./Si35_TZ2P.inp
    "$AMSBIN/ams" < ./Si35_TZ2P.inp > ./Si35_TZ2P.log
    ```
     
=== "Puhti, paikallinen levy"
    
    ```bash
    #!/bin/bash
    #SBATCH --partition=large
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=40      # MPI tasks per node
    #SBATCH --account=yourproject     # insert here the project to be billed
    #SBATCH --time=00:15:00           # time as `hh:mm:ss`
    #SBATCH --mem-per-cpu=1500        # requested memory per process in MB
    #SBATCH --gres=nvme:100           # requested local disk space in GB
    module load ams/2024.102
    export SCM_TMPDIR=$LOCAL_SCRATCH
    # Create an example input file from the examples
    sed '1,4d;$d;/Print/,/End/d' $AMSHOME/examples/Benchmarks/ADF/Si35_TZ2P/Si35_TZ2P.run  > ./Si35_TZ2P.inp
    "$AMSBIN/ams" < ./Si35_TZ2P.inp > ./Si35_TZ2P.log
    ```

=== "Mahti"
    
    ```bash
    #!/bin/bash
    #SBATCH --partition=medium
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=128 # MPI tasks per node
    #SBATCH --account=yourproject # insert here the project to be billed
    #SBATCH --time=00:20:00       # time as `hh:mm:ss`
    module purge
    module load ams/2024.102
    export SCM_TMPDIR=$PWD/$SLURM_JOB_ID
    mkdir -p $SCM_TMPDIR
    
    # Create an example input file from the examples
    sed '1,4d;$d;/Print/,/End/d' $AMSHOME/examples/Benchmarks/ADF/Si35_TZ2P/Si35_TZ2P.run  > ./Si35_TZ2P.inp
    "$AMSBIN/ams" < ./Si35_TZ2P.inp > ./Si35_TZ2P.log
    ```

### [AMS-GUI](../apps/ams-gui.md) { #the-ams-gui }

AMS sisältää integroidun graafisen käyttöliittymän, [AMS-GUI](ams-gui.md), joka helpottaa mallinnustehtävien määrittämistä, ajamista ja analysointia.
Käyttöliittymää voi kokeilla Puhtin verkkokäyttöliittymän kautta, mutta laajempaa käyttöä varten suosittelemme asentamaan
käyttöliittymän omalle kannettavalle/työasemalle. Yksityiskohtaiset ohjeet löytyvät [AMS-GUI-dokumentaatiosta.](ams-gui.md)

## Viitteet { #references }

Käytöstä riippuen muista viitata asianmukaisesti AMS-ajuriin, käytettyihin laskentamoottoreihin sekä ominaisuusviittauksiin. Lisätietoja on saatavilla [asianmukaisesta AMS-dokumentaatiosta](https://www.scm.com/doc/Documentation/ ) 

## Lisätietoa { #more-information }

-   [AMS:n tukisivut](https://www.scm.com/contact-us/)
-   [Opetusohjelmat](https://www.scm.com/doc/Tutorials/index.html)
-   [Työpajat](https://www.scm.com/workshops/)
-   [UKK](https://www.scm.com/faq/)
-   [Tietopankki](https://www.scm.com/knowledgebank/)
-   [Tuoreimmat uutiset](https://www.scm.com/news/)