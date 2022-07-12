<style>
.admonition-title { background-color: rgba(255, 145, 0, 0.1) !important; }
.admonition { background-color: white !important; }
</style>
!!! Attention "⚠️ Rahti 3 is deprecated"

    This page is about a deprecated version of Rahti, please consult the [updated documentation article](../../../rahti4/tutorials/annotations/)

# Annotations

You can use Kubernetes annotations to attach arbitrary non-identifying metadata to objects. Clients such as tools and libraries can retrieve this metadata. Annotations, like labels, are key/value maps.

Annotations can be added to any object by simply doing:

```
oc annotate <object_type> <object_name> <key>=<value>
```

Here are some examples that use annotations:

* [Protecting Against DDoS Attacks](/support/faq/DDos/)
* [Route annotations](/cloud/rahti/concepts/#route)
* [Custom domain names and secure transport](/cloud/rahti/tutorials/custom-domain/)
