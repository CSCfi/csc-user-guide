# SSH-avainten käyttöönotto { #setting-up-ssh-keys }

--8<-- "auth-update-ssh.md"

[SSH-avaimet](https://www.ssh.com/academy/ssh-keys) tarjoavat kätevämmän ja
turvallisemman todennuksen. Niiden käyttöönotto on kaksivaiheinen prosessi ja
se vaaditaan, jotta voit muodostaa yhteyden CSC:n supertietokoneisiin SSH-asiakkaalla.

1. [Luo SSH-avaimet omalla työasemallasi](#generating-ssh-keys).
    - SSH-avaimet luodaan aina pareittain: yksi _julkinen avain_ ja yksi
      _yksityinen avain_. Luo avaimet sille laitteelle, jota aiot käyttää
      yhteyden muodostamiseen CSC:n supertietokoneisiin.
2. [Kopioi julkinen avain työasemaltasi MyCSC:hen](#copying-public-key-to-supercomputer).
    - Avainparilla todennettavaa SSH-yhteyttä varten sinun tulee kopioida
      julkinen avain MyCSC:hen. **Älä kopioi yksityistä avainta.** Huomaa,
      että julkisen avaimen kopioiminen suoraan CSC:n supertietokoneille
      työkaluilla kuten `ssh-copy-id` ei toimi.

Lisätietoja SSH-avaimista:

- [Opas: SSH-avainten käyttöönotto CSC:llä](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-keys.html)
- [UKK: SSH-avaimiin liittyvien ongelmien vianmääritys](../../support/faq/ssh-keys-not-working.md).

!!! warning
    Yksityistä avainta ei tule **koskaan** jakaa kenellekään, ei edes CSC:n
    henkilökunnalle. Sen tulee olla tallennettuna vain paikalliselle työasemalle.

## SSH-avainten luominen { #generating-ssh-keys }

Lue järjestelmäkohtaiset ohjeet, kuinka luot SSH-avaimet paikallisella
työasemallasi:

1. [Unix-pohjaiset järjestelmät](ssh-unix.md) (macOS ja Linux)
2. [Windows-järjestelmät](ssh-windows.md)

Voit palata näihin ohjeisiin, kun sinulta kysytään avainten tiedostonimeä ja
tallennussijaintia. Seuraavat ohjeet olettavat, että olet SSH-avaimen
luontidialogissa.

Jos et ole aiemmin ottanut SSH-avaimia käyttöön, voit hyväksyä oletusnimen ja
-sijainnin painamalla `ENTER`. Jos oletustiedostonimen käyttäminen kuitenkin
ylikirjoittaisi olemassa olevan avaimen, saat seuraavan varoituksen:

```text
/home/<username>/.ssh/id_ed25519 already exists. Overwrite (y/n)?
```

Yleensä olemassa olevia avaimia ei kannata ylikirjoittaa, joten syötä `n`,
aja `ssh-keygen` uudelleen ja anna eri tiedostonimi, kun sitä kysytään. Katso
myös osio
[SSH-avaintiedosto ei-oletusnimellä tai -sijainnissa](#ssh-key-file-with-non-default-name-or-location).

Seuraavaksi sinulta kysytään salalausetta. Valitse turvallinen salalause.
Sen tulisi olla vähintään 8 merkkiä pitkä ja sisältää numeroita, kirjaimia ja
erikoismerkkejä.

!!! warning
    Älä koskaan jätä salalausetta tyhjäksi luodessasi SSH-avainparia!

### SSH-avaintiedosto ei-oletusnimellä tai -sijainnissa { #ssh-key-file-with-non-default-name-or-location }

Jos haluat tallentaa avainparisi muuhun kuin oletussijaintiin (muualle kuin
`~/.ssh/` tai `C:\Users\<username>\.ssh\`), määritä avaimen sijainti
`.ssh/config`-tiedostossa tai käytä todennusagenttia (katso
järjestelmäkohtaiset ohjeet). Voit myös käyttää `ssh`-komennon `-i`-valintaa
seuraavasti:

```bash
# Replace <username> with the name of your CSC user account and
# <host> with "puhti" or "mahti"

ssh <username>@<host>.csc.fi -i /<path-to-key-files>/<private-key>
```

Jos aiot käyttää RStudioa, Jupyter-työkirjoja tai jotain muuta, missä
yhteyden muodostaminen paikalliselta työasemalta laskentasolmulle vaatii
kulkemista kirjautumissolmun kautta, ota käyttöön agentin välitys ja määritä
polku yksityiselle avaimelle `.ssh/config`-tiedostossa seuraavasti:

```bash
Host <host>.csc.fi
  HostName <host>.csc.fi
  User <username>
  ForwardAgent yes
  IdentityFile /<path-to-key-files>/<private-key>

Host *.bullx
  IdentityFile /<path-to-key-files>/<private-key>
```

## Julkisen avaimen kopioiminen supertietokoneelle { #copying-public-key-to-supercomputer }

Ainoa tapa kopioida julkinen avain supertietokoneelle on MyCSC-asiakasportaalin
kautta.
[Lue ohjeet alta](ssh-keys.md#adding-public-key-in-mycsc).

### Julkisen avaimen lisääminen MyCSC:hen { #adding-public-key-in-mycsc }

Voit lisätä julkisen avaimesi
[MyCSC-asiakasportaalissa](https://my.csc.fi) seuraavasti:

1. Kirjaudu MyCSC:hen CSC- tai Haka/Virtu-tunnuksillasi.
2. Valitse _Profile_ vasemmasta navigaatiosta tai oikean yläkulman
   pudotusvalikosta.
3. Etsi _SSH PUBLIC KEYS_ -osio ja valitse _+ Add key_. Turvallisuussyistä
   sinua pyydetään kirjautumaan uudelleen, jos edellisestä kirjautumisesta
   portaaliin on kulunut muutama minuutti.

    ![Lisää avain](https://a3s.fi/docs-files/ssh-no-keys.png 'Lisää avain')

4. Lisää julkinen avaimesi joko
    1. lataamalla julkisen avaimen tiedosto _Upload file_ -välilehdellä, tai
    2. liittämällä sen sisältö käsin _Manual input_ -välilehden _Key_-kenttään.
       Lisää tällöin myös avaimelle _Title_, esim. "my-ssh-key".

        === "Lataa tiedosto"
            ![Lataa tiedosto](https://a3s.fi/docs-files/ssh-upload-file.png 'Lataa tiedosto')

        === "Manuaalinen syöttö"
            ![Manuaalinen syöttö](https://a3s.fi/docs-files/ssh-manual-input.png 'Manuaalinen syöttö')

5. Valitse _Upload_ tai _Add_.
6. Näet nyt uuden avaimesi listattuna _SSH PUBLIC KEYS_ -osiossa. Huomaa, että
   avaimen aktivoituminen voi kestää jopa tunnin. Jos kestää pidempään, ole
   hyvä ja
   [ota yhteyttä CSC Service Deskiin](../../support/contact.md).

    ![Uusi avain lisätty](https://a3s.fi/docs-files/ssh-key-added.png 'Uusi avain lisätty')

!!! warning "Tuetut avaintyypit ja muotoilu"
    Tuetut avaintyypit ovat Ed25519 ja RSA 4096–16384. **Suosittelemme
    vahvasti Ed25519-avainta**.

    Julkisen avaimen tulee koostua SSH-avaintyypistä, avainjonosta ja
    valinnaisesta kommentista, eroteltuna yksittäisillä välilyönneillä. Varmista,
    että koko SSH-avain on samalla rivillä, eikä mukaan ole lisätty muita
    välilyöntimerkkejä kuin tavallisia välilyöntejä. Jos avain on väärin
    muotoiltu, näytetään virheilmoitus. Oikein muotoiltu avain näyttää tältä:
    ```
    ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDlapOdeoxNvz/1AZFRjGAPnPj8pzzz3skI+a+yJS5b7 optional-comment
    ```

Käyttäjät voivat tarkistaa julkiset avaimensa Puhtissa tai Mahtissa
seuraavilla komennoilla:

```bash
# Check timestamp of file (time of previous sync)
ls -l /var/lib/acco/sshkeys/${USER}/${USER}.pub

# Check its contents (public keys)
cat /var/lib/acco/sshkeys/${USER}/${USER}.pub
```

Jos olet lisännyt useita avaimia MyCSC:hen, niiden tulisi kaikki näkyä samassa
`${USER}.pub`-tiedostossa.

## Lisätietoja { #more-information }

- [Opas SSH-avainten käyttöönottoon CSC:llä](https://csc-training.github.io/csc-env-eff/hands-on/connecting/ssh-keys.html)
- [SSH-avaimiin liittyvien ongelmien vianmääritys](../../support/faq/ssh-keys-not-working.md)