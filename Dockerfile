FROM centos:7

LABEL maintainer="CSC Service Desk <servicedesk@csc.fi>"

# These need to be owned and writable by the root group in OpenShift
ENV ROOT_GROUP_DIRS='/var/run /var/log/nginx /var/lib/nginx'

RUN yum -y install epel-release &&\
    yum -y install nginx python-pip python git-lfs &&\
    yum clean all

RUN git lfs install &&\
    git lfs pull

RUN chgrp -R root ${ROOT_GROUP_DIRS} &&\
    chmod -R g+rwx ${ROOT_GROUP_DIRS}

COPY . /tmp

WORKDIR /tmp

RUN pip install --no-cache-dir -r requirements.txt && \
    mkdocs build -d /usr/share/nginx/html

COPY nginx.conf /etc/nginx

EXPOSE 8000

CMD [ "/usr/sbin/nginx" ]
