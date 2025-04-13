# Luo kiinteä IP VM:lle

## Johdanto {#introduction}

On yksinkertainen prosessi tietää/kiinnittää VM:n IP-osoite ennen sen käynnistämistä. Myös IP voidaan varata, jos haluat käynnistää VM:n uudelleen.

### Kiinnitä IP-osoite ennen VM:n käynnistämistä {#fix-ip-address-before-launching-a-vm}

Noudata seuraavaa menettelyä:

1. Projektisi valikossa, mene **Verkot** ja napsauta `project_XXXXXXX-network` linkkiä, missä XXXXXXX on projektinumero.

![Projekti](../../img/project.png)

2. Siirry **Portit**-välilehteen ja napsauta **Luo portti** oikeassa yläkulmassa.

![Projekti-verkko](../../img/project-network.png)

3. Dialogi-ikkuna ilmestyy seuraavan kuvan mukaisesti. Syötä nimi ja napsauta **Luo**.

![Luo-portti](../../img/Create-port-unspecified.png)

4. Nyt, kun käynnistät instanssia, siirry **Verkkoportit** ja käytä tätä porttia.

![käynnistä-instanssi](../../img/launch-instance.png)

### Varaa IP uudelleenkäynnistettävälle VM:lle {#reserve-ip-to-re-launch-a-vm}

Menettely on melkein sama muutamalla lisäaskeleella:

1. Kirjoita muistiin nykyisen VM:n IP-osoite ja turvallisuusryhmien lista.

2. Sammuta VM.

3. Ota tilannekuva.

4. Napsauta projektisi verkon **Portit**.

5. Poista nykyisen VM:si IP:tä vastaava portti. Tämä johtuu siitä, että kyseinen portti on automaattisesti luotu eikä sitä voi osoittaa mihinkään muuhun VM:ään kuin siihen, johon se on tällä hetkellä osoitettu. Poistonappi on Toiminnot-kohdassa.

6. Nyt, luo portti edellä mainitulla tavalla. Tässä, **Määritä IP-osoite tai aliverkko**, vaihda se **Kiinteä IP-osoite**. Uusi kenttä ilmestyy, syötä siihen nykyisen VM:si IP-osoite.

7. Käytä tätä porttia, kun käynnistät VM:ää.
