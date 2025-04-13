
# Kuinka voin liittää Allas S3 -ämpärin cPoutassa toimivaan VM:ään {#how-can-i-mount-my-allas-s3-bucket-to-a-vm-running-in-cpouta}

Yhdistämällä cPouta-pilviympäristön ja Allas-tallennusympäristön voit rakentaa skaalautuvia tiedonhallintaympäristöjä. Tämä asiakirja näyttää yhden esimerkin siitä, kuinka voit yhdistää nämä kaksi palvelua liittämällä ämpärin Allaksesta cPoutassa toimivaan Ubuntu 22.04 (testattu myös Ubuntu 20.04 ja 18.04) tai Centos7-pohjaiseen virtuaalikoneeseen.

[TOC]

## OpenStackin, s3cmd:n ja s3fs:n asennus {#installing-openstack-s3cmd-and-s3fs}

### Ubuntussa 22.04 LTS (toimii myös Ubuntu 20.04 ja 18.04) {#in-ubuntu-2204-lts-works-for-ubuntu-2004-and-1804-as-well}

* Käynnistettyäsi Ubuntu-pohjaisen virtuaalikoneen cPoutassa, avaa terminaaliyhteys virtuaalikoneeseen ja päivitä se komennolla:

	```sh
	sudo apt update
	```

!!! warning
    Vanhemmissa Ubuntu-versioissa on vanhat ja vanhentuneet Python-versiot. Suositellaan käyttämään käytössä olevaa uusinta Ubuntua Poutassa.

* Asenna sitten OpenStack-asiakasohjelma:

	```sh
	sudo apt install python3-pip python3-dev python3-setuptools
	sudo pip install --upgrade pip
	sudo pip install python-openstackclient
	```

	!!! info
		Ubuntu 18.04:ssä suorita nämä komennot:  
		```sh
		sudo apt install python3-pip python3-dev python3-setuptools
		sudo pip3 install --upgrade pip
		sudo pip install python-openstackclient --ignore-installed PyYAML
		```
		
		Jos jätät `--ignore-installed PyYAML` pois, saat virheilmoituksen:  
		```
		Cannot uninstall 'PyYAML'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.
		```
		Se tulisi asentaa **distutils**-työkalun kautta, joten poistoprosessi ei pysty vahvistamaan, mitkä tiedostot kuuluvat siihen.

* Seuraavaksi asenna **s3cmd** ja **s3fs** komennot virtuaalikoneeseesi.

	```sh
	sudo apt install s3cmd s3fs
	```

### Centos7:ssä (Ylläpitopäivitykset EOL 2024-06-30) {#in-centos7-maintenance-updates-eol-2024-06-30}

* Käynnistettyäsi Centos7-pohjaisen virtuaalikoneen cPoutassa, avaa terminaaliyhteys virtuaalikoneeseen ja päivitä se komennolla:

	```sh
	sudo yum update
	```

* OpenStack ja s3cmd voidaan asentaa sitten seuraavasti:

	```sh
	sudo yum install python3 python3-devel wget
	sudo python3 -m pip install --upgrade pip
	sudo python3 -m pip install python-openstackclient
	sudo yum install s3cmd
	```

* s3fs-fuse voidaan asentaa tällä komennolla:

	```sh
	sudo yum install s3fs-fuse
	```

## Allaksen konfigurointi ja käyttäminen {#configuring-and-using-allas}

### Käytä s3cmd:ää tiedostojen lukemiseen ja kirjoittamiseen {#use-s3cmd-to-read-and-write-files}

Kun olet asentanut openstackin, s3cmd:n ja s3fs:n, lataa ja suorita **poutaos_configure** työkalu konfiguroidaksesi _s3cmd_ siten, että se käyttää cPouta-projektiasi. Voit myös käyttää tätä työkalua vaihtaaksesi eri Allas-projektien välillä, jos sinulla on useampi niistä.

```
wget https://a3s.fi/tools/poutaos_configure
chmod u+x poutaos_configure
./poutaos_configure
```

_poutaos_configure_ kysyy ensin käyttäjä- ja salasanaasi CSC:lle. Voit nähdä CSC-käyttäjänimesi [MyCSC-profiili](https://my.csc.fi/profile) sivultasi, ja voit myös vaihtaa salasanasi siellä. Työkalu listaa sitten Allas-projektisi ja kysyy käytettävää projektia. Lopuksi se kysyy **chunk size** -arvoa, on suositeltavaa jättää oletusarvo.

Tämän jälkeen voit käyttää Allas-projektisi tallennustilaa _s3cmd_ komennoilla. Nyt voit nähdä, ladata ja lähettää tiedostoja tähän ämpäriin _s3cmd_:llä.

* Listaa kaikki ämpärisi:

```sh
$ s3cmd ls s3://
2022-10-17 07:03  s3://data-europe
2020-09-17 11:12  s3://images-sky
2020-11-06 13:56  s3://case_1
```

* Oletetaan, että sinulla on jo ämpäri nimeltä **case_1** Allaksessa ja siinä on joitakin dataobjekteja (eli tiedostoja).

```sh
$ s3cmd ls s3://case_1
2022-10-17 07:14     67213268  s3://case_1/file1.txt
```

* Tiedoston hakeminen:

```sh
s3cmd get s3://case_1/file1.txt
```

* Uuden tiedoston lataaminen:

```sh
s3cmd put file2.txt s3://case_1/
```

Tämä on **suositeltu tapa** käyttää Allasta S3-protokollan kautta komentoriviltä. On myös mahdollista liittää ämpäri virtuaalikoneeseesi siten, että se näkyy "liitettynä levynä". Voit käyttää `s3fs`:ää tähän.

### Käytä s3fs:ää kansion liittämiseen virtuaalikoneeseesi {#use-s3fs-to-mount-a-folder-into-your-vm}

1. Tee ensin tyhjä hakemisto (kuten **os_case_1**), jota käytetään liitäntäpisteenä:

	```sh
	mkdir os_case_1
	```

	!!! info
	    Mikä tahansa tyhjä hakemisto voidaan käyttää liitäntäpisteenä

1. Luo `.passwd-s3fs` tiedosto kotihakemistoosi. Tiedoston muoto on: `ACCESS_KEY_ID:SECRET_ACCESS_KEY` ja siinä on oltava _600_ oikeudet. (Projektisi on oltava määritettynä: `source project_xxxxxxx`)

	```sh
	$ openstack ec2 credentials list -f value | grep $OS_PROJECT_ID | tail -1 |\
	   awk '{print $1":"$2}' >.passwd-s3fs
	Password:
	$ chmod 600 .passwd-s3fs
	```

1. Käytä sitten _s3fs_ komentoa liittääksesi ämpäri.

	```sh
	s3fs case_1 os_case_1 -o passwd_file=~/.passwd-s3fs -o url=https://a3s.fi/ \
		-o use_path_request_style -o umask=0333,uid=$(id -u)
	```

	!!! info 
	    `id -u` komennon palauttama uid-arvo on oletuskäyttäjälle 1000

	!!! info
	    Umask-arvo `0333` liittää tiedostot **vain luku** -tilassa. Jos haluat liittää ne luku-kirjoitus -tilassa, käytä `0027` sijaan.

1. Tämän jälkeen sinun pitäisi voida nähdä liitetyn ämpärin objektit tiedostoina. Kokeile esimerkiksi seuraavaa komentoa:

	```sh
	ls -l os_case_1
	```

	Tulos pitäisi olla sama kuin `s3cmd ls s3://case_1`

	!!! info 
	    Voit myös tarkistaa liitäntäpisteen komennolla `df -h`

1. Kun olet valmis, voit irrottaa kansion:

	```sh
	sudo umount os_case_1
	```
```

