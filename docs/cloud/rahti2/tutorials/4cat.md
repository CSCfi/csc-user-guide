# How to deploy 4cat in Rahti

This tutorial is a long format one, it explains all the different steps that were necessary to deploy the [4cat_fi](https://github.com/uh-dcm/4cat_fi) application into Rahti. The idea is to explain the story of how the different issues were found and solved. Each issue will have its own chapter and hopefully the solution will be easy to apply to any other application with similar issues.

4Cat is a capture and analysis toolkit. From the Github page linked above, we learnt that the tool is used for analysing social media platforms and that one of the installation methods is docker compose. This is good news because:

1. We can test the application deployment using docker compose and see how it looks.
1. We do not need to create a docker container from scratch.
1. We can use the docker compose deployment as a base and adapt it to Kubernetes deployment using [kompose](https://kompose.io). This tool is specifically designed to make this conversions. From their website: "Our conversions are not always 1:1 from Docker Compose to Kubernetes, but we will help get you 99% of the way there!". And it indeed will save us a lot of tedious conversion time, but it will not be the end of it.

!!! warning "Linux is used for all the examples"
    We have prepared this tutorial using a Linux machine. In principle, all these commands run also in Windows and Mac, but if confused I recommend you to [install a tiny VM in Pouta](https://docs.csc.fi/cloud/pouta/launch-vm-from-web-gui/) and use it for following the tutorial instead. This is usefull even for Linux users, as you will be able to install, uninstall or change software without risking your local installation.


## Docker compose

1. Before continuing, we will need to have docker and the docker compose plugin installed. You can find instructions on how to install docker compose here:

    - https://docs.docker.com/compose/install/

    For Debian and Ubuntu you can install it by:

    ```sh
    sudo apt-get update
    sudo apt-get install docker.io docker-compose
    ```

    You can use podman compose or similar, but we will use docker as it is the most common tool.

1. Once docker compose is installed, let's deploy it and see how the application works. You will need to clone the repository and run docker-compose inside the cloned folder:

    ```sh
    git clone https://github.com/uh-dcm/4cat_fi
    cd 4cat_fi
    sudo docker compose up
    ```

    This will start the process for deploying the application in the machine. It can take some time to pull the images and configure the application. If you `Ctrl+C` the application will exit. If you want to run it on the background, you just need to add `-d` or  `--detach`.

    ![docker-compose output](/cloud/img/4cat-docker-compose.png)

    After a while the application will be available on port `80` (The `PUBLIC_PORT`):

    ![4cat first run](/cloud/img/4cat.png)

### Analysis

The [docker-compose.yml](https://github.com/digitalmethodsinitiative/4cat/blob/master/docker-compose.yml) file is the following:

```yaml
services:
  db:
    container_name: 4cat_db
    image: postgres:${POSTGRES_TAG}
    restart: unless-stopped
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_HOST_AUTH_METHOD=${POSTGRES_HOST_AUTH_METHOD}
    volumes:
      - 4cat_db:/var/lib/postgresql/data/
    healthcheck:
      test: [ "CMD-SHELL", "pg_isready -U $${POSTGRES_USER}" ]
      interval: 5s
      timeout: 5s
      retries: 5

  backend:
    image: digitalmethodsinitiative/4cat:${DOCKER_TAG}
    container_name: 4cat_backend
    restart: unless-stopped
    env_file:
      - .env
    depends_on:
      db:
        condition: service_healthy
    ports:
      - ${PUBLIC_API_PORT}:4444
    volumes:
      - 4cat_data:/usr/src/app/data/
      - 4cat_config:/usr/src/app/config/
      - 4cat_logs:/usr/src/app/logs/
    entrypoint: docker/docker-entrypoint.sh

  frontend:
    image: digitalmethodsinitiative/4cat:${DOCKER_TAG}
    container_name: 4cat_frontend
    restart: unless-stopped
    env_file:
      - .env
    depends_on:
      - db
      - backend
    ports:
      - ${PUBLIC_PORT}:500
      - ${TELEGRAM_PORT}:443
    volumes:
      - 4cat_data:/usr/src/app/data/
      - 4cat_config:/usr/src/app/config/
      - 4cat_logs:/usr/src/app/logs/
    command: ["docker/wait-for-backend.sh"]

volumes:
  4cat_db:
    name: ${DOCKER_DB_VOL}
  4cat_data:
    name: ${DOCKER_DATA_VOL}
  4cat_config:
    name: ${DOCKER_CONFIG_VOL}
  4cat_logs:
    name: ${DOCKER_LOGS_VOL}
```

Also let's check the [.env](https://github.com/uh-dcm/4cat_fi/blob/master/.env) file:

```ini
# 4CAT Version: Update with latest release tag or 'latest'
# https://hub.docker.com/repository/docker/digitalmethodsinitiative/4cat/tags?page=1&ordering=last_updated
DOCKER_TAG=stable
# You can select Postrgres Docker image tags here to suit your needs: https://hub.docker.com/_/postgres
POSTGRES_TAG=latest

# Database setup
POSTGRES_USER=fourcat
POSTGRES_PASSWORD=supers3cr3t
POSTGRES_DB=fourcat
POSTGRES_HOST_AUTH_METHOD=trust
# POSTGRES_HOST should correspond with the database container name set in docker-compose.yml
POSTGRES_HOST=db
POSTGRES_PORT=5432  # Docker postgres image uses port 5432

# Server information
# SERVER_NAME is only used on first run; afterwards it can be set in the frontend
SERVER_NAME=localhost
PUBLIC_PORT=80

# Backend API
# API_HOST is used by the frontend; in Docker it should be the backend container name
# (or "localhost" if front and backend are running together in one container
API_HOST=backend
PUBLIC_API_PORT=4444

# Telegram apparently needs its own port
TELEGRAM_PORT=443

# Docker Volume Names
DOCKER_DB_VOL=4cat_4cat_db
DOCKER_DATA_VOL=4cat_4cat_data
DOCKER_CONFIG_VOL=4cat_4cat_config
DOCKER_LOGS_VOL=4cat_4cat_logs

# Gunicorn settings
worker_tmp_dir=/dev/shm
workers=4
threads=4
worker_class=gthread
log_level=debug
```

As you can see this `docker-compose.yml` file is a [YAML](https://en.wikipedia.org/wiki/YAML) file with two main sections: `services` and `volumes`. There are 3 `services` and 4 `volumes`. In Kubernetes this will mean 3 `Deployments` and 4 `PersistentVolumeClaim`s (PVC). The most important fields of a service are:

- `image` is the image that docker will need to pull and run for every service. In our case, we have two different images, the `postgres` image (a well known database) and the `4cat_fi`. As docker compose is working we know that both images exists and can be pulled with no issue.
- `environment` and `env_file` define the environment variables that will configure the services. For example `POSTGRES_PASSWORD` is used to pass the password to the database.
- `volumes` is where we tell docker which volumes we need to be attached to the service and in which folder they need to be mounted.
- `ports` tells us the public ports, the internal ports, and the mapping between themselves. The notation is `<external_port>:<internal_port>`.
- `entrypoint` and `command` are the commands to be executed when the image is launched. Postgres does not have either due to the fact that the image has already a `command`/`entrypoint`.

The volumes section is simpler and only contains a list of names. A "docker compose volume" is a normal docker volume and does not include a size, because it will be using the local disk, and the size will be the limit of the local disk. Volumes in Kubernetes do have a size and we will need to account for that when we do the conversion.

The `.env` file has the default values to properly deploy the application. Like `PUBLIC_PORT` that is set to `80`.

## Kompose

Kompose will allow us to translate the `docker-compose.yaml` file into a set of Kubernetes YAML files.

1. We need to have [kompose](https://kompose.io/) installed. You can follow the instruction here:

    - https://kompose.io/installation/

    As we have docker already installed, we can follow the docker method that will build the image from source:

    ```sh
    sudo docker build -t kompose https://github.com/kubernetes/kompose.git\#main
    ```

1. Run kompose (while still being in the 4cat_fi folder):

    ```sh
    $ docker run --rm -it -v $PWD:/opt kompose sh -c "cd /opt && kompose convert"
    WARN The "DOCKER_CONFIG_VOL" variable is not set. Defaulting to a blank string.
    WARN The "DOCKER_LOGS_VOL" variable is not set. Defaulting to a blank string.
    WARN The "DOCKER_DB_VOL" variable is not set. Defaulting to a blank string.
    WARN The "DOCKER_DATA_VOL" variable is not set. Defaulting to a blank string.
    WARN The "PUBLIC_PORT" variable is not set. Defaulting to a blank string.
    WARN The "TELEGRAM_PORT" variable is not set. Defaulting to a blank string.
    WARN The "DOCKER_TAG" variable is not set. Defaulting to a blank string.
    WARN The "POSTGRES_TAG" variable is not set. Defaulting to a blank string.
    WARN The "POSTGRES_USER" variable is not set. Defaulting to a blank string.
    WARN The "POSTGRES_PASSWORD" variable is not set. Defaulting to a blank string.
    WARN The "POSTGRES_DB" variable is not set. Defaulting to a blank string.
    WARN The "POSTGRES_HOST_AUTH_METHOD" variable is not set. Defaulting to a blank string.
    WARN The "PUBLIC_API_PORT" variable is not set. Defaulting to a blank string.
    WARN The "DOCKER_TAG" variable is not set. Defaulting to a blank string.``
    WARN Restart policy 'unless-stopped' in service frontend is not supported, convert it to 'always'
    WARN Restart policy 'unless-stopped' in service db is not supported, convert it to 'always'
    WARN Restart policy 'unless-stopped' in service backend is not supported, convert it to 'always'
    WARN File don't exist or failed to check if the directory is empty: stat :/usr/src/app/data: no such file or directory
    WARN File don't exist or failed to check if the directory is empty: stat :/usr/src/app/config: no such file or directory
    WARN File don't exist or failed to check if the directory is empty: stat :/usr/src/app/logs: no such file or directory
    WARN Service "db" won't be created because 'ports' is not specified
    WARN File don't exist or failed to check if the directory is empty: stat :/var/lib/postgresql/data: no such file or directory
    WARN File don't exist or failed to check if the directory is empty: stat :/usr/src/app/data: no such file or directory
    WARN File don't exist or failed to check if the directory is empty: stat :/usr/src/app/config: no such file or directory
    WARN File don't exist or failed to check if the directory is empty: stat :/usr/src/app/logs: no such file or directory
    INFO Kubernetes file "backend-service.yaml" created
    INFO Kubernetes file "frontend-service.yaml" created
    INFO Kubernetes file "backend-deployment.yaml" created
    INFO Kubernetes file "env-configmap.yaml" created
    INFO Kubernetes file "4cat-data-persistentvolumeclaim.yaml" created
    INFO Kubernetes file "4cat-config-persistentvolumeclaim.yaml" created
    INFO Kubernetes file "4cat-logs-persistentvolumeclaim.yaml" created
    INFO Kubernetes file "db-deployment.yaml" created
    INFO Kubernetes file "4cat-db-persistentvolumeclaim.yaml" created
    INFO Kubernetes file "frontend-deployment.yaml" created
    ```

1. You should have few new files created:

    - "backend-service.yaml"
    - "frontend-service.yaml"
    - "backend-deployment.yaml"
    - "env-configmap.yaml"
    - "4cat-data-persistentvolumeclaim.yaml"
    - "4cat-config-persistentvolumeclaim.yaml"
    - "4cat-logs-persistentvolumeclaim.yaml"
    - "db-deployment.yaml"
    - "4cat-db-persistentvolumeclaim.yaml"
    - "frontend-deployment.yaml"

### Analysis

The tool has generated 4 kind of files: `service`, `deployment`,  `configmap` and `persistentvolumeclaim`. Let start with the simpler ones:

- `persistentvolumeclaim` files are the definitions of volumes. There is one file per `volume` definition in the docker compose file. Let's see an example and see the meaning of the relevant lines:

    ```yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      labels:
        io.kompose.service: 4cat-logs
      name: 4cat-logs
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 100Mi
    ```

    We can see that the `name` is the same (In `metadata > name`). The `accessMode` is set to `ReadWriteOnce`, which means that the volume can only be mounted once. Finaly the size is set to `100Mi` by default (In `spec > resources > request > storage`).

- The `configmap` file(s) store configuration. In our case the (relevant) variables defined in `.env` have been translated to `env-configmap.yaml`. The `name` is set to `env` and the variables are defined under `data`.

- The `service` files define "stable network identities". A service is created for each `deployment` and it exports every port that the deployment provides. For example in `frontend-service.yaml`:

    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      annotations:
        kompose.cmd: kompose convert
        kompose.version: 1.34.0 (cbf2835db)
      labels:
        io.kompose.service: frontend
      name: frontend
    spec:
      ports:
        - name: "5000"
          port: 5000
          targetPort: 5000
        - name: "443"
          port: 443
          targetPort: 443
      selector:
        io.kompose.service: frontend
    ```

    The two relevant parts are `selector` and `ports`. The first one links the service with the `deployment` the second lists the ports are a possible remap. Se more information about [Services](/cloud/rahti2/networking/#services).

- `deployment` is the most complex configuration generated. We can try to map the con figuration of `docker-compose.yaml` into these files. For example using the shortest one generated:

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      annotations:
        kompose.cmd: kompose convert
        kompose.version: 1.34.0 (cbf2835db)
      labels:
        io.kompose.service: db
      name: db
    spec:
      replicas: 1
      selector:
        matchLabels:
          io.kompose.service: db
      strategy:
        type: Recreate
      template:
        metadata:
          annotations:
            kompose.cmd: kompose convert
            kompose.version: 1.34.0 (cbf2835db)
          labels:
            io.kompose.service: db
        spec:
          containers:
            - env:
                - name: POSTGRES_DB
                - name: POSTGRES_HOST_AUTH_METHOD
                - name: POSTGRES_PASSWORD
                - name: POSTGRES_USER
              image: 'postgres:'
              livenessProbe:
                exec:
                  command:
                    - pg_isready -U ${POSTGRES_USER}
                failureThreshold: 5
                periodSeconds: 5
                timeoutSeconds: 5
              name: 4cat-db
              volumeMounts:
                - mountPath: /var/lib/postgresql/data
                  name: 4cat-db
          restartPolicy: Always
          volumes:
            - name: 4cat-db
              persistentVolumeClaim:
                claimName: 4cat-db
    ```

    - The `image` is defined at `spec > template > spec > containers > image`, and in this case is `postgres:`. This is a mistake as the tag `latest` is missing.
    - The `enviroment` is defined at `spec > template > spec > containers > env`, values are also missing.
    - The `volumes` are defined at `spec > template > spec > volumes` and `spec > template > spec > containers > volumeMounts`.
    - The `ports` are defined in `spec > template > spec > containers > ports` and in the already mentioned corresponding `service` files.
    - Finally the `command` is defined in `spec > template > spec > containers > command` (you can see the example in `backend-deployment.yaml`).

    As you can see the generated YAML files sare not perfect, but will be fine as a base for continuing the deployment.

## First deployment to Rahti

We will take the current unmodified YAML files and deploy them one by one. First you need to [install oc](/cloud/rahti2/usage/cli/#how-to-install-the-oc-tool) and [login into Rahti](/cloud/rahti2/usage/cli/#how-to-login-with-oc). Then you need to [create a Rahti project](/cloud/rahti2/usage/projects_and_quota/#creating-a-project). Make sure you are in the correct project: `oc project <project_name>`.

### Volumes, ConfigMaps and Services

1. We can start creating the `volumes` one by one:

   ```sh
   $ oc create -f 4cat-config-persistentvolumeclaim.yaml
   persistentvolumeclaim/4cat-config created

   $ oc create -f 4cat-data-persistentvolumeclaim.yaml
   persistentvolumeclaim/4cat-data created

   $ oc create -f 4cat-db-persistentvolumeclaim.yaml
   persistentvolumeclaim/4cat-db created

   $ oc create -f 4cat-logs-persistentvolumeclaim.yaml
   persistentvolumeclaim/4cat-logs created
   ```

    This will create 4 volumes in `Pending` status. They will remain in `Pending` till we deploy the `deployments`. This is expected.

1. We will also create the `configMap`:

    ```sh
    $ oc create -f env-configmap.yaml
    configmap/env created

    $ oc get cm
    NAME                       DATA   AGE
    env                        22     5s
    kube-root-ca.crt           1      5m45s
    openshift-service-ca.crt   1      5m45s
    ```

    The other two entries (`kube-root-cs.crt` and `openshift-service-ca.crt`) are pre-created Kubernetes and Openshift base config maps.

1. We do not expect any error while creating the `services` (db service is missing and we will need to create it ourselves manually later):

    ```sh
    $ oc create -f frontend-service.yaml
    service/frontend created

    $ oc create -f backend-service.yaml
    service/backend created

    $ oc get service
    NAME       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)            AGE
    backend    ClusterIP   172.30.109.120   <none>        4444/TCP           21h
    frontend   ClusterIP   172.30.139.56    <none>        5000/TCP,443/TCP   21h
    ```

    The result is the expected for the backend, the mapping was `4444:4444`. But not for the frontend, which was `80:5000`. This is not a big deal, as in order to access the service from outside Rahti, we will use a `Route`, and the `Route` allows us to translate and expose any port to the standard 80/443 ports. We will leave it as it is.

### DB Deployments

Finally we will create the deployments. We have 3 deployments and we will start with the DB deployment.

1. Let's create what we currently have:

    ```sh
    $ oc create -f db-deployment.yaml
    deployment.apps/db created

    $ oc get pods
    NAME                  READY   STATUS             RESTARTS   AGE
    db-66db46fb89-vzqrz   0/1     InvalidImageName   0          26s
    ```

1. This is expected as the tag `latest` was missing in the image name. Let's fix it and try again. So we will edit the file `db-deployment.yaml`, add latest to the image filed so it looks like: `postgres:latest`,

    ```diff
    @@ -33,5 +33,5 @@
                 - name: POSTGRES_USER
    -          image: 'postgres:'
    +          image: 'postgres:latest'
               livenessProbe:
                 exec:
    ```

    and recreate/replace the deployment:

    ```sh
    $ oc replace -f db-deployment.yaml
    deployment.apps/db replaced

    $ oc get pods
    NAME                  READY   STATUS              RESTARTS   AGE
    db-76fcbdc9d8-dgmqr   0/1     CrashLoopBackOff    1 (1s ago)   24s
    ```

    !!! Info "YAML files"
        We are making the modifications into the `YAML` file so we can re-create the deployment afterwards. You can also add the files to a Git repository and commit every change so later the history and reasons of modifications is clear.

1. The deployment is not working, but for a different reason. Let's see why:

    ```sh
    $ oc logs db-76fcbdc9d8-dgmqr
    chmod: changing permissions of '/var/lib/postgresql/data': Operation not permitted
    chmod: changing permissions of '/var/run/postgresql': Operation not permitted
    Error: Database is uninitialized and superuser password is not specified.
           You must specify POSTGRES_PASSWORD to a non-empty value for the
           superuser. For example, "-e POSTGRES_PASSWORD=password" on "docker run".

           You may also use "POSTGRES_HOST_AUTH_METHOD=trust" to allow all
           connections without a password. This is *not* recommended.

           See PostgreSQL documentation about "trust":
           https://www.postgresql.org/docs/current/auth-trust.html
    ```

    This shows two kind of errors folder permission errors and missing variables errors. Let's to reproduce the error localy on our machine. The command will be:

    ```sh
    docker run -it --rm -u 1000 postgres:latest
    chmod: changing permissions of '/var/lib/postgresql/data': Operation not permitted
    chmod: changing permissions of '/var/run/postgresql': Operation not permitted
    Error: Database is uninitialized and superuser password is not specified.
           You must specify POSTGRES_PASSWORD to a non-empty value for the
           superuser. For example, "-e POSTGRES_PASSWORD=password" on "docker run".

           You may also use "POSTGRES_HOST_AUTH_METHOD=trust" to allow all
           connections without a password. This is *not* recommended.

           See PostgreSQL documentation about "trust":
           https://www.postgresql.org/docs/current/auth-trust.html
    ```

    We added `-u 1000` to change the UID to a non root UID, so we can reproduce the same error Rahti is showing us. Any random UID can be used, this is the way Rahti runs imnages. with random UIDs. Let's repeat it with the `POSTGRES_HOST_AUTH_METHOD` variable defined as suggested:

    ```sh
    $ podman run -it --rm -u 1000 -e  POSTGRES_PASSWORD=password postgres:latest
    WARN[0000] Error validating CNI config file /home/galvaro/.config/cni/net.d/4cat_default.conflist: [plugin firewall does not support config version "1.0.0"] 
    chmod: changing permissions of '/var/lib/postgresql/data': Operation not permitted
    chmod: changing permissions of '/var/run/postgresql': Operation not permitted
    The files belonging to this database system will be owned by user "1000".
    This user must also own the server process.

    The database cluster will be initialized with locale "en_US.utf8".
    The default database encoding has accordingly been set to "UTF8".
    The default text search configuration will be set to "english".

    Data page checksums are disabled.

    fixing permissions on existing directory /var/lib/postgresql/data ... initdb: error: could not change permissions of directory "/var/lib/postgresql/data": Operation not permitted
    ```

    In this case we can see that this container image will never work in Rahti, as it needs to be able to change folder permissions. Luckily Rahti/Openshift provides a PostgreSQL template that is available in the developer catalog.

    ![Developer Catalog](/cloud/img/db-developer-catalog.png)

    In the description of the template we can see a link to a Github page <https://github.com/sclorg/postgresql-container/>. On the page we can see the list of all the available images. We will choose [quay.io/sclorg/postgresql-15-c9s](https://quay.io/repository/sclorg/postgresql-15-c9s) as it is the newest available version and uses Centos 9 as a base.

1. After replacing the image (`postgres:latest` to `quay.io/sclorg/postgresql-15-c9s:latest`) the logs are:

    ```sh
    $ oc logs db-747df6885c-sh289
    For general container run, you must either specify the following environment
    variables:
      POSTGRESQL_USER  POSTGRESQL_PASSWORD  POSTGRESQL_DATABASE
    Or the following environment variable:
      POSTGRESQL_ADMIN_PASSWORD
    Or both.

    To migrate data from different PostgreSQL container:
      POSTGRESQL_MIGRATION_REMOTE_HOST (hostname or IP address)
      POSTGRESQL_MIGRATION_ADMIN_PASSWORD (password of remote 'postgres' user)
    And optionally:
      POSTGRESQL_MIGRATION_IGNORE_ERRORS=yes (default is 'no')

    Optional settings:
      POSTGRESQL_MAX_CONNECTIONS (default: 100)
      POSTGRESQL_MAX_PREPARED_TRANSACTIONS (default: 0)
      POSTGRESQL_SHARED_BUFFERS (default: 32MB)

    For more information see /usr/share/container-scripts/postgresql/README.md
    within the container or visit https://github.com/sclorg/postgresql-container.
    ```

    The variable names are different, but easy to translate. We will also take the values from the `env` `configMap`:

    ```diff
        @@ -25,13 +25,11 @@
           containers:
             - env:
    -            - name: POSTGRES_DB
    -            - name: POSTGRES_HOST_AUTH_METHOD
    -            - name: POSTGRES_PASSWORD
    -            - name: POSTGRES_USER
    -          image: 'postgres:'
    +          - name: POSTGRESQL_DATABASE
    +            valueFrom:
    +              configMapKeyRef:
    +                key: POSTGRES_DATABASE
    +                name: env
    +          - name: POSTGRESQL_PASSWORD
    +            valueFrom:
    +              configMapKeyRef:
    +                key: POSTGRES_PASSWORD
    +                name: env
    +          - name: POSTGRESQL_USER
    +            valueFrom:
    +              configMapKeyRef:
    +                key: POSTGRES_USER
    +                name: env
    +          image: 'quay.io/sclorg/postgresql-15-c9s'
               livenessProbe:
                 exec:
    ```

    This last change made the trick and the Pod now it running as expected:

    ```sh
    $ oc get pods
    NAME                  READY   STATUS    RESTARTS   AGE
    db-58947cf497-p4vnq   1/1     Running   0          66s
    ```

### Backend deployment

This deployment also needs few changes. Let's go through them in more agile way:

1. Fix the image name. The error:

    ```sh
    $ oc get pods
    NAME                       READY   STATUS             RESTARTS   AGE
    backend-7f47d4c5d4-zrxjp   0/1     InvalidImageName   0          41s
    ```

    The solution:

    ```diff
    @@ -137,5 +137,5 @@
                       key: workers
                       name: env
    -          image: 'digitalmethodsinitiative/4cat:'
    +          image: 'digitalmethodsinitiative/4cat:stable'
               name: 4cat-backend
               ports:
    ```

1. Then we get this other error:

    ```sh
    db: forward host lookup failed: Unknown host
    ```

    This requires us to create the db service:

    ```sh
    $ oc expose deploy/db --port 5432
    service/db exposed
    ```

1. The next error is about password authentication:

    ```
    Password for user fourcat:
    psql: error: connection to server at "db" (172.30.154.239), port 5432 failed: fe_sendauth: no password supplied`
    ```

    This is due to the fact that meanwhile we are defining `POSTGRESQL_PASSWORD` the application is expcting `PGPASSWPRD`. This mean that the fix is:

    ```diff
    @@ -72,5 +72,5 @@
                       key: POSTGRES_HOST_AUTH_METHOD
                       name: env
    -            - name: POSTGRES_PASSWORD
    +            - name: PGPASSWORD
                   valueFrom:
                     configMapKeyRef:
    ```

1. The output of the backend Pod is now much longer but it ends with this error:

    ```py
    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "helper-scripts/migrate.py", line 336, in <module>
        finish(args, logger, no_pip=pip_ran)
      File "helper-scripts/migrate.py", line 122, in finish
        check_for_nltk()
      File "helper-scripts/migrate.py", line 74, in check_for_nltk
        nltk.download('punkt_tab', quiet=True)
      File "/usr/local/lib/python3.8/site-packages/nltk/downloader.py", line 774, in download
        for msg in self.incr_download(info_or_id, download_dir, force):
      File "/usr/local/lib/python3.8/site-packages/nltk/downloader.py", line 642, in incr_download
        yield from self._download_package(info, download_dir, force)
      File "/usr/local/lib/python3.8/site-packages/nltk/downloader.py", line 698, in _download_package
        os.makedirs(download_dir, exist_ok=True)
      File "/usr/local/lib/python3.8/os.py", line 223, in makedirs
        mkdir(name, mode)
    PermissionError: [Errno 13] Permission denied: '/nltk_data'
    ```

    We need to create an emptyDir for that folder.
