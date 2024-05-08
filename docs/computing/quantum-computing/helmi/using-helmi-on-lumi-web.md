# Using Helmi on Lumi-web interface

This page goes through the steps required for accessing Helmi using the LUMI web interface. It is assumed you you are a member of an active project with QPUs.

## Logging in to the web interface

Details for logging in to the LUMI web interface can be read through the [LUMI Documentation page](https://docs.lumi-supercomputer.eu/firststeps/loggingin-webui/).

### Accessing Helmi

After successfully authenticating, you should now have access to your dashboard. Click on the jupyter app
, select your project and the partition as q_fiqci. If you have an active reservation, you can use it by selecting it under reservation.

It is recommended to use the Advanced settings, select Custom init Text and under the 'Script to start' textbox enter the following script to configure the environment to use the quantum software stack.

```bash
module use /appl/local/quantum/modulefiles
module load helmi_qiskit
```

<p align="center">
    <img src="../../../../img/helmi_with_lumi_web.png" alt="Helmi's with LUMI web">
</p>


Click on launch to start your Jupyter session. This will launch Jupyter using the command python -m jupyter lab

## Further Reading
* [Lumi web interface](https://docs.lumi-supercomputer.eu/runjobs/webui/)
* [Jupyter on Lumi web interface](https://docs.lumi-supercomputer.eu/runjobs/webui/jupyter/)
