FROM rockylinux:8 

LABEL maintainer="CSC Service Desk <servicedesk@csc.fi>"

# These need to be owned and writable by the root group in OpenShift
ENV ROOT_GROUP_DIRS='/var/run /var/log/nginx /var/lib/nginx'

ARG repo_branch=master

RUN yum -y install epel-release &&\
    yum -y install nginx &&\
    yum -y install python38 &&\
    yum -y install git &&\
    yum -y install findutils &&\
    yum clean all


COPY requirements.txt /requirements.txt
RUN chgrp -R root ${ROOT_GROUP_DIRS} && \
    chmod -R g+rwx ${ROOT_GROUP_DIRS} && \
    pip3 install --no-cache-dir -r /requirements.txt

COPY nginx.conf /etc/nginx
EXPOSE 8000
CMD [ "/usr/sbin/nginx" ]

COPY . /tmp
WORKDIR /tmp

RUN bash scripts/generate_alpha.sh && \
    bash scripts/generate_by_system.sh && \
    bash scripts/generate_new.sh && \
    bash scripts/generate_glossary.sh && \
    mkdocs build -d /usr/share/nginx/html

