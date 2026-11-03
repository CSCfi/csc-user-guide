# Deployment Security
 
This section controls image verification and vulnerability enforcement.
 
Administrators can enforce security policies such as:
 
## Allowing only signed images
 
Two image signature verification mechanisms are there, cosign and Notation. If enabled, only signed images can be deployed. It ensures image integrity and authenticity. 

### How to sign your images?

As mentioned before, you can use [CoSign](https://docs.sigstore.dev/) or [Notation](https://notaryproject.dev/docs/notary-project-overview/) to sign your images after being pushed

Here is an example with CoSign:

1. Install CoSign:

    If you are using macOS:

    ```
    brew install cosign
    ```

    If you are using Linux, you can download the binary for your platform from the [CoSign releases page](https://github.com/sigstore/cosign/releases/latest):

    ```sh
    # binary
    curl -O -L "https://github.com/sigstore/cosign/releases/latest/download/cosign-linux-amd64"
    sudo mv cosign-linux-amd64 /usr/local/bin/cosign
    sudo chmod +x /usr/local/bin/cosign

    # rpm
    LATEST_VERSION=$(curl https://api.github.com/repos/sigstore/cosign/releases/latest | grep tag_name | cut -d : -f2 | tr -d "v\", ")
    curl -O -L "https://github.com/sigstore/cosign/releases/latest/download/cosign-${LATEST_VERSION}-1.x86_64.rpm"
    sudo rpm -ivh cosign-${LATEST_VERSION}-1.x86_64.rpm

    # dkpg
    LATEST_VERSION=$(curl https://api.github.com/repos/sigstore/cosign/releases/latest | grep tag_name | cut -d : -f2 | tr -d "v\", ")
    curl -O -L "https://github.com/sigstore/cosign/releases/latest/download/cosign_${LATEST_VERSION}_amd64.deb"
    sudo dpkg -i cosign_${LATEST_VERSION}_amd64.deb
    ```

2. Generate Self-Managed Keys:

    Generate a key-pair by running the command `cosign generate-key-pair`. You'll be prompted to enter a password:

    ```sh
    $ cosign generate-key-pair
    Enter password for private key:
    Enter again:
    Private key written to cosign.key
    Public key written to cosign.pub
    ```

3. Signing with Self-Managed Keys:

    Once the key-pair generated, you can sign your images pushed on Satama by running this command:

    ```sh
    cosign sign --key cosign.key --new-bundle-format=false --use-signing-config=false satama.csc.fi/project/myimage@sha256:<digest> # It is better to use the digest instead of the tag
    ```

    _You can answer NO to the question_

!!! NOTE
    You need to use the arguments `--new-bundle-format` and `--use-signing-config` if you are using the latest version of CoSign. The current version of Satama (Harbor v2.14.4) doesn't support the new Sigstore bundle format

## Preventing the use of vulnerable images
 
If 'Prevent vulnerable images from running' is enabled, Satama blocks deployment of images that contain vulnerabilities above a selected severity level. 
 
You can adjust severity threshold from dropdown. If 'Low' vulnerability severity is selected, that means if any vulnerability (Low, Medium, High, Critical) exists, deployment can be blocked.
