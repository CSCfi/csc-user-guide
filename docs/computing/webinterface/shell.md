
# Shell {#shell}

Shell-sovellukset löytyvät _Näkyvät sovellukset_ -kohdasta tai ylävalikkorivin
_Työkalut_-osiosta. On olemassa kaksi erilaista shelliä.

_Login solmun shelli_ käynnistää normaalin Linux-shellin yhdestä sisäänkirjautumissolmuista.
Kaikki komennot, jotka ovat käynnissä sisäänkirjautumissolmun shell-selaimen välilehden sulkemisen yhteydessä,
pysähtyvät. Huomaa, että samat säännöt pätevät kuin normaalin SSH-istunnon aikana:

!!! error-label 
    **Sisäänkirjautumissolmut ovat ainoastaan kevyeen esikäsittelyyn/jälkikäsittelyyn**
    (katso [käyttöpolitiikka](../usage-policy.md)).

_Laskentasolmun shelli_ käynnistää pysyvän shellin laskentasolmussa raskaammille komennoille, joita ei tule
ajaa sisäänkirjautumissolmuissa. Pysyvä shelli jatkaa toimintaansa, vaikka sulkisit selaimen tai menettäisit
internet-yhteyden.
