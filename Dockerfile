FROM centos:7

LABEL maintainer="CSC Rahti Team <rahti-team@postit.csc.fi>"

ARG SYSTEM_NAME
ARG OSO_WEB_UI_URL
ARG OSO_REGISTRY_URL
ARG LDAP_LOGIN_SUPPORT
ARG GITLAB_LOGIN_SUPPORT
ARG SUI_INTEGRATION_DONE
ARG OPENSHIFT_VERSION

ENV SYSTEM_NAME=${SYSTEM_NAME}
ENV OSO_WEB_UI_URL=${OSO_WEB_UI_URL}
ENV OSO_REGISTRY_URL=${OSO_REGISTRY_URL}
ENV LDAP_LOGIN_SUPPORT=${LDAP_LOGIN_SUPPORT}
ENV GITLAB_LOGIN_SUPPORT=${GITLAB_LOGIN_SUPPORT}
ENV SUI_INTEGRATION_DONE=${SUI_INTEGRATION_DONE}
ENV OPENSHIFT_VERSION=${OPENSHIFT_VERSION}

# These need to be owned and writable by the root group in OpenShift
ENV ROOT_GROUP_DIRS='/var/run /var/log/nginx /var/lib/nginx'

RUN yum -y install epel-release &&\
    yum -y install nginx python-pip python &&\
    yum clean all &&\
    chmod g+rwx /var/run /var/log/nginx &&\
    sed -i -e "/listen\(.*\)\[/d" \
           -e "s/listen\(.*\)80 default_server;/listen 8000 default_server;/" \
           -e "s/^error_log \/var\/log\/nginx\/error.log;/error_log stderr;/" \
           -e "/worker_processes/a daemon off;" \
           -e "s/^user/#user/" /etc/nginx/nginx.conf

RUN chgrp -R root ${ROOT_GROUP_DIRS} &&\
    chmod -R g+rwx ${ROOT_GROUP_DIRS}

COPY . /tmp

WORKDIR /tmp

RUN pip install --no-cache-dir -r requirements.txt && \
    sh -c /tmp/make_config.sh && \
    mkdocs build -d /usr/share/nginx/html

EXPOSE 8000

CMD [ "/usr/sbin/nginx" ]
