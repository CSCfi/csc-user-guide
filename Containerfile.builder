ARG base_image
FROM ${base_image}

LABEL maintainer="CSC Service Desk <servicedesk@csc.fi>"

ADD requirements.txt ./

ARG PIP_ROOT_USER_ACTION=ignore
RUN \
  pip3.12 install --upgrade pip \
&& \
  pip3.12 install \
            --use-pep517 \
            --no-cache-dir \
            --no-deps \
            --requirement=requirements.txt
