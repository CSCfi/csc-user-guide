# Orkestrointi Heatillä {#orchestration-with-heat}

Tässä artikkelissa esitellään virtuaalikoneiden palveluorkestrointi OpenStack Heatia hyödyntäen Poudalle.

Voit käyttää tätä ominaisuutta verkkokäyttöliittymän vasemmassa paneelissa tai OpenStackin tai Heatin komentoriviohjelmalla. Orkestrointi tarjoaa helpon tavan luoda koko infrastruktuuri uudelleenkäytettävän ja ihmisen luettavissa olevan mallin avulla. Malli voi kuvata monia infrastruktuurin komponentteja, kuten palvelimia, levyjä ja kelluvia IP-osoitteita. Samassa tiedostossa voi liittää levyt ja IP-osoitteet tiettyihin instansseihin. Malli voi myös määrittää useita instansseja, jotka on yhdistetty tiettyihin verkkoihin, joista joillakin on kelluvia IP-osoitteita ja joillakin levy. Tiedostoa voi myös käyttää olemassa olevan infrastruktuurin muokkaamiseen.

### Orkestrointi verkkokäyttöliittymän kautta {#orchestration-via-the-web-user-interface}

!!! info

    Sinun tulisi käyttää "2018-08-31" ("rocky") tai vanhempia [Heatin malliversioina](https://docs.openstack.org/heat/latest/template_guide/hot_spec.html#rocky). Uudempien malliversioiden ominaisuudet eivät ehkä ole tuettuja.

Nämä ohjeet tarjoavat yksinkertaisen esimerkin pinojen asettamisesta verkkokäyttöliittymän kautta. Luodaksesi Heat-pinon, klikkaa "Stacks" linkkiä _Orchestration_ valikossa. Avaamassa näkymä näyttää kaikki olemassa olevat pinot ja tarjoaa painikkeen "Launch Stack" uuden pinon käynnistämiseen. Ikkunassa, joka avautuu "Launch Stack" painikkeen jälkeen, voit ladata olemassa olevan luomasi mallin tai voit aloittaa pinosi konfiguroinnin. Mallin valinta on pakollista, ja mallin tiedot voidaan myös antaa suorana syötteenä, kuten kuvassa esitetään. Huomaa, että kuva sisältää kelvollisen, mutta yksinkertaisen esimerkin mallista, joka rakentaa kaksi instanssia ja näyttää ensimmäisen instanssin IP-osoitteen.

![Mallin valinta](../../../img/stacks-view.png)

Tässä esimerkki:  
```yaml
heat_template_version: rocky # Kuten yllä mainittu, voit käyttää joko päivämäärää tai nimeä

description: Yksinkertainen malli yhden instanssin käyttöönottamiseksi cPoudassa

resources:
  instance0:
    type: OS::Nova::Server
    properties:
      image: Ubuntu-22.04
      flavor: standard.small
      key_name: my-key
      networks:
        - network: project_xxxxx

  instance1:
    type: OS::Nova::Server
    properties:
      image: Centos-7
      flavor: standard.small
      key_name: my-key
      networks:
        - network: project_xxxx

outputs:
  network0:
    description: Tulosta instance0:n verkot
    value: { get_attr: [instance0, networks] }
  network1:
    description: Tulosta instance1:n verkko
    value: { get_attr: [instance1, networks]}
```

Kun valitset "Next", verkkokäyttöliittymä kysyy pinoasi nimeä ja salasanaasi. Tämän jälkeen voit käynnistää pinon. Kun pino on rakennettu, sen hallinta onnistuu orkestroinnin _Stacks_ näkymässä. Pinon osana rakennetut kohteet löytyvät vastaavista valikoista. Tässä tapauksessa molemmat instanssit näkyvät ja niitä voi hallita instanssivalikossa. Pinon Yleiskatsaus-välilehdessä (Orchestration -&gt; Stacks -&gt; klikkaa pinoa) näet myös esimerkissä määritellyn "outputs" osion määritykset. Poistaaksesi kaikki pinon mallin luomat komponentit, paina yksinkertaisesti "Delete Stack" pinot-sivulla.

### Orkestroinnin käyttö komentoriviasiakkaalla {#using-orchestration-with-the-command-line-client}

!!! info

    Varmista, että `python-heatclient` on asennettu. Voit asentaa sen komennolla `pip install python-heatclient` (https://pypi.org/project/python-heatclient/)

Heatin käyttö onnistuu OpenStackin komentoriviasiakkaalla, mutta tällä hetkellä voit käyttää myös vanhentunutta Heatin komentoriviasiakasta. Luo pino komentorivillä:

```sh
openstack stack create -t /path/to/my/stack.yml my-heat-stack
```

Näytä uudenluodun pinon yksityiskohdat muiden olemassa olevien pinojen joukossa, syötä komento `openstack stack list`:

    openstack stack list
    +--------------------------------------+---------------+-----------------+----------------------+--------------+
    | ID                                   | Stack Name    | Stack Status    | Creation Time        | Updated Time |
    +--------------------------------------+---------------+-----------------+----------------------+--------------+
    | 98077bd5-9d69-47c3-98db-b0e19a60b1fa | my-heat-stack | CREATE_COMPLETE | 2016-06-08T07:34:46Z | None         |
    +--------------------------------------+---------------+-----------------+----------------------+--------------+

### Selitykset {#explanations}
Malli koostuu kahdesta pääosiosta:  
- Käytetty versio (`heat_template_version`)  
- Resurssi(t) (`resources`)  

Lisäksi on valinnaisia osioita, kuten:  
- Kuvaus (`description`)  
- Parametriryhmä(t) (`parameter_groups`)  
- Parametri(t) (`parameters`)  
- Tulosteet (`outputs`)  
- Ehto(t) (`conditions`)  

Tässä yksityiskohtaisesti jokaisesta osiosta:  

`heat_template_version`  
&nbsp;&nbsp;&nbsp;&nbsp; Ilmoittaa, että YAML-dokumentti on HOT (Heat Orchestration Template) -malli määritellyllä versiolla.

`description`  
&nbsp;&nbsp;&nbsp;&nbsp; Mahdollistaa mallin kuvauksen antamisen.

`parameter_groups`  
&nbsp;&nbsp;&nbsp;&nbsp; Mahdollistaa syöteparametrien ryhmittelyn ja parametrien tarjoamisjärjestyksen määrittämisen.

`parameters`  
&nbsp;&nbsp;&nbsp;&nbsp; Mahdollistaa syöteparametrien määrittämisen, jotka on annettava mallin käyttöönotossa.

`resources`  
&nbsp;&nbsp;&nbsp;&nbsp; Sisältää mallin yksittäisten resurssien julistuksen.

`outputs`  
&nbsp;&nbsp;&nbsp;&nbsp; Mahdollistaa tuotettujen parametrien määrittämisen, kun malli on instantoitu.

`conditions`  
&nbsp;&nbsp;&nbsp;&nbsp; Sisältää lausekkeita, joita voidaan käyttää rajoittamaan resurssin luomista tai ominaisuuden määrittämistä.

### Edistynyt esimerkki: mallin luominen yhden tai useamman instanssin rakentamiseksi {#advanced-example-create-a-template-to-build-one-or-more-instances}
Suunnitelmana on:  
- Luo parametrien tiedosto Openstack Heatille.  
- Luo kaksi Openstack Heat -mallia: yksi instanssien määrälle (OS::Heat::ResourceGroup) ja toinen käyttöönoton spesifikaatiolle.  
- Luo Ansible-skripti käyttöönoton automatisoimiseksi.  

!!! info

    Asenna seuraavat työkalut:  
    - [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)  
    - python-openstackclient (`pip install python-openstackclient`)  
    - python-heatclient (`pip install python-heatclient`)  

Ensiksi, voit luoda `heat_params.yaml` tiedoston, joka sisältää erilaisia muuttujia käytettäväksi instanssissasi. Käytä omia arvojasi:  

```yaml
parameter_defaults:
  ssh_key_name:
  vm_flavor:
  vm_image:
  vm_network:
  count:
```

Toiseksi, kaksi Openstack Heat -mallia. Ensimmäiseen otamme edelliset esimerkkimme muutamin muutoksin. Nimitämme sen `heat_stack_vm.yaml`:  

```yaml
heat_template_version: rocky # Kuten yllä mainittu, voit käyttää joko päivämäärää tai nimeä

description: Yksinkertainen malli yhden tai usean instanssin käyttöönottamiseksi cPoudassa

parameters: # Koska loimme heat_params.yaml, ne haetaan tästä tiedostosta
  ssh_key_name:
    description: SSH-avaimen nimi
    type: string
  vm_name:
    description: VM:n nimi
    type: string
  vm_flavor:
    description: VM:n flavor
    type: string
  vm_image:
    description: VM:n kuva
    type: string
  vm_network:
    description: VM:n verkko
    type: string

resources:
  instance:
    type: OS::Nova::Server
    properties:
      name: { get_param: vm_name } # Tämä arvo haetaan servers_group.yaml tiedostosta. Katso alla.
      image: { get_param: vm_image }
      flavor: { get_param: vm_flavor }
      key_name: { get_param: ssh_key_name }
      networks:
        - network: { get_param: vm_network }

outputs:
  network:
    description: Tulosta instanssien verkostot
    value: { get_attr: [instance, networks] }
```

Kolmanneksi, luomme tiedoston nimeltä `servers_group.yaml`, [ResourceGroup](https://docs.openstack.org/heat/latest/template_guide/openstack.html#OS::Heat::ResourceGroup), joka mahdollistaa instanssiemme skaalaamisen:  

```yaml
heat_template_version: rocky

description: Resource Group yhden tai useamman instanssin käyttöönottoa varten

parameters: # Parametri haetaan heat_params.yaml tiedostosta.
  count:
    description: Resurssien määrä
    type: string

resources:
  instances_group:
    type: OS::Heat::ResourceGroup
    properties:
      count: { get_param: count }
      resource_def:
        type: heat_stack_vm.yaml # Määrittelimme aiemman mallimme.
        properties:
          vm_name: test-stack-%index% # Arvo %index% kasvaa, jos luodaan useampi kuin yksi VM.

outputs:
  print_out:
    value: { get_attr: [instances_group, network] }
```

Lopuksi, luomme ansible-skriptin, joka rakentaa ja ottaa käyttöön vm-instanssimme. Nimetään se `build-heat-stack.yaml`:  

```yaml
- hosts: localhost
  gather_facts: false
  vars:
    heat_environment_file: "heat_params.yaml" # Varmista, että tiedosto sijaitsee build-heat-stack.yaml tasolla

  tasks:
    - name: Rakenna Heat-stack VM
      register: heat_stack
      os_stack:
        name: "{{ stack_name }}"
        state: present
        template: "servers_group.yaml" # Varmista, että tiedosto sijaitsee build-heat-stack.yaml tasolla
        environment: 
          - "{{ heat_environment_file }}"

    - name: Tulosta verkko
      debug:
        var: heat_stack
```

Aja cPouta-projektisi ympäristöön (`source project_xxxxx.sh`) ja suorita komento:   
```sh
ansible-playbook -e stack_name="test-stack" build-heat-stack.yaml`
```

Jos kaikki sujui hyvin, voit tarkistaa pinon luoduksi, joko käyttämällä cPoutan verkkoliittymää tai kirjoittamalla komento: `openstack stack list`.  
Voit myös tarkistaa luodut instanssit: `openstack server list`.

Jos poistat pinon, kaikki siitä luodut resurssit poistetaan myös.

### Heatin ohjeet ja komennon viitteet {#heat-guidelines-and-command-references}

Lisätietoja saatavilla OpenStackin [Heatin wikistä](https://wiki.openstack.org/wiki/Heat). Täydellinen viite OpenStackin komentoriviasiakkaalle löytyy [komentoriviviitteestä](http://docs.openstack.org/cli-reference/openstack.html).  
Tässä esimerkki GitHubistamme yhden tai useamman instanssin käyttöönotosta nginx:lla [Lue lisää GitHub-reposta](https://github.com/CSCfi/heat-openstack-example){ target="_blank" }