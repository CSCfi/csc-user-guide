# Best practices for client side encryption

## Introduction

The intended audience of this document is end users who want to store sensitive
data in CSC's data services for research. 

Scientific research data may contain also sensitive data. There is no single
simple definition of sensitive data but rather it is derived from national and
EU legislations.[^1] Some guidelines can be found from
[here](https://research.csc.fi/definition-of-sensitive-data).

Note that the topics discussed here are not applicable to such data that is
controlled by law of secondary use of health and social data. More information
about using CSC with secondary use data can be found
[here](../sensitive-data/sd-desktop-audited.md).

The **data controller** — meaning the customer, i.e. usually the
research project or a researcher — is responsible for knowing if the data
is sensitive or not and handling it appropriately. In case of using CSC's data
services for research the question about sensitivity of the data must be
resolved by the customer already before transferring the data to CSC's
services, which acts as **data processor** that provides storage and computing
resources for the data controller.

Generic examples of use cases where CSC's services might be used with encrypted
sensitive data are:

- Using CSC sensitive data services for analyzing data
- Distributing sensitive research data to customer's partner organizations
- Disaster recovery copy of customer's local sensitive research data
- Sharing sensitive research data within a research group

Some use cases may not be applicable to all CSC's data services, please see the
Terms and Conditions and Service Description of each service itself.

CSC provides a set of services that are intended to support management of
sensitive data. Currently, these services include:

- [SD Connect](../sensitive-data/sd_connect.md): A service for storing and
  sharing sensitive data
- [SD Desktop](../sensitive-data/sd_desktop.md): A service for processing
  sensitive data

These services provide secure and easy-to-use tools and protocols that CSC
recommends using for sensitive data. However, you can store sensitive data at
CSC also by using other tools, as long as the processes follow the general
guidelines described below.

## Encryption

Protecting data with encryption has been around for a long time and the basics
of secure encryption are well understood. This document gives some best
practices on how to encrypt the data once the customer has decided that
encryption is an appropriate way to protect the data content.

There are two main encryption methods, _symmetric_ and _asymmetric_ encryption.
In symmetric encryption, the same key is used for encrypting and decrypting the
data. In basic asymmetric encryption, there are two keys, a _private key_ and a
_public key_. Data encrypted with the public key can be decrypted only with the
private key. For verifying the origin of data, the data (normally a hash of the
data) signed with the private key can be verified with the public key.

In a general data storage use case, straightforward symmetric encryption
is usually a good choice. In that general case, all who need access to the data
content — for instance a research group — are equal, they all know the same
symmetric key.

When the use case is more targeted to data distribution and has specific
recipient(s) for the data, asymmetric encryption has advantages in key
management. The data uploader could use the recipient's asymmetric public key
to encrypt, or actually encrypt the recipient-specific symmetric key with it.
The key management is more flexible with asymmetric encryption, but the
drawback is that there is a copy of the data for each recipient.

## Scope

This document gives some best practices on how to encrypt data if storing it in
to CSC's data services for research. The decision whether encryption is an
appropriate way to protect the data content against unwanted exposure is at
the responsibility of the customer.

A customer's own environment is out of the scope of this document. As the
sensitive data exists at the customer's own environment already before it will
be stored (transferred) to CSC's data service, this document assumes that all
the necessary safeguards at the customer side — policies, procedures,
practices, etc. — are already in place.

Classified data, which requires separation by the service other than access
control is out of the scope of this document.[^7]

Computational processing of data is out of the scope of this document too, as
this document simply describes the best practices for storing sensitive data.
You can access CSC's data services for research directly from your own
environment just like from CSC's supercomputing environment. From the point of
view of the service there is no difference from where the data is transferred
to it.

## Risks of encryption

Using encryption to protect data reduces the risk to expose the data content to
unwanted parties, but it also introduces some new risks which need to be
considered. This chapter highlights the main two risks.

1. **Losing your encryption keys** — or to be more precise, the key to
   decrypt the data — is equivalent to losing your data. If you still have
   your data files but don't have the decryption key anymore, you can't restore
   the actual data content. You need to plan how to manage your keys before you
   start to use data encryption, more details on this can be found in
   [Key management](#key-management).
2. **Using poor encryption tools.** Picking just some nice or reliable looking
   software to take care of encryption may well introduce a risk of exposing
   the data content. It may be unintentional like poor software engineering or
   weak algorithms in the software. It may also be intentional, a deliberate
   attack targeted to data which is considered important enough to be
   encrypted. See [Standards and algorithms](#standards-and-algorithms) and
   [Notes on specific software](#notes-on-specific-software).

The SD Connect service mitigates these risks by applying automatically strong
asymmetric encryption for the stored data. The service also adds a CSC-hosted
encryption key to the data. This can be used in cases where the users own
encryption key is lost.

## Best practices

Copying sensitive data from a customer's own protected environment to CSC's
data service requires protecting the data both in transit and at rest on CSC's
data service.

Access to these services is protected in transit by encrypted traffic based on
HTTPS/TLS.

From the customer's perspective, protecting data at rest on a remote service is
best done by protecting it with client-side encryption and not exposing the
encryption related keys to the storage service. Client-side encryption is a
method where the customer encrypts the data in the customer's own environment
before transferring it to the service. When using client-side encryption and
not exposing the keys, the customer is the only party who controls exposing the
content of the data.[^4] [^6] Even with this, it is good to remember that
encryption should not be the only protection; storing securely at a remote
location should always be a layered approach with more than one measure, i.e.
clear user roles and access control definitions, least privileges principle,
etc.[^5]

The data which is stored at CSC's data service should not be the only existing
copy of the data.

Make sure you don't leak sensitive information in file or directory names.
Either anonymize or randomize such names or create a package — for
instance zip or tar — of the files/directories and then encrypt the whole
package.

### Standards and Algorithms

*Symmetric encryption algorithm* to use is AES (either in CBC or CTR mode, but
never in ECB) with minimum key length of 256 bits, thus an AES-256 encryption.

AES-128 and AES-192 are also currently considered to be strong enough, but as
the performance penalty is rather small between those and AES-256, and with the
fact that switching later to a stronger version of AES would mean re-encrypting
all the data, it is better to start straight with AES-256.[^2] [^3]

*Asymmetric encryption algorithm* to use is RSA and the minimum key length is
4096 bits.[^2] [^3]

Symmetric encryption software usually gives an option to use a passphrase as a
"user-friendly key". The actual encryption key is then derived from this
passphrase using a key derivation algorithm. The key derivation algorithm must
also be strong enough, preferred ones are scrypt, bcrypt, or PBKDF2 (with high
iteration count, for instance 100 000).[^2] [^8]

### Key management

Symmetric encryption software usually give an option to use a password, or a
passphrase as a "user-friendly key". In those cases, the protection of your
data is only as good as the encryption password is; encryption does not help if
you use a weak or an easy-to-guess password. Guidance on how to create strong
passwords can be found for instance in references.[^9]

Leaking a symmetric or asymmetric decryption passphrase/key means that you must
encrypt the original content with a new passphrase/key, and replace all stored
old passphrase/key encrypted data with the new encrypted data. This holds true
also for asymmetric keys in data at rest, unlike other use cases where key
revocation could be used.

Losing your symmetric data encryption passphrase/keys is equivalent to data
loss. You, or your research project should have either a copy of data content
locally available (in plain format or encrypted with some other key), or a
method to recover the encryption keys to access the data content even if the
original data encrypting party loses the passphrase/keys. Consult your local
organization where and how to save your encryption passphrase/keys securely for
recovery purposes.

Data decryption passphrase/key information must be transferred securely between
the encrypting party and the decrypting party. This is often referred to as Key
Transport.

Asymmetric encryption is the easiest way to manage data encryption key
transport with several keyholders, as public keys can be — as the name suggests
— public and exchanged openly. There are also existing Public Key
Infrastructures or "web of trusts" that can certify the origin of the public
key. Being sure that a public key is the desired recipient's public key is
essential as whoever holds the corresponding private key can decrypt data which
is encrypted with the public key. In this kind of hybrid encryption systems,
the symmetric data encryption key is encrypted with an asymmetric public key
and then transported together with the encrypted data.

For a small group of parties also a face-to-face data decryption key transport
can be an option.

Storing and retrieving encrypted data from the CSC's service can also be
arranged at the customer's local environment so that the trusted local
environment has a service that takes care of accessing the CSC's storage
service on behalf of the end user. So, only that local trusted service needs to
know the keys instead of the local end users.

There is unfortunately a bit too much flexibility in the ways different
applications behave when encrypting files — not in the actual encryption per
se, but for instance in how they store the metadata about selected encryption
choices into the encrypted file or how to derive the key from a passphrase.

The easiest way to deal with this lack of interoperability is to decide and
document what encryption software to use and how to use it in your project
before you start storing encrypted data in CSC's data services for research.

### Notes on specific software

#### GnuPG2

GnuPG version 2 is likely the most widely used good free-of-charge and open
source suite of software for encrypted messaging. GnuPG 2.2 is compliant with
the OpenPGP RFC4880 and can utilize asymmetric encryption with public keys for
easier key exchange and transport. Selecting option `--rfc4880` for maximum
portability would select symmetric encryption algorithm to be 3DES which is not
considered good enough anymore.

On the command-line the algorithm defaults can be seen with option `--verbose`.
Starting with version 2.1, the default for symmetric encryption is AES128, for
older versions it is CAST5. On the command-line AES256 encryption is selected
with options `--symmetric --cipher-algo AES256` which should be the symmetric
algorithm to be used.

**Example symmetric encryption run where file data.dat is encrypted:**

```bash
gpg --symmetric --cipher-algo AES256 data.dat
```

This example command creates the encrypted file `data.dat.gpg`.

#### OpenSSL

OpenSSL is more a toolkit for encryption related needs than a standalone
application. It is anyway an easy-to-use tool for symmetric encryption.

AES256 encryption is selected with options `enc -aes-256-cbc`. If you use a
password to generate the actual encryption key, then use only version 1.1.1 or
later and with options `-pbkdf2 -iter 100000`. These same options must also be
used when decrypting the data.

**Example run with OpenSSL 1.1.1 where file data.dat is encrypted to data.enc:**

```bash
openssl enc -aes-256-cbc -pbkdf2 -iter 100000 -in data.dat -out data.enc
enter aes-256-cbc encryption password:
Verifying - enter aes-256-cbc encryption password:
```

If you choose to generate the actual random binary key and initialization
vector yourself, then you can also use older versions than 1.1.1 of OpenSSL.

#### Crypt4GH 

Crypt4gt is an asymmetric encryption tool that is designed for encrypting large
datasets. This tool is recommended by Global Alliance for Genomics and Health,
and it is used as the encryption tool of CSC sensitive data services. A more
detailed description of this encryption tool can be found from the
[SD Connect instructions](../sensitive-data/sd_connect.md).

#### Cyberduck (Cryptomator)

Cyberduck includes an open source tool called Cryptomator for client-side
encryption. Cyberduck's strong point is its multiplatform GUI interface,
drawback is so far short history as cryptography tool, compared to GnuPG or
OpenSSL.

To make managing encryption easy for the end user, the Cryptomator treats a
remote directory as if it were a single encrypted structure (a vault), but it
actually encrypts each file for its own. In addition to the content of files,
file and directory names are encrypted.

[^1]: CSC Services for Research. Sensitive data  
      [https://research.csc.fi/sensitive-data](https://research.csc.fi/sensitive-data){ target=_blank }
[^2]: Kryptografiset vahvuusvaatimukset luottamuksellisuuden suojaamiseen — kansalliset suojaustasot  
      [https://www.kyberturvallisuuskeskus.fi/[...]/ohje-kryptografiset-vahvuusvaatimukset-kansalliset-suojaustasot.pdf](https://www.kyberturvallisuuskeskus.fi/sites/default/files/media/regulation/ohje-kryptografiset-vahvuusvaatimukset-kansalliset-suojaustasot.pdf){ target=_blank }
[^3]: NIST Special Publication 800-57 Part 1 Revision 4. Recommendation for Key Management. Part 1: General  
      [https://doi.org/10.6028/NIST.SP.800-57pt1r4](https://doi.org/10.6028/NIST.SP.800-57pt1r4){ target=_blank }
[^4]: Best practices for securing PaaS web and mobile applications using Azure Storage  
      [https://docs.microsoft.com/en-us/azure/security/fundamentals/paas-applications-using-storage](https://docs.microsoft.com/en-us/azure/security/fundamentals/paas-applications-using-storage){ target=_blank }
[^5]: Security Best Practices for Amazon S3  
      [https://docs.aws.amazon.com/AmazonS3/latest/dev/security-best-practices.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/security-best-practices.html){ target=_blank }
[^6]: Security Guidance for Critical Areas of Focus in Cloud Computing v4.0  
      [https://cloudsecurityalliance.org/artifacts/security-guidance-v4](https://cloudsecurityalliance.org/artifacts/security-guidance-v4){ target=_blank }
[^7]: Katakri 2015 — Tietoturvallisuuden auditointityökalu viranomaisille  
      [https://www.defmin.fi/files/3165/Katakri_2015_Tietoturvallisuuden_auditointityokalu_viranomaisille.pdf)](https://www.defmin.fi/files/3165/Katakri_2015_Tietoturvallisuuden_auditointityokalu_viranomaisille.pdf){ target=_blank }
[^8]: NIST Recommendation for Password-Based Key Derivation. Part 1: Storage Applications  
      [https://doi.org/10.6028/NIST.SP.800-132](https://doi.org/10.6028/NIST.SP.800-132){ target=_blank }
[^9]: 6 Techniques For Creating Strong Passwords  
      [https://www.lifewire.com/8-character-password-2180969](https://www.lifewire.com/8-character-password-2180969){ target=_blank }
