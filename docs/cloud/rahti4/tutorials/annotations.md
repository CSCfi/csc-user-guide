# Annotations

You can use Kubernetes annotations to attach arbitrary non-identifying metadata to objects. Clients such as tools and libraries can retrieve this metadata. Annotations, like labels, are key/value maps.

Annotations can be added to any object by simply doing:

```
oc annotate <object_type> <object_name> <key>=<value>
```

Here are some examples that use annotations:

* [Protecting Against DDoS Attacks](../../../../support/faq/DDos/)
* [Route annotations](../../concepts/#route)
* [Custom domain names and secure transport](../custom-domain/)
