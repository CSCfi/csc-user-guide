---
tags:
  - Other
catalog:
  name: MedeA
  description: Materials modeling and simulation environment
  license_type: Other
  disciplines:
    - Chemistry
    - Physics
  available_on:
    - Roihu
---

# MedeA

[MedeA](https://www.materialsdesign.com/medea-software) is an integrated software
environment for atomistic materials modeling and simulation by Materials Design Inc.

## Available

- Roihu-CPU: 1.13.1

## License

Commercial, more info from [Materials Design](https://www.materialsdesign.com/).

## Usage

These instructions assume the MedeA GUI is already installed on your own computer. The MedeA JobServer and TaskServer run in a container on a Roihu login node, and the TaskServer submits calculations to Slurm. VASP and LAMMPS calculations use Roihu's own `vasp` and `lammps` modules.

## 1. Set up the servers on Roihu (once)

Log in to the login node where your servers will run. Always use the same node, because the servers run there:

```bash
ssh roihu-cpu-login1.csc.fi
```

Load the MedeA server scripts:

```bash
module load medea-servers/3.13.1
```

Create a work directory and generate the server option files `JobServer.options` and `TaskServer.options`:

```bash
mkdir -p /scratch/<project>/$USER/medea
cd /scratch/<project>/$USER/medea
medea-init-servers.py --jobserver-port 32077 --taskserver-port 23077
```

The login node is shared with other users, so choose your own two port numbers instead of `32077` and `23077` (any free ports between 1024 and 65535).

The generated `TaskServer.options` submits jobs with these settings. Edit the file if you need different ones:

| Line | Meaning |
|------|---------|
| `-batch_project project_2003810` | Billing project (Slurm `--account`) |
| `-batch_queue small` | Slurm partition |
| `-nprocessors 128` | Maximum cores per task |
| `-ntasks 4` | Maximum concurrent tasks |

## 2. Start and stop the servers

Run these on the same login node, in your work directory, with the module loaded:

```bash
module load medea-servers/3.13.1
cd /scratch/<project>/$USER/medea
```

Start the JobServer and TaskServer:

```bash
medea-start-servers.sh
```

Check that the instances `medea-jobserver` and `medea-taskserver` are running:

```bash
apptainer instance list
```

Stop the servers when you no longer need them:

```bash
medea-stop-servers.sh
```

## 3. Open an SSH tunnel from your computer

On your own computer, forward a local port to your JobServer port (here `32077`):

```bash
ssh -N -f -L localhost:32001:localhost:32077 roihu-cpu-login1.csc.fi
```

The JobServer web page is now at <http://localhost:32001/index.html>.

Close the tunnel:

```bash
pkill -f "ssh -N -f -L localhost:32001:localhost:32077 roihu-cpu-login1.csc.fi"
```

## 4. Connect the GUI to Roihu

Start the MedeA GUI, then go to **File » Preferences » JobServers** and add a JobServer with name `Roihu` and address `http://localhost:32001`.

Each time you work with MedeA: start the servers on Roihu (step 2), open the tunnel (step 3), then start the GUI.

## Troubleshooting

- **Servers do not start or a port is in use:** choose other ports, run `medea-init-servers.py` again with them, and use the new JobServer port in the SSH tunnel.
- **Where are my files?** Job data is in `<workdir>/JobServer/Jobs` and task run directories in `<workdir>/TaskServer`.

## More information

- [MedeA documentation](https://www.materialsdesign.com/)
