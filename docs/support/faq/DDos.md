# Protecting Against DDoS Attacks

 A [denial-of-service](https://en.wikipedia.org/wiki/Denial-of-service_attack#Distributed_DoS) attack (DoS attack) is a cyber-attack in which the perpetrator seeks to make a machine or network resource unavailable to its intended users by temporarily or indefinitely disrupting services of a host connected to the Internet. Denial of service is typically accomplished by flooding the targeted machine or resource with superfluous requests in an attempt to overload systems and prevent some or all legitimate requests from being fulfilled. A distributed denial-of-service (DDoS) is a large-scale DoS attack where the perpetrator uses more than one unique IP address or machines, often from thousands of hosts infected with malware.

Rahti 2's routers are already configured to have some protection against DDoS. The timeout `http-request` and others have been added to the default HAProxy router image to protect the cluster against DDoS attacks (for example, [slowloris](https://en.wikipedia.org/wiki/Slowloris_(computer_security))). The current configured values are:

| Parameter | Default timeout | Description |
|:--|:--|:--|
|http-request| 10s| HAProxy gives a client 10 seconds to send its headers HTTP request. [http-request](https://cbonte.github.io/haproxy-dconv/1.7/configuration.html#4-timeout%20http-request) manual |
|connect| 10s| Set the maximum time to wait for a connection attempt to a server to succeed. [connect](https://cbonte.github.io/haproxy-dconv/1.7/configuration.html#4.2-timeout%20connect) manual |
|http-keep-alive| 10s| Set the maximum allowed time to wait for a new HTTP request to appear [http-keep-alive](https://cbonte.github.io/haproxy-dconv/1.7/configuration.html#4-timeout%20http-keep-alive) manual |
|check| 10s| Set additional check timeout, but only after a connection has been already
established. [check](https://cbonte.github.io/haproxy-dconv/1.7/configuration.html#4-timeout%20check) manual |

It is possible to enable further protections on a per route basis. These annotations must be added accordingly to the `Route` you may want to protect:

|Setting|Description|
|:--|:--|
|haproxy.router.openshift.io/rate-limit-connections|Enables the settings be configured (when set to true, for example).|
|haproxy.router.openshift.io/rate-limit-connections.concurrent-tcp|The number of concurrent TCP connections that can be made by the same IP address on this route.|
|haproxy.router.openshift.io/rate-limit-connections.rate-tcp|The number of TCP connections that can be opened by a client IP.|
|haproxy.router.openshift.io/rate-limit-connections.rate-http|The number of HTTP requests that a client IP can make in a 3-second period.|

* See [Route-specific Annotations](https://docs.openshift.com/container-platform/4.13/networking/routes/route-configuration.html#nw-route-specific-annotations_route-configuration)
