# Monitoring the load on Puhti
Server information, current CPU load, CPU load history and job count history of Puhti supercluster and other CSC's servers can be checked with *Host Monitor* tool of CSC's *Scientist's User Interface* web portal. In addition, signing in offers additional features such as details of all running batch jobs:

- [Host monitor (CSC account required, full access)](https://sui.csc.fi/group/sui/host-monitor)
- [Host monitor (no authentication, limited functionality)](https://sui.csc.fi/web/guest/host-monitor)
	
Once you have logged in to Taito, you can check load status also with commands:
```batch
squeue
```
and
```batch
sinfo
```
These commands and tools show the jobs that are currently running or waiting in the batch job system.
