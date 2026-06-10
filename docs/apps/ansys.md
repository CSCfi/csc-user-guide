---
tags:
  - Other
catalog:
  name: Ansys
  description: Ansys Academic research CFD
  license_type: Other
  disciplines:
    - Computational Engineering
  available_on:
    - Roihu
---

# Ansys
Ansys offers a comprehensive software suite that spans the entire range of physics, providing access to virtually any field of engineering simulation that a design process requires ([Ansys - Products](https://www.ansys.com/products)). Ansys Academic Research CFD simulation products have been validated and are highly regarded for their superior computing power and accurate results. 

## License
The terms of use of this software allow it to be used only by affiliates (staff
and students) of Finnish higher education institutions.

## Available
Ansys Academic Reseach CFD licenses are available on CSC's [Roihu](../computing/available-systems.md) supercomputer for analysis runs only.

## Usage
After login on the server, make sure that you have transferred all your input files for the analysis run from your local computer to the server. Locate the files in your project's scratch directory. Home directory is not intended for computing.

To find out which versions of ANSYS are installed on the server, give command
```bash
module spider ansys
```
For example to load Ansys version 2026R1, give command
```bash
module load ansys/2026R1
```

There are examples of **batch job files** available on Roihu both CFX and Fluent in a directory
```bash
/appl/soft/manual/eng/x86_64/ansys/example_batch_job_scripts
```
Copy those files and modify them for your own use. Further instructions are given in the files.

## Support
If you encounter issues, please [contact CSC Service Desk](../support/contact.md).

## More information
* [Ansys Inc.](https://www.ansys.com/)
* [Ansys Academic product reference table](https://www.ansys.com/content/dam/web/academic/academic-product-reference-guide.pdf)
* [ANSYS - Academic, terms and conditions page](https://www.ansys.com/academic/terms-and-conditions)
