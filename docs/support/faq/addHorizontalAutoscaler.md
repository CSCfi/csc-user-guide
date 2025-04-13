# Kuinka automaattisesti skaalata replikoita ylös ja alas

Rahti mahdollistaa automaattisen horisontaalisen skaalauksen CPU- ja muistin kulutuksen perusteella. Tämä tarkoittaa, että alusta voidaan määrittää lisäämään sovelluksesta enemmän kopioita (skaalata ylös), kun nykyiset kopiot kuluttavat liikaa CPU:ta ja/tai muistia, ja poistamaan sovelluksen kopioita (skaalata alas), kun CPU:n ja/tai muistin kulutus on liian alhainen, ja pienempi määrä kopioita riittää nykyiselle kuormalle.

!!! info "Horisontaalinen/Vertikaalinen skaalaminen"

    Horisontaalinen skaalaminen tarkoittaa, että sovelluksesta lisätään enemmän kopioita tai replikoita. Kubernetesissa tämä tarkoittaa, että enemmän palkeleita (Pods) suoritetaan samalla säilöllä ja parametreilla. Virtuaalikoneissa tämä tarkoittaa, että lisätään enemmän virtuaalikoneita samalla mallilla ja kuvalla.

    Vertikaalinen skaalaminen on, kun nykyiseen kopioon lisätään enemmän resursseja. Kubernetesissa tämä tarkoittaa, että asetetaan korkeammat CPU- tai muistirajat. Virtuaalikoneissa se tarkoittaa koneen uudelleenluontia suuremmalla mallilla, jossa on enemmän CPU:ta tai muistia.

Tämän selvä hyöty on, että se mahdollistaa resurssien kulutuksen automaattisen ja dynaamisen optimoinnin. Se alentaa sovelluksen ylläpitäjän kustannuksia, koska sovelluksella on vain satunnaisesti korkea kuorma. Skaalautumisajan vasteaika on sekunneissa, ja kun se on oikein säädetty, se voi tarjota saumattoman kokemuksen sovelluksen käyttäjille.

## Määritykset {#setup}

Tätä varten tarvitsemme ensin `Deploymentin`. Mikä tahansa käyttöönotto toimii, mutta voit käyttää tätä esimerkkiä, joka ottaa käyttöön kuvitteellisen sovelluksen:

**Huom:** Muista ensin [kirjautua Rahiin](../../cloud/rahti/usage/cli.md#how-to-login-with-oc)

```sh
echo "apiVersion: apps/v1
kind: Deployment
metadata:
  name: example
spec:
  selector:
    matchLabels:
      app: httpd
  replicas: 4
  template:
    metadata:
      labels:
        app: httpd
    spec:
      containers:
        - name: httpd
          image: docker.io/lvarin/oom-killer
          command:
           - /app/app.py
           - '10'
          ports:
            - containerPort: 8080
" | oc create -f -
```

Tämän käyttöönoton tulisi nyt pyörittää 4 kopiota samasta `Podista`. Myöhemmin määritämme sen vähentämään tai lisäämään Podien määrää resurssienkulutuksen perusteella.

### Lisää resurssirajoja {#add-resources-limits}

![Toiminnot>MuokkaaResurssirajoja](../../cloud/img/editResourceLimits.png){ align=right }

Seuraava askel on asettaa resurssirajoituksia CPU:lle ja muistille. Tämä on se CPU:n ja muistin enimmäismäärä, jota kukin Pod pystyy käyttämään. Deployment-sivulta mene **Toiminnot > Muokkaa resurssirajoja**

Sinun on asetettava rajoitus (per Pod) CPU:lle ja muistille. "Pyynnön" kenttää ei tarvitse täyttää.

Tässä esimerkissä asetamme:

* `1` CPU-rajoitus.
* `1` Gi muistirajaksi.

![Muokkaa Resurssirajoja](../../cloud/img/editResourceLimitsDialog.png)

### Lisää HorisontaalinenSkaalaaja {#add-the-horizontalautoscaler}

Kun Pod-rajat on asetettu, voit nyt lisätä horisontaalisen automaattisäätäjän. Deployment-sivulta mene **Toiminnot > Lisää horisontaalinen Pod-automaattisäätäjä**.

![Toiminnot>LisääHorisontaalinenSkaalaaja](../../cloud/img/addHorizontalAutoscaler.png){ align=right }

Aseta ensin replikoinnin **maksimi** ja **minimi** määrä. Yleensä minimimääräksi jätetään 1 ja maksimimääräksi asetetaan arvo, joka on "reilu osuus" kokonaiskiintiöstä. Esimerkiksi, jos kiintiö on yhteensä 20 Podille ja on yksittäinen käyttöönotto, enimmäismääräksi tulisi asettaa 20, jotta käytetään kaikki saatavilla olevat kiintiö. Mutta jos jakaa saman nimisen tilan kahden käyttöönoton välillä, maksimi pitäisi asettaa arvoon 10 kummallekin.

Kun vähimmäis- ja enimmäisarvot on asetettu, meidän tulee konfiguroida se % resurssikäytöstä, joka käynnistää skaalaamisen ylös. Voidaan asettaa yksi tai molemmat kahdesta resurssista (CPU ja muisti). Mikä raja ja mihin resurssiin riippuu ajamastasi sovelluksesta. Jotkin sovellukset ovat enemmän CPU-käyttäjäintensiivisiä, toiset muistintensiivisiä, ja jotkut ovat molempia. Käytännössä se on iteratiivinen prosessi parametrien säätämiseksi.

Kun konfiguroitujen resurssien käyttö ylittyy, luodaan uusi kopio. Esimerkiksi asetamme 50% muistista 1 Gi:n rajalla. Kun muistin käyttö saavuttaa ja ylittää 500MB, luodaan uusi kopio, joka kaksinkertaistaa käytettävissä olevan muistin. Tämä skaalaus jatkuu, kunnes kokonaismuistin käyttö ylittää 50% käytettävissä olevasta muistista.

Toisaalta, skaalaus alaspäin tapahtuu, kun lisäkapasiteettia ei enää tarvitse, esim.: Kun yhden kopion poistamisen jälkeen käytetyn muistin määrä ei ylitä 50% saatavilla olevasta muistista skaalaus alaspäin tapahtumisen jälkeen.

![Lisää Horisontaalinen Pod Automaattisäätäjä -dialogi](../../cloud/img/addHorizontalPodAutoscalerDialog.png)

Tässä esimerkissä asetamme:

* `1` Podien vähimmäismääräksi.
* `4` Podien enimmäismääräksi.
* `50`% muistinkäytöstä.

Emme koske CPU:n käyttöön. 

## Testaa ja seuraa {#test-and-monitor}

Muutaman minuutin kuluttua pitäisi olla vain yksi Pod, jossa on lähes nolla CPU:n käyttöä ja 100MB muistinkäyttöä. Automaattisäätäjä odottaa jopa 10 minuuttia poistaakseen Podeja välttääkseen räpyttelyä, lisätietoja alla. Voit tarkistaa tämän `Podit`-sivulta (**Projekti > Podit** kehittäjäsivulla).

![Podit](../../cloud/img/podsAutoscaler.png)

!!! info "CLI:n käyttäminen"

    Voit käyttää komentorivikäyttöliittymää saadaksesi nykyisen automaattisäätäjän tilan:
    ```
    $ oc get HorizontalPodAutoscaler example   
    NAME      REFERENCE            TARGETS          MINPODS   MAXPODS   REPLICAS   AGE
    example   Deployment/example   9%/50%, 0%/50%   1         4         1          1h
    ```

Tähän tarvitaan vain yksi Pod, koska käytetään vain ~100MB yhteensä 1 Gi muistin kapasiteetista. Tämä on vähemmän kuin 50% muistissa, jonka olemme konfiguroineet. Nyt nostamme muistin käyttöä keinotekoisesti. Menemme sillä hetkellä käynnissä olevan yksittäisen Podin terminaaliin (Klickaa Podin nimeä ja sitten "Terminaali"-välilehteä), ja suoritamme seuraavan komennon:

```sh
/app/app.py 5 100
```

Tämä käynnistää uuden prosessin, joka varaa 5 kpl 100MB RAM:ia. Koska 100+500 MB on yli 50% yhteensä 1 Gi muistista, uusi Pod luodaan automaattisäätäjän toimesta. 

![2 Podia](../../cloud/img/pods2Autoscaler.png)

Seuraa tilannetta ja odota toisen Podin luomista. Resurssit voidaan seurata projektin pääsivulta, tämä antaa yleisen näkemyksen koko projektista, mukaan lukien kiintiön käyttö. Vaihtoehtoisesti voit siirtyä luodun käyttöönoton sivulle (Projektista, mene **Deployment**, klikkaa **example**, ja lopuksi Metrics-välilehteä.

Tämän jälkeen voit lopettaa luomasi prosessin ja nähdä, kuinka sovellus skaalautuu alas tappamalla toisen Podin.

!!! Info "Skaalaus alaspäin viive"
    Tarkoituksena on, että skaalaus ylös on mahdollisimman nopeaa, mutta skaalaus alaspäin voi kestää jopa 10 minuuttia. Tämä johtuu vakautusikkunasta, [kuluuvan Kubernetes dokumentaation](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#stabilization-window) mukaan:

    > Vakautusikkunaa käytetään rajoittamaan säätelyä replikoiden määrässä, kun skaalautumiseen käytettävät mittarit vaihtelevat. Autoskaalausalgoritmi käyttää tätä ikkunaa havaitakseen aiemman toivotun tilan ja välttääkseen ei-toivottuja muutoksia työkuorman skaalaamisessa.