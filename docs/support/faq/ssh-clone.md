# Why my private SSH key does not work in Rahti 2?

You may need a SSH key pair for the case of a build from a private GitHub repository.  
This article can help you to debug why your keys are not working.

For a comprehensive guide of the whole process of using SSH keys to clone a private repository in Rahti, please follow: [Repository SSH Keys](https://cloud.redhat.com/blog/private-git-repositories-part-2a-repository-ssh-keys) guide.

## Mismatched keys

There are few reasons why a SSH key may not work, the simplest one is when the **private key** does not match the **public key**. In order to check this, you can re-generate the public key from the private one by doing:

```bash
ssh-keygen -y -f private_key_file
```

Please check that the generated public key matches the one used. Some servers also generate a key fingerprint, you may generate this fingerprint from the public or private keys, the fingerprint must match. The command to use is:

```bash
$ ssh-keygen -l -f repo-openshift-builder
2048 SHA256:ijP8/1P3ZSOBrJDD2PoCWmJceKd5JwDAmzmEqsH1itk openshift-source-builder/repo (RSA)

$ ssh-keygen -l -f repo-openshift-builder.pub
2048 SHA256:ijP8/1P3ZSOBrJDD2PoCWmJceKd5JwDAmzmEqsH1itk openshift-source-builder/repo (RSA)
```

## Passphrase protected key

Another common reason for failure is when the private key is protected by a passphrase. Even though it is generally recommended to protect a private key with a passphrase when storing the key in a workstation, Rahti 2 does not have any mechanism to store the passphrase and will then fail to use the key. To check if a private key is protected with a passphrase, you may use the same command above to generate the public key, If the key is protected, the command will ask for the password.

## Miscellaneous format errors

The SSH key format is strict. A private SSH key can be considered invalid in the following cases:

* The key is encoded using DOS format line endings. Text files created on DOS/Windows machines have different line endings than files created on Unix/Linux. DOS uses carriage return and line feed (`\r\n`) as a line ending, which Unix uses just line feed (`\n`). The **solution** is to use a tool like `dos2unix` or recreate the key in Linux.
* The header (`-----BEGIN OPENSSH PRIVATE KEY-----`) or the footer (`-----END OPENSSH PRIVATE KEY-----`) of the key is not copied correctly. There must be 5 `-` characters in both ends of both the header and the footer, and there must be an end of line after the footer, i.e.: the last character of the file is not a '-' but a newline('\n'). This problem is created normally by copy paste errors when the end or beginning of the key file are not copied correctly, and it is the source of most common "format errors".

As a general rule, use `ssh-keygen -l -f <file>` to check the formatting of the key is correct.
