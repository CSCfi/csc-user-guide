
# Siirtyminen Rahtiin

## Milloin siirtyä Kubernetesiin {#when-to-migrate-to-kubernetes}

Kun harkitset palvelujesi siirtämistä Poudasta Kubernetesiin (k8s), on tärkeää ottaa huomioon
kummankin alustan suhteelliset vahvuudet. Sekä Pouta että Kubernetes-pohjaiset alustat, kuten Rahti, ovat Pilvilaskentapalveluita, mutta niissä on joitain tärkeitä eroja. OpenStack-pohjaiset palvelut, kuten
cPouta, luokitellaan Infra-as-a-Service (IaaS) pilvipalveluiksi, joissa käyttäjät voivat varata oman
infrastruktuurinsa virtuaalikoneena. Rahti puolestaan luokitellaan Platform-as-a-Service (PaaS) -palveluksi, jossa käyttäjät voivat ottaa
käyttöön konttipohjaisia alustojaan jaetussa Kubernetes-klusterissa, joka on vahvistettu tukemaan monen käyttäjän ympäristöjä.

Pääasiallinen ero IaaS- ja PaaS-palvelujen välillä on se, että IaaS:ssa käyttäjä on vastuussa
käyttöjärjestelmän ja mahdollisesti monien sovellusten hallinnoinnista, kun taas PaaS:ssa,
käyttäjä on vastuussa vain sovelluksen ja datan hallinnoinnista. Voit lukea lisää pilvilaskentakonsepteista [täältä](concepts.md).

Konteilla on tiettyjä etuja perinteisiin virtuaalikoneisiin verrattuna. Konttikuvat ovat tyypillisesti
pienempiä ja vähemmän muistia ja prosessoritehoa kuluttavia kuin virtuaalikonekuvat. Uusien konttien käynnistäminen on
nopeaa, mikä antaa niille mahdollisuuden suureen skaalautuvuuteen. Koska konttien käyttöönotto on myös suhteellisen helppoa, jatkuvan käyttöönoton ja integroinnin käytännöt toimivat erittäin hyvin konttipohjaisissa lähestymistavoissa.

Käyttämällä konttien orkestrointipalvelua, kuten Kubernetesin päälle rakennettua Rahtia, tekee sovellusten
käyttöönotosta helppoa. Rahtissa voit hallinnoida sovelluksiasi suoraan verkkoselaimen kautta käytettävän
verkkoliittymän avulla. Rahti tarjoaa alustan, jossa voit isännöidä omia sovelluksiasi ja tehdä ne
saataville verkon kautta. Rahti voi ajaa monenlaisia sovelluksia ja työkuormia, kuten verkkopalvelimia
ja tietokantoja sekä data-analyysiputkia.

Joihinkin esimerkkikäyttötapauksiin, jotka sopivat Rahtiin, kuuluvat:

* Interaktiivisen verkkosovelluksen tai tavallisen verkkosivuston isännöinti. Rahti sisältää monia
yleisimmistä verkkosovelluksissa tarvittavista ominaisuuksista.
* Monimutkainen esipakattu sovellus, kuten Apache Spark. Sovellusten skaalauksen kasvattaminen useille
käyttäjille on myös helppoa.
* Käyttöönotto katalogista, joka sisältää monia yleisesti käytettyjä sovelluspohjia vain yhdellä komennolla.

Toisin sanoen, tilanteissa, joissa tarvitaan skaalautuvuutta tai haluat hallita vain yhtä sovellusta, konttien
orkestrointipalvelu voi olla oikea valinta.

Kontit eivät luonteensa vuoksi ole yhtä turvallisia kuin virtuaalikoneet. Sellaisten konttien
orkestrointipalveluiden, kuten Rahti ja Openshift, kanssa kontteja ei saa ajaa root-oikeuksilla, mikä voi aiheuttaa
joitain rajoituksia tietyissä tilanteissa ja vaatii lisämuokkauksia kuviin. Herkän datan käsittelytehtävissä on
parempi harkita muita CSC-palveluja, kuten ePoutaa, joka on aina ensisijainen alusta. Se
on erityisesti suunniteltu korkean suorituskyvyn ja korkean turvallisuuden tehtäviin, joissa käsitellään herkkiä tietoja ja käytetään monenlaisia resursseja.

### Lisätietoja {#additional-information}

[Mikä on Rahti?](rahti-what-is.md)

[Kontepilvien perusteet](https://rahti-course.a3s.fi/index.html#1)

[Miksi käyttää kontteja vs. VM:itä? | VMware](https://www.vmware.com/topics/glossary/content/vms-vs-containers.html)

[Kontit vs. virtuaalikoneet (VM:t): Mitä eroa? | IBM](https://www.ibm.com/cloud/blog/containers-vs-vms)

[Palvelun siirtyminen Kubernetesista OpenShiftiin | IBM](https://developer.ibm.com/learningpaths/migrate-kubernetes-openshift/)
