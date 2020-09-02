FROM centos:8

LABEL maintainer="CSC Service Desk <servicedesk@csc.fi>"

# These need to be owned and writable by the root group in OpenShift
ENV ROOT_GROUP_DIRS='/var/run /var/log/nginx /var/lib/nginx'

ARG repo_branch=master

RUN yum -y install epel-release &&\
    yum -y install nginx &&\
    yum -y install python3 &&\
    yum -y install python3-pip &&\
    yum -y install git &&\
    yum clean all

RUN chgrp -R root ${ROOT_GROUP_DIRS} &&\
    chmod -R g+rwx ${ROOT_GROUP_DIRS}

COPY . /tmp

WORKDIR /tmp


RUN git clone --no-checkout https://github.com/CSCfi/csc-user-guide git_folder && \
    mv git_folder/.git . && \
    rm -r git_folder && \
    git reset HEAD --hard && \
    git checkout $repo_branch 

RUN pip3 install --no-cache-dir -r requirements.txt && \
    bash scripts/generate_stamps.sh && \
    bash scripts/generate_alpha.sh && \
    bash scripts/generate_by_system.sh && \
    mkdocs build -d /usr/share/nginx/html

COPY nginx.conf /etc/nginx

EXPOSE 8000

CMD [ "/usr/sbin/nginx" ]
