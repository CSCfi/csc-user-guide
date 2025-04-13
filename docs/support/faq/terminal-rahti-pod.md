
# Kuinka avata pääte Podille? {#how-to-open-a-terminal-to-a-pod}

Jotta voit avata päätteen **Käynnissä** -tilassa olevalle Podille, on kaksi vaihtoehtoa:

## Käyttäen verkkokäyttöliittymää {#using-the-web-interface}

1. Kirjaudu Rahtin verkkokäyttöliittymään ja siirry kohtaan **Projekti > Podit**. (Tai **Kuormitukset > Podit** ylläpitäjän näkymässä)

1. Klikkaa minkä tahansa **Käynnissä** -tilassa olevan Podin nimeä.

1. Klikkaa **Pääte**-välilehteä nähdäksesi päätteen.

![Terminal Pod](img/terminal.png)

## Käyttäen komentoriviä `oc`:llä {#using-the-command-line-with-oc}

1. Ensin, hanki Podin nimi, johon haluat avata interaktiivisen päätetilaisuuden:

	```sh
	$ oc get pods
	NAME                READY     STATUS      RESTARTS   AGE
	django-ex-1-build   0/1       Completed   0          2h
	django-ex-1-svwg2   1/1       Running     0          2h
	django-ex-1-rtbak   1/1       Running     0          2h
	```

1. Näemme, että pääte joko `django-ex-1-svwg2` tai `django-ex-1-rtbak` -nonatomic voi avata.

	```sh
	oc rsh pod/django-ex-1-rtbak
	```
