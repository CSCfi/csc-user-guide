
# Kuinka saada Allas S3 -tunnistetiedot {#how-to-get-allas-s3-credentials}

On mahdollista käyttää openstack API:a saadaksesi Allas S3 -tunnistetiedot (AWS_ACCESS_KEY_ID ja AWS_SECRET_ACCESS_KEY). Jokainen tunnistepari on linkitetty yhteen OpenStack-projektiin.

1. Asenna [OpenStack komentorivityökalut](../../cloud/pouta/install-client.md)

1. Kirjaudu OpenStackiin noudattamalla artikkelia [Määritä terminaaliympäristösi OpenStackille](../../cloud/pouta/install-client.md#configure-your-terminal-environment-for-openstack).

1. Voit joko hakea jo luotuja tunnistetietoja tai luoda uusia

    1. Jo luotujen tunnistetietojen hakeminen:

        ```sh
        openstack ec2 credentials list
        ```

        Tämä luetteloi kaikkien projektien tunnistetiedot, ja näet vain "Project ID" kunkin tunnisteparin vieressä. Voit käyttää `openstack project list` nähdäksesi kaikki projektit, joihin sinulla on pääsy, se luettelee kunkin projektin nimen ja tunnuksen.

    1. Uusien tunnistetietojen luominen:

        ```sh
        openstack ec2 credentials create
        ```
