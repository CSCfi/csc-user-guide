# SSH-avainten määrittäminen {#setting-up-ssh-keys}

[SSH-avaimet](https://www.ssh.com/academy/ssh-keys) tarjoavat kätevämmän ja turvallisemman tunnistuksen. Niiden määrittäminen on kaksivaiheinen prosessi, ja se on tarpeen, jotta voit käyttää CSC:n supertietokoneita SSH-asiakkaan avulla.

1. [Luo SSH-avaimet paikallisella työasemallasi](#generating-ssh-keys).
    - SSH-avaimet luodaan aina parina, johon kuuluu yksi _julkinen avain_ ja yksi _yksityinen avain_. Luo nämä avaimet laitteella, jota aiot käyttää CSC:n supertietokoneisiin yhdistämiseen.
2. [Kopioi julkinen avain työasemaltasi MyCSC:hen](#copying-public-key-to-supercomputer).
    - Jotta SSH-yhteys voidaan todentaa avainparin avulla, sinun on kopioitava julkinen avain MyCSC:hen. **Älä kopioi yksityistä avainta.** Huomaa, että julkisen avaimen kopioiminen suoraan CSC:n supertietokoneisiin työkaluilla, kuten `ssh-copy-id`, ei toimi.

Lisätietoa SSH-avaimista löydät:

- [Opetus: SSH-avainten määrittäminen CSC:ssä](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-keys.html)
- [UKK: SSH-avainten ongelmien korjaaminen](../../support/faq/ssh-keys-not-working.md).

!!! warning
    Yksityistä avainta ei tule **koskaan** jakaa kenenkään kanssa, ei edes CSC:n henkilökunnalle. Sen tulee olla tallennettuna vain paikallisella työasemalla.

## SSH-avainten luominen {#generating-ssh-keys}

Jos haluat tietää, miten luoda SSH-avaimet paikallisella työasemallasi, katso järjestelmäkohtaiset ohjeet:

1. [Unix-pohjaiset järjestelmät](ssh-unix.md) (macOS ja Linux)
2. [Windows-järjestelmät](ssh-windows.md)

Voit palata näihin ohjeisiin, kun sinua pyydetään nimeämään ja valitsemaan avainten tallennuspaikka. Seuraavat ohjeet olettavat, että olet SSH-avaimen luontidialogissa.

Jos et ole aiemmin määrittänyt SSH-avaimia, voit hyväksyä oletusnimen ja sijainnin painamalla `ENTER`. Jos oletusnimen käyttäminen kuitenkin ylikirjoittaisi olemassa olevan avaimen, saat varoituksen, joka näyttää tältä:

```text
/home/<username>/.ssh/id_ed25519 already exists. Overwrite (y/n)?
```

Yleisesti ottaen et halua ylikirjoittaa olemassa olevia avaimia, joten kirjoita `n`, suorita `ssh-keygen` uudelleen ja syötä eri tiedostonimi, kun sitä pyydetään. Katso myös osio
[SSH-avaintiedostot, joiden nimi tai sijainti ei ole oletus](#ssh-key-file-with-non-default-name-or-location).

Seuraavaksi sinua pyydetään valitsemaan salasana. Valitse turvallinen salasana. Sen tulisi olla vähintään 8 merkkiä pitkä ja sisältää numeroita, kirjaimia ja erikoismerkkejä.

!!! warning
    Älä koskaan jätä salasanaa tyhjäksi, kun luot SSH-avaimen paria!

### SSH-avaintiedosto, jonka nimi tai sijainti ei ole oletus {#ssh-key-file-with-non-default-name-or-location}

Jos haluat tallentaa avainparisi muualle kuin oletuspaikkaan (muualle kuin `~/.ssh/` tai `C:\Users\<username>\.ssh\`), määritä avainten sijainti `.ssh/config`-tiedostossa tai käyttämällä tunnistautumisagenttia (katso järjestelmäkohtaiset ohjeet). Voit myös käyttää `ssh`-komennon `-i`-vaihtoehtoa seuraavasti:

```bash
# Korvaa <username> CSC:n käyttäjätilisi nimellä ja
# <host> arvolla "puhti" tai "mahti"

ssh <username>@<host>.csc.fi -i /<path-to-key-files>/<private-key>
```

Jos aiot käyttää RStudioa, Jupyter-muistikirjoja tai jotain muuta, missä paikalliselta työasemaltasi yhdistäminen laskentasolmuun vaatii tunneloinnin kirjautumissolmun kautta, määritä agentti-siirto ja yksityisen avaimen polku `.ssh/config`-tiedostoon seuraavasti:

```bash
Host <host>.csc.fi
  HostName <host>.csc.fi
  User <username>
  ForwardAgent yes
  IdentityFile /<path-to-key-files>/<private-key>

Host *.bullx
  IdentityFile /<path-to-key-files>/<private-key>
```

## Julkisen avaimen kopiointi supertietokoneelle {#copying-public-key-to-supercomputer}

Ainoa tapa kopioida julkinen avain supertietokoneelle on MyCSC-asiakasportaalin kautta.
[Lue ohjeet täältä](ssh-keys.md#adding-public-key-in-mycsc).

### Julkisen avaimen lisääminen MyCSC:hen {#adding-public-key-in-mycsc}

Voit lisätä julkisen avaimesi
[MyCSC-asiakasportaalissa](https://my.csc.fi) seuraavasti:

1. Kirjaudu MyCS:hen CSC- tai Haka/Virtu-tunnuksillasi.
2. Valitse _Profiili_ vasemmasta navigaatiosta tai oikean yläkulman valikosta.
3. Etsi _SSH JULKISET AVAIMET_ -osio ja valitse _+ Lisää avain_. Turvatoimena sinua pyydetään kirjautumaan uudelleen, jos on kulunut useita minuutteja viimeisestä portaalikirjautumisestasi.
4. Syötä avainparillesi _Otsikko_, esim. "my-ssh-key".
5. Liitä **julkinen** SSH-avaimesi _Avaimen_ kenttään. Tuettuja avaintyyppejä ovat Ed25519 ja RSA 2048 - 16384. **Suosittelemme vahvasti Ed25519:**. Jos valitset RSA:n, käytä vähintään 4096 bittiä.
6. Valitse _Lisää_.
7. Uuden avaimesi pitäisi nyt näkyä _SSH JULKISET AVAIMET_ -kohdassa. Huomioi, että uuden avaimesi aktivointi voi kestää jopa tunnin. Jos se kestää kauemmin, ota yhteyttä [CSC:n palvelupisteeseen](../../support/contact.md).

Käyttäjät voivat tarkistaa julkiset avaimensa Puhtissa tai Mahtissa seuraavilla komennoilla:

```bash
# Tarkista tiedoston aikaleima (edellisen synkronoinnin aika)
ls -l /var/lib/acco/sshkeys/${USER}/${USER}.pub

# Tarkista sen sisältö (julkiset avaimet)
cat /var/lib/acco/sshkeys/${USER}/${USER}.pub
```

Jos olet lisännyt useita avaimia MyCSC:hen, niiden pitäisi kaikki näkyä samassa `${USER}.pub` tiedostossa.

!!! info "Vaadittu avainformaatiomuoto"
    Julkisen avaimesi tulisi koostua SSH-avaintyypistä ja avainsekvenssistä, erotettuna yhdellä välilyönnillä. Varmista, että lisäät koko SSH-avaimen samalle riville äläkä lisää muita välilyöntejä kuin normaaleja välilyöntimerkkejä. Jos avaimesi on väärin muotoiltu, näytetään virheilmoitus. Oikein muotoiltu avain näyttää tältä:
    ```
    ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDlapOdeoxNvz/1AZFRjGAPnPj8pzzz3skI+a+yJS5b7
    ```

## Lisätietoja {#more-information}

- [Opetus SSH-avainten määrittämisestä CSC:ssä](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-keys.html)
- [Ongelmien ratkaiseminen SSH-avaintein kanssa](../../support/faq/ssh-keys-not-working.md)