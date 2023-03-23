# Kustomize

[Kustomize](https://kustomize.io) is similar to [Helm](helm.md), both are good for bundling kubernetes elements such as services, deployments, etc...  
Helm can act as a package manager for kubernetes/oc as well as apt or yum can do for Debian, RedHat.  
The main difference is Helm uses **Templates** whereas Kustomize uses **Overlays**. Kustomize is also developed by the kubernetes teams, you can build a project using this command:

```sh
oc kustomize build FOLDER
```

However some features are missing with the built-in tool, you can install the [tool](https://kubectl.docs.kubernetes.io/installation/kustomize/) separately. The command to build with `kustomize` is:

```sh
kustomize build FOLDER
```
A build won't apply, it will only output to `stdout`.

Here is a table that compares both solutions:

|   	| Helm | Kustomize |
|---	|--- | --- |
|Pros   |- Template functions are powerful <br>- Helm is a package manager, like apt or yum does, but for kubernetes <br>- Large amount of existing charts already out that can boost productivity |- Native in from kubectl v1.14 <br>- Uses of plain YAML <br>- Not a templating system but a yaml patching system |
|Cons   |- More abstraction layers <br>- Less readable templates <br>- Require an external dependency <br>- Folder structure |- The strength of Helm is to be used as a package manager <br>- Does not follow the [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) principle |

## When using Kustomize?
It can be harsh to use Helm in a way that your applications will have more curly brackets than nouns.  Kustomize allows you to work with a bunch of YAML files. It can be a good alternative by using **overlays** instead of **templates**.

## What are overlays?
Overlays are a kustomization (*kustomization.yaml*) that depend on another kustomization. They can include new resource manifests, or patches for existing resources.

## Example
Let's see an example on how kustomize works. We'll take this repo: [https://github.com/lvarin/kustomize-openshift](https://github.com/lvarin/kustomize-openshift)

If we look at the directory, this is what we have:

```sh
├── README.md
├── base
│   ├── deployment.yaml
│   ├── kustomization.yaml
│   ├── pvc.yaml
│   ├── route.yaml
│   └── service.yaml
└── overlays
    └── production
        ├── db.yaml
        ├── deployment.yaml
        ├── kustomization.yaml
        ├── pvc.yaml
        └── route.yaml

4 directories, 11 files
```

We have a **base** and an **overlays** folder. Inside the overlays folder, we can find another folder called **production**.
To start using kustomize, you need to create a kustomization.yaml file. Use this command to create a kustomization file (optional):  

```sh
kustomize create
``` 

Here is the content of the kustomization file inside the base folder:

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
metadata:
  name: arbitrarky

resources:
- pvc.yaml
- deployment.yaml
- service.yaml
- route.yaml
```

You will notice a **resources** key, with different yaml files as values. A resource is a root relative path to a YAML or JSON file describing a k8s API object.  
And now, let's have a look of the content at `kustomization.yaml` file inside `overlays/production`:

```yaml
resources:
- ../../base

patchesStrategicMerge:
- pvc.yaml
- route.yaml

configMapGenerator:
- name: dbparams
  files:
  - db.yaml
```

Basically, if you run the command `oc kustomize base` or `kustomize build base`, you will have the output of `pvc.yaml, deployment.yaml, service.yaml` and `route.yaml`.  

Now, if you run the same command as above but with `overlays/production` instead of `base`, you will have the same output but with some new stuff, like a configMap and modifications in `pvc.yaml` and `route.yaml`:

```diff
+apiVersion: v1
+data:
+  db.yaml: |
+    user: pepe
+    password: pardo
+kind: ConfigMap
+metadata:
+  name: dbparams-btb7dgb89t
```

```diff
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: html
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
-      storage: 500Mi
status: {}


apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: html
spec:
  resources:
    requests:
+      storage: 1Gi
```

```diff
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: nginx
spec:
-  host: example.rahtiapp.fi
  tls:
    insecureEdgeTerminationPolicy: Redirect
    termination: edge
  to:
    kind: Service
    weight: 100
    name: nginx
status:
  ingress: []


apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: nginx
spec:
+  host: t-test-kustomize.2.rahtiapp.fi
```
What does this mean?  
You can see by applying **overlays** you'll patch your files without editing the originals. The only thing to do is to add different values for what you want to be changed and apply the overlays.  
With **overlays** you can have several files ordered into folders. For example, if you need to modify some values inside a yaml file for a production environment, you can easily do it by using **overlays** without affecting your main files. You can also create another folder `nightly` for beta testing and put there different values.  

To apply an overlay, use this command:

```sh
oc apply -k overlays/production
```

It also possible to delete everything created by an overlay using this command:

```sh
oc delete -k overlays/production
```