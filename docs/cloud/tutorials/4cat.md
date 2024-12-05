# How to deploy 4cat in Rahti

This tutorial is a long format one, it explains all the different steps that were necessary to deploy the [4cat](https://github.com/digitalmethodsinitiative/4cat) application into Rahti. The idea is to explain the story of how the different issues were found and solved. Each issue will have its own chapter and hopefully thge solution will be easy to apply to any other application with similar issues.

4Cat is a capture and analysis toolkit. From the Github page linked above, we learnt that the tool is used for analysing social media platforms and that one of the installation methods is docker compose. This is good news because:

1. We can test the application deployment using docker compose and see how it looks.
1. We do not need to create a docker container from scratch.
1. We can use the docker compose deployment as a base and adapt it to Kubernetes deployment using [kompose](https://kompose.io). This tool is specifically designed to make this conversions. From their website: "Our conversions are not always 1:1 from Docker Compose to Kubernetes, but we will help get you 99% of the way there!". And it indeed will save us a lot of tedious conversion time, but it will not be the end of it.

## Docker compose

!!! warning "Linux is used for all the examples"
    We have prepared this tutrial using a Linux machine. In principle, all these commands run also in Windoes and Mac, but if confused I recommend to [install a tiny VM in Pouta](https://docs.csc.fi/cloud/pouta/launch-vm-from-web-gui/) and use it for the tutorial instead. This is an advantage if you use Linux, as you you won't need to install anything in your local machine.

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
      - ${PUBLIC_PORT}:5000
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

!!! Info "Install docker compose"
    Before continuing, we need have docker and the docker compose plugin installed. You can find instructions on how to install docker compose here:

    - [https://docs.docker.com/compose/install/](/cloud/pouta/launch-vm-from-web-gui.md)

    For Debian and Ubuntu you can install it by:

    ```sh
    sudo apt-get update
    sudo apt-get install docker-compose
    ```

    You can use podman compose or similar, but we use docker as it is the most common tool.

Before anything else, let's deploy the docker compose and see how the application works:

```sh
sudo docker compose up
```

This will start the process for deploying the application in our (local) machine. It can take some time to pull the images and configure the application. If you `Ctrl+C` the application will exit. If you want to run it on the background, you just need to add `-d` or  `--detach`.

After a while the application will be available on port `80`:

![4cat first run](/cloud/img/4cat.png)

### Analysis

As you can see this `docker-compose.yml` file is a [YAML](https://en.wikipedia.org/wiki/YAML) file with two main sections: `services` and `volumes`. There are 3 `services` and 4 `volumes`. The most important fields of a service are:

- `image`,
- `environment`,
- `volumes`,
- `ports`,
- `entrypoint` and `command`,

The volumes section is simpler and only contains a list of names. A "docker compose volume" is a normal docker volume and does not include a size, because it will be using the local disk, and the size will be the limit of the disk. In Kubernetes volumes do have a size and we will need to account for that.
