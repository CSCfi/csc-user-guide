
# Kuinka pelastaa instansseja? {#how-to-rescue-instances}

OpenStack tarjoaa pelastustilan virtuaalikoneiden palauttamiseen. Tämä komento antaa mahdollisuuden käynnistää VM eri kuvasta. Tätä voi käyttää, kun virtuaalikone ei käynnisty ytimen paniikin vuoksi, levy on täynnä tai yksinkertaisesti olet menettänyt pääsyn yksityiseen avaimeen. Kun voit käynnistää eri kuvasta, voit liittää nykyisen levysi ja muokata tiedostoja sekä korjata ongelman.

## Oireet {#symptoms}

### Kernel Panic {#kernel-panic}

Tarkista instanssin konsoliloki (verkkokäyttöliittymä: **Instances** > `<your instance>` > **Log**)

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

Loki kertoo, että instanssia ei voitu käynnistää, koska se ei löytänyt juurihakemistoa "Kernel panic - not syncing: VFS: Unable to mount root fs onunknown-block(0,0)". Korjauksena on käyttää aiempaa, toimivaa ydintä. Koska et voi käynnistää palvelinta, sinun on tehtävä korjaus volyymille (käynnistystiedostot) käyttämällä toista instanssia.

### Pääsy estetty

Ongelma voi olla niinkin yksinkertainen kuin:

```sh
$ ssh cloud-user@<floating-ip>
cloud-user@<floating-ip>: Permission denied (publickey,gssapi-keyex,gssapi-with-mic).
```

## Kuinka korjata ongelma, nova rescue {#how-to-fix-the-issue-nova-rescue}

Huomioi, että minkä tahansa ongelman korjaamiseen on aina useita tapoja, tämä FAQ on pääasiassa tarkoitettu näyttämään yksi tapa korjata tällaisia ongelmia. Samalla kun sinulla on mahdollisuus muokata Grub-käynnistysparametreja, juuriyksittäisellä tilalla pääsy on oletuksena poistettu käytöstä turvallisuussyistä. Pelastustoimenpiteen suorittaminen tapahtuu seuraavasti:

1. Sinun täytyy olla asentanut [OpenStack komentorivityökalut](../../cloud/pouta/install-client.md). Sinun täytyy kirjautua sisään ja katsoa [Määritä terminaaliympäristösi OpenStackille](../../cloud/pouta/install-client.md#configure-your-terminal-environment-for-openstack) viitteeksi.

1. Hae palvelimen ID ja tallenna se ympäristömuuttujaan nimeltään: `INSTANCE_UUID`:

	```sh
	$ openstack server list
	+--------------------------------------+-----------+--------+----------------------------+-------+----------------+
	| ID                                   | Name      | Status | Networks                   | Image | Flavor         |
	+--------------------------------------+-----------+--------+----------------------------+-------+----------------+
	| 55555566-ffff-4a52-5735-356251902325 | comp1     | ACTIVE | net=192.168.211.211        |       | standard.small |
	+--------------------------------------+-----------+--------+----------------------------+-------+----------------+

	```

1. Hae kuvan ID. Voit tallentaa ID:n ympäristömuuttujaan `IMAGE_UUID`. Sinun tulisi käyttää samaa kuvaa kuin instanssisi: (ID saattaa vaihdella alla olevassa esimerkissä)

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

1. Varmista, että VM on sammutettu:
	
	```sh
	openstack server list
	```

	Tilan pitäisi olla `SHUTOFF`

1. Voit nyt käynnistää instanssin pelastusmoodissa:

	```sh
	openstack server rescue --image $IMAGE_UUID $INSTANCE_UUID
	```

1. Varmista, että instanssi on pelastusmoodissa:

	```sh
	openstack server list
	```

	Tilan pitäisi olla `RESCUE`

## Yhdistäminen {#connecting}

### Ssh:n käyttäminen {#using-ssh}

Pelastuskuva saa samat SSH-avaimet, jotka on määritetty pelastettavassa VM:ssä, joten sinun pitäisi pystyä ssh:lla yhdistämään instanssiin käyttämällä samoja käyttäjätunnuksia sekä IP-osoitetta kuin normaalisti.

```sh
ssh <default-user>@<floating-ip>
```

Saat tämän varoituksen: `WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!`. Tämä viittaa niin kutsuttuihin `host keys` avaimiin, jotka tallennetaan VM:n levylle ja muuttuvat, koska käynnistät eri levyllä. Korjaa se poistamalla instanssin IP-osoite tiedostosta `~/.ssh/known_hosts`. Vaihtoehtoinen tapa on suorittaa seuraava komento:

```sh
ssh-keygen -f "~/.ssh/known_hosts" -R "$INSTANCE_IP"
```

### Poutan verkkokonsolin käyttäminen (Cirrosilla) {#using-poutas-web-console-with-cirros}

Joissain tapauksissa, kuten silloin, kun olet menettänyt yksityisen SSH-avaimen, sinun täytyy käyttää Poutan verkkokonsolia. Tämän toimiakseen sinun täytyy valita **Cirros** kuva edellisessä vaiheessa 3.

Kirjaudu sisään Poutan verkkokäyttöliittymään: <https://pouta.csc.fi>. Etsi instanssisi ja klikkaa `console`.

![Verkkokonsoli](/img/pouta-web-console.png)

Käyttäjätunnus ja salasana pitäisi olla tulostettu konsolin tekstiin, kirjautumistietojen yläpuolelle.

!!! Warning "Cirros"
    Cirros kuva on pieni Linux-jakelukuva, jossa on rajallinen ohjelmistotuki ja tietoturvapäivitykset. Sitä tulisi käyttää vain pelastustoimintaan, kun normaalinen SSH-yhteys ei ole mahdollinen.

## Levyn liittäminen {#mount-the-disk}

1. Tarkista, mitä levyjä sinulla on. Jos sinulla ei ole muita liitettyjä levyjä, sen pitäisi näyttää tältä:

	```sh
	$ lsblk
	NAME   MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
	vda    253:0    0  10G  0 disk
	└─vda1 253:1    0  10G  0 part
	vdb    253:16   0  80G  0 disk
	└─vdb1 253:17   0  80G  0 part /
	```

1. Nyt haluat liittää `vdb1` hakemistoon `/tmp/mnt` ja mennä siihen hakemistoon:

	```sh
	$ sudo mkdir -p /tmp/mnt
	$ sudo mount /dev/vdb1 /tmp/mnt/
	```

## Käynnistyslataimen (Grub) muuttaminen {#change-bootloader-grub}

1. Ota varmuuskopio grubista:

	```sh
	$ cp /tmp/mnt/boot/grub2/grub.cfg /tmp/mnt/root/grub.cfg.bak-$(date +"%F")
	```

1. Avaa `/tmp/mnt/boot/grub2/grub.cfg` suosikkieditorillasi. Poista ensimmäinen `menuentry` osio.

    *HUOM:* Tämä ei välttämättä ole oikea ratkaisu juuri sinun ongelmaasi. Ensimmäinen menuentry on yleensä uusin ja oletuksena käytettävä ydin.

## `chroot`in käyttäminen `/` kansion muuttamiseen {#use-chroot-to-change-the-folder}

Jos instanssissasi on ongelmia rikkoutuneiden pakettien tai ajureiden vuoksi, voit siirtyä alkuperäiseen ja korjata ongelmat seuraavien komentojen avulla:

```sh
$ sudo mv /tmp/mnt/etc/resolv.conf{,.bak}
$ sudo cp /etc/resolv.conf /tmp/mnt/etc/resolv.conf
$ sudo chroot /tmp/mnt
```

`chroot` on nyt vaihtanut juurikansion `/` hakemistoksi `/tmp/mnt/` (VM:n levyn osio). Voit tehdä minkä tahansa korjauksen tai muutoksen, kuten paketin asennuksen tai poistamisen.

## Poistu pelastustilasta {#get-out-of-rescue}

1. Kirjaudu ulos instansseista ja `unrescue` instanssi:

	```sh
	openstack server unrescue $INSTANCE_UUID
	```

1. Kannattaa tarkistaa, että uudelleenkäynnistys toimii ytimen uudelleenasennuksen jälkeen:

	```sh
	ssh <default-user>@<floating-ip> reboot
	```

    odota, että käynnistyy ja yhdistä ssh:lla uudelleen:

	```sh
	ssh <default-user>@<floating-ip>
	```

    Sen pitäisi toimia kuten ennen tapausta.

## Jos instanssisi käynnistyy käynnistettävästä volyymista {#if-your-instance-boot-from-a-bootable-volume}

Jos olet tässä tapauksessa:

```
$ openstack server list
+--------------------------------------+-------------------+--------+------------------------------------------------+--------------------------+-----------------+
| ID                                   | Name              | Status | Networks                                       | Image                    | Flavor          |
+--------------------------------------+-------------------+--------+------------------------------------------------+--------------------------+-----------------+
| 8bbffd1b-99b2-494a-9501-890db20fc2a7 | machine           | ACTIVE | project_200xxxx=192.168.1.0, 123.45.67.89      | N/A (booted from volume) | standard.small  |
```

Voit käynnistää uuden koneen ja liittää volumyn muokataksesi tiedostoja.

!!! Warning  
    Ennen kuin poistat koneen, varmista, ettei volyymiä poisteta automaattisesti. Voit tarkistaa tämän ajamalla seuraavan komennon:

	```sh
	$ openstack server show $INSTANCE_UUID | grep 'volumes_attached'

      volumes_attached   | delete_on_termination='False', id='6183d89e-59ac-4b25-b2d5-ef802fd5ef82'
	```

1. Poista kone, joka käynnistyy volyymista

    ```sh
    $ openstack server delete $INSTANCE_UUID
    ```

1. Luo uusi kone (käynnistetään kuvasta) ja liitä volyymi

1. Liitä kelluva IP ja yhdistä siihen

1. SSH:lla vastaluotuun koneeseen ja tunnista volyymi. Todennäköisesti vdb1 on etsimäsi osio.

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

1. Luo liitäntäpiste ja liitä osio
   
	```sh
	$ sudo mkdir -p /tmp/mnt
	$ sudo mount /dev/vdb1 /tmp/mnt/
	```

1. Voit nyt muokata tarvitsemiasi tiedostoja `/tmp/mnt`

Kun olet valmis, voit yksinkertaisesti sammuttaa VM:n, irrottaa volyymin ja käynnistää uuden koneen käynnistettävällä volyymilla.
