ARG builder_image
FROM ${builder_image} as builder

LABEL maintainer="CSC Service Desk <servicedesk@csc.fi>"

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
