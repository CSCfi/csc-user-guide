# Discovery Studio

Discovery Studio is a protein modeling program that contains tools to
visualize, analyse, modify and simulate protein structures. University
and polytechnic researchers working in Finland can install Discovery
Studio into their local Windows or Linux computers for academic
research.

## License

Discover Studio is a commercial program by Biovia Inc. CSC has purchased
a national academic license for Discovery Studio that allows non-profit
usage in Finnish universities.

!!! Note
    CSC has obtained a reduced Discovery Studio license for 2022 (maximum 3 simultaneous users, heavy usage is recommended
    to be done with [Maestro](maestro.md)). Decision to continue beyond 2023 
    will be made by autumn 2022.

## Available

The following server versions are available on CSC (in Pouta):

-   Discovery studio DS2019 is available in
    [http://dstudio19.csc.fi:9944](http://dstudio19.csc.fi:9944)
-   Discovery studio DS2018 is available in
    [http://dstudio18.csc.fi:9944](http://dstudio19.csc.fi:9944)

## Usage

To use Discovery Studio you need to install a Discovery
Studio client on your own computer. Discovery Studio client is available for Windows (Windows 7, 8 and 10) and Linux
operating systems (Red hat Enterprise linux 6 and 7, Centos7, or SuSE 11 SP4
recommended). The license provided by CSC is available only 
for university researchers working in Finland. Due to that, your computer must be
within the university network (FUNET) be able to use the 
license.

You can download the Windows and Linux clients using the links below:
* [Discovery Studio 2019 client](http://dstudio19.csc.fi:9944/DS/)
* [Discovery Studio 2018 client](http://dstudio18.csc.fi:9944/DS/)

Discovery Studio client provides an extensive manual and large set of tutorials that
help you to get started with the software.

### Installing the Discovery Studio client in Windows

DS2019Client.exe starts a graphical installation tool, that will guide you through the Discovery Studio client installation.
In most cases you can just accept the default installation settings that the installation tool suggest.

[Sign in eDuuni to learn the information needed to set up a connection to the License server](https://wiki.eduuni.fi/display/cscjemma/Discovery+Studio)

If licensing information is not asked during the installation, start the Discovery Studio client, you just installed, 
and press button _Enable additional features_ in the lower right corner of the interface.
This opens a license configuration session where you should apply the license settings listed abowe.

To use Discovery Studio servers of CSC, start the Discovery Studio client normally and select command:

**File | Change server...**

And set server name to be:

*   https://dstudio19.csc.fi:9943  (For Discovery Studio 2019)
*   https://dstudio18.csc.fi:9943  (For Discovery Studio 2018)

 
### Installing the Discovery Studio client in Linux

[Sign in eDuuni for installation and licensing instructions](https://wiki.eduuni.fi/display/cscjemma/Discovery+Studio).

After the steps detailed in the link above, you should be ready to run (as long as the IP address of your machine is within the FUNET network, i.e. in your university network or in a VPN to it).

To use Discovery Studio servers of CSC, start the Discovery Studio client normally and select command:

**File | Change server...**

And set server name to be:

*   https://dstudio19.csc.fi:9943  ( For Discovery Studio 2019)
*   https://dstudio18.csc.fi:9943  ( For Discovery Studio 2018)


### Tricks for installing Discovery Studio client to Ubuntu

Below are some tricks you can try to use to install Discovery Studio Client to an Ubuntu Linux machine.  
By default, the _sh_ that Ubuntu is using is actually a command shell called _dash_ that diffters from 
the sh shell that is in use in e.g. Redhat and Centos linuxes. 

In Discovery studio installation this causes problems as the installation process is based on sh scripts.

One way to fix this issue is to redefine sh shell in your Ubuntu server as described e.g. in:

[https://unix.stackexchange.com/questions/442510/how-to-use-bash-for-sh-in-ubuntu](https://unix.stackexchange.com/questions/442510/how-to-use-bash-for-sh-in-ubuntu)

Alternatively you can try following:

Start installation with bash shell and _--keep_ option:
```text
bash DS2019Client.bin --keep
```
The installation process fails, but provides a temporary installation directory. Go to this direcory and modify the 
actual installation script a bit and execute the modified version:

```text
cd client/
sed s/"echoe"/"echo -e"/g install_DSClient.sh > install_DSClient_e.sh
bash install_DSClient_e.sh
```
This command does most of the installation but the Lincese Pack installtion fails 
for the same reason as the main instllation process. The fix is also the same:

```text
cd lp_installer/
bash lp_setup_linux.sh --keep
cd lpbuild/
sed s/"echoe"/"echo -e"/g install_lp.sh > install_lp_e.sh
```
Now the installation is done and you just need to add the license data as described in the previous example.

## References

Please see method descriptions and log files in Discovery Studio for details.

## More information

Discovery Studio client provides an extensive manual and large set of tutorials that
help you to get started with the software.

* [Discovery Studio home page](https://www.3dsbiovia.com/products/collaborative-science/biovia-discovery-studio/)
* [Discovery Studio training resources](https://www.3ds.com/products-services/biovia/resource-center/?woc=%7B%22brand%22%3A%5B%22brand%2Fbiovia%22%5D%2C%22biovia%20products%22%3A%5B%22biovia%20products%2Fdiscovery%20studio%22%5D%7D)
 
