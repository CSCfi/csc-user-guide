# How to pull images from Rahti v1 registry

If you want to use the images stored in Rahti 1 Registry from Rahti 2 in a `Pod` you can make it via `Secret`.  
Here are the steps.

## Create a secret in Rahti v2
Type this command to create the `Secret`:

```
oc create secret docker-registry rahti-docker-pull-secret-unused --docker-server=docker-registry.rahti.csc.fi --docker-username=unused --docker-password=<token_from_rahti1_registry>
```

Replace __token_from_rahti1_registry__. You can retrieve this token by going to [Rahti Registry](https://registry-console.rahti.csc.fi/registry) web interface.

## Create a yaml file
Then, you can create a `pod.yaml` file for example:

_`pod.yaml`_:
```
- apiVersion: v1
  kind: Pod
  metadata:
    name: mypod
  spec:
    containers:
      - name: mypod
        image: docker-registry.rahti.csc.fi/project/image:tag
    imagePullSecrets:
      - name: rahti-docker-pull-secret-unused
```

Finally, apply the file using the command:
```sh
oc apply -f pod.yaml
```

Keep in mind this is an example for a `Pod`. Such procedure can also be used for `BuildConfig`, `Deployment`, `StatefulSet`, ...


# Pushing and pulling with image manifest v2 schema 1
Future releases of Docker will only able to pull images in OCI image spec format. More information [here](https://docs.docker.com/engine/deprecated/#pushing-and-pulling-with-image-manifest-v2-schema-1)

Images in Rahti v1 registry are `docker` format. If you want to copy your images from Rahti v1 registry to Rahti v2, you can use [Skopeo](https://github.com/containers/skopeo).

This command allows you to copy direcly from Rahti v1 registry to Rahti v2 and convert the format from `docker` to `oci`:
```
skopeo copy -f oci --src-creds unused:$(rahtiv1-token) docker://docker-registry.rahti.csc.fi/project/image:tag --dest-creds $(rahtiv2-login):$(rahtiv2-token) docker://image-registry.apps.2.rahti.csc.fi/project/image:tag
```

You can find your image in the `ImageStreams` section (Administrator view) or nby typing this command:
```
oc get is
```