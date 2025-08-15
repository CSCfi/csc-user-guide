FROM image-registry.apps.2.rahti.csc.fi/docs-csc-development/docs-csc-builder AS builder

ARG repo_org=CSCfi
ARG repo_name=csc-user-guide
ARG repo_branch=master
ARG config_file=mkdocs.yml

ADD .git-revision-date-ignore-revs "${config_file}" .

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
  mkdocs build --site-dir=/tmp/site \
               --config-file="${config_file}"


FROM registry.access.redhat.com/ubi8/nginx-124

LABEL maintainer="CSC Service Desk <servicedesk@csc.fi>"

COPY --from=builder /tmp/site "${NGINX_APP_ROOT}/src"
ADD nginx.conf "${NGINX_CONF_PATH}"

EXPOSE 8000/tcp

CMD nginx
