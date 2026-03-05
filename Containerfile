ARG builder_image=docs-csc/docs-csc-builder:latest
ARG server_image=ubi8/nginx-124
FROM ${builder_image} AS builder

ARG repo_org=CSCfi
ARG repo_name=csc-user-guide
ARG repo_branch=master
ENV REPO_ORG=${repo_org} \
    REPO_NAME=${repo_name} \
    REPO_BRANCH=${repo_branch} \
    CLONE_PATH=/tmp/${repo_name}

RUN \
  /sparse-clone.bash '!/*/' \
&& \
  mv "${CLONE_PATH}/.git" ./ \
&& \
  rmdir "$CLONE_PATH"

ADD csc-overrides/ csc-overrides/
ADD docs/ docs/
ADD hooks/ hooks/
ADD .git-revision-date-ignore-revs \
    mkdocs.yml \
    ./

RUN mkdocs build --site-dir=/tmp/site/


FROM ${server_image}

LABEL maintainer="CSC Service Desk <servicedesk@csc.fi>"

COPY --from=builder /tmp/site/ "${NGINX_APP_ROOT}/src/"
ADD nginx.conf "${NGINX_CONF_PATH}"

EXPOSE 8000/tcp

CMD nginx
