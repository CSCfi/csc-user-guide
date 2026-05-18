ARG base_image
FROM ${base_image}

LABEL maintainer="CSC Service Desk <servicedesk@csc.fi>"

ADD requirements.txt .

ARG PIP_ROOT_USER_ACTION=ignore
RUN \
  pip3 install --upgrade pip \
&& \
  pip3 install --requirement=requirements.txt
