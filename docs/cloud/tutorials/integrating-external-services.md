# Integrating External Services

Kubernetes, and by extension OpenShift OKd, gives a lot of flexibility regarding network use cases. One of the uses cases is the one that allows to use external services, like databases, transparently in a OpenShift project. Other of the use cases would be to to have a network proxy between OpenShift installations. This could be used
to ease migration periods.

![Proxy between clusters](../img/proxy.drawio.svg)

In the example above we are redirecting traffic from Rahti 1 to Rahti 2. This is obtained by creating two routes, a service and an Endpoint.

1. First deploy an application in Rahti 2. Any application is suitable for this test.

1. Create a special `Route` in Rahti 2:

    ```yaml
     apiVersion: route.openshift.io/v1
    kind: Route
    metadata:
      name: test-route
    spec:
      host: <test>.rahtiapp.fi
      port:
        targetPort: http
      to:
        kind: Service
        name: <Service-name>
        weight: 100
      wildcardPolicy: None
    status: {}
    ```
    You can replace `<test>` by any available URL in Rahti 1. The `<service-name>` must be the one corresponding to the application you deployed. You can test the setup so far:

    ```sh
    curl <test>.rahtiapp.fi -vL --resolve <test>.rahtiapp.fi:80:195.148.21.61
    ```
    The command above uses `--resolve` to chage the ip associated to a DNS.

1. Then create an `EndPoint` in Rahti 1:

    ```yaml
    kind: "Endpoints"
    apiVersion: "v1"
    metadata:
      name: "proxy-service" 
    subsets: 
      -
        addresses:
          -
            ip: "195.148.21.61"
        ports:
          -
            port: 80
            name: "http"
    ```
    The IP in the example, is the one behind `router-default.apps.2.rahti.csc.fi`.  

1. Then a `Service`, also in Rahti 1:

    ```yaml
    kind: "Service"
    apiVersion: "v1"
    metadata:
      name: "proxy-service"
    spec:
      ports:
        -
          name: "http"
          protocol: "TCP"
          port: 80
          targetPort: 80 
          nodePort: 0
    selector: {}
    ```
    The name of the `Service` and the `EndPoint` must be the same.

1. Finally the `Route` in Rahti 1:

    ```yaml
    apiVersion: route.openshift.io/v1
    kind: Route
    metadata:
      name: test-route
    spec:
      host: <test>.rahtiapp.fi
      port:
        targetPort: http
      to:
        kind: Service
        name: proxy-service
        weight: 100
      wildcardPolicy: None
    status: {}
    ```
    The URL must be the same as in step 2.

It is possible to "proxy" more than one URL, the only necessary step is to create the `Route`s in Rahti 1 and 2 with the same URL in each service. It is not necessary to replicate the `Service` and `Endpoint` in Rahti 1.

For more information and other options:

- <https://docs.openshift.com/dedicated/3/dev_guide/integrating_external_services.html>
