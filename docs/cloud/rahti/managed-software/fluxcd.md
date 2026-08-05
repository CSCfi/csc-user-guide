# FluxCD

[FluxCD](https://fluxcd.io/flux/) is a set of controllers that keep your applications in Rahti in sync with a source of truth that you maintain outside the cluster, typically a Git repository. In Rahti, FluxCD is provided as a managed component, so you do not need to install or maintain the controllers yourself: you _describe_ what should be running in your Rahti project, and Flux applies it for you.

## What is GitOps

GitOps is a way of operating applications where the desired state of the system is stored in version control, and a controller running in the cluster continuously makes the cluster match it. Instead of running `oc apply` from your own machine, you commit a change and the cluster picks it up.

This has a few practical consequences:

* **The repository is the source of truth.** What is committed is what runs. If you want to know what is deployed, you read the repository rather than querying the cluster.
* **Every change has a history.** Deployments are commits, so they can be reviewed, approved, and reverted with the same tools you already use for code.
* **Nobody needs to deploy by hand.** No credentials for the cluster are needed in your continuous integration system, because nothing is pushed to Rahti from outside. Flux pulls from the repository instead.
* **Manual changes do not stick.** If someone edits a Deployment directly in the cluster, Flux changes it back on the next reconciliation. This is a feature: the cluster cannot drift away from what is written down.

## How automatic deployment works

Flux splits the work into two kinds of objects, and you normally create one of each:

* A **source** object describes where your manifests come from and how often to look for changes: a [`GitRepository`](#deploying-from-a-git-repository), an [`OCIRepository`](#deploying-from-an-oci-registry), or a [`HelmRepository`](#deploying-a-helm-chart). The source controller fetches the content and stores it inside the cluster as an artifact.
* An **applier** object describes what to do with that content: a `Kustomization` applies plain YAML or [Kustomize](../tutorials/advanced/kustomize.md) overlays, and a `HelmRelease` installs or upgrades a Helm chart.

Both kinds of object have an `interval` field, which is how often Flux checks and re-applies. This is the reconciliation loop: on every interval, Flux compares the desired state with what is in your project and corrects any difference. The interval is not a deployment delay you have to wait for in normal use, because you can always trigger a reconciliation immediately when you want one:

```bash
oc annotate --overwrite gitrepository/podinfo reconcile.fluxcd.io/requestedAt="$(date +%s)"

```

The examples on this page use an interval of one or two hours, which is a sensible default for a production application: changes are picked up automatically without polling the source every minute.

Rahti runs Flux with multi-tenancy enabled. In practice this means two things for you:

* Flux does not apply anything with its own cluster-wide permissions. Every `Kustomization` and `HelmRelease` must name a service account in your project, and Flux acts as that service account. This is what keeps one project from deploying into another.
* Sources and appliers must live in the same Rahti project. Cross-namespace references are disabled, for example, a `Kustomization` cannot use a `GitRepository` from another project.

## Prerequisites

The [`oc` command line tool](../get-started/cli.md) needs to be installed, and you need to be logged in to the right Rahti project (`oc project <project_name>`).

Before creating any Flux object, create the service account that Flux will use and grant it the `admin` role inside your project:

```bash
oc create serviceaccount flux
oc adm policy add-role-to-user admin -z flux
```

The same can be done declaratively, which is useful if you want the binding itself under version control. A `RoleBinding` that references the `admin` `ClusterRole` grants those rights only inside the project it is created in:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: flux
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: flux-admin
subjects:
- kind: ServiceAccount
  name: flux
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: admin
```

Every applier object in the examples below refers to this service account with `spec.serviceAccountName`. If you leave it out, or if the service account lacks the rights for something in your manifests, the object stays not ready and reports the permission error in its conditions.

## Deploying from a Git repository

This is the most common setup. The `GitRepository` object below tracks the `master` branch of the public [podinfo](https://github.com/stefanprodan/podinfo) repository, which Flux uses in its own documentation and which is convenient for testing, and the `Kustomization` applies the manifests found under `./kustomize`:

```yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: GitRepository
metadata:
  name: podinfo
spec:
  interval: 1h
  url: https://github.com/stefanprodan/podinfo
  ref:
    branch: master
---
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: podinfo
spec:
  interval: 1h
  targetNamespace: <NAMESPACE>
  serviceAccountName: flux
  sourceRef:
    kind: GitRepository
    name: podinfo
  path: ./kustomize
  prune: true
  timeout: 3m
```

```bash
oc apply -f podinfo-git.yaml
```

`prune: true` means that when you delete a manifest from the repository, Flux deletes the corresponding object from your project as well. Without it, removed manifests would be left running.

For a private repository, create a `Secret` with your credentials and reference it from the source:

```bash
oc create secret generic my-repo-auth \
  --from-literal=username=<GIT_USERNAME> \
  --from-literal=password=<GIT_TOKEN_OR_APP_PASSWORD>
```

```yaml
# For GitRepository resource
spec:
...
  secretRef:
    name: my-repo-auth
```

Use a token or deploy key with read-only access. An SSH key works as well, in which case the `Secret` holds `identity`, `identity.pub`, and `known_hosts` entries.

## Deploying a Helm chart

To install a chart, combine a `HelmRepository` source with a `HelmRelease`. The example uses the public podinfo chart repository:

```yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: HelmRepository
metadata:
  name: podinfo
spec:
  interval: 2h
  url: https://stefanprodan.github.io/podinfo
---
apiVersion: helm.toolkit.fluxcd.io/v2
kind: HelmRelease
metadata:
  name: podinfo
spec:
  interval: 1h
  serviceAccountName: flux
  chart:
    spec:
      chart: podinfo
      version: '6.*'
      sourceRef:
        kind: HelmRepository
        name: podinfo
      interval: 2h
  values:
    replicaCount: 1
    ingress:
      enabled: false
```

```bash
oc apply -f podinfo-helm.yaml
```

The `version` field takes a semantic version range, so `6.*` picks up patch and minor releases of the 6 series automatically while never jumping to 7. The `interval` inside `chart.spec` is how often Flux checks the chart repository for a new version matching that range, and the `interval` of the `HelmRelease` is how often the release itself is reconciled. Anything you would normally put in a `values.yaml` file goes under `values`.

!!! note "Charts in an OCI registry"

    Many projects now publish charts to an OCI registry instead of a chart repository. For those, set `type: oci` in the `HelmRepository` and use an `oci://` URL, for example `oci://ghcr.io/stefanprodan/charts`. The `HelmRelease` stays the same.

Bear in mind the support levels described on the [Rahti catalog](../usage/catalog.md) page when choosing a chart, and prefer charts whose images you can rely on being updated.

## Deploying from an OCI registry

Manifests can also be packaged as an OCI artifact and stored in a container registry, next to your images. This removes the dependency on Git being reachable at deployment time and gives you immutable, digest-addressable releases. An `OCIRepository` replaces the `GitRepository`, and the `Kustomization` is unchanged apart from the source reference:

```yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: OCIRepository
metadata:
  name: podinfo
spec:
  interval: 2h
  url: oci://ghcr.io/stefanprodan/manifests/podinfo
  ref:
    semver: '6.*'
---
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: podinfo
spec:
  interval: 1h
  targetNamespace: <NAMESPACE>
  serviceAccountName: flux
  sourceRef:
    kind: OCIRepository
    name: podinfo
  path: ./
  prune: true
  timeout: 3m
```

```bash
oc apply -f podinfo-oci.yaml
```

Instead of `semver`, the `ref` can name a `tag` or pin a `digest` for a fully immutable deployment. For a private registry, add a `secretRef` pointing to a pull secret, which can be the same one you use for images in your project.

## Encrypting secrets with SOPS

A GitOps repository holds your whole deployment, which means it would also hold your `Secret` objects. Committing them in plain text is not acceptable, even in a private repository. Flux solves this with [SOPS](https://github.com/getsops/sops), which encrypts only the values inside a YAML file and leaves the structure readable. The encrypted file is safe to commit, and the `kustomize-controller` decrypts it inside the cluster when it applies the manifest, so the plaintext exists only in your project.

The default way of doing this is with a GPG key pair. Generate one without a passphrase, since Flux has to use it unattended:

```bash
export KEY_NAME="my-project.rahti.csc.fi"
export KEY_COMMENT="flux secrets"

gpg --batch --full-generate-key <<EOF
%no-protection
Key-Type: 1
Key-Length: 4096
Subkey-Type: 1
Subkey-Length: 4096
Expire-Date: 0
Name-Comment: ${KEY_COMMENT}
Name-Real: ${KEY_NAME}
EOF
```

Take note of the key fingerprint, which identifies the key in the commands that follow:

```bash
gpg --list-secret-keys "${KEY_NAME}"
```

```sh
sec   rsa4096 2026-08-04 [SC]
      1F3D1CED2F865F5E59CA564553241F147E7C5FA4
```

```bash
export KEY_FP=1F3D1CED2F865F5E59CA564553241F147E7C5FA4
```

Store the private key in your Rahti project so that Flux can decrypt with it. The entry in the `Secret` has to end in `.asc`:

```bash
gpg --export-secret-keys --armor "${KEY_FP}" |
  oc create secret generic sops-gpg --from-file=sops.asc=/dev/stdin
```

Back up the private key somewhere safe, and then remove it from your own machine, so that the only copy that can decrypt is the one in the cluster:

```bash
gpg --delete-secret-keys "${KEY_FP}"
```

The **public** key is what you and your colleagues use to encrypt, so it can be committed to the repository:

```bash
gpg --export --armor "${KEY_FP}" > .sops.pub.asc
```

Anyone who needs to add an encrypted file imports it once with `gpg --import .sops.pub.asc`.

Next, tell SOPS which key to use and which fields to encrypt by adding a `.sops.yaml` file to the root of the repository. Encrypting only `data` and `stringData` keeps the rest of the manifest readable, so changes to it can still be reviewed in a diff:

```yaml
creation_rules:
  - path_regex: .*.yaml
    encrypted_regex: ^(data|stringData)$
    pgp: 1F3D1CED2F865F5E59CA564553241F147E7C5FA4
```

With that file in place, encrypting a manifest needs no further arguments:

```bash
sops --encrypt --in-place my-secret.yaml
```

Commit the encrypted file, and tell the `Kustomization` to decrypt:

```yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: my-app
spec:
  interval: 1h
  serviceAccountName: flux
  sourceRef:
    kind: GitRepository
    name: my-app
  path: ./deploy
  prune: true
  decryption:
    provider: sops
    secretRef:
      name: sops-gpg
```

!!! warning

    The private key in the `sops-gpg` `Secret` can decrypt every secret in your repository. Keep it out of the repository itself, restrict who has access to the Rahti project that holds it, and rotate it if it is ever exposed. Anyone who can read secrets in your project can also read the decrypted values, so treat project membership as equivalent to access to those credentials.
    You can add GPG public key to your repository but **never commit the private key**.

SOPS supports other kinds of keys as well. [age](https://github.com/FiloSottile/age) is a simpler alternative to GPG, and a key management service avoids storing a private key in the cluster at all, at the cost of needing credentials for that external service. Both are documented in the upstream [Flux guide on Mozilla SOPS](https://fluxcd.io/flux/guides/mozilla-sops/).

## Checking what Flux is doing

The status of every Flux object is visible with `oc`:

```bash
oc get gitrepositories,ocirepositories,helmrepositories
oc get kustomizations,helmreleases
```

```sh
NAME                        URL                                        READY   STATUS
gitrepository/podinfo       https://github.com/stefanprodan/podinfo    True    stored artifact for revision 'master@sha1:...'

NAME                        READY   STATUS
kustomization/podinfo       True    Applied revision: master@sha1:...
```

If `READY` is `False`, the reason is in the object's conditions:

```bash
oc describe kustomization podinfo
oc describe helmrelease podinfo
```

To stop Flux from reconciling temporarily, for example while debugging something by hand, suspend the object and resume it afterwards:

```bash
oc patch kustomization podinfo --type=merge -p '{"spec":{"suspend":true}}'
oc patch kustomization podinfo --type=merge -p '{"spec":{"suspend":false}}'
```

!!! note "The flux command line tool"

    Flux has its own CLI, which offers shortcuts such as `flux get all` and `flux reconcile`. It is convenient, but its `flux bootstrap` and `flux install` commands need cluster-admin rights and are not usable in Rahti, since the controllers are already installed and managed for you. The `oc` commands above work with ordinary project permissions.

## More information

* [Flux documentation](https://fluxcd.io/flux/): the full reference for all source and applier kinds.
* [Flux Kustomization reference](https://fluxcd.io/flux/components/kustomize/kustomizations/): every field of the applier used above, including SOPS decryption.
* [Flux guide on SOPS](https://fluxcd.io/flux/guides/mozilla-sops/): encrypting secrets with GPG, age, or a key management service.
* [Kustomize](../tutorials/advanced/kustomize.md): how to structure the manifests that a `Kustomization` applies.
* [CI/CD on Rahti](../tutorials/advanced/ci-cd-introduction.md): how automatic deployment fits into a wider pipeline.
