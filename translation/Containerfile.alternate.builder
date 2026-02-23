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
    --chmod=774 \
  translation/entrypoint.alternate.builder.bash /entrypoint.bash

ARG repo_org=CSCfi
ARG repo_name=csc-user-guide
ARG repo_branch=master
ENV REPO_ORG=${repo_org} \
    REPO_NAME=${repo_name} \
    REPO_BRANCH=${repo_branch} \
    DOCS_DIR=docs

ENTRYPOINT ["/entrypoint.bash"]
