ARG builder_image
FROM ${builder_image}

LABEL maintainer="CSC Service Desk <servicedesk@csc.fi>"

ADD requirements.txt ./

RUN \
  pip install --upgrade pip \
&& \
  pip install \
        --use-pep517 \
        --no-cache-dir \
        --no-deps \
        --requirement=requirements.txt

ADD --chown=0:0 \
    --chmod=774 \
  scripts/sparse-clone.bash /sparse-clone.bash
