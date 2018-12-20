FROM centos:7

LABEL maintainer="CSC Service Desk <servicedesk@csc.fi>"

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
    mkdocs build -d /usr/share/nginx/html

EXPOSE 8000

CMD [ "/usr/sbin/nginx" ]
