
# Kuinka voin antaa pääsyn muille henkilöille VM:lleni Poutassa? {#how-can-i-give-access-to-other-people-to-my-vm-in-pouta}

Kun [uusi VM luodaan](../../cloud/pouta/launch-vm-from-web-gui.md), luodaan automaattisesti yksi oletuskäyttäjä. Ja yksi SSH-avaimien pari on antanut pääsyn tälle oletuskäyttäjälle siinä VM:ssä. Tämä antaa pääsyn siihen VM:ään yhdelle henkilölle, sille, joka on luonut VM:n ja joka omistaa SSH:n **yksityisen** avaimen. Katso lisää Wikipedia-artikkelista [Secure Shell](https://en.wikipedia.org/wiki/Secure_Shell), jossa on lisätietoa SSH-avaimista ja protokollasta yleisesti.

On yleinen käyttötapaus (ja hyvä käytäntö tuotantopalveluille), että useammalla kuin yhdellä henkilöllä on pääsy VM:lle. Seuraava menettely on yksi useista vaihtoehdoista tämän saavuttamiseksi. Luomme uuden käyttäjän ja annamme pääsyn tälle käyttäjälle yhdelle henkilölle.

## Luo uusi käyttäjä {#create-a-new-user}

1. [Yhdistä VM:ään](../../cloud/pouta/connecting-to-vm.md) oletuskäyttäjänä. Tällä käyttäjällä on järjestelmänvalvojan oikeudet (`sudo`).

2. Luo uusi käyttäjä, katso [adduser](https://linux.die.net/man/8/adduser) -manuaali lisätietoja varten.

    ```sh
    sudo adduser -m <user>
    ```

!!! info "Korvaa `<user>` luotavan käyttäjätunnuksen kanssa"

Käyttäjä on luotu VM:ssä, mutta kenelläkään ei ole pääsyä siihen. Antaaksesi pääsyn tälle käyttäjälle, meidän täytyy määrittää **Authorized Keys** tälle tilille.

## Määritä Authorized keys {#configure-authorized-keys}

Ennen kuin aloitat, tarvitset **public** ssh-avaimen. Tämä julkinen avain tulee olla luotu sen uuden henkilön toimesta, jolle pääsy VM:ään annetaan. Kun SSH-avaimien pari on luotu, luodaan kaksi avainta: **julkinen** SSH-avain ja **yksityinen** avain. Julkinen voi olla julkisesti julkaistu koko maailmalle, esimerkiksi GitHub julkaisee kaikkien käyttäjiensä avaimet. Toisaalta **yksityistä** avainta ei saa koskaan jakaa kenellekään, eikä sen pitäisi poistua siitä tietokoneesta, johon se on luotu.

### Luo SSH-avainten pari {#create-ssh-key-pair}

On suositeltavaa luoda uusi ssh-avainten pari per käyttäjä ja palvelu, tällä tavalla, jos **yksityinen** avain vuotaa, vahinko on rajattu vain siihen käyttäjään siinä palvelussa. Jos käytät samaa avainta jokaiselle VM:lle, jokainen niistä voi potentiaalisesti vaarantua ja täytyy luoda uudelleen. Linuxissa ja Mac:ssa voit luoda uuden yksityisen/julkisen avainten parin tekemällä:

```sh
$ ssh-keygen 
Generating public/private rsa key pair.
Enter file in which to save the key (/home/ubuntu/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/ubuntu/.ssh/id_rsa
Your public key has been saved in /home/ubuntu/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:9MKfQAUs+b2tmpXjqsa0DinzFbW+9qdpFAPYKh4P1i8 ubuntu@ab-tests
The key's randomart image is:
+---[RSA 3072]----+
|       =...      |
|      + +.       |
|     . ++o       |
|    = o=.o+      |
|   o =..S .=     |
|    ..Eo.+oo.    |
|  o oo.o..*.     |
|   + o+ .=oo.    |
|    .ooo===o     |
+----[SHA256]-----+
```

Yllä olevassa esimerkissä luotiin kaksi tiedostoa: `id_rsa` **yksityinen** avain, ja `id_rsa.pub` **julkinen** avain. Viitteeksi, **julkinen** ssh-avain näyttää tältä:

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCoQ9S7V+CufAgwoehnf2TqsJ9LTsu8pUA3FgpS2mdVwcMcTs++8P5sQcXHLtDmNLpWN4k7NQgxaY1oXy5e25x/4VhXaJXWEt3luSw+Phv/PB2+aGLvqCUirsLTAD2r7ieMhd/pcVf/HlhNUQgnO1mupdbDyqZoGD/uCcJiYav8i/V7nJWJouHA8yq31XS2yqXp9m3VC7UZZHzUsVJA9Us5YqF0hKYeaGruIHR2bwoDF9ZFMss5t6/pzxMljU/ccYwvvRDdI7WX4o4+zLuZ6RWvsU6LGbbb0pQdB72tlV41fSefwFsk4JRdKbyV3Xjf25pV4IXOTcqhy+4JTB/jXxrF
```

!!! info "Yllä oleva avain on [Linus Torvald](https://github.com/torvalds.keys)'n julkinen ssh-avain GitHubissa"

### Lisää avaimet `authorized_keys`-tiedostoon {#adding-keys-to-authorized-keys}

Kun uusi henkilö on lähettänyt sinulle julkisen avaimen, sinun täytyy kopioida se palvelimelle ja lisätä se `authorized_keys` "tietokanta"-tiedostoon:

1. Lataa julkisen avaimen tiedosto palvelimelle, Linuxissa tai Mac:ssa voit käyttää `SCP` (Secure copy protocol):

    ```sh
    scp id_rsa.pub <default_user>@<floating_ip>:
    ```

    Huom: `<default_user>` on edelleen se, joka löytyy [kuvauksen dokumentaatiosta](../../cloud/pouta/images.md#images)

2. Varmista, että erityinen SSH-konfiguraatiokansio on olemassa:

    ```sh
    mkdir -p ~<user>/.ssh
    ```

    Taas kerran, korvaa `<user>` juuri luomallasi käyttäjänimellä. Esimerkiksi, käyttäjälle `pepe` komento olisi: `mkdir -p ~pepe/.ssh`.

3. tee varmuuskopio `authorized_keys`-tiedostosta (tämä on valinnainen mutta suositeltava):

    ```sh
    cp ~<user>/.ssh/authorized_keys ~<user>/.ssh/authorized_keys.$(date +%s)
    ```

4. Lisää julkinen avain `authorized_keys`-tiedostoon:

    ```sh
    cat id_rs.pub >> ~<user>/.ssh/authorized_keys
    ```

5. Varmista, että oikeudet ovat oikeat:

    ```sh
    chmod 700 ~<user>/.ssh
    chmod 600 ~<user>/.ssh/authorized_keys
    ```

6. Lopuksi, tarkista, että `authorized_keys`-tiedosto näyttää siltä kuin pitäisi, yksi julkinen avain per rivi.

Uusi henkilö voi nyt seurata artikkelia [yhdistäminen VM:ään](../../cloud/pouta/connecting-to-vm.md). Komennon (Linuxissa ja Mac:ssa) pitäisi olla jotakin seuraavanlaista:

```sh
ssh -i id_rsa <user>@<floating_ip>
```

## Anna pääsy samalle käyttäjälle usealle julkiselle avaimelle {#give-access-to-the-same-user-to-several-public-keys}

Voi olla hyvä käytäntö antaa pääsy samalle käyttäjälle samassa VM:ssä usealle SSH-avaimelle. Esimerkiksi, jos samalla henkilöllä on eri laitteet, jokaisella laitteella on eri yksityinen avain, ja jos yksi laitteista katoaa, vain yksi avaimista täytyy poistaa `authorized_keys`-tiedostosta. Tätä käyttötapaa varten on mahdollista käyttää työkalua [ssh-copy-id](https://linux.die.net/man/1/ssh-copy-id). Tämä työkalu toimii vain, jos sinulla on jo pääsy kyseiseen käyttäjään kyseisessä VM:ssä.

```sh
ssh-copy-id -i ~/.ssh/id_rsa.pub <user>@<floating_ip>
```

Tiedosto `~/.ssh/id_rsa.pub` on uusi lisättävä SSH-avain.

!!! warning "Älä anna eri ihmisille pääsyä samalle käyttäjänimelle"
    Ei ole hyvä käytäntö antaa eri ihmisille pääsyä samalle käyttäjälle. Tämä johtuu siitä, että se tekee lähes mahdottomaksi tarkistaa, kuka ja milloin yhdistyi VM:ään.

