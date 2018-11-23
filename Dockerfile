FROM python:3.6-alpine

MAINTAINER CSC Rahti Team <rahti-team@postit.csc.fi>

WORKDIR /usr/src/docs

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN chgrp -R 0 /usr/src/docs && \
    chmod -R g=u /usr/src/docs

EXPOSE 8000

ENTRYPOINT ["sh", "-c", "./make_config.sh && mkdocs serve -a 0.0.0.0:8000"]
