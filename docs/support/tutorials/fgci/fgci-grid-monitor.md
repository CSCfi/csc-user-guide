# 3. Grid Monitor

The Grid Monitor is a web based tool for getting information about the
status of ARC based grids and the clusters running the jobs. The monitor
is maintained by the Nordugrid community and it is located at the
following URL address:

http://www.nordugrid.org/monitor

The main page of the grid-monitor shows information about grid clusters
from several countries. As we are only interested about the FGI
environment here, we can alternatively use the URL address:

<http://www.nordugrid.org/monitor/loadmon.php?display=vo=Finland>

that shows just the Finnish ARC clusters. Figure 3. shows the status
page of Finnish grid clusters.  
  
![]

**Figure 3.** ARC Grid Monitor.

 

The main view of the Grid Monitor shows a list of clusters and the load
of each cluster. The relative load of each cluster are shown as a bar
diagram, where the dark gray bar shows the total load of the cluster
(including the jobs submitted by the local users) and the green bar
shows the amount of grid jobs submitted through the ARC middleware.

The main view of the Grid Monitor contains a large amount of links. If
you click the cluster name in the Site column, you can open a window
that shows the details of the cluster including, for example, the name
of the machine, its operating system and the available runtime
environments.

Clicking on one of the green bars in the *Load* diagram opens a new
window showing the grid jobs currently running in the corresponding
cluster (Figure 4.) and if you click on a number in the *Queueing*
column you will get a similar view about the grid jobs queuing in the
batch job system of that cluster. In the job lists you can further click
the *Job name* to see the details of a specific job or *Owner* to see
more information of the user and the status of all the FGI jobs of that
user.

![][1]

**Figure 4.** Joblist of a cluster in grid monitor.

A more detailed description about the Grid Monitor tool can be found
from the Grid Monitor manual, provided by the Nordugrid community:

<http://www.nordugrid.org/documents/monitor.pdf>

 

 

 

  []: https://research.csc.fi/documents/48467/84606/FGI-guide_image3.jpg/965efe9b-45ff-4bc4-81e4-ece876eb7a2e?t=1383829096000
  [1]: https://research.csc.fi/documents/48467/84606/FGI-guide_image4.jpg/1b827c0b-e9e1-448a-98c8-5ab7ca3980a3?t=1383828754000
