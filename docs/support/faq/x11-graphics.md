
# X11-etägrafiikka ei toimi {#x11-remote-graphics-does-not-work}

Etägrafiikka vaatii X11:n tunneloinnin SSH:n kautta käyttämällä `-X`-lipuketta. Linuxissa yhdistä esimerkiksi Puhtiin käyttäen:  

```bash
ssh -X <your-user-name>@puhti.csc.fi
```

Virhe voi ilmetä, jos olet ylittänyt levykiintiösi.

Toinen (parempi) tapa käyttää etägrafiikkaa on käyttää etätyöpöytää [Puhti-verkkoliittymän](../../computing/webinterface/index.md) kautta.

Lisätietoja saat
[graafisten yhteyksien ohjeistuksestamme](../../computing/connecting/index.md#graphical-connection).
