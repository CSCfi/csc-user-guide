# Why my private SSH key does not work in Rahti?

## Mismached keys

There are few reasons why a SSH key may not work, the simplest one is when the **private key** does not match the **public key**. In order to check this, you can re-generate the public key from the private one by doing:

```
ssh-keygen -y -f private_key_file
```

Please check that the generated public key matches the one used. Some servers also generate a key fingerprint, you may generate this fingerprint from the public or private keys, the firgerprint must match. The command to use is:

```
$ ssh-keygen -l -f repo-openshift-builder
2048 SHA256:ijP8/1P3ZSOBrJDD2PoCWmJceKd5JwDAmzmEqsH1itk openshift-source-builder/repo (RSA)

$ ssh-keygen -l -f repo-openshift-builder.pub
2048 SHA256:ijP8/1P3ZSOBrJDD2PoCWmJceKd5JwDAmzmEqsH1itk openshift-source-builder/repo (RSA)
```

## Passphrase protected key

Another common reason for failure is when the private key is protected by a passphrase. Meanwhile it is generaly recommended to protect a private key with a passphrase when storing the key in a workstation, Rahti does not have any mechanism to store the passphase and will then fail to use the key. To check if a private key is protected by a passphrase, you may use the same command above to generate the public key, If the key is portected, the command will ask for the password.

## Too new format used

The most obscure reason is that Rahti expects the key to be provided in **PEM format**. PEM used to be the default key format, but now it is considered a legacy format. Newer versions of OpenSSH will generate keys in its own format that is not recognized by the current version of Rahti (v3.11). When generating keys with `ssh-keygen` to be used in Rahti, please use the parameter `-m PEM`. A complete example would be:

```
ssh-keygen -C "openshift-source-builder/repo" -f repo-openshift-builder -N '' -m PEM
```

This will generate two files `repo-openshift-builder` and `repo-openshift-builder.pub`.

For a comprehensive guide of the whole process of using SSH keys to clone a repository in Rahti, please follow: [Repository SSH Keys](https://cloud.redhat.com/blog/private-git-repositories-part-2a-repository-ssh-keys).
