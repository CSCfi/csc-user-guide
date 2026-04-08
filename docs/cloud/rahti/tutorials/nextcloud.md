!!! error "Advanced level"
    This tutorial requires a good knowledge of Kubernetes environment.

# Set up Nextcloud on Rahti

In this tutorial, we will show how to deploy Nextcloud on Rahti.

## Prerequisites

You need the [oc](../usage/cli.md) installed on your computer as well as [helm](https://helm.sh).

Create a new folder named `nextcloud`

At the end, our tree will look like this:

```sh
nextcloud
├── docker
│   ├── 32
│   │   ├── apache
│   │   │   └── config
│   │   ├── fpm
│   │   │   └── config
│   │   └── fpm-alpine
│   │       └── config
│   └── 33
│       ├── apache
│       │   └── config
│       ├── fpm
│       │   └── config
│       └── fpm-alpine
│           └── config
├── kustomize
│   ├── base
│   └── nextcloud
└── post-render
```

The `docker` is the GitHub repository that we will clone in the next step.

The `kustomize` and the `post-render` folders will be created later in this tutorial.

## Nextcloud GitHub repository

We'll need to bring some modifications to the `Dockerfile` to be able to run Nextcloud on Rahti.

Rahti runs OKD which includes some [default security policies](../security-guide.md#cluster-policy). Also, it is not possible to bind the ports 80 or 443 without elevated privileges.

Our modifications will:

- Change the rights on `/usr/local/etc/php/conf.d` for the `entrypoint` to be able to write.
- Change the exposed port from 80 to 8080.

Clone the repository:

```sh
git clone git@github.com:nextcloud/docker.git
```

After cloning the repository, navigate to `docker/33/apache` (_NOTE: The name may change over time_) and edit the `Dockerfile` to add the lines:

```diff
    [...]
    RUN set -ex; \
        fetchDeps=" \
            gnupg \
            dirmngr \
        "; \
        apt-get update; \
        apt-get install -y --no-install-recommends $fetchDeps; \
        \
        curl -fsSL -o nextcloud.tar.bz2 "https://github.com/nextcloud-releases/server/releases/download/v33.0.2/nextcloud-33.0.2.tar.bz2"; \
        curl -fsSL -o nextcloud.tar.bz2.asc "https://github.com/nextcloud-releases/server/releases/download/v33.0.2/nextcloud-33.0.2.tar.bz2.asc"; \
        export GNUPGHOME="$(mktemp -d)"; \
    # gpg key from https://nextcloud.com/nextcloud.asc
        gpg --batch --keyserver keyserver.ubuntu.com --recv-keys 28806A878AE423A28372792ED75899B9A724937A; \
        gpg --batch --verify nextcloud.tar.bz2.asc nextcloud.tar.bz2; \
        tar -xjf nextcloud.tar.bz2 -C /usr/src/; \
        gpgconf --kill all; \
        rm nextcloud.tar.bz2.asc nextcloud.tar.bz2; \
        rm -rf "$GNUPGHOME" /usr/src/nextcloud/updater; \
        mkdir -p /usr/src/nextcloud/data; \
        mkdir -p /usr/src/nextcloud/custom_apps; \
        chmod +x /usr/src/nextcloud/occ; \
+       chmod 777 /usr/local/etc/php/conf.d/; \
+       sed -i.BAK "s/80/8080/g" /etc/apache2/ports.conf; \
+       sed -i.BAK "s/80/8080/g" /etc/apache2/sites-enabled/000-default.conf; \
        \
        apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $fetchDeps; \
        apt-get dist-clean

    COPY *.sh upgrade.exclude /
    COPY config/* /usr/src/nextcloud/config/

+   EXPOSE 8080

    ENTRYPOINT ["/entrypoint.sh"]
    CMD ["apache2-foreground"]
```

Build the images:

```sh
docker build . --platform linux/amd64 --tag image-registry.apps.2.rahti.csc.fi/<YOUR_PROJECT>/nextcloud:33.0.0-apache
```

_Replace YOUR_PROJECT by your Rahti project_

Once built, [push](../images/Using_Rahti_integrated_registry.md) the image on the Rahti registry:

```sh
docker push image-registry.apps.2.rahti.csc.fi/<YOUR_PROJECT>/nextcloud:33.0.0-apache
```

## Nextcloud Helm Chart

We will install Nextcloud via Helm. We will use this Helm Chart: [https://github.com/nextcloud/helm](https://github.com/nextcloud/helm)

1. Add the Helm Repository

    ```sh
    helm repo add nextcloud https://nextcloud.github.io.helm/
    helm repo update
    ```

2. Create a `nextcloud-values.yaml` file:

    ```yaml
    image:
      registry: image-registry.apps.2.rahti.csc.fi
      repository: <YOUR_PROJECT>/nextcloud
      tag: 33.0.0-apache
      pullPolicy: Always

    ingress:
      enabled: false

    nextcloud:
      host:
      username:
      password:

    containerPort: 8080

    objectStore:
      s3:
        enabled: true
        accessKey:
        secretKey:
        host: a3s.fi
        region: regionOne
        bucket:

    extraInitContainers:
      - name: init-permissions
        image: busybox
        command: ["sh", "-c", "set -eux; mkdir -p /var/www/html/data; chmod 770 /var/www/html/data"]
        securityContext:
          allowPrivilegeEscalation: false
          capabilities:
            drop: ["ALL"]
        volumeMounts:
          - name: nextcloud-main
            mountPath: /var/www/html

    internalDatabase:
      enabled: false

    externalDatabase:
      enabled: true
      type: postgresql
      host:
      user:
      password:

    redis:
      enabled: true

    persistence:
      enabled: true
      size: 8Gi

    resources:
      limits:
        cpu: 500m
        memory: 512Mi
      requests:
        cpu: 500m
        memory: 512Mi

    livenessProbe:
      enabled: false
    readinessProbe:
      enabled: false
    ```

### Required settings

* `image.registry` - Name of the registry where the built image is located. In our example, Rahti registry

* `image.repository` - Name of the repository where the built image is located. In our example, the name of your Rahti project and the name of the image (nextcloud)

* `image.tag` - Tag of the built image

* `nextcloud.host` - Public URL of your Nextcloud application. Use `.rahtiapp.fi` for an OKD Route (see [later](#helm-post-renderer-and-kustomize))

* `nextcloud.username` - Username of your Nextcloud admin

* `nextcloud.password` - Password for your Nextcloud admin

* `nextcloud.objectStore.s3.accessKey` - Access Key to Allas. See our [FAQ](../../../support/faq/how-to-get-Allas-s3-credentials.md) on how to get Allas S3 credentials

* `nextcloud.objectStore.s3.secretKey` - Secret Key to Allas. See our [FAQ](../../../support/faq/how-to-get-Allas-s3-credentials.md) on how to get Allas S3 credentials

* `nextcloud.objectStore.s3.bucket` - Name of your bucket on Allas

* `externalDatabase.host` - Public IP of your Pukki Database

* `externalDatabase.user` - Username of your Pukki Database

* `externalDatabase.password` - Password of your Pukki Database

## Helm post-renderer and Kustomize

!!! info Documentations  
    For more information about Kustomize, check our [documentation](kustomize.md)
    
    For more information about Helm, check our [FAQ](../../../support/faq/helm.md)

Since Helm 4, post renderers are [implemented as plugins](https://helm.sh/docs/overview#post-renderers-implemented-as-plugins), which means that we need to create our Helm plugin.

**Why do we need a custom-made plugin?**

Because Helm will need to edit some templates before applying them. `--post-renderer <plugin>` is here to fulfill our needs.

1. Create a new folder called `post-render` in the root of your `nextcloud` folder

2. Create a new bash file and save it as `kustomize-postrenderer` in `post-render`:

    ```bash
    #!/usr/bin/env bash

    set -x

    SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
    cd "$SCRIPT_DIR" || exit 6

    env >/tmp/kustomize.log

    # Save Helm-rendered YAML to base.yaml
    cat >"$OLDPWD/kustomize/base/base.yaml"

    # Build final manifests
    if type kustomize >/dev/null 2>&1; then
    KBIN="kustomize build"
    elif command -v oc >/dev/null 2>&1; then
    KBIN="oc kustomize"
    else
    echo "ERROR, oc command not found. Exiting." >&2
    exit 5
    fi

    exec $KBIN "$OLDPWD/kustomize/nextcloud" 2> >(tee -a /tmp/kustomize.log >&2)
    ```

3. Still in `post-render` folder, create a `plugin.yaml` file:

    ```yaml
    apiVersion: "v1"
    type: "postrenderer/v1"
    name: "kustomize"
    version: "0.1.0"
    runtime: "subprocess"
    runtimeConfig:
      platformCommand:
        - os: linux
        command: "$HELM_PLUGIN_DIR/kustomize-postrenderer"
        - os: darwin
        command: "$HELM_PLUGIN_DIR/kustomize-postrenderer"
    ```

4. Install your newly created plugin:

    ```sh
    helm plugin install post-render
    ```

    Check if the plugin is installed by running the command `helm plugin list`

5. Create a folder named `kustomize` and two subfolders: `base` and `nextcloud`

6. In the `base` folder, create two files:

    `kustomization.yaml`

    ```yaml
    apiVersion: kustomize.config.k8s.io/v1beta1
    kind: Kustomization

    resources:
      - base.yaml
      - route.yaml
    ```

    `route.yaml`

    ```yaml
    apiVersion: route.openshift.io/v1
    kind: Route
    metadata:
      name: nextcloud
    spec:
      host:
      tls:
        insecureEdgeTerminationPolicy: Redirect
        termination: edge
      to:
        kind: Service
        name: nextcloud
        weight: 100
    ```

7. In the `nextcloud` folder, create one file named `kustomization.yaml`:

    ```yaml
    apiVersion: kustomize.config.k8s.io/v1beta1
    kind: Kustomizations

    resources:
      - ../base/

    patches:
      - target:
          kind: Deployment
          labelSelector: app.kubernetes.io/name=nextcloud
        patch: |
          - op: remove
            path: /spec/template/spec/securityContext

      - target:
          kind: Route
          name: nextcloud
        patch: |
          - op: replace
            path: /spec/host
            value: # Must be the same as `.Values.nextcloud.host`
    ```

    This file will be our "kustomization". We need to remove the `securityContext` and we will create an OKD Route.

    For the Route, you need to add in `value:` the value defined in `.Values.nextcloud.host`

## Deploy

Once everything is ready, you can deploy Nextcloud by running this command:

```sh
helm install nextcloud nextcloud/nextcloud -f nextcloud-values.yaml --post-renderer kustomize
```