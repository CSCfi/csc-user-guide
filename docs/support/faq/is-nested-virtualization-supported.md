# Onko sisäkkäinen virtualisointi tuettu Poutassa? { #is-nested-virtualization-supported-on-pouta }

Ei, toistaiseksi sisäkkäinen virtualisointi ei ole käytössä Poutassa. Sisäkkäinen virtualisointi estää live-siirrot, ja tällä hetkellä katsomme, että live-siirto on käyttäjillemme paljon hyödyllisempi ominaisuus kuin sisäkkäinen virtualisointi.

!!! Info "Sisäkkäinen virtualisointi"
    Sisäkkäinen virtualisointi on ominaisuus, jonka avulla voit ajaa virtuaalikoneita (VM:t) toisten virtuaalikoneiden sisällä. Tästä on hyötyä testaus- ja kehitystarkoituksiin

!!! Info "Live-siirto"
    Live-siirto on käynnissä olevan virtuaalikoneen siirtämistä eri fyysisten koneiden välillä ilman virtuaalikoneen uudelleenkäynnistystä tai sammuttamista. Siirron aikana voi olla lyhyt katkos, mutta virtuaalikoneessa käynnissä olevat prosessit eivät havaitse tätä katkosta.