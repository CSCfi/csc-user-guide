# Miten pelastaa instansseja? { #how-to-rescue-instances }

OpenStack tarjoaa pelastustilan (rescue mode) VM:ien palauttamiseen. Sen avulla voidaan käynnistää virtuaalikone eri levykuvasta. Tästä on apua, kun virtuaalikone ei käynnisty esimerkiksi kernel panicin, täyden levyn tai yksityisen avaimen katoamisen vuoksi. Käynnistämällä eri levykuvasta voit liittää ja muokata nykyisen levyn tiedostoja ja korjata ongelman.

## Oireet { #symptoms }

### Kernel panic { #kernel-panic }

Tarkista instanssisi Console Log (web-käyttöliittymä: **Instances** > `<your instance>` > **Log**)

```sh
[    1.041853] Loading compiled-in X.509 certificates
[    1.043433] Loaded X.509 cert 'CentOS Linux kpatch signing key:ea0413152cde1d98ebdca3fe6f0230904c9ef717'
[    1.046556] Loaded X.509 cert 'CentOS Linux Driver update signing key:7f421ee0ab69461574bb358861dbe77762a4201b'
[    1.050310] Loaded X.509 cert 'CentOS Linux kernel signing key:d4115f110055db56c8d605ab752173cfb1ac54d8'
[    1.053448] registered taskstats version 1
[    1.055861] Key type trusted registered
[    1.057771] Key type encrypted registered
[    1.059249] IMA: No TPM chip found, activating TPM-bypass! (rc=-19)
[    1.061680]   Magic number: 14:548:18
[    1.063246]  ep_81: hash matches
[    1.064844] rtc_cmos 00:00: setting system clock to 2018-08-23 08:02:54 UTC(1535011374)
[    1.067954] md: Waiting for all devices to be available before autodetect
[    1.069982] md: If you don't use raid, use raid=noautodetect
[    1.072041] md: Autodetecting RAID arrays.
[    1.073689] md: autorun ...
[    1.074976] md: ... autorun DONE.
[    1.076358] List of all partitions:
[    1.077771] No filesystem could mount root, tried: 
[    1.079600] Kernel panic - not syncing: VFS: Unable to mount root fs onunknown-block(0,0)
[    1.082286] CPU: 1 PID: 1 Comm: swapper/0 Not tainted 3.10.0-862.11.6.el7.x86_64 #1
[    1.085033] Hardware name: Fedora Project OpenStack Nova, BIOS 0.5.1 01/01/2011
[    1.087639] Call Trace:
[    1.088800]  [<ffffffff871135d4>] dump_stack+0x19/0x1b
[    1.090453]  [<ffffffff8710d11f>] panic+0xe8/0x21f
[    1.091982]  [<ffffffff8776c761>] mount_block_root+0x291/0x2a0
[    1.093704]  [<ffffffff8776c7c3>] mount_root+0x53/0x56
[    1.095394]  [<ffffffff8776c902>] prepare_namespace+0x13c/0x174
[    1.097281]  [<ffffffff8776c3df>] kernel_init_freeable+0x1f8/0x21f
[    1.099244]  [<ffffffff8776bb1f>] ? initcall_blacklist+0xb0/0xb0
[    1.101131]  [<ffffffff87101bc0>] ? rest_init+0x80/0x80
[    1.102813]  [<ffffffff87101bce>] kernel_init+0xe/0xf0
[    1.104497]  [<ffffffff871255f7>] ret_from_fork_nospec_begin+0x21/0x21
[    1.106367]  [<ffffffff87101bc0>] ? rest_init+0x80/0x80
[    1.107997] Kernel Offset: 0x5a00000 from 0xffffffff81000000 (relocation range:0xffffffff80000000-0xffffffffbfffffff)
```

Loki kertoo, ettei instanssi pystynyt käynnistymään, koska rootia ei löydy: "Kernel panic - not syncing: VFS: Unable to mount root fs onunknown-block(0,0)". Korjauksena on käyttää aiempaa, toimivaa kerneliä. Koska et voi käynnistää palvelinta, korjaus täytyy tehdä volyymiin (boot-tiedostot) toista instanssia käyttäen.

### Pääsy estetty { #access-denied }

Ongelma voi olla niinkin yksinkertainen kuin:

```sh
$ ssh cloud-user@<floating-ip>
cloud-user@<floating-ip>: Permission denied (publickey,gssapi-keyex,gssapi-with-mic).
```

## Kuinka korjata ongelma, nova rescue { #how-to-fix-the-issue-nova-rescue }

Huomaa, että ongelman voi korjata monella tavalla; tämä UKK näyttää yhden tavan ratkaista tällaisia ongelmia. Samalla kun voit muokata Grubin käynnistysparametreja, rootin single-tilan pääsy on oletuksena estetty tietoturvasyistä. Pelastustoimenpide etenee seuraavasti:

1. Sinulla tulee olla asennettuna [OpenStackin komentorivityökalut](../../cloud/pouta/install-client.md). Lisäksi sinun pitää kirjautua; katso viite [Configure your terminal environment for OpenStack](../../cloud/pouta/install-client.md#configure-your-terminal-environment-for-openstack).

1. Hae palvelimen ID ja tallenna se ympäristömuuttujaan nimeltä `INSTANCE_UUID`:

	```sh
	$ openstack server list
	+--------------------------------------+-----------+--------+----------------------------+-------+----------------+
	| ID                                   | Name      | Status | Networks                   | Image | Flavor         |
	+--------------------------------------+-----------+--------+----------------------------+-------+----------------+
	| 55555566-ffff-4a52-5735-356251902325 | comp1     | ACTIVE | net=192.168.211.211        |       | standard.small |
	+--------------------------------------+-----------+--------+----------------------------+-------+----------------+

	```

1. Hae levykuvan ID. Voit tallentaa sen ympäristömuuttujaan `IMAGE_UUID`. Käytä samaa levykuvaa kuin instanssissasi: (ID voi poiketa alla olevasta esimerkistä)

	```sh
	$ openstack image list
	+--------------------------------------+----------------------+--------+
    | ID                                   | Name                 | Status |
	+--------------------------------------+----------------------+--------+
	| 56b70226-0c52-48c6-973f-3f726b5e7dc0 | CentOS-7             | active |
	| 2d20266d-43f7-499e-b6e6-090b09416b16 | CentOS-7-Cuda        | active |
	| c80adfec-05a8-4c42-8922-4bccdf90df40 | CentOS-8-Stream      | active |
	| 2ca237c5-bd0a-4469-ae9f-20878dd288a9 | Fedora Cloud Base 31 | active |
	| ee19819d-17d5-4f71-ac38-e024d046eb6a | Ubuntu-18.04         | active |
	| 668d235f-e6e4-421d-964c-0016f9560206 | Ubuntu-20.04         | active |
	| aea0bf58-85fb-4f9c-b2ea-ffa6c7a07c02 | Ubuntu-22.04         | active |
	| 3a9aad67-0f9c-4493-b574-17fe28d40afc | cirros               | active |
	+--------------------------------------+----------------------+--------+
	```

1. Sammuta instanssi:

	```sh
	openstack server stop $INSTANCE_UUID
	```

1. Varmista, että VM on pysäytetty:
	
	```sh
	openstack server list
	```

	Tilan pitäisi olla `SHUTOFF`

1. Voit nyt käynnistää instanssin pelastustilan:

	```sh
	openstack server rescue --image $IMAGE_UUID $INSTANCE_UUID
	```

1. Varmista, että instanssi on rescue-tilassa:

	```sh
	openstack server list
	```

	Tilan pitäisi olla `RESCUE`

## Yhteyden muodostaminen { #connecting }

### SSH:n käyttö { #using-ssh }

Pelastuskuva perii samat SSH-avaimet, jotka on määritetty pelastamassasi VM:ssä, joten sinun pitäisi pystyä yhdistämään instanssiin samoilla käyttäjillä ja IP-osoitteella kuin normaalistikin.

```sh
ssh <default-user>@<floating-ip>
```

Saat varoituksen: `WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!`. Tämä liittyy niin sanottuihin `host keys` -avaimiin. Ne tallennetaan VM:n levylle ja muuttuvat, koska käynnistät eri levyltä. Korjaa poistamalla instanssisi IP-osoitetta vastaava rivi tiedostosta `~/.ssh/known_hosts`. Vaihtoehtoisesti voit suorittaa seuraavan komennon:

```sh
ssh-keygen -f "~/.ssh/known_hosts" -R "$INSTANCE_IP"
```

### Poutan verkkokonsolin käyttäminen (Cirrosin kanssa) { #using-poutas-web-console-with-cirros }

Joissakin tapauksissa, kuten yksityisen SSH-avaimen kadotessa, sinun on käytettävä Poutan verkkokonsolia. Jotta tämä toimii, valitse yllä kohdassa 3 kuva **Cirros**.

Kirjaudu Poutan web-käyttöliittymään: <https://pouta.csc.fi>. Etsi instanssisi ja napsauta `console`.

![Web console](/img/pouta-web-console.png)

Käyttäjätunnus ja salasana tulostuvat konsolin tekstiin kirjautumisruudun yläpuolelle.

!!! Warning "Cirros"
    Cirros-levykuva on pieni Linux-jakelu, jossa on rajallinen ohjelmistotuki ja tietoturvapäivitykset. Sitä tulisi käyttää vain pelastustoimiin, kun normaali SSH-yhteys ei ole mahdollinen.

	Cirros ei tue XFS-tiedostojärjestelmää, jota Almalinux käyttää.

## Liitä levy { #mount-the-disk }

1. Tarkista, mitä volyymeja on. Jos sinulla ei ole muita liitettyjä volyymeja, näkymä näyttää suunnilleen tältä:

	```sh
	$ lsblk
	NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
	vda     253:0    0  3.5G  0 disk
	├─vda1  253:1    0  2.5G  0 part /
	├─vda14 253:14   0    4M  0 part
	├─vda15 253:15   0  106M  0 part
	└─vda16 259:0    0  913M  0 part
	vdb     253:16   0   80G  0 disk
	├─vdb1  253:17   0   79G  0 part
	├─vdb14 253:30   0    4M  0 part
	├─vdb15 253:31   0  106M  0 part /boot/efi
	└─vdb16 259:1    0  913M  0 part /boot
	```

1. Liitä nyt `vdb1` hakemistoon `/tmp/mnt` ja siirry siihen:

	```sh
	$ sudo mkdir -p /tmp/mnt
	$ sudo mount /dev/vdb1 /tmp/mnt/
	```

## Muokkaa käynnistyslataajaa (Grub) { #edit-bootloader-grub }

Joskus ongelma johtuu viallisesta kernelistä. Voit muokata Grubia näyttämään käynnistysvalikon koneen käynnistyessä.

1. Tunnista `boot`-osio aiemmin ajetun `lsblk`-komennon tulosteesta.

1. Tässä esimerkissä `boot`-osio on `/dev/vdb16`. Aja nämä komennot tarvittavien tiedostojärjestelmien liittämiseksi: (`root`-osio on jo liitetty. Katso kohta [above](#mount-the-disk))

	```sh
	sudo mount /dev/vdb16 /tmp/mnt/boot
	sudo mount --bind /dev /tmp/mnt/dev
	sudo mount --bind /sys /tmp/mnt/sys
	sudo mount --bind /proc /tmp/mnt/proc
	```

1. Seuraavaksi muokataan grubbia. Muokattavat tiedostot ovat hieman erilaisia `Almalinux`- ja `Ubuntu`-järjestelmissä:

	#### Almalinux { #almalinux }

	```sh
	sudo vi /tmp/mnt/etc/default/grub
	```

	Muuta `GRUB_TIMEOUT` arvoon `15` (esimerkiksi). Tallenna ja poistu.

	#### Ubuntu { #ubuntu }

	```sh
	sudo vi /tmp/mnt/etc/default/grub.d/50-cloudimg-settings.cfg
	```

	Muuta `GRUB_TIMEOUT` arvoon `15` (esimerkiksi). Tallenna ja poistu.

	```sh
	sudo vi /tmp/mnt/etc/default/grub
	```

	Muuta `GRUB_TIMEOUT_STYLE` arvoon `menu`. Tallenna ja poistu.

1. Päivitetään nyt grub tekemiemme muutosten mukaiseksi. Aja nämä komennot:

	#### Almalinux { #almalinux }

	```sh
	sudo chroot /tmp/mnt
	sudo grub2-mkconfig -o /boot/grub2/grub.cfg
	```

	#### Ubuntu { #ubuntu }

	```sh
	sudo chroot /tmp/mnt
	update-grub
	```

Nyt voit poistua VM:stä ja perua rescue-tilan noudattamalla ohjetta [here](#get-out-of-rescue)

Kun VM käynnistyy, näet käynnistysvalikon ja voit valita toisen kernelin.

## Käytä `chroot`-komentoa vaihtamaan `/`-hakemistoa { #use-chroot-to-change-the-folder }

Jos instanssissasi on ongelmia rikkinäisten pakettien tai ajureiden vuoksi, voit siirtyä alkuperäiseen ympäristöösi ja korjata ongelmat seuraavilla komennoilla:

```sh
$ sudo mv /tmp/mnt/etc/resolv.conf{,.bak}
$ sudo cp /etc/resolv.conf /tmp/mnt/etc/resolv.conf
$ sudo chroot /tmp/mnt
```

`chroot` on nyt vaihtanut juurihakemiston `/` polkuun `/tmp/mnt/` (VM:si levyosio). Voit tehdä tarvittavat korjaukset, kuten poistaa tai asentaa paketteja uudelleen.

## Poistu pelastustilasta { #get-out-of-rescue }

1. Kirjaudu ulos instansseista ja aja `unrescue` instanssille:

	```sh
	openstack server unrescue $INSTANCE_UUID
	```

1. On suositeltavaa varmistaa, että uudelleenkäynnistys toimii kernelin uudelleenasennuksen jälkeen:

	```sh
	ssh <default-user>@<floating-ip> reboot
	```

    odota käynnistymistä ja muodosta SSH-yhteys uudelleen:

	```sh
	ssh <default-user>@<floating-ip>
	```

    Sen pitäisi toimia kuten ennen häiriötä.

## Jos instanssisi käynnistyy käynnistettävältä volyymiltä { #if-your-instance-boot-from-a-bootable-volume }

Jos olet tässä tilanteessa:

```
$ openstack server list
+--------------------------------------+-------------------+--------+------------------------------------------------+--------------------------+-----------------+
| ID                                   | Name              | Status | Networks                                       | Image                    | Flavor          |
+--------------------------------------+-------------------+--------+------------------------------------------------+--------------------------+-----------------+
| 8bbffd1b-99b2-494a-9501-890db20fc2a7 | machine           | ACTIVE | project_200xxxx=192.168.1.0, 123.45.67.89      | N/A (booted from volume) | standard.small  |
```

Voit käynnistää uuden koneen ja liittää volyymin muokataksesi tiedostoja.

!!! Warning  
    Ennen kuin poistat koneen, varmista, ettei volyymi poistu automaattisesti. Voit tarkistaa tämän ajamalla komennon:

	```sh
	$ openstack server show $INSTANCE_UUID | grep 'volumes_attached'

      volumes_attached   | delete_on_termination='False', id='6183d89e-59ac-4b25-b2d5-ef802fd5ef82'
	```

1. Poista volyymiltä käynnistyvä kone

    ```sh
    $ openstack server delete $INSTANCE_UUID
    ```

1. Luo uusi kone (käynnistys levykuvasta) ja liitä volyymi

1. Liitä kelluva IP-osoite (Floating IP) ja yhdistä siihen

1. Ota SSH-yhteys uuteen koneeseen ja tunnista volyymi. vdb1 on todennäköisesti etsimäsi osio.

    ```sh
    $ lsblk

    NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
    vda     253:0    0   80G  0 disk
    ├─vda1  253:1    0   79G  0 part /
    ├─vda14 253:14   0    4M  0 part
    ├─vda15 253:15   0  106M  0 part /boot/efi
    └─vda16 259:0    0  913M  0 part /boot
    vdb     253:16   0   20G  0 disk
    ├─vdb1  253:17   0   19G  0 part
    ├─vdb14 253:30   0    4M  0 part
    ├─vdb15 253:31   0  106M  0 part
    └─vdb16 259:1    0  913M  0 part
    ```

1. Luo liitoskohta ja liitä osio
   
	```sh
	$ sudo mkdir -p /tmp/mnt
	$ sudo mount /dev/vdb1 /tmp/mnt/
	```

1. Voit nyt muokata tarvitsemiasi tiedostoja hakemistossa `/tmp/mnt`

Kun olet valmis, voit yksinkertaisesti sammuttaa virtuaalikoneen, irrottaa volyymin ja käynnistää uuden koneen käynnistettävällä volyymilla.