ARG python_image=ubi8/python-311
FROM ${python_image}

LABEL maintainer="CSC Service Desk <servicedesk@csc.fi>"

USER 0
ADD requirements.txt mkdocs.yml .
ADD csc-overrides ./csc-overrides
ADD hooks ./hooks
ADD scripts ./scripts
RUN \
  mkdir /tmp/src \
&& \
  chown -R 1001:0 /tmp/src ./
USER 1001

RUN \
  pip install --upgrade pip \
&& \
  pip install --requirement=requirements.txt
