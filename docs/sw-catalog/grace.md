---
template: sw-catalog-templates/app.html
software_catalog:
  name: Grace
  description: Plotting tool for xvg-files in particular
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - web_interfaces:
        - Puhti
    - Puhti
---

Grace is foremost a plotting tool, and e.g. GROMACS produces tailored input for
it, but Grace can also be used for some numerical analyses.

## Available

* Puhti: 5.1.25

## License

* [GPL](https://plasma-gate.weizmann.ac.il/Grace/doc/GPL.html)

## Usage

Initialize Grace with:

```bash
module load grace
```

And start with `xmgrace` or show a plot directly with `xmgrace input.xvg`.

Note, that you need remote graphics to work with Grace. An easy way is through the
[Puhti web interface remote desktop](../computing/webinterface/desktop.md).

## More information

* [Grace home page](https://plasma-gate.weizmann.ac.il/Grace/)
* [Grace user guide](https://plasma-gate.weizmann.ac.il/Grace/doc/UsersGuide.html)
