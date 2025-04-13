# Järjestelmät {#systems}

CSC:n laskentaympäristö koostuu supertietokoneista Puhti ja Mahti sekä kvanttista oppimista varten tarkoitetusta koneesta Kvasi. Puhtilla ja Mahtilla on melko samanlainen laskentaympäristö, ja laaja valikoima työkuormia voi hyödyntää molempia tehokkaasti. Samalla niiden laitteisto on erilainen, ja tämä tekee joistakin työkuormista erityisen sopivia joko Puhtille tai Mahtille.

Kansallisten resurssien lisäksi CSC:n datakeskus Kajaanissa isännöi pan-Eurooppalaista pre-eksaskaalaista supertietokonetta LUMI. LUMIn CPU-osio on ollut käytettävissä vuoden 2022 alusta lähtien, kun taas järjestelmän suurin osio, joka koostuu GPU-kiihdytetyistä solmuista, tuli saataville vuonna 2023.

CSC:n kansalliset supertietokoneet Puhti ja Mahti korvataan vuonna 2026 uudella järjestelmällä, Roihu.

## LUMI {#lumi}

LUMI on yksi kolmesta Euroopan pre-eksaskaalaisesta supertietokoneesta. Se on HPE Cray EX supertietokone, joka koostuu useista eri käyttötarkoituksiin suunnatuista osioista. Järjestelmän suurin osio on "LUMI-G" osio, joka koostuu GPU-kiihdytetyistä solmuista käyttäen tulevaisuuden sukupolven AMD Instinct GPU:ta. Tämän lisäksi on pienempi CPU-osio, "LUMI-C", jossa on AMD EPYC "Milan" CPU:t sekä aputietokanta data-analytiikkaa varten suurilla muistisolmuilla ja joillakin GPU:illa datan visualisointiin. Laskentaan omistettujen osioiden lisäksi LUMI tarjoaa myös useita tallennusosioita yhteensä 117 PB tallennustilaa.

- [LUMIn käyttäjädokumentaatio](https://docs.lumi-supercomputer.eu/)
- [Teknisempi kuvaus LUMIsta](https://docs.lumi-supercomputer.eu/hardware/)
- [Miten LUMI-C eroaa Mahtista?](lumi-vs-mahti.md)

## Puhti {#puhti}

Puhti supertietokone, Atos BullSequana X400 klusteriin perustuva Intel CPU:illa, otettiin käyttöön syyskuun 2, 2019. Siinä on voimakas CPU-osio, jossa on lähes 700 solmua erilaisilla muistimäärillä ja paikallisilla tallennusvaihtoehdoilla, kaikki yhdistettynä nopealla yhteenliitännällä. Puhti sallii käyttäjän varata laskenta- ja muistiresursseja joustavasti, ja käyttäjä voi suorittaa kaikkea vuorovaikutteisesta yksittäisen ytimen tietojenkäsittelystä keskikokoisiin simulointeihin, jotka laajenevat useisiin solmuihin.

Lisäksi on 80 GPU-solmua, joiden yhteensä 320 Nvidia Volta V100 GPU:ta. Tämä osio soveltuu kaikille työkuormille, jotka pystyvät hyödyntämään GPU:ita, jopa raskaille tekoälymalleille, jotka laajenevat useisiin solmuihin.

Puhtilla on laaja valikoima asennettua [tieteellistä ohjelmistoa](../apps/by_system.md#puhti).

- [Teknisempi kuvaus Puhtista](systems-puhti.md)

## Mahti {#mahti}

Mahti supertietokone, Atos BullSequana XH2000 järjestelmä, joka perustuu AMD CPU:ihin, otettiin käyttöön elokuun 26, 2020. Mahti on suunniteltu laajasti rinnakkaisille tehtäville, jotka vaativat korkeaa liukulukusuorituskykyä ja nopeaa yhdistettä. Järjestelmässä on yhteensä 1404 solmua varustettuna tehokkailla AMD Rome CPU:illa. Nämä on yhdistetty nopealla yhteenliitännällä, mikä mahdollistaa tehtävien skaalautumisen koko järjestelmässä. Mahtissa käyttäjä varaa kokonaisia solmuja, jotta tehtävät voivat hyödyntää kunkin solmun täyden suorituskyvyn. Mahti sopii erityisesti keskikokoisiin ja suuriin simulointeihin, jotka vaativat Petaflops-luokan laskentatehoa. Myös pienemmät rinnakkaiset työkuormat, jotka pystyvät käyttämään solmuja tehokkaasti, voivat hyödyntää Mahtia.

Lisäksi on 24 GPU-solmua, joiden yhteensä 96 Nvidia Ampere A100 GPU:ta. Tämä osio soveltuu kaikille työkuormille, jotka pystyvät hyödyntämään GPU:ita, jopa raskaille tekoälymalleille, jotka laajenevat useisiin solmuihin. Osa A100 GPU:ista on jaettu pienemmiksi GPU:iksi, joiden laskenta- ja muistikapasiteetti on yksi seitsemäsosa täydestä A100 GPU:sta. Näitä voidaan käyttää vuorovaikutteisiin työkuormiin, kursseihin ja koodin kehittämiseen.

Mahtin valikoima asennettua [tieteellistä ohjelmistoa](../apps/by_system.md#mahti) on rajoitetumpi kuin Puhtilla.

- [Teknisempi kuvaus Mahtista](systems-mahti.md)

## Roihu (tulossa pian) {#roihu-coming-soon}

CSC:n seuraava kansallinen supertietokone Roihu, BullSequana XH3000 hybridijärjestelmä, korvaa Puhti ja Mahti supertietokoneet. Roihu sijoitetaan CSC:n Kajaanin datakeskukseen, ja sen odotetaan olevan tutkijoiden käytössä vuoden 2026 alussa.

- [Lisätietoa Roihusta](systems-roihu.md)