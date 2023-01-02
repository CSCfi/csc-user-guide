# Grid Monitor

The Grid Monitor is a web based tool for getting information about the
status of ARC based grids and the clusters running the jobs. The monitor
is maintained by the Nordugrid community and it is located at the
following URL address:

* [http://www.nordugrid.org/monitor](http://www.nordugrid.org/monitor)

The main page of the grid-monitor shows information about grid clusters
from several countries. If we are only interested about the Finnish
environment here, we can alternatively use the URL address:

* [http://www.nordugrid.org/monitor/loadmon.php?display=vo=Finland](http://www.nordugrid.org/monitor/loadmon.php?display=vo=Finland)

that shows just the Finnish ARC clusters.

The main view of the Grid Monitor shows a list of clusters and the load
of each cluster. The relative load of each cluster are shown as a bar
diagram, where the blue bar shows the locally submitted jobs the green
bar shows the amount of grid jobs submitted through the ARC middleware.

The main view of the Grid Monitor contains a large amount of links. If
you click the cluster name in the Site column, you can open a window
that shows the details of the cluster including, for example, the name
of the machine, its operating system and the available runtime
environments.

Clicking on one of the green bars in the *Load* diagram opens a new
window showing the grid jobs currently running in the corresponding
cluster and if you click on a number in the *Queueing*
column you will get a similar view about the grid jobs queuing in the
batch job system of that cluster. In the job lists you can further click
the *Job name* to see the details of a specific job or hash of the job
*Owner*.

A more detailed description about the Grid Monitor tool can be found
from the [Grid Monitor manual (pdf)](http://www.nordugrid.org/documents/monitor.pdf)
, provided by the Nordugrid community.

