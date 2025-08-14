FROM registry.access.redhat.com/ubi8/python-311:latest

LABEL maintainer="CSC Service Desk <servicedesk@csc.fi>"

WORKDIR /tmp

COPY requirements.txt ./

RUN \
  pip install --upgrade pip \
&& \
  pip install --requirement=requirements.txt

ARG repo_org=CSCfi
ARG repo_name=csc-user-guide
ARG repo_branch=master

RUN \
  git config --global --add safe.directory /tmp/src \
&& \
  git clone --no-checkout \
            --single-branch \
            --branch=${repo_branch} \
        https://github.com/${repo_org}/${repo_name} src \
&& \
  git -C src sparse-checkout init --no-cone \
&& \
  git -C src sparse-checkout set docs \
&& \
  git -C src checkout

WORKDIR /tmp/src

COPY mkdocs.yml .git-revision-date-ignore-revs ./
COPY scripts/ ./scripts/
COPY hooks/ ./hooks/
COPY csc-overrides/ ./csc-overrides/

RUN \
  for feat in new glossary; do \
    bash scripts/generate_${feat}.sh; \
  done
