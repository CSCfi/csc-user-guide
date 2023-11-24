# How to get Allas S3 credentials

It is possible to use the openstack API to get Allas S3 credentials (AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY). Each credential pair is linked to a single OpenStack project.

1. Install [OpenStack command line tools](/cloud/pouta/install-client/)

1. Login into OpenStack by following the [Configure your terminal environment for OpenStack](/cloud/pouta/install-client/#configure-your-terminal-environment-for-openstack) article.

1. You can either retrieve already created credentials or create new ones

    1. In order to retrieve already created credentials:

        ```sh
        openstack ec2 credentials list
        ```

        It will list the credentials of every project, and you will see only the "Project ID" next to each credential pair. You can use `openstack project list` in order to see all the projects you have access, it will list the name and the id of each of them.

    1. Create new credentials:

        ```sh
        openstack ec2 credentials create
        ```
