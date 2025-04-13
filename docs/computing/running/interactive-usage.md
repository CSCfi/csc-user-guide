
# Interaktiivinen käyttö

Kun kirjaudut CSC:n supertietokoneelle, yhdistät sen johonkin sen kirjautumissolmuista. Kirjautumissolmuja jakavat kaikki käyttäjät, eikä niitä tule käyttää raskaaseen laskentaan. [Katso käyttöpolitiikkamme yksityiskohdat](../usage-policy.md). Jos sinun täytyy suorittaa raskaita laskentoja interaktiivisesti, voit käyttää Puhtin ja Mahtin `interactive`-osioita.

`Interactive`-osio tarjoaa vähemmän resursseja kuin muut osiot, mutta sinne lähetetyillä töillä on paljon korkeampi prioriteetti, joten ne viettävät tyypillisesti hyvin vähän aikaa jonossa. Osio voidaan käyttää [web-käyttöliittymäsovellusten](../webinterface/apps.md) ja [erätöiden](getting-started.md) ajamiseen, mutta kätevin tapa käyttää sitä on `sinteractive`-komennolla.

## `sinteractive`-komento {#the-sinteractive-command}

`sinteractive` käynnistää uuden shell-ohjelman laskentasolmussa käyttäjän määrittelemillä resursseilla. Prosessit voidaan käynnistää ikään kuin käyttäisit omaa laitettasi, eli Slurm-komennot kuten `srun` eivät ole tarpeellisia tai edes mahdollisia. Shell-ympäristö eroaa hieman kirjautumissolmuista, esim. "raskaammat" tekstieditorit kuten Vim ja Emacs eivät ole saatavilla, joten niiden sijasta on käytettävä Vi:tä tai Nanoa.

Koska `sinteractive` käynnistää uuden shellin, kaikki ympäristömuuttujat, joita ei aseteta käyttäjän aloitustiedostoissa, on määriteltävä uudelleen manuaalisesti. Kun interaktiivinen istunto päättyy, palaat alkuperäiseen shell-ohjelmaasi, ja kaikki istunnon aikana `$TMPDIR`:iin ja `$LOCAL_SCRATCH`:iin kirjoitettu väliaikainen data häviää.

Vaikka graafisten sovellusten suositeltu käyttötapa on [virtuaalidesktoppi](../webinterface/desktop.md), on myös mahdollista tehdä tämä interaktiivisessa istunnossa komentoriviltä käsin [käyttäen X11-ohjailua](#starting-an-interactive-application-with-x11-graphics).

Helpoin tapa käyttää `sinteractive`-komentoa on ajaa komento `-i`-vaihtoehdolla:

```bash
sinteractive -i
```

Kun tämä vaihtoehto valitaan, käyttäjältä kysytään istunnon yksittäiset parametrit (suoritusaika, muisti, ytimet, jne.). Jos et halua määritellä resursseja interaktiivisesti, voit yksinkertaisesti välittää ne komennolle argumentteina. Huomaa, että Puhtissa ja Mahtissa saatavilla olevat vaihtoehdot ja resurssit eivät ole samat laitteiston eroista johtuen.

### `sinteractive` Puhtissa {#sinteractive-on-puhti}

Puhtissa jokaisella käyttäjällä voi olla enintään kaksi aktiivista istuntoa `interactive`-osiossa.

Jos resurssipyyntösi ylittävät [Puhtin `interactive`-osion rajat](./batch-job-partitions.md#puhti-interactive-partition), tai jos sinulla on jo kaksi aktiivista istuntoa siellä, sinulle tarjotaan mahdollisuus lähettää työ `small`- tai `gpu`-osioihin sen sijaan. Tässä tapauksessa työsi ei hyödynnä `interactive`-osion korkeampaa prioriteettia, joten sinun on odotettava jonkin aikaa ennen kuin pyydetyt resurssit tulevat saataville ja interaktiivinen istunto alkaa. Jos pyydät GPU:ita `-g`-vaihtoehdolla, työsi lähetetään automaattisesti `gpu`-osioon.

Kaikki `sinteractive`-komennolla käynnistetyt istunnot suoritetaan solmuilla, joilla on [nopea paikallinen NVMe-tallennus](../disk.md#compute-nodes-with-local-ssd-nvme-disks) saatavilla. Tämä paikallinen levyalue on ihanteellinen sijainti prosessiesi luomille väliaikaistiedostoille korkean I/O-kapasiteettinsa ansiosta. Muista, että tämä levyalue tyhjennetään, kun interaktiivinen istunto päättyy. Ympäristömuuttujat `$TMPDIR` ja `$LOCAL_SCRATCH` osoittavat työn paikalliseen levyalueeseen.

Voit nähdä Puhtin komentovaihtoehdot seuraavasti, kun olet kirjautuneena järjestelmään:

```bash
sinteractive --help
```

### `sinteractive` Mahtissa {#sinteractive-on-mahti}

Mahtissa jokaisella käyttäjällä voi olla jopa 8 aktiivista istuntoa `interactive`-osiossa. Katso [Mahtin `interactive`-osion yksityiskohdat](batch-job-partitions.md#mahti-cpu-partitions-with-core-based-allocation) saadaksesi tietoa saatavilla olevista resursseista. On myös mahdollista pyytää [GPU-leikkauksia](./batch-job-partitions.md#gpu-slices) interaktiiviseen työhön käyttämällä `-g`-lippua, joka lähettää työn `gpusmall`-osioon. Huomaa, että GPU-leikkauksen käyttäminen rajoittaa käytettävissä olevien CPU-ytimien ja muistin määrää työssäsi.

Kuten Puhtissa, voit nähdä Mahtin erikoiskomentovaihtoehdot seuraavasti kirjautuneena järjestelmään:

```bash
sinteractive --help
```

### Esimerkki: Jupyter-muistikirjan tai RStudio-palvelimen ajo `sinteractive`:lla {#example-running-a-jupyter-notebook-or-rstudio-server-via-sinteractive}

Katso opetusohjelma [RStudion tai Jupyter-muistikirjojen käytöstä](../../support/tutorials/rstudio-or-jupyter-notebooks.md).

### Esimerkki: MPI-työn suorittaminen interaktiivisessa istunnossa {#example-running-an-mpi-job-in-an-interactive-session}

Koska interaktiivisessa istunnossa käynnistetty shell on jo Slurm-työvaihe, lisätyövaiheita ei voida luoda. Tämä estää esim. GROMACS-työkalujen käyttämisen tavanomaisella tavalla, koska `gmx_mpi` on rinnakkainen ohjelma ja yleensä edellyttää `srun`-käyttöä. Tässä tapauksessa `srun` on korvattava `orterun -n 1`-komennolla interaktiivisessa shellissä. Orterun ei tunnista Slurm-lippuja, joten sille on kerrottava, montako tehtävää/kierrettä käytetään. Seuraava esimerkki suorittaa [GROMACS](../../apps/gromacs.md)-ohjelman keskimääräisen siirtymäanalyysin olemassa olevalle trajektorialle:

```bash
sinteractive --account <project>
module load gromacs-env
orterun -n 1 gmx_mpi msd -n index.ndx -f traj.xtc -s topol.tpr
```

Käyttääksesi kaikkia pyydettyjä ytimiä rinnakkain, sinun täytyy lisätä `--oversubscribe`. Esimerkiksi 4 ytimen rinnakkainen interaktiivinen työ (käynnistetty *interaktiivisesta istunnosta*) voidaan suorittaa seuraavasti:

```bash
sinteractive --account <project> --cores 4
module load gromacs-env
orterun -n 4 --oversubscribe gmx_mpi mdrun -s topol.tpr
```

## Eksplisiittinen interaktiivinen shell ilman X11-grafiikkaa {#explicit-interactive-shell-without-x11-graphics}

Jos et halua käyttää `sinteractive`-suojainta, on myös mahdollista käyttää Slurm-komentoja eksplisiittisesti interaktiivisen istunnon käynnistämiseen. Koska voit joutua jonottamaan, on suositeltavaa pyytää sähköposti-ilmoitusta resurssien myöntämisen jälkeen.

```bash
srun --ntasks=1 --time=00:10:00 --mem=1G --pty \
     --account=<project> --partition=small --mail-type=BEGIN \
     bash
```

Kun resurssit ovat saatavilla, voit työskennellä normaalisti shellissä. Bash-kehote näyttää laskentasolmun nimen:

```bash
[username@r07c02 ~]$
```

Kun pyydetty aika on kulunut umpeen, shell sulkeutuu automaattisesti.

## Interaktiivisen sovelluksen käynnistäminen X11-grafiikalla {#starting-an-interactive-application-with-x11-graphics}

Aktivoidaksesi X11-grafiikat lisää `--x11=first`-vaihtoehto komentoon. Seuraavasti käynnistyy sovellus `myprog`:

```bash
srun --ntasks=1 --time=00:10:00 --mem=1G --x11=first --pty \
     --account=<project> --partition=small --mail-type=BEGIN \
     myprog
```

Huomaa, että voit korvata `myprog`-ohjelman `bash`-komennolla, joka käynnistää shellin laskentasolmussa, jota voit puolestaan käyttää graafisten sovellusten käynnistämiseen. Kun pyydetty aika on kulunut umpeen, sovellus suljetaan automaattisesti.

