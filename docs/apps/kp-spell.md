---
tags:
  - Free
catalog:
  name: kp-spell (enchant)
  description: Finnish and Swedish spell-checking via the enchant interface
  license_type: Free
  disciplines:
    - Language Research and Other Digital Humanities and Social Sciences
  available_on:
    - Puhti
    - Roihu
---

# kp-spell

kp-spell provides Finnish and Swedish spell-checking on CSC systems. While it is
used through the command-line tools of
[enchant](https://abiword.github.io/enchant/) — a generic library that offers a
single interface to several spelling backends — kp-spell is more than plain
enchant: it bundles the language-specific backends and dictionaries needed for
Finnish (via [Voikko](https://voikko.puimula.org/)) and Swedish (via
[Hunspell](https://hunspell.github.io/)) and exposes them through the common
`enchant-2` interface.

## Available

* Puhti: 1.0
* Roihu: 1.0

## License

kp-spell builds on enchant, which is licensed under the
[LGPL 2.1 or later](https://github.com/AbiWord/enchant/blob/master/COPYING.LIB),
together with the Voikko and Hunspell backends and their dictionaries, which
have their own open-source licenses.

## Usage

Initialize kp-spell with:

```bash
module load kp-spell
```

Spell-checking is done with `enchant-2`, and `enchant-lsmod-2` lists the
available dictionaries. Use the language code with `-d` (`fi` for Finnish, `sv`
for Swedish). For example, to check Finnish text in ispell pipe mode:

```bash
echo "Koiro käveli kadulla." | enchant-2 -a -d fi
```

This returns spelling suggestions in ispell format, for example:

```
& Koiro 5 0: Kairo, Kiro, Koira, Koiso, Koiaro
```

A personal word list can be supplied with the `-p` option.

## More information

* [enchant home page](https://abiword.github.io/enchant/)
* [Voikko](https://voikko.puimula.org/)
* [Hunspell](https://hunspell.github.io/)
