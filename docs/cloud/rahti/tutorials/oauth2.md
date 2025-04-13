
# Kuinka ottaa käyttöön OAuth2-proxy Rahtissa {#how-to-deploy-oauth2-proxy-in-rahti}

Selitämme, kuinka ottaa käyttöön ja käyttää [OAuth2 Proxy](https://oauth2-proxy.github.io/oauth2-proxy/) käytettävissä autentikoinnin hallintaan
käyttäen tarjoajia kuten Google, GitHub ja muita.

Tässä opetusohjelmassa käymme läpi, miten käyttää GitHubia

!!! varoitus
    Tämä on yksinkertainen esimerkkitoteutus. Luonnollisesti sovelluksesi tulisi pystyä hallitsemaan pääsyä ryhmien, sähköpostin, käyttäjätunnuksen jne. perusteella.

## Ota web-sovelluksesi käyttöön {#deploy-your-web-application}

Ensiksi otamme käyttöön hyvin yksinkertaisen web-sovelluksen, tämän [flask-demo](https://github.com/CSCfi/rahti-flask-hello). Seuraa ohjeita
GitHub-reposta.

Älä luo Routea, sitä ei tarvita, koska käytämme `NGINX`:ää käänteisenä proxy-palvelimena.

## Ota NGINX käyttöön {#deploy-nginx}

Voit käyttää meidän [NGINX-kuvaamme](https://github.com/CSCfi/nginx-okd) ajaaksesi NGINX:ää Rahtissa (OpenShift 4)

Rahatissa voit suoraan rakentaa kuvan. Lisätietoa [täältä](../images/creating.md#using-the-source-to-image-mechanism)

Suorita tämä komento:

```sh
oc new-app https://github.com/CSCfi/nginx-okd
```

Kun koonti on valmis, suorita tämä komento luodaksesi Route:

```sh
oc create route edge flask-demo --service=nginx-okd --hostname=demo-oauth2.2.rahtiapp.fi --insecure-policy='Redirect' --port=8081
```

!!! tieto
    Voit asettaa oman `--hostname`:n. Tässä esimerkissä käytämme Rahtin oletusdomainia `2.rahtiapp.fi`.

    Voit myös käyttää omaa domainiasi, mutta tässä tapauksessa sinun on luotava `Ingress`.
    Lisätietoa [täältä](https://kubernetes.io/docs/concepts/services-networking/ingress/)

Meidän on luotava erityinen konfiguraatio, jotta NGINX toimisi käänteisenä proxy-palvelimena. Tätä varten käytämme [ConfigMapia](../concepts.md#configmap)

Luo uusi `configmap.yaml` tiedosto:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-default
data:
  default.conf: |
    server {
      listen 8081; # NGINX-palvelun portti
      server_name demo-oauth2.2.rahtiapp.fi; # Sama kuin aiemmin Routeen luotu --hostname
    
    location /oauth2/ {
      proxy_pass       http://oauth2-proxy:4180;
      proxy_set_header Host                    $host;
      proxy_set_header X-Real-IP               $remote_addr;
      proxy_set_header X-Auth-Request-Redirect $request_uri;
      # tai jos käsittelet useita domaineja:
      # proxy_set_header X-Auth-Request-Redirect $scheme://$host$request_uri;
    }
    
    location = /oauth2/auth {
      proxy_pass       http://oauth2-proxy:4180;
      proxy_set_header Host             $host;
      proxy_set_header X-Real-IP        $remote_addr;
      proxy_set_header X-Forwarded-Uri  $request_uri;
      # nginx auth_request sisältää otsikot mutta ei vartaloa
      proxy_set_header Content-Length   "";
      proxy_pass_request_body           off;
    }
    
    location / {
      root   /usr/share/nginx/html;
      index  index.html index.htm;
      auth_request /oauth2/auth;
      error_page 401 =403 /oauth2/sign_in;
    
      # siirrä tiedot X-User ja X-Email otsikoiden kautta backendille
      # vaatii, että ajetaan --set-xauthrequest lippu mukana
      auth_request_set $user   $upstream_http_x_auth_request_user;
      auth_request_set $email  $upstream_http_x_auth_request_email;
      proxy_set_header X-User  $user;
      proxy_set_header X-Email $email;
      proxy_set_header Host $http_host;
    
      # jos otit käyttöön --pass-access-token, tämä välittää tokenin backendille
      auth_request_set $token  $upstream_http_x_auth_request_access_token;
      proxy_set_header X-Access-Token $token;
    
      # jos otit käyttöön --cookie-refresh, tätä tarvitaan sen toimimiseksi auth_requestin kanssa
      auth_request_set $auth_cookie $upstream_http_set_cookie;
      add_header Set-Cookie $auth_cookie;
    
      # Kun käytät --set-authorization-header lippua, joidenkin tarjoajien evästeet voivat ylittää 4 kb
      # rajan ja siksi OAuth2 Proxy jakaa ne useampaan osaan.
      # Nginx kopioi normaalisti vain ensimmäisen `Set-Cookie` otsikon auth_requestista vasteeseen,
      # joten jos evästeesi ovat suurempia kuin 4 kb, sinun on manuaalisesti noudettava ylimääräisiä evästeitä.
      auth_request_set $auth_cookie_name_upstream_1 $upstream_cookie_auth_cookie_name_1;
    
      # Hae evästeattribuutit ensimmäisestä Set-Cookie-otsikosta ja liitä ne
      # toiseen osaan ($upstream_cookie_* muuttujat sisältävät vain raakatiedon evästeisiin)
      if ($auth_cookie ~* "(; .*)") {
          set $auth_cookie_name_0 $auth_cookie;
          set $auth_cookie_name_1 "auth_cookie_name_1=$auth_cookie_name_upstream_1$1";
      }
    
      # Lähetä molemmat Set-Cookie-otsikot nyt, jos oli toinen osa
      if ($auth_cookie_name_upstream_1) {
          add_header Set-Cookie $auth_cookie_name_0;
          add_header Set-Cookie $auth_cookie_name_1;
      }
    
      proxy_pass http://course-flask-demo:8080/; # Aseta backend-si, jonne sinut ohjataan. Tässä, meidän flask-demo web-sovellus. Se on palvelun nimi ja sen portti.
    # tai "root /polku/sivustoon;" tai "fastcgi_pass ..." jne
    }
    
      error_page   500 502 503 504  /50x.html;
      location = /50x.html {
        root   /usr/share/nginx/html;
      }
    }
```

Löydät lisätietoa tästä konfiguraatiosta [OAuth2 Proxy verkkosivustolta](https://oauth2-proxy.github.io/oauth2-proxy/configuration/integration)

Tärkeimmät arvot muokattavaksi tässä ConfigMapissa ovat:

- `listen 8081`: Mikä edustaa NGINX-palvelun porttia
- `server_name`: Sama kuin aiemmin Routeen luotu --hostname
- `proxy_pass`: Aseta backendisi, jonne sinun tulisi tulla ohjatuksi. Tässä, meidän flask-demo web-sovellus. Se on palvelun nimi ja sen portti.

Sovella ConfigMap-konfiguraatiota:

```sh
oc apply -f configmap.yaml
```

## Luo GitHub OAuth-sovelluksesi {#create-your-github-oauth-apps}

Sinun on mentävä [GitHubiin](https://github.com/settings/developers) > OAuth Apps

Klikkaa uutta OAuth-sovellusta

![New GitHub OAuth App](../../img/GitHub-new-oauth-app.png)

Täytä eri kentät:

- **Sovelluksen nimi**: Anna nimi GitHub OAuth -sovelluksellesi
- **Kotisivu-URL**: Web-sovelluksesi kotisivu. Tässä esimerkissä se on NGINX:n käänteisen proxyn reitti (`https://demo-oauth2.2.rahtiapp.fi`)
- **Valtuutuksen palautus-URL**: Sovelluksesi palautus-URL. Tässä esimerkissä se on kuin `https://demo-oauth2.2.rahtiapp.fi/oauth2/callback`

## Ota käyttöön OAuth2 Proxy {#deploy-oauth2-proxy}

Jotta voit ottaa käyttöön [OAuth2 Proxy](https://oauth2-proxy.github.io/oauth2-proxy/):n, käytämme .yaml tiedostoa. Luo uusi tiedosto nimeltä `oauth2.yaml` ja kopioi tämä:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    k8s-app: oauth2-proxy
  name: oauth2-proxy
spec:
  replicas: 1
  selector:
    matchLabels:
      k8s-app: oauth2-proxy
  template:
    metadata:
      labels:
        k8s-app: oauth2-proxy
    spec:
      containers:
      - args:
        - --provider=github
        - --client-id=<CLIENT_ID_FROM_GITHUB>
        - --client-secret=<CLIENT_SECRET_FROM_GITHUB>
        - --redirect-url=https://demo-oauth2.2.rahtiapp.fi/oauth2/callback
        - --email-domain=*
        - --reverse-proxy=true
        - --upstream=static://200
        - --http-address=0.0.0.0:4180
        - --set-authorization-header=true
        - --set-xauthrequest=true
        - --pass-access-token=true
        - --pass-authorization-header=true
        - --pass-user-headers=true
        - --pass-host-header=true
        - --cookie-secret=<YOUR_COOKIE_SECRET>
        image: quay.io/oauth2-proxy/oauth2-proxy:latest
        imagePullPolicy: Always
        name: oauth2-proxy
        ports:
        - containerPort: 4180
          protocol: TCP
        resources: {}

---

apiVersion: v1
kind: Service
metadata:
  labels:
    k8s-app: oauth2-proxy
  name: oauth2-proxy
spec:
  ports:
  - name: http
    port: 4180
    protocol: TCP
    targetPort: 4180
  selector:
    k8s-app: oauth2-proxy
```

Tärkeimmät asiat ovat:

- `--provider=github`
- `--client-id=` Kopio GitHub OAuth Appsista, joka luotiin aiemmin
- `--client-secret=` Kopio GitHub OAuth Appsista, joka luotiin aiemmin
- `--cookied-secret=` Voit luoda yhden suorittamalla tämän komennon: `docker run -ti --rm python:3-alpine python -c 'import secrets,base64; print(base64.b64encode(base64.b64encode(secrets.token_bytes(16))));'`

Kun tämä on tehty, sovella konfiguraatio:

```sh
oc apply -f oauth2.yaml
```

## Lähes valmis {#almost-done}

Nyt kun meillä on:

1. Web-sovelluksemme
2. NGINX käänteisenä proxy-palvelimena
3. GitHub OAuth -sovelluksemme
4. Käytössä oleva OAuth2-proxy

Meidän on kerrottava NGINX:lle, että sen on kommunikoitava OAuth2 Proxy:n kanssa, joka tavoittaa GitHubin, jotta voimme päästä käsiksi web-sovellukseemme

Tässä on kaavio:

![OAuth2 kaavio](../../img/oauth2.png)

Muistatko, että loimme aiemmin ConfigMapin? Mikä sen tarkoitus on? No, se tulee olemaan uusi NGINX:n oletuskonfiguraatiotiedosto.

Luo `patch-configmap.yaml` tiedosto:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-okd
spec:
  template:
    spec:
      containers:
        - name: nginx-okd
          volumeMounts:
            - mountPath: /etc/nginx/conf.d/
              name: nginx-default
      volumes:
        - configMap:
            name: nginx-default
            defaultMode: 420
          name: nginx-default
```

Korjaa deployisi:

```sh
oc patch deploy/nginx-okd --patch-file=patch-configmap.yaml
```

Tämä käynnistää automaattisesti uuden NGINX-podin käyttöönoton.

Kun pod on valmis, voit kokeilla uutta konfiguraatiotasi. Avaa websovellussivustosi (sen pitäisi olla NGINX:n käyttöönotossa luotu reitti
eli https://demo-oauth2.2.rahtiapp.fi tässä esimerkissä).

Sinun pitäisi nähdä OAuth2 Proxy -kotisivu ja **Kirjaudu GitHubilla** -painike.

![oauth2 proxy kotisivu](../../img/oauth2-proxy-homepage.png)

Jatka

Kun olet vahvistanut tunnistetietosi ja antanut GitHubille oikeuden päästä tietoihisi, sinut pitäisi ohjata websovellukseen:

![Flask kotisivu](../../img/flask-demo-homepage.png)

# Muutama huomio {#few-comments}

Onneksi olkoon! Onnistuit ottamaan käyttöön OAuth2 Proxyn päästäksesi verkkosivustollesi.

Pidä mielessä, että tämä esimerkki ei kontrolloi nimeä, käyttäjätunnusta tai sähköpostia. Hyvän sovelluksen on pystyttävä tarkistamaan esimerkiksi sähköposti ja
päästämään käyttäjä sovelluksiin tai ei.

Tässä esimerkki OAuth2 Proxy + Kubernetes-Dashboard: <https://kubernetes.github.io/ingress-nginx/examples/auth/oauth-external-auth/#example-oauth2-proxy-kubernetes-dashboard>

Tässä esimerkissä on mahdollista antaa pääsy klusteriin kontrolloimalla käyttäjän sähköpostia [kubernetes RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/):lla

