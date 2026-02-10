ARG base_image=docs-csc-base:latest
FROM ${base_image} as base

LABEL maintainer="CSC Service Desk <servicedesk@csc.fi>"

RUN \
  dnf --refresh --assumeyes install \
                              python3.11 \
                              python3.11-pip \
                              git

USER 1001

ADD requirements.txt ./

RUN pip3 install --use-pep517 --requirement requirements.txt

ADD --chown=0:0 \
    --chmod=754 \
  translation/entrypoint.alternate.builder.bash /entrypoint.bash

ENTRYPOINT ["/entrypoint.bash"]
