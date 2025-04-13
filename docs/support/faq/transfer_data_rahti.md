
# Kuinka siirtää tietoja Rahtiin? {#how-to-transfer-data-to-rahti}

Kuten [saatavilla olevissa tallennusvaihtoehdoissa](../../cloud/rahti/storage/index.md) -artikkelissa keskusteltiin, on mahdollista tallentaa tietoja käyttäen pysyvää voluumia tai esimerkiksi objektitallennuspalvelua, kuten [Allas](../../data/Allas/index.md).

## pysyvään volyymiin {#to-a-persistent-volume}

Jotta tietoja voidaan siirtää Rahtiin, paras menetelmä on käyttää komentorivityökalua `oc rsync`. Ohjeistosta:

```bash
$ oc rsync
Copy local files to or from a pod container

This command will copy local files to or from a remote container. It only copies the changed files
using the rsync command from your OS. To ensure optimum performance, install rsync locally. In UNIX
systems, use your package manager. In Windows, install cwRsync from https://www.itefix.net/cwrsync.
```

Ensinnäkin, on [asennettava oc](../../cloud/rahti/usage/cli.md).

Kun `oc` on asennettu, prosessi on seuraava:

* Luo `PersistentVolumeClaim` (PVC) tietojen tallentamiseksi Rahtiin. Voit käyttää web-käyttöliittymää tai suoraan komentoriviä. Tässä esimerkissä käytämme komentoriviä. Yksinkertainen tapa luoda `1Gi` volyymi nimeltään `testing-pvc` on:

```bash
$ echo 'apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: testing-pvc
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi' | oc create -f -
```

* Liitä PVC PODiin, jossa `rsync` on asennettuna. On mahdollista käyttää mitä tahansa kuvaa, jossa `rsync`-komento on asennettuna. Jos tällaiseen kuvaan ei ole pääsyä, `oc rsync` toimii myös kuvan kanssa, jossa `tar` on asennettuna (`centos` ja `ubuntu` kuvat sisältävät `tar`:in).

* Käytä lopuksi `oc rsync`-komentoa synkronoidaksesi paikallisen hakemiston ja PODin hakemiston:

```bash
oc rsync ./local/dir/ POD:/remote/dir
```

Jos paikallinen data muuttuu, voit yksinkertaisesti ajaa saman komennon uudelleen. Jos kuvassa on `rsync` asennettuna, vain muuttuneet tiedot kopioidaan PVC:hen.

## Allakseen objektitallennukseen {#to-allas-object-storage}

Katso [Allaksen käyttäminen Rclone:n kanssa](../../data/Allas/using_allas/rclone.md) saadaksesi ohjeet tietojen kopioimiseen Allakseen. Kun tiedot ovat Allaksessa, voit käyttää mitä tahansa *Swift*- tai *S3*-yhteensopivaa asiakasta tai kirjastoa, kuten `rclone`, sovelluksessasi.
