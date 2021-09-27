# Why Rahti cannot find this docker image?

![Could not load image](img/Could_not_load_image_metadata.png)

Often there are simple causes for this problem. Maybe there is a typo in the image name, or the image might have been removed since the last time it was successfully pulled. These two problems are common, and as such, it is worth double-checking the image source.

![Failed to pull image](img/Failed_to_pull_image.png)

## Private image

Another cause is that maybe the image is private. In this case, it is necessary to set up a `docker-registry` secret with an account credential having the required permissions to pull the image. For example, for an image stored in docker hub:

```bash
$ oc create secret docker-registry <SECRET-NAME> \
      --docker-username=<USERNAME> \
      --docker-server=docker.io \
      --docker-email=<EMAIL> \
      --docker-password=<PASSWORD>

$ oc secrets link default myprivaterepoaccess --for=pull
```

**Note**: Substitute place holders with actual username, password and email (without <>).
secret-name.

You can find more information in the [How to add docker hub credentials to a project](../../../cloud/rahti/tutorials/docker_hub_login/) article.

## Unsupported image format

Other more obscure problem is when the format of the image is not supported by the current version of Rahti (v3.11), which uses an old version of the docker client. Currently there are two docker image formats, docker (`application/vnd.docker.container.image.v1+json`) and OCI (`application/vnd.oci.image.manifest.v1+json`), the current version of Rahti only supports `docker`.

When an old client is used to try to pull a image with the newer format, the client cannot find it and returns a `repository does not exist` error. There is not a trivial and definitive procedure to confirm that the image indeed exists but it is stored in the newer format. One way is to use an old version of docker (Rahti uses the one coming with centos7) to try to pull the image, and then use a newer version to try to pull the same image. If it pulls in the new, but not in the old, it is a clear indication that the image is using the new format.

### Script

Other option is to use the script below. When an image is pulled from a registry, the REST API of the registry is used. In the REST request it is necessary to indicate the accepted media type using an HTTPD header. The script makes a request using the old format media type. If the return code is `200` the image is in the old format, and if it is `404` the new.

```bash
#!/bin/bash -e

readonly REGISTRY_ADDRESS="${REGISTRY_ADDRESS:-registry-1.docker.io}"
readonly MEDIA_TYPE="${MEDIA_TYPE:-application/vnd.docker.container.image.v1+json}"
#readonly MEDIA_TYPE="${MEDIA_TYPE:-application/vnd.oci.image.manifest.v1+json}"

main() {

  local image=$1
  local tag=$2

  if [ -z "$tag" ];
  then
    echo "Use: $0 <image> <tag>"
    exit 1
  fi

  local token
  token="$(get_token "$image")"

  if [ -z "$token" ];
  then
    echo "No token returned" >&2
    exit 2
  fi

  get_manifest "$image" "$tag" "$token"

}

get_token() {
  local image=$1

  curl \
    --silent \
    "https://auth.docker.io/token?scope=repository:$image:pull&service=registry.docker.io" \
    | jq -r '.token'
}

get_manifest() {
  local image=$1
  local tag=$2
  local token=$3

  TMPF=$(mktemp)

  code=$(curl \
    -s \
    --header "Accept: $MEDIA_TYPE" \
    --header "Authorization: Bearer $token" \
    -o "$TMPF" \
    -w "%{http_code}" \
    "https://$REGISTRY_ADDRESS/v2/$image/manifests/$tag")

    if [ "$code" -eq "404" ];
    then
      cat "$TMPF" >&2
    else
     echo "($code) Image stored in $MEDIA_TYPE format" >&2
    fi

    rm "$TMPF"
}

main "$@"
```

## Workarounds

* A trivial fix is to pull the image using a compatible client, re-tag it, and push it to Rahti's internal registry. This new pushed image will be using the old docker format. Follow the link for a guide on [How to manually cache images in Rahti's registry](../../../cloud/rahti/tutorials/docker_hub_manual_caching/).

* If the image was built by your team, the [buildah](https://buildah.io) tool can be used. It allows to build docker images without the extra privileges the `docker build` requires, and even though by default it will build an image using the `OCI` format, it has an option to use the `docker` format instead:

```bash
buildah bud -t image/name:tag --format=docker
```
