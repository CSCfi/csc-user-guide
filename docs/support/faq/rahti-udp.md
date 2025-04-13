
# Tukeeko Rahti UDP-yhteyksiä? {#does-rahti-support-udp-connections}

Ei, sillä välin sisäinen UDP-liikenne on mahdollista, eli: Podien välinen viestintä saman namespace-nimen sisällä. UDP-protokollaa ei voida käyttää Rahtin kanssa. Vain HTTP/HTTPS on tuettu `Route`-reiteille, ja `oc port-forwarding` tukee vain TCP-portteja.
