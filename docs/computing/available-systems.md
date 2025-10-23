# Järjestelmät { #systems }

CSC:n laskentaympäristö koostuu Puhti- ja Mahti-supertietokoneista. Puhtissa ja Mahtissa on melko samankaltainen laskentaympäristö, ja laaja kirjo työkuormia pystyy hyödyntämään kumpaakin tehokkaasti. Samalla niiden laitteistot ovat erilaisia, mikä tekee joistakin työkuormista erityisen sopivia jommallekummalle: joko Puhtille tai Mahtille.

Kansallisten resurssien lisäksi CSC:n Kajaanin konesalissa toimii koko Euroopan yhteinen pre-eksaluokan supertietokone LUMI. LUMIn CPU-osio on ollut käytettävissä vuoden 2022 alusta, kun taas järjestelmän suurin osio, joka koostuu GPU-kiihdytetyistä solmuista, tuli käyttöön vuonna 2023.

CSC:n kansalliset supertietokoneet Puhti ja Mahti korvataan vuonna 2026 uudella järjestelmällä, Roihulla.

## LUMI { #lumi }

LUMI on yksi kolmesta Euroopan pre-eksaluokan supertietokoneesta. Se on HPE Cray EX -supertietokone, joka koostuu useista eri käyttötarkoituksiin suunnatuista osioista. Järjestelmän suurin osio on "LUMI-G", joka koostuu GPU-kiihdytetyistä solmuista ja käyttää seuraavan sukupolven AMD Instinct -GPU:ita. Lisäksi on pienempi pelkkiin CPU:ihin perustuva osio "LUMI-C", jossa on AMD EPYC "Milan" -suorittimet, sekä data-analytiikkaan tarkoitettu apuosio, jossa on suurimuistisia solmuja ja joitakin GPU:ita datavisualisointia varten. Laskentaan omistettujen osioiden lisäksi LUMI tarjoaa myös useita tallennusosioita, yhteensä 117 PB tallennustilaa.

- [LUMIn käyttäjädokumentaatio](https://docs.lumi-supercomputer.eu/)
- [LUMIn teknisempi kuvaus](https://docs.lumi-supercomputer.eu/hardware/)
- [Miten LUMI-C eroaa Mahtista?](lumi-vs-mahti.md)

## Puhti { #puhti }

Puhti-supertietokone, Intel-suorittimiin perustuva Atos BullSequana X400 -klusteri, otettiin käyttöön 2. syyskuuta 2019. Siinä on tehokas CPU-osio, jossa on lähes 700 solmua erilaisilla muistimäärillä ja paikallisen tallennuksen vaihtoehdoilla; kaikki on yhdistetty nopealla kytkentäverkolla. Puhti mahdollistaa laskenta- ja muistiresurssien joustavan varaamisen, ja käyttäjä voi ajaa kaikkea interaktiivisesta yksittäisen ytimen tietojenkäsittelystä useaan solmuun ulottuviin keskisuuriin simulaatioihin.

Lisäksi on 80 GPU-solmua, joissa on yhteensä 320 Nvidia Volta V100 -GPU:ta. Tämä osio soveltuu kaikenlaisille GPU:ita hyödyntäville työkuormille, jopa usealle solmulle skaalautuville raskaille tekoälymalleille.

Puhtiin on asennettu laaja valikoima [tieteellistä ohjelmistoa](../apps/by_availability.md#puhti).

- [Puhtin teknisempi kuvaus](systems-puhti.md)

## Mahti { #mahti }

Mahti-supertietokone, AMD-suorittimiin perustuva Atos BullSequana XH2000 -järjestelmä, otettiin käyttöön 26. elokuuta 2020. Mahti on suunniteltu massiivisesti rinnakkaisille töille, jotka vaativat korkeaa liukulukusuorituskykyä ja nopeaa kytkentäverkkoa. Järjestelmässä on yhteensä 1404 solmua, joissa on tehokkaat AMD Rome -suorittimet. Nämä on yhdistetty nopealla kytkentäverkolla, mikä mahdollistaa töiden skaalautumisen koko järjestelmän laajuudelle. Mahtissa käyttäjä varaa kokonaisia solmuja, jotta työt pystyvät hyödyntämään kunkin solmun suorituskyvyn täysimääräisesti. Mahti on erityisesti suunnattu keski- ja suurikokoisiin simulaatioihin, jotka vaativat petaflops-luokan laskentatehoa. Myös pienemmät rinnakkaiset työkuormat, jotka pystyvät käyttämään kokonaisia solmuja tehokkaasti, voivat hyödyntää Mahtia.

Lisäksi on 24 GPU-solmua, joissa on yhteensä 96 Nvidia Ampere A100 -GPU:ta. Tämä osio soveltuu kaikenlaisille GPU:ita hyödyntäville työkuormille, jopa usealle solmulle skaalautuville raskaille tekoälymalleille. Osa A100-GPU:ista on jaettu pienemmiksi GPU:iksi, joissa on yksi seitsemäsosa täyden A100-GPU:n laskenta- ja muistikapasiteetista. Näitä voidaan käyttää interaktiivisiin työkuormiin, kursseihin ja koodin kehittämiseen.

Mahtiin asennetun [tieteellisen ohjelmiston](../apps/by_availability.md#mahti) valikoima on rajatumpi kuin Puhtissa.

- [Mahtin teknisempi kuvaus](systems-mahti.md)

## Roihu (tulossa pian) { #roihu-coming-soon }

CSC:n seuraava kansallinen supertietokone Roihu, BullSequana XH3000 -hybridijärjestelmä, korvaa Puhti- ja Mahti-supertietokoneet. Roihu sijoitetaan CSC:n Kajaanin konesaliin, ja sen arvioidaan olevan tutkijoiden käytössä alkuvuodesta 2026.

- [Lisätietoa Roihusta](systems-roihu.md)