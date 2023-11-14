# Julia Jupyter

## Selecting the Julia-Jupyter application

![ood application menu](../../img/julia-jupyter/ood-application-menu.png)

We can use [Julia](../../apps/julia.md) on Jupyter through the
[Puhti](https://www.puhti.csc.fi) and [Mahti](https://www.mahti.csc.fi) web
interfaces by selecting the **Julia-Jupyter** application from the menu.

## Launching Julia-Jupyter

![julia jupyter options](../../img/julia-jupyter/options-1.png)

Now, we need to select the resources for running Julia-Jupyter. First, we must
select a project for billing and partition for computing resources.

![julia jupyter options](../../img/julia-jupyter/options-2.png)

Next, we must set the desired computing resources: CPU cores, memory, local
disk, and time.

![julia jupyter options](../../img/julia-jupyter/options-3.png)

Finally, we must select the Jupyter type. We recommend using Jupyter lab, but
the classic notebook is also available. The working directory sets the root
directory for Jupyter. The Julia depot directory sets the location for package
installations, compiled files, and other Julia depots. If you plan to install
large amounts of Julia packages, we recommend using `/projappl` or `/scratch`
instead of the `$HOME` directory as it could run out of quota. For example,
Plots.jl installs over 10k files and is quite large.

## Starting Julia kernel

![available julia kernels on jupyter lab](../../img/julia-jupyter/julia-kernels.png)

Inside the Jupyter session, we can start notebooks with the desired Julia
version. Starting a kernel loads the corresponding Julia module and starts the
notebook. We launch the Julia kernel using
[IJulia.jl](https://github.com/JuliaLang/IJulia.jl). Note that the Jupyter
installation for Julia is separate from the Jupyter installation for Python and
is not intended for other use.
