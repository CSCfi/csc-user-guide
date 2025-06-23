FROM rockylinux:8 

LABEL maintainer="CSC Service Desk <servicedesk@csc.fi>"

# These need to be owned and writable by the root group in OpenShift
ENV ROOT_GROUP_DIRS='/var/run /var/log/nginx /var/lib/nginx'

ARG repo_org=CSCfi
ARG repo_name=csc-user-guide
ARG repo_branch=master

COPY requirements.txt /tmp

WORKDIR /tmp

RUN dnf -y install epel-release \
                   nginx \
                   python3.11 \
                   python3.11-pip \
                   git \
                   findutils &&\
    dnf clean all &&\
    pip3 install --use-pep517 --no-cache-dir -r requirements.txt

RUN chgrp -R root ${ROOT_GROUP_DIRS} &&\
    chmod -R g+rwx ${ROOT_GROUP_DIRS}

COPY . /tmp

RUN if [ ! -d ".git" ]; then \
    git clone --bare --single-branch --branch=$repo_branch https://github.com/$repo_org/$repo_name .git && \
    git init && \
    git switch --force $repo_branch; \
    fi && \
    bash scripts/generate_new.sh && \
    bash scripts/generate_glossary.sh && \
    mkdocs build -d /usr/share/nginx/html

COPY nginx.conf /etc/nginx

EXPOSE 8000

CMD [ "/usr/sbin/nginx" ]
