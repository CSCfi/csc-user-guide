
# Olen määrittänyt SSH-avaimet, mutta kirjautuminen Puhtiin ei toimi tai se kysyy edelleen salasanaa {#i-have-set-up-ssh-keys-but-logging-in-to-puhti-does-not-work-or-still-asks-for-password}

Puhti on tässä käytetty esimerkki. Samat toimenpiteet pätevät myös Mahtiin.

## Tarkista seuraavat {#please-check-the-following}

1. Olet
   [lisännyt SSH-julkisen avaimen MyCSC:hen](../../computing/connecting/ssh-keys.md#adding-public-key-in-mycsc)
   ja se näkyy _SSH PUBLIC KEYS_ osiossa profiilisivullasi. Muita tapoja
   avaimen lataamiseen **ei** tueta.
   * Varmista, että lataamasi avain on oikein muotoiltu. Sen tulee koostua SSH-avain tyypistä, avainsekvenssistä ja valinnaisesta kommentista, kaikki yksittäisillä väleillä erotettuina. Varmista, että lisäät koko SSH-avaimen samalle riville äläkä lisää muuta välilyöntiä kuin tavallisia välilyöntimerkkejä. Jos avain ei ole oikein muotoiltu, näyttöön tulee virheilmoitus. Oikein muotoiltu avain näyttää tältä:
      ```bash
      ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDlapOdeoxNvz/1AZFRjGAPnPj8pzzz3skI+a+yJS5b7 optional-comment
      ```
2. MyCSC:ssä oleva avaimen sormenjälki (alkaa _SHA256:llä_) vastaa paikallisella koneellasi olevaa avainta. **Windowsissa** ladatun avaimen sormenjälki näytetään MobaKeyGenin tai PuTTYgenin _Key_-osiossa. Tarkistaaksesi sormenjäljen **Linuxissa** tai **macOS:ssa**, suorita komento:
   ```bash
   ssh-keygen -l -f <key file>
   ```
   Jos sormenjälki ei vastaa sitä, joka on MyCSC:ssä, et ole lisännyt oikeaa avainta. Tuloste `<key file> is not a public key file` tarkoittaa, että avaimesi on virheellinen. Molemmissa tapauksissa on helpointa luoda uusi avainpari ja lisätä uusi julkinen avain MyCSC:hen.
3. Jos olet tallentanut SSH-avain tiedoston ei-oletus nimeen tai sijaintiin, sinun täytyy kertoa `ssh`-komennolle, mistä avain löytyy. Kun muodostat yhteyttä terminaalista, käytä `-i`-vaihtoehtoa seuraavasti:
   ```bash
   ssh -i /path/to/key/file <username>@puhti.csc.fi
   ```
4. Jos `ssh`-komento edelleen kysyy salasanaa, tarkista tarkkaan, kysytäänkö oikeasti Puhtin salasanaa vai _avaimen komentoa_. Jos olet määrittänyt avaimellesi komennon (**vahvasti suositeltu**), on normaalia, että joudut syöttämään sen, kun muodostat yhteyden. Välttääksesi komentoa, voit määrittää 
   [autentikointivälityksen](../../computing/connecting/ssh-unix.md#authentication-agent), joka voi säilyttää avaimesi muistissa.
5. Olet odottanut vähintään tunnin avaimen lisäämisen jälkeen MyCSC:hen. Tiedonsiirto CSC:n palvelimille vie aikaa ja voi riippua järjestelmän nykyisestä kuormituksesta. Tarkistaaksesi, onko julkinen avain synkronoitu, voit kirjautua [Puhti web-käyttöliittymään](https://www.puhti.csc.fi), avata kirjautumissolmun shellin ja suorittaa:
   ```bash
   cat /var/lib/acco/sshkeys/${USER}/${USER}.pub
   ```
   Jotta SSH-kirjautuminen toimisi, yllä olevan tiedoston tulee olla olemassa **ja** sisältää avain, jota yrität käyttää.
6. **Linuxissa** ja **macOS:ssa**, varmista, että `~/.ssh`-kansiosi ja yksityinen avaintiedostosi ovat 0700 ja 0600-oikeuksilla, vastaavasti. Esimerkki oikeista käyttöoikeuksista:
   ```bash
   $ ls -ld ~/.ssh
   drwx------ 2 username group 4096 Apr 10 13:47 /home/username/.ssh
   $ ls -l ~/.ssh/<private key file>
   -rw------- 1 username group  464 Apr 10 13:47 /home/username/.ssh/<private key file>
   ```
   Asiataksesi oikeat käyttöoikeudet:
   ```bash
   chmod 0700 ~/.ssh
   chmod 0600 ~/.ssh/<private key file>
   ```

Jos kaikki yllä oleva on tarkistettu, ja et vieläkään pysty kirjautumaan Puhtiin, ole hyvä ja
[ota yhteyttä CSC-palvelupisteeseen](../contact.md).

## Lisätietoja {#more-information}

* [SSH-avaindokumentaatio CSC:n Docsissa](../../computing/connecting/ssh-keys.md)
* [Opetusohjelma SSH-avainten määrittämiseksi CSC:ssä](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-keys.html)
* [UKK: Muiden kirjautumisongelmien ratkaisu](i-cannot-login.md)
