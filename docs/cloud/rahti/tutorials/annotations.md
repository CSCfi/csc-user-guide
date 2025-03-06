!!! success "Basic level"
    You need a knowledge of OpenShift CLI tool [oc](../usage/cli.md) and kubernetes [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)

# Annotations

You can use Kubernetes annotations to attach arbitrary non-identifying metadata to objects. Clients such as tools and libraries can retrieve this metadata. Annotations, like labels, are key/value maps.

Annotations can be added to any object by simply doing:

```
oc annotate <object_type> <object_name> <key>=<value>
```

Here are some examples that use annotations:

* [Protecting Against DDoS Attacks](../../../support/faq/DDos.md)
* [Route annotations](../concepts.md#route)
* [Custom domain names and secure transport](custom-domain.md)
