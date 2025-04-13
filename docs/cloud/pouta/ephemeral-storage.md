# Katoava tallennustila {#ephemeral-storage}

Joillakin Pouta-virtuaalikoneen [mauilla](vm-flavors-and-billing.md) on *katoava tallennustila* juurilevyn lisäksi. Tämä toimii lisätallennustilana
instanssin keston ajan.

!!! Warning "Varoitus"
    Tämä tallennustila ei tallennu instanssin mukana. Tämä tallennustila **ei** tallennu, kun luot kuvan tilannevedoksen. Sitä ei kopioida, kun suoritetaan koon muutoksia tai siirtoja.

On erityisen tärkeää huomata, että io.\* maut perustuvat suuritehoisiin RAID0-asemaryhmiin, jotka eivät tarjoa mitään redundanssia. Io.2.\* maissa tallennus perustuu RAID1-järjestelmiin, mikä tarjoaa enemmän turvallisuutta ja ehkäisee tiedostojen menettämistä.

Katoava tallennustila näkyy virtuaalikoneelle lisälevynä (yleensä /dev/vdb). Valitusta kuvasta ja metatiedoista riippuen virtuaalikonetta luodessa levy saattaa olla jo alustettuna `vfat`-tiedostojärjestelmään ja liitettynä `/mnt`-hakemistoon. Jos tämä sopii käyttötarkoitukseesi, voit alkaa käyttää levyä välittömästi.

Jos tarvitset levyn alustamisen eri tiedostojärjestelmällä (tai jos levyä ei ole alustettu eikä liitetty), voit noudattaa tätä menettelyä:

Varmista ensin, että osio ei ole liitetty:

    sudo umount /dev/vdb

ja ettei `/etc/fstab`-tiedostossa ole tällä levyllä merkintää:

    cat /etc/fstab

Etsi rivi, joka sisältää `/dev/vdb` tai `LABEL=EPHEMERAL`,
ja kommentoi se (lisäämällä `#` rivin alkuun).

Nyt voit jatkaa levyn alustamista ja liittämistä. Alla olevassa esimerkissä käytämme ext4:ää:

    sudo mkfs.ext4 /dev/vdb
    sudo mkdir /mnt/myephdisk
    sudo mount /dev/vdb /mnt/myephdisk

Sinun täytyy myös lisätä merkintä koneen /etc/fstab-tiedostoon varmistaaksesi, että levy liitetään uudelleenkäynnistyksen jälkeen:

    sudo umount /mnt/myephdisk/
    sudo e2label /dev/vdb EPHEMERAL
    sudo bash -c 'echo "LABEL=EPHEMERAL   /mnt/myephdisk   ext4  defaults,nofail 0 2 " >> /etc/fstab'
    sudo mount /mnt/myephdisk

Kun tallennustila on liitetty, sinun täytyy vaihtaa omistajuus, jotta voit lukea ja kirjoittaa dataa siihen.
Seuraavassa komennossa oletamme, että käyttäjänimi on cloud-user.

    sudo chown cloud-user:cloud-user /mnt/myephdisk

Huomaa, että joillakin vanhoilla mauilla (tiny, mini, small, medium, large, fullnode) oli myös katoava levy, joka oli esialustettu ja liitetty automaattisesti.