!!! success "Perustaso"
    HTTP-uudelleenohjauksen määrittäminen Rahtissa on erittäin helppoa nginxin kaltaisella verkkopalvelimella. Voimme ohjata käytännössä mihin tahansa URL-osoitteeseen hyvinkin monimutkaisilla säännöillä. Tässä ohjeessa pidämme sen yksinkertaisena ja ohjaamme toiseen isäntään, mutta säilytämme URL-osoitteen polun.

# Määritä HTTP-uudelleenohjaus Rahtissa { #setup-a-http-redirection-in-rahti }

## Menettely { #procedure }

1. Ota käyttöön NGINX-kuva. Suosittelemme käyttämään `bitnami/nginx`

    ![bitnami/nginx](../../img/bitnami-nginx-deploy.png)

1. Lisää Route sen URL-osoitteen kanssa, jonka haluat uudelleenohjata. Kun vierailet URL-osoitteessa, sinun pitäisi nähdä "nginx welcome page"

    ![route](../../img/create-route-nginx.png)

1. Lisää ConfigMap, jossa on palvelimen uudelleenohjauslohko. Siirry kohtaan **Workloads > ConfigMaps**, valitse **Create ConfigMap**. **Name**-arvoa käytetään myöhemmin ConfigMapin liittämisessä. **Key** on tiedoston nimi ja **Value** tiedoston sisältö. 

    ```nginx
    #default.conf
    server {
            listen *:8080;
            server_name test.com;
            return 301 $scheme://test2.com$request_uri;
    }
    ```

    Tässä esimerkissä `test.com` on alkuperäinen URL ja `test2.com` on se, jonne käyttäjä uudelleenohjataan.

1. Liitä ConfigMap nginx-deploymentsiin taltiona. Siirry deploymenttiin ja lisää seuraava koodi YAML-tiedostoon.

    ```yaml
    spec:
        containers:
          volumeMounts:
          - mountPath: /opt/bitnami/nginx/conf/server_blocks
            name: nginx-conf
          volumes:
          - configMap:
              defaultMode: 420
              name: nginx-config
            name: nginx-conf
    ```

    Tässä esimerkissä nginx-conf on configMapin **name**, nginx-config on **key**, ja ConfigMap on liitettävä polkuun `/opt/bitnami/nginx/conf/server_blocks/`. Muut imaget saattavat tallentaa nginxin konfiguraation eri kansioihin.

## Lisää useampia isäntäverkkotunnuksia { #add-more-host-domains }

Jos sinun täytyy ohjata useampi kuin yksi isäntäverkkotunnus, voit käyttää samaa nginx-palvelinta. Sinun tarvitsee vain (1) lisätä uusi Route uudella isännällä ja (2) lisätä uusi server-lohko olemassa olevaan ConfigMapiin. Jotta nginx ottaa uuden konfiguraation käyttöön, voit joko poistaa Podin tai mennä Podin terminaaliin ja suorittaa `nginx -s reload`.

## Yhteenveto ja muuta { #conclusion-and-more }

Nginx on tehokas verkkopalvelin. Voit käyttää sitä myös HTTP-välityspalvelimena ja kuormantasaajana. Lisätietoja on dokumentaatiossa: <https://nginx.org/en/docs/>.