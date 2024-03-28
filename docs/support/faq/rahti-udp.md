# Does Rahti 2 support UDP connections?

No, meanwhile, internal UDP traffic is possible, i.e.: during Pod to Pod communications inside the same namespace. It is not possible to contact Rahti 2 using the UDP protocol. Only HTTP/HTTPS is supported for `Route`s, and `oc port-forwarding` only supports TCP ports.
