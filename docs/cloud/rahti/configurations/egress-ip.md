# Egress IPs

Currently, all outgoing traffic uses the IP `86.50.229.150`. In other words, any running Pod uses this IP by default to reach endpoints located outside Rahti, including on the internet. A dedicated egress IP is typically needed when an external service, such as a database or an API behind a firewall, only accepts connections from a known IP address. If needed, you can request a dedicated egress IP for your Rahti project by contacting the [Service Desk](../../../support/contact.md). Each request is reviewed on a case-by-case basis due to the limited size of the IP pool.

!!! warning "Egress IP may change"

    The egress IP of Rahti might change in the future. This could happen, for example, if there is a major change in the underlying network infrastructure.
