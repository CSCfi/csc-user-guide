ARG builder_image
FROM ${builder_image} AS builder

ARG config_file=mkdocs.yml
ARG site_url
ARG lang

ENV SITE_URL="${site_url}${lang:+/}${lang}${lang:+/}"

COPY "${config_file}" ./

RUN mkdocs build --site-dir=/tmp/site \
                 --config-file="${config_file}"


FROM registry.access.redhat.com/ubi8/nginx-124

LABEL maintainer="CSC Service Desk <servicedesk@csc.fi>"

ADD nginx.conf "${NGINX_CONF_PATH}"

COPY --from=builder /tmp/site /usr/share/nginx/html

EXPOSE 8000/tcp

CMD nginx
