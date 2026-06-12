!!! error "Advanced level"
    This tutorial uses OpenShift CLI tool [oc](../usage/cli.md) and [Helm](https://helm.sh)
    You must understand that OpenShift [Routes](../concepts.md#route) only exposes HTTP/HTTPS port to the internet

# Accessing databases on Rahti from CSC supercomputers

Many HPC workflows require a database, for most cases [Pukki](../../dbaas/index.md) is probably the preferred solution. However, it is possible to use Rahti as well to deploy and expose your databases. This tutorial explains how to access your Rahti database from CSC super computers.

## Step 1: Setting up MariaDB on Rahti

We will use the [Bitnami MariaDB Helm chart](https://github.com/bitnami/charts/tree/main/bitnami/mariadb). This Helm Chart is not meant for production use, but it is sufficient for demonstration purposes.

Simply run this command:

```bash
helm install my-release oci://registry-1.docker.io/bitnamicharts/mariadb
```

## Step 2: Setup a LoadBalancer Service Type on Rahti

We will setup a [LoadBalancer](../networking.md#using-loadbalancer-service-type-with-dedicated-ips) in Rahti. Unlike [Routes](../networking.md#routes), the LoadBalancer service allows you to expose services to the Internet without being limited to HTTP/HTTPS. Have a look at the documentation linked above to learn more.

First, you need to submit a request to the service desk (servicedesk@csc.fi). The request must include the following details:

    - Project Name: Provide the exact name of the Rahti project for which you want to enable LoadBalancer services.
    - CSC Project Number: The csc_project number that is used for Rahti Project.
    - Use Case: Clearly describe the use case, including:
        - That you will be running MariaDB databases and that you weill be connecting from a CSC supercomuter.
        - Any specific requirements or considerations. (e.g., how many ips)

Once your request is approved by the Rahti admins, you will receive the **LoadBalancer** public **IP** address that can be used to access your service(s).

Finally, you need to create the `Service` that will expose your MariaDB to the external network. Create a `service.yaml` file:

```yaml
kind: Service
apiVersion: v1
metadata:
  name: mysqllb
  namespace: my-namespace
spec:
  ports:
    - protocol: TCP
      port: 33306
      targetPort: 3306
  allocateLoadBalancerNodePorts: false
  type: LoadBalancer
  selector:
    app.kubernetes.io/name: mariadb
```

and then run `oc` to create the Service:

```sh
oc create -f sevice.yaml
```

You now have your database exposed on the **LoadBalancer IP** you recevied and on port **33306**.

## Step 3: Connect to MariaDB from CSC supercomputers

MariaDB and the LoadBalancer have now been set up on Rahti and you should have the following details: MariaDB **username**, **password**, **database name**, and the **LoadBalancer IP** and **port**. These are needed when connecting to the database.

!!! info

    For this example to work, you need to install the mariadb python module. At the time of writing this the command to use is:
    `pip3 install mariadb=1.0.11`
    This is due to the fact that the current last version of the module is broken for the platforms we tested this with. See the upstream documentation for more information: <https://mariadb.com/docs/connectors/mariadb-connector-python/install>


```python
# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="<username>",
        password="<password>",
        host="<LoadBalancer IP>",
        port=<port>,
        database="<database name>"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()
```

**Note:** The database will only listen on IPv4.
