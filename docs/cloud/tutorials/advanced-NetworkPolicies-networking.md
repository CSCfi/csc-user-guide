# Advanced NetworkPolicies

In this YAML example below there is a `NetworkPolkicy` that will allow communication **initiated from** another namespace `<NAME OF ANOTHER NAMESPACE>` to the current namespace:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: 'namespacelink'
spec:
  podSelector: {}
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector: {}
          namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: <NAME OF ANOTHER NAMESPACE>
```

This NetworkPolicy needs to be created in the current namespace.

In order to apply it, you just need to create a file with the contents above, remember to replace the value of the namespace. Once the file is created:

```sh
oc create -f file.yaml
```

You can check that the NetworkPolicy was created correctly by:

```sh
$ oc describe NetworkPolicy namespacelink
Name:         namespacelink
Namespace:    test-httpd2
Created on:   2024-01-22 11:35:41 +0200 EET
Labels:       <none>
Annotations:  <none>
Spec:
  PodSelector:     <none> (Allowing the specific traffic to all pods in this namespace)
  Allowing ingress traffic:
    To Port: <any> (traffic allowed to all ports)
    From:
      NamespaceSelector: kubernetes.io/metadata.name=test-rc
      PodSelector: <none>
  Not affecting egress traffic
  Policy Types: Ingress
```

For more information check our [Network](../../rahti2/networking/) information page
