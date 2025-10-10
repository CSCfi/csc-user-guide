# Kuinka hankkia Allas S3 -tunnukset? { #how-to-get-allas-s3-credentials }

Miten saada Allas S3 -tunnukset: access key ja secret key? Jokainen tunnuspari on liitetty yhteen CSC-projektiin.

## 'allas-conf' { #allas-conf }

Käytä [`allas-conf`](../../data/Allas/using_allas/allas-conf.md#s3-connection-details) -työkalua S3-tunnustesi selvittämiseen.
Se on esiasennettu CSC:n supertietokoneille tai sen voi asentaa Linuxiin ja Maciin.

## openstack API { #openstack-api }

1. Asenna [OpenStack-komentorivityökalut](../../cloud/pouta/install-client.md)

1. Kirjaudu OpenStackiin noudattamalla artikkelia [Configure your terminal environment for OpenStack](../../cloud/pouta/install-client.md#configure-your-terminal-environment-for-openstack).

1. Voit joko hakea jo luodut tunnukset tai luoda uudet

    1. Hae jo luodut tunnukset:

        ```sh
        openstack ec2 credentials list
        ```

        Tämä listaa kaikkien projektien tunnukset, ja näet kunkin tunnusparin vieressä vain "Project ID" -tunnisteen. Voit käyttää komentoa `openstack project list` nähdäksesi kaikki projektit, joihin sinulla on pääsy; se listaa kunkin projektin nimen ja ID:n.

    1. Luo uudet tunnukset:

        ```sh
        openstack ec2 credentials create
        ```