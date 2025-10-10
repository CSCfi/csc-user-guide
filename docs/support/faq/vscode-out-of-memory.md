# VS Code Remote-SSH -laajennus antaa muistin loppumisvirheen yhdistettäessä CSC:n supertietokoneisiin { #vs-code-remote-ssh-plugin-gives-out-of-memory-error-when-connecting-to-csc-supercomputers }

Yhteyden muodostaminen CSC:n supertietokoneisiin VS Coden versioilla 1.101 ja uudemmilla saattaa epäonnistua virheeseen `Out of memory: Cannot allocate Wasm memory for new instance`. Ongelman voi kiertää kolmella tavalla:

1. Lisää CSC:n supertietokoneissa `.bashrc`-tiedostoosi rivi `export NODE_OPTIONS="--disable-wasm-trap-handler"`, tai
2. kasvata kirjautumissolmun virtuaalimuistin rajoitusta lisäämällä rivi `ulimit -v "$(ulimit -Hv)"` CSC:n supertietokoneissa `.bashrc`-tiedostoosi, tai
3. palaa VS Coden versioon 1.100.