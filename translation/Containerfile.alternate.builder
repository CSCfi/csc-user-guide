ARG base_image=docs-csc/docs-csc-base:latest
FROM ${base_image} as base

LABEL maintainer="CSC Service Desk <servicedesk@csc.fi>"

ADD requirements.txt ./

ARG PIP_ROOT_USER_ACTION=ignore
RUN \
  pip3 install --upgrade pip \
&& \
  pip3 install --use-pep517 --requirement requirements.txt

ADD --chown=0:0 \
    --chmod=744 \
  translation/entrypoint.alternate.builder.bash /entrypoint.bash

ENTRYPOINT ["/entrypoint.bash"]
