# Multi-attach Cinder -levyt {#multi-attach-cinder-volumes}

!!! varoitus    
    Oletusarvoisesti kiintiö on asetettu 0:ksi, sinun tulee pyytää sitä lähettämällä sähköpostia osoitteeseen servicedesk@csc.fi

On mahdollista liittää ja liittää sama _cinder_ -levy useampaan kuin yhteen virtuaalikoneeseen samanaikaisesti. Tämä tarkoittaa, että kukin virtuaalikone voi lukea ja kirjoittaa samaan lohkolaitteeseen. Tämä on samanlaista kuin mitä SAN mahdollistaa.

![Moniliitäntä](../img/multi-attach.drawio.svg)

Tällä ominaisuudella on useita etuja ja haittoja. Toisaalta se mahdollistaa tiedostojen jakamisen virtuaalikoneiden kesken ilman mitään välikäsiä, joita tarvitaan ratkaisuissa kuten `NFS` tai `GlusterFS`. Tämä vähentää tarvittavien virtuaalikoneiden määrää, jolloin ylläpitoa on vähemmän ja yksittäisiä virhekohta ei ole niin paljon. Toisaalta on välttämätöntä käyttää niin kutsuttua [klusteroitua tiedostojärjestelmää](https://en.wikipedia.org/wiki/Clustered_file_system#SHARED-DISK) kuten [Oracle Cluster File System 2 (ocfs2)](https://en.wikipedia.org/wiki/OCFS2) tai Red Hat [Global File System (GFS2)](https://en.wikipedia.org/wiki/GFS2). Näissä järjestelmissä tarvitaan klusteri yhteydessä olevia demoneita, jotka koordinoivat tiedostojen luku- ja kirjoitusoperaatioita. Muut tiedostojärjestelmät kuten **ext4** tai **xfs** eivät tue tätä käyttötapausta ja niiden käyttö voi johtaa lukuvirheisiin tai jopa tietojen korruptoitumiseen, niiden käyttöä ei suositella. Kukin virtuaalikone käyttää demoni kopion eikä ole isäntädemonia vaan järjestelmä perustuu äänestykseen. Valinta kahden tiedostojärjestelmän välillä riippuu käyttötapauksesta ja käytettävistä toimittajien mieltymyksistä. Testeissämme GFS2 näyttää olevan sopivampi Redhat-pohjaisille järjestelmille ja OCFS2 Debianille, mutta kokemuksesi saattaa vaihdella.

!!! Varoitus
    Näiden tiedostojärjestelmien konfigurointi, ylläpito ja käyttö eivät ole **triviaali tehtävä**. Alla olevat oppaat ovat **lähtökohta** eivätkä kata kaikkia mahdollisuuksia. Laajemman tiedon saamiseksi tarkista alkuperäinen dokumentaatio.

## Luodaan ja liitetään levy {#create-and-attach-a-volume}

!!! Tieto "kiintiö"
    Varmista, että sinulla on saatavilla olevaa kiintiötä tämän tyyppiselle levylle.

### WebUI

1. Mene [Levyjen sivulle](https://pouta.csc.fi/dashboard/project/volumes/) Poutassa.

2. Klikkaa "+Luo Levy"

3. Luo levy kuten tekisit normaalistikin jokaiselle **Tyypille**. Aseta **Levy Nimi** ja **Koko (GiB)** haluamallasi tavalla.

4. Vaihda **Tyyppi** `standard.multiattach`.

5. Klikkaa "Luo Levy".

![Luo Moniliitäntä Levy](../img/create-volume-multiattach.png)

!!! Varoitus "ei tueta"
    Et voi liittää levyä useaan virtuaalikoneeseen verkkokäyttöliittymästä, voit vain tarkistaa sen tilan. Voit liittää levyn useaan virtuaalikoneeseen vain komentoriviltä (CLI).

### CLI

Ennen tämän tekemistä, sinun täytyy [asentaa openstack-asiakas](install-client.md):

1. Luo moniliitäntälevy:

    ```sh
    openstack volume create --size <size_in_GB> --type standard.multiattach <volume_name>
    ```
    Sinun täytyy korvata `<volume_name>` haluamallasi nimen volyymille, ja `<size_in_GB>` haluamallasi gigatavujen määrällä, jonka haluat volyymille.

2. Liitä levy VM-solmulle:

    ```sh
    openstack --os-compute-api-version 2.60 server add volume "<VM_nimi>" <volume_name>
    ```
    Sinun täytyy korvata `<volume_name>` luomasi levyn nimellä edellisessä vaiheessa ja `<VM_nimi>` VM-solmun nimellä. Kun teet tämän VM:den klusterille, sinun täytyy suorittaa komento kerran per VM.

## GFS2 esimerkkinä {#gfs2-as-an-example}

Global file system tai (GFS2 lyhyesti) on tiedostojärjestelmä, jota Red Hat parhaillaan kehittää. Se käyttää [dlm](https://en.wikipedia.org/wiki/Distributed_lock_manager) tiedostojärjestelmäoperaatioiden koordinoimiseksi klusterin solmujen välillä. Varsinaiset tiedot luetaan ja kirjoitetaan suoraan jaetulle lohkolaitteelle.

!!! Varoitus
    GFS2 tukee jopa 16 solmua yhdistettynä samaan levyyn. 

![GFS2 DLM:llä](../img/GFS2.drawio.svg)

### GFS2 ansible asennus

Olemme kirjoittaneet pienen ansible [cinder-multiattach](https://github.com/lvarin/cinder-multiattach/) playbookin, joka asentaa solmuista koostuvan klusterin ja niihin jaetun GFS2 tiedostojärjestelmän. Playbook on tarkoitettu oppaaksi ja esittelyksi, se ei ole tuotantokäyttöön valmis. Esimerkiksi on olemassa manuaalinen vaihe, liitä levy joka solmussa. Ansible playbook luo klusterin VM:stä ja asentaa pyydetyn tiedostojärjestelmän niihin. Lopputuloksena on sama levy asennettuna joka VM:ssa. Nopean aloituksen komennot ovat nämä:  

```sh
$> source ~/Downloads/project_XXXXXXX-openrc.sh
Please enter your OpenStack Password for project project_XXXXXXX as user YYYYYYYY: 

$> ansible-playbook main.yml -e fs='gfs2' -e csc_username='johndoe' -e csc_password='easyaccess'

$> for i in $(seq 1 16);
do
    openstack --os-compute-api-version 2.60 server add volume "cinder-gfs2-$i" multi-attach-test-gfs2
done

$> ansible-playbook main.yml -e fs='gfs2'
```

*`csc_username` ja `csc_password` voidaan myös lisätä tiedostoon `all.yaml`*  
*Se voi olla [robottitili](../../accounts/how-to-create-new-user-account.md#getting-a-machine-to-machine-robot-account)*

Ansible täytyy suorittaa kahdesti johtuen bugista `openstack.cloud.server_volume`, joka pystyy liittämään levyn vain yhteen virtuaalikoneeseen ja epäonnistuu muiden kanssa.

Jos sinulla on jo VM-klusteri tai haluat luoda ne manuaalisesti, on silti mahdollista käyttää `gfs2` ansible roolia. Vaiheet ovat yksinkertaiset:

1. Luo ja liitä levy. Katso manuaalista [Luo ja liitä levy](#create-and-attach-a-volume) yllä.

2. Luo standardi Ansible -inventaario, kuten tämä:

    ```ini
    [all]
    <VM_nimi> ansible_host=192.168.1.XXX ansible_user=<user>
    # ...
    [all:vars]
    ansible_ssh_common_args='-J <jumphost>'
    ```

    Esimerkin yllä sinun tulisi korvata `<VM_nimi>` virtuaalikoneen nimellä, IP `192.168.1.XXX` tulee olla oikea IP-osoite ja lopuksi `<user>` korvataan asianmukaisella käyttäjänimellä. Sinun täytyy lisätä yksi rivi per virtuaalikone, jonka haluat sisällyttää klusteriin. Lopuksi, jos käytät kyynärisolmua (Jump Host), sinun on korvattava `<jumphost>` sen yhteystiedoilla, kuten `ubuntu@177.51.170.99`

3. Luo playbook, kuten tämä:

    ```yaml
    ---

    - name: Configure VMs
      hosts: all
      gather_facts: true
      become: true
      roles:
        - role: hosts
        - role: gfs2
    ```

    Se suorittaa kaksi roolia: `hosts` luo `/etc/hosts` tiedoston jokaisessa VM:ssä IP-osoitteilla ja nimillä jokaiselle VM:lle. `gfs2` rooli asentaa ja konfiguroi klusterin.

4. Suorita se:

    ```sh
    $> ansible-playbook main-gfs2.yml -i inventory.ini
    ```

### GFS2 manuaalinen asennus

Jotta voit asentaa GFS2, sinun täytyy noudattaa muutamia vaiheita:

1. Asenna VM solmut. Tässä vaiheessa ei ole erityistä huomioitavaa, kunhan varmistat, että solmut voivat nähdä toisensa verkossa (se on oletusasetuksena VM-soluissa, jotka on luotu samassa Pouta-projektissa) ja että ne on asennettu samalla jakeluversiolla. Olemme testanneet tämän `AlmaLinux-9`-versiolla, mutta muut jakelut ja versiot saattavat myös toimia, mutta niitä emme ole testanneet.

2. Luo ja liitä levy. Katso manuaalista [Luo ja liitä levy](#create-and-attach-a-volume) yllä.

3. AlmaLinuxin ja muiden RedHat-pohjaisten jakeluiden kohdalla sinun täytyy vain ottaa käyttöön kaksi hallintaryhmää ja asentaa muutama paketti **jokaisella solmulla:**

    ```sh
    $> dnf config-manager --enable  highavailability resilientstorage
    $> dnf install pacemaker corosync pcs dlm gfs2-utils lvm2-lockd
    ```

#### Klusterin asennus
!!! varoitus "root käyttäjä"
    Seuraavat komennot suoritetaan root-käyttäjänä  
    Kerrotaan koko opetusohjelman ajan, jos komennot täytyy suorittaa yhdellä tai jokaisella solmulla.

1. Suorita seuraavat komennot **jokaisella solmulla:**

    ```sh
    $> systemctl start pcsd.service
    $> systemctl enable pcsd.service
    ```

1. Kun asennat `pacemaker`-ohjelman, se luo käyttäjän nimeltä `hacluster`. Sinun täytyy asettaa tälle käyttäjälle salasana:
   
    ```sh
    $> passwd hacluster
    ```

1. Varmista, että jokaisen solmun **domain nimi** voidaan ratkaista jokaisessa muussa solmussa. Poutassa, yksinkertaisin tapa on käyttää [ /etc/hosts ](https://en.wikipedia.org/wiki/Hosts_(file)), jossa jokaisella isännällä on rivi, joka on samankaltainen kuin:

    ```sh
    <ip> <vm_nimi>
    ```

1. Suorita seuraavat komennot **vain yhdellä solmulla**:

    ```sh
    $> pcs host auth node1 node2 node3 ...
    Username: hacluster
    Password: *******
    $> pcs cluster setup <cluster_nimi> node1 node2 node3 ...
    $> pcs cluster start --all
    ```

1. Voit tarkistaa tilan suorittamalla komennot:

    ```sh
    $> pcs cluster status
    $> pcs status corosync
    ```

Oletusarvoisesti `corosync` ja `pacemaker` palvelut on poistettu käytöstä:

    $> pcs status
    Daemon Status:
      corosync: active/disabled
      pacemaker: active/disabled
      pcsd: active/enabled

Pacemaker-dokumentointien mukaan:

    vaativat manuaalista klusteripalveluiden aloittamista antaa sinulle mahdollisuuden
    tehdä post-mortem tutkimus solmun virheestä
    ennen kuin se palautetaan klusteriin.

Mikä tarkoittaa, jos solmu kaatuu ja käynnistyy uudelleen, sinun täytyy suorittaa komento `pcs cluster start [ <NODENAME> | --all]` aloittaaksesi klusteri siinä.  
Voit ottaa ne käyttöön, jos haluat käyttää `pcs`:

    $> pcs cluster enable [<NODENAME> | --all]
    

#### Fencing asennus
!!! varoitus "root käyttäjä"
    Seuraavat komennot suoritetaan root-käyttäjänä.  
    Kerrotaan koko opetusohjelman ajan, jos komennot täytyy suorittaa yhdellä tai jokaisella solmulla.

1. Suorita seuraavat komennot **jokaisella solmulla:**

    ```sh
    $> setenforce 0
    $> sed -i.bak "s/SELINUX=enforcing/SELINUX=permissive/g" /etc/selinux/config
    $> dnf install -y fence-agents-openstack pip
    $> pip install python-openstackclient python-novaclient
    ```

1. Koska asennamme `python-openstackclient`-ohjelman root-käyttäjän avulla, sinun täytyy lisätä `/usr/local/bin` PATH:iin:

    ```sh
    $> vim ~/.bashrc
    export PATH=/usr/local/bin:$PATH
    ```

1. Luo kansio nimeltä `openstack` hakemistoon `/etc`. Luo sitten tiedosto nimeltä `clouds.yaml` hakemistossa `/etc/openstack`. YAML-tiedosto tulee olla kuten:

    ```yaml
    clouds:
      ha-esimerkki:
        auth:
          auth_url: https://pouta.csc.fi:5001/v3
          project_name: project_xxxxxxx
          username: <username>
          password: <password>
          user_domain_name: Default
          project_domain_name: Default
    <. . . lisäasetukset . . .>
      region_name: regionOne
      verify: False
    ```

1. Suorita seuraavat komennot **vain yhdellä solmulla:**

    ```sh
    $> pcs property set stonith-enabled=true
    ```

1. Tarkista arvo:
   
    ```sh
    $> pcs property
    ```

1. Luo fencing HA-klusterille. Ensin sinun täytyy määrittää UUID jokaiselle solmulle klusterissasi. Voit suorittaa komennon:
   
    ```sh
    $> openstack server list
    ```

    Sitten:

    ```
    $> pcs stonith create <fence_nimi> fence_openstack pcmk_host_map="node1:node1_UUID;node2:node2_UUID;node3:node3_UUID" power_timeout="240" pcmk_reboot_timeout="480" pcmk_reboot_retries="4" cloud="ha-esimerkki"
    ```
    Korvaa `cloud="ha-esimerkki"` pilven nimellä, jonka määrittelit `clouds.yaml` tiedostossa.

1. Voit nähdä käytettävissä olevat vaihtoehdot seuraavalla komennolla:

    ```sh
    $> pcs stonith describe fence_openstack
    ```

1. Voit testata fencingia suorittamalla nämä komennot:
   
    ```sh
    $> pcs stonith fence node2
    $> pcs status
    $> pcs cluster start node2
    ```

!!! tieto "Vihje"  
    Jos haluat käynnistää (tai käynnistää uudelleen) aidan, voit käyttää tätä komentoa:
    ```sh
    $> pcs stonith cleanup <fence_nimi>
    ```
    Kätevä, jos esimerkiksi sovellat uutta `clouds.yaml` asetusta.


#### GFS2 asennus
!!! varoitus "root käyttäjä"
    Seuraavat komennot suoritetaan root-käyttäjänä.  
    Kerrotaan koko opetusohjelman ajan, jos komennot täytyy suorittaa yhdellä tai jokaisella solmulla.

1. Suorita seuraava komento **jokaisella solmulla:**

    ```sh
    $> sed -i.bak "s/# use_lvmlockd = 0/use_lvmlockd = 1/g" /etc/lvm/lvm.conf
    ```

1. Suorita seuraavat komennot **vain yhdellä solmulla:**

    ```sh
    $> pcs property set no-quorum-policy=freeze
    ```

1. Aseta dlm (Distributed Lock Manager) resurssi:

    ```sh
    $> pcs resource create dlm --group locking ocf:pacemaker:controld op monitor interval=30s on-fail=fence
    ```

1. Kopioi resurssi muille solmuille:

    ```sh
    $> pcs resource clone locking interleave=true
    ```

1. Aseta lvmlockd resursseja varten sisällytettäväksi locking resurssiryhmään:

    ```sh
    $> pcs resource create lvmlockd --group locking ocf:heartbeat:lvmlockd op monitor interval=30s on-fail=fence
    ```

1. Tarkista tila:

    ```sh
    $> pcs status --full
    ```

1. Edelleen **vain yhdellä solmulla**, luo yksi jaettu volyymiryhmä:

    ```sh
    $> vgcreate --shared shared_vg1 /dev/vdb
    ```

1. **Muille solmuille**, lisää jaettu laite laitetiedostoon:

    ```sh
    $> lvmdevices --adddev /dev/vdb
    ```

1. Käynnistä luontihallinta:

    ```sh
    $> vgchange --lockstart shared_vg1
    ```

1. **Yhdellä solmulla** suorita:

    ```sh
    $> lvcreate --activate sy -L <size>G -n shared_lv1 shared_vg1
    $> mkfs.gfs2 -j <number_of_nodes> -p lock_dlm -t ClusterName:FSName /dev/shared_vg1/shared_lv1
    ```
    ClusterName on klusterin nimi (voit hakea tiedon komennolla `pcs status`)  
    FSName on tiedostojärjestelmän nimi (eli: gfs2-demo)

1. Luo LVM-activate resurssi, jotta logiikkamääritys aktivoidaan kaikilla solmuilla:

    ```sh
    $> pcs resource create sharedlv1 --group shared_vg1 ocf:heartbeat:LVM-activate lvname=shared_lv1 vgname=shared_vg1 \
        activation_mode=shared vg_access_mode=lvmlockd
    ```

1. Kopioi uusi resurssiryhmä:

    ```sh
    $> pcs resource clone shared_vg1 interleave=true
    ```

1. Määritä ordering constraints varmistaa, että locking resurssiryhmää, joka sisältää dlm:n ja lvmlockd:n, käynnistyy ensin:

    ```sh
    $> pcs constraint order start locking-clone then shared_vg1-clone
    ```

1. Määritä sijainti rajoittaa varmistaakseen, että vg1-resurssiryhmät käynnistyvät samalla solmulla kuin locking resurssiryhmät:

    ```sh
    $> pcs constraint colocation add shared_vg1-clone with locking-clone
    ```

1. Varmista solmujen klusterissa, että logiikkamääritys on aktiivinen. Saattaa olla muutaman sekunnin viive ennen tätä:

    ```sh
    $> lvs
        LV         VG         Attr       LSize   Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
        shared_lv1 shared_vg1 -wi-a----- <size>g
    ```

1. Luo tiedostojärjestelmäresurssi, jotta GFS2 tiedostojärjestelmä asennetaan automaattisesti.  
   Älä lisää sitä tiedostoon /etc/fstab, koska se hallitaan Pacemaker-klusteriresurssina.:

    ```sh
    $> pcs resource create sharedfs1 --group shared_vg1 ocf:heartbeat:Filesystem device="/dev/shared_vg1/shared_lv1" \
        directory="/mnt/gfs" fstype="gfs2" options=noatime op monitor interval=10s on-fail=fence
    ```

1. Voit tarkistaa, onko GFS2 tiedostojärjestelmä asennettu:

    ```sh
    $> mount | grep gfs2
    $> pcs status --full
    ```

### GFS2 UKK {#gfs2-faq}

* **Kuinka lisätä lisää solmuja?**

    On mahdollista lisätä uusia solmuja GFS2-klusteriin. Tuettu **raja** on **16** solmua.

    Ensin sinun täytyy varmistaa, että journal-päivityksiä on tarpeeksi. Käytä `gfs2_edit`-kohtaa saadaksesi journalien kokonaismäärän:

    ```sh
    sudo gfs2_edit -p jindex /dev/vdb | grep journal
    ```

    Jos se ei ole riittävä, voit helposti lisätä niitä `gfs2_jadd`-komennolla: 

    ```sh
    $> sudo gfs2_jadd -j 1 /mnt
    Filesystem: /mnt
    Old journals: 15
    New journals: 16
    ```

    Toiseksi, luo uusi solmu, asenna vaadittu ohjelmisto ja liitä levy openstack API:n avulla. Prosessi on kuvattu yllä.

    Sitten sinun täytyy muokata tiedostoa `/etc/corosync/corosync.conf` jokaisessa solmussa ja lisätä kirjaus uudelle:

    ```json
    node {
     ring0_addr: cinder-gfs2-16
     nodeid: 16
    }
    ```

    Kun tiedosto on päivitetty, sinun täytyy pysäyttää asennus ja käynnistää dlm ja corosync-daemonit uudelleen jokaisessa solmussa klusterissa.

    Lopuksi, sinun täytyy vain asentaa levy:

    ```sh
    $> pcs resource create sharedfs1 --group shared_vg1 ocf:heartbeat:Filesystem device="/dev/shared_vg1/shared_lv1" directory="/mnt/gfs" fstype="gfs2" options=noatime op monitor interval=10s on-fail=fence
    ```

* **Kuinka laajentaa GFS2 levyn kokoa?**

    GFS2-levy on konfiguroitu LVM:n ([Logical Volume Manager](https://en.wikipedia.org/wiki/Logical_volume_management)) avulla, joka parantaa fyysisen tallennustilan hallintaa ja joustavuutta.

    a. Luo uusi multiattah-levy ja liitä se instansseihisi. Tarkista että levy on hyvin liitetty suorittamalla komento `sudo parted -l`

    b. Yhdellä solmulla, lisää uusi levy Volyymiryhmään:

    ```sh
    sudo vgextend VolumeGroupName /dev/vdX
    ```

    c. Edelleen yhdellä solmulla, laajenna Logiikkamääritystä:

    ```sh
    sudo lvextend -l +100%FREE /dev/VolumeGroupName/LogicalVolumeName
    ```

    d. Tarkista, että Logiikkamääritys on laajennettu suorittamalla komento `sudo lvs`

    e. Ennen GFS2 volyymin laajentamista, tarkista muilta solmuilta, että sinulla ei ole virheilmoituksia. Suorita `sudo pvs`. Jos näet jotain tällaista:

    ```
    WARNING: Couldn't find device with uuid JuoyG2-ftdd-U9xm-LLei-VrY7-4GZz-FgC2dr.
    WARNING: VG shared_vg1 is missing PV JuoyG2-ftdd-U9xm-LLei-VrY7-4GZz-FgC2dr (last written to /dev/vdX)
    ```
    Sinun pitää lisätä laite suorittamalla komento:

    ```
    sudo lvmdevices --adddev /dev/vdX
    ```

    Tarkista uudelleen `sudo pvs`-komennolla. Varoitusviestin ei pitäisi ilmestyä.

    f. Jos kaikki on kunnossa, voit kasvattaa GFS2 volyymia kirjoittamalla:

    ```sh
    sudo gfs2_grow <YourGFS2MountVolume>
    ```

    !!! varoitus
        Et voi pienentää GFS2 tiedostojärjestelmää
    
* **Mitä tapahtuu, jos VM irrotetaan?**

    Tämä kattaa kaksi eri käyttötapausta, ajallisen ja/tai odottamattoman katkaisun sekä pysyvän katkaisun.

    Ajallisen ja odottamattoman katkaisun tapauksessa klusterin pitäisi olla kykenevä selviämään tämäntyyppisistä ongelmista automaattisesti. Kun solmu on takaisin-verkossa, sinun täytyy tarkistaa, että kaikki palautui normaaliksi. Joissain tapauksissa automaattinen asennus voi epäonnistua, jos näin käy, asenna levy yllä selitetyllä tavalla.

    Jos se on ajallinen mutta odotettu, kuten ytimen päivittäminen. Irroita levy solmusta ennen solmun uudelleenkäynnistystä. Tätä ei vaadita mutta se on suositeltavaa.

    Pysyvän katkaisun kohdalla, yksi tarvitsee tehdä päinvastainen prosessin lisäämiselle uudelle solmulle. Irroita levy, poista merkintä tälle virtuaalikoneelle `/etc/corosync/corosync.conf` -tiedostosta jokaisesta solmusta ja lopuksi käynnistä daemonit uudelleen jokaisessa solmussa. Tämä täytyy tehdä koska se vaikuttaa klusterin äänestyslaskentaan.

* **Onko mahdollista asentaa solmu vain luku -moodissa?**

    Kyllä, GFS2:lla on "katselutila":

    ```
    spectator
       Asenna tämä tiedostojärjestelmä käyttäen erityistä muoto luku-moodissa. Asennus ei
       käytä tiedostojärjestelmän journaleja. Solmu ei pysty palauttamaan journaleja muille solmuille.

    norecovery
       Synonymi spectator:ille
    ```

    Joten yksinkertaisesti suorita tämä komento:

    ```sh
    $> pcs resource create sharedfs1 --group shared_vg1 ocf:heartbeat:Filesystem device="/dev/shared_vg1/shared_lv1" directory="/mnt/gfs" fstype="gfs2" options=noatime,spectator op monitor interval=10s on-fail=fence
    ```
    `fstype="gfs2"` ei ole tiukasti ottaen välttämätön, koska mount voi havaita tiedostojärjestelmätyypin, mutta se on suositeltavaa vältettävän väärän tiedostojärjestelmän asentamista.
    Tarkista vielä, että asennus meni kuten odotettiin seuraavalla tavalla:

    ```sh
    $ mount | grep /mnt
    /dev/vdb on /mnt type gfs2 (ro,relatime,spectator,rgrplvb)
    ```

### GFS2 Linkit

- [Pacemaker dokumentaatio](https://clusterlabs.org/projects/pacemaker/doc/2.1/Clusters_from_Scratch/html/cluster-setup.html)
- [GFS2 Amazon EBS Moniliitos levyissä](https://aws.amazon.com/blogs/storage/clustered-storage-simplified-gfs2-on-amazon-ebs-multi-attach-enabled-volumes/)
- [Aloitetaan Pacemakerin kanssa](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_high_availability_clusters/assembly_getting-started-with-pacemaker-configuring-and-managing-high-availability-clusters#proc_learning-to-use-pacemaker-getting-started-with-pacemaker)
- [Red Hat Korkean saatavuuden klusterin konfigurointi Red Hat OpenStack alustalla](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_a_red_hat_high_availability_cluster_on_red_hat_openstack_platform/index)
- [GFS2 tiedostojärjestelmät klusterissa](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_gfs2_file_systems/assembly_configuring-gfs2-in-a-cluster-configuring-gfs2-file-systems#proc_configuring-gfs2-in-a-cluster.adoc-configuring-gfs2-cluster)
- [GFS2 tiedostojärjestelmän laajentaminen](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_gfs2_file_systems/assembly_creating-mounting-gfs2-configuring-gfs2-file-systems#proc_growing-gfs2-filesystem-creating-mounting-gfs2)
- [LVM tilavuusryhmien hallinta](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_logical_volumes/managing-lvm-volume-groups_configuring-and-managing-logical-volumes#managing-lvm-volume-groups_configuring-and-managing-logical-volumes)

## OCFS2 toisena esimerkkinä {#ocfs2-as-a-second-example}

[Oracle Cluster File System](https://en.wikipedia.org/wiki/OCFS2) versio 2 on jaettu levytiedostojärjestelmä, jonka on kehittänyt Oracle Corporation ja julkaistu GNU General Public License alla. Samaan aikaan se on erilainen koodipohja, jonka on kehittänyt toinen toimittaja. Lähestymistapa on sama kuin GFS2:

![OCFS2](../img/OCFS2.drawio.svg)

Yksi levy on liitetty klusteriin VM solmuista, mikä mahdollistaa datan luku- ja kirjoitusoperaatiot suoraan ja jokaisessa VM-solmussa on demoni, joka koordinoi luku- ja kirjoitusoperaatioita.

### OCFS2 ansible asennus

Kuten GFS2:n kanssa, Ansible playbook luo klusterin VM:iä ja asentaa pyydetyn tiedostojärjestelmän niille. Lopputuloksena on sama levy asennettuna joka VM:ssä. Se on hyvin samanlainen kuin GFS2:n ohjeet. Pikakäynnistyksen komennot näyttävät tältä:

```sh
$ source ~/Downloads/project_XXXXXXX-openrc.sh
Please enter your OpenStack Password for project project_XXXXXXX as user YYYYYYYY: 

$ ansible-playbook main.yml -e fs='ocfs2'

$ for i in $(seq 1 16);
do
    openstack --os-compute-api-version 2.60 server add volume "cinder-ocfs2-$i" multi-attach-test-ocfs2
done

$ ansible-playbook main.yml -e fs='ocfs2'
```

Ansible täytyy suorittaa kahdesti johtuen bugista `openstack.cloud.server_volume`, joka pystyy liittämään levyn vain yhteen virtuaalikoneeseen ja epäonnistuu muiden kanssa.

Jos sinulla on jo klusteri VM:istä tai haluat luoda ne manuaalisesti, on silti mahdollista käyttää `ocfs2` Ansible roolia. Vaiheet ovat yksinkertaiset:

1. Luo ja liitä levy. Katso manuaalista [Luo ja liitä levy](#create-and-attach-a-volume) yllä.

1. Luo standardi Ansible -inventaario, tällainen:

    ```ini
    [all]
    <VM_nimi> ansible_host=192.168.1.XXX ansible_user=<user>
    # ...
    [all:vars]
    ansible_ssh_common_args='-J <jumphost>'
    ```

    Esimerkin yllä sinun tulisi korvata `<VM_nimi>` virtuaalikoneen nimellä, IP `192.168.1.XXX` tulee olla oikea IP-osoite ja lopuksi `<user>` korvataan asianmukaisella käyttäjänimellä. Sinun täytyy lisätä yksi rivi per virtuaalikone, jonka haluat sisällyttää klusteriin. Lopuksi, jos käytät kyynärisolmua (Jump Host), sinun on korvattava `<jumphost>` sen yhteystiedoilla, kuten `ubuntu@177.51.170.99`

1. Luo playbook (tässä esimerkissä `main-ocfs2.yml`), kuten tämä:

    ```yaml
    ---

    - name: Configure VMs
      hosts: all
      gather_facts: true
      become: true
      roles:
        - role: hosts
        - role: ocfs2
    ```

    Tämä suorittaa kaksi roolia: `hosts` luo `/etc/hosts` tiedoston jokaisessa VM:ssä IP-osoitteilla ja nimillä jokaiselle VM:lle. `ocfs2` rooli asentaa ja konfiguroi klusterin.

1. Suorita se:

    ```sh
    $ ansible-playbook main-ocfs2.yml -i inventory.ini
    ```

### OCFS2 manuaalinen asennus

Jotta voit asentaa OCFS2, sinun täytyy noudattaa muutamia vaiheita:

1. Asenna VM solmut. Tässä vaiheessa ei ole erityistä huomioitavaa, kunhan varmistat, että solmut voivat nähdä toisensa verkossa (se on oletusasetuksena VM-soluissa, jotka on luotu samassa Pouta-projektissa) ja että ne on asennettu samalla jakeluversiolla. Olemme testanneet tämän `Ubuntu v22.04` ja `AlmaLinux-9`-versioilla, mutta muut jakelut ja versiot saattavat myös toimia, mutta niitä emme ole testanneet. Tämä opas käyttää **Ubuntua** esimerkkinä.  
AlmaLinux vaatii tietyn [Oracle-ytimen](https://support.oracle.com/knowledge/Oracle%20Linux%20and%20Virtualization/1253272_1.html) asennuksen. Lisätietoja [UKK](#ocfs2-faq)

1. Luo ja liitä levy. Katso manuaalista [Luo ja liitä levy](#create-and-attach-a-volume) yllä.

1. Asenna OCFS2 ohjelmisto:

    ```sh
    ocfs2-tools linux-modules-extra-<kernel_version> linux-image-$(uname -r)
    ```
    Olemme testanneet tämän version kanssa `<kernel_version>` == `6.5.0-21-generic`, mutta uudemmat versiot saattavat työskennellä myös tai paremmin.

1. Varmista, että jokaisen solmun domain nimi voidaan ratkaista jokaisessa muussa solmussa. Poutassa, yksinkertaisin tapa on käyttää [ /etc/hosts ](https://en.wikipedia.org/wiki/Hosts_(file)), jossa jokaisella isännällä on rivi, joka on samankaltainen kuin:

    ```sh
    <ip> <vm_nimi>
    ```

1. Ota ocfs2 käyttöön jokaisessa solmussa käyttämällä:

    ```sh
    sudo dpkg-reconfigure ocfs2-tools
    ```

1. Luo tiedostojärjestelmä. Sinun tulee tehdä tämä **vain yhdellä** VM solmujen kohdalla.

    ```sh
    mkfs.ocfs2 -N <numero_instanssia> /dev/vdb
    ```

    Korvaa `<numero_instanssia>` klusterin solmujen lukumäärällä. Kiinnitä huomiota ja varmista, että `/dev/vdb` on oikein levyn nimi. Periaatteessa `vdb` on ensimmäinen liitetty levy