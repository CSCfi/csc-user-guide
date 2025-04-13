
# Suorituskykyiset kirjastot {#high-performance-libraries}

Eri suorituskykyisiä kirjastoja tiheään lineaarialgebraan, nopeisiin
Fourier-muunnoksiin *jne.* on saatavilla modulesysteemin kautta. Monet
kirjastot ovat saatavilla sekä yksisäikeisinä että monisäikeisinä
versioina, monisäikeiset moduulit on merkitty `omp` moduuliversiossa.
Puhtaissa MPI-sovelluksissa ja sovelluksissa, joissa kutsutaan kirjastoja
useista säikeistä, suositellaan käyttämään yksisäikeistä kirjastoa.

Kirjastojen saatavuus voi riippua ladatusta kääntäjäpaketista ja
MPI-ympäristöstä, käytä `module avail` nähdäksesi saatavilla olevat
kirjastot. Katso kirjaston dokumentaatiosta ohjeet kuinka rakentaa
tietylle kirjastolle. Huomaa, että useimmat moduulit asettavat
`LIBRARY_PATH` ja `LD_LIBRARY_PATH` ympäristömuuttujat, joten
`-llibrary` linkkauslippu on usein riittävä. Useimmat moduulit asettavat
myös `<library>_INSTALL_ROOT` ympäristömuuttujat, joita voidaan
hyödyntää räätälöidyissä rakennusskripteissä. Esimerkiksi `fftw`
kirjastoa voidaan käyttää seuraavasti:

```bash
module load fftw
<compiler_command> -o myprog myprog.o -lfftw3
```

ja hakemisto, joka sisältää `include`, `lib`, *jne.*, löytyy
`FFTW_INSTALL_ROOT` ympäristömuuttujan alta.

## Kirjastot Puhtissa {#libraries-in-puhti}

Puhtissa saatavilla olevat valitut kirjastot:

- Tiheä lineaarialgebra: `intel-oneapi-mkl`
- Tiheä jaettu lineaarialgebra: `intel-oneapi-mkl`, `netlib-scalapack`
- Nopeat Fourier-muunnokset: `fftw`

## Kirjastot Mahtissa {#libraries-in-mahti}

Mahtissa saatavilla olevat valitut kirjastot:

- Tiheä lineaarialgebra: `openblas`, `amdblis`, `amdlibflame`
- Tiheä jaettu lineaarialgebra: `netlib-scalapack`, `amdscalapack`
- Nopeat Fourier-muunnokset: `fftw`
