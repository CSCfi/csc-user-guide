ARG builder_image
FROM ${builder_image} AS builder

ARG repo_org=CSCfi
ARG repo_name=csc-user-guide
ARG repo_branch=master

ADD .git-revision-date-ignore-revs mkdocs.yml .

RUN \
  git clone --no-checkout \
            --single-branch \
            --branch=${repo_branch} \
    https://github.com/${repo_org}/${repo_name} \
    /tmp/src \
&& \
  git -C /tmp/src sparse-checkout init --no-cone \
&& \
  git -C /tmp/src sparse-checkout set docs \
&& \
  git -C /tmp/src checkout \
&& \
  mv /tmp/src/{.git,docs} ./ \
&& \
  for feat in new glossary; do \
    bash scripts/generate_${feat}.sh; \
  done \
&& \
  mkdocs build --site-dir=/tmp/site


FROM registry.access.redhat.com/ubi8/nginx-124

LABEL maintainer="CSC Service Desk <servicedesk@csc.fi>"

COPY --from=builder /tmp/site "${NGINX_APP_ROOT}/src"
ADD nginx.conf "${NGINX_CONF_PATH}"

EXPOSE 8000/tcp

CMD nginx
