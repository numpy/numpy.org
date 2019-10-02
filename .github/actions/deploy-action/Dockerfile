FROM node:10-alpine
ADD ../.. ./app
WORKDIR /app

RUN apk add --no-cache curl
RUN apk add --no-cache wget
RUN apk add --no-cache bash

RUN chmod +x .scripts/install.sh
RUN chmod +x .scripts/build.sh
RUN chmod +x .scripts/deploy.sh

RUN .github/actions/.scripts/install.sh
RUN .github/actions/.scripts/build.sh

ENTRYPOINT .github/actions/.scripts/deploy.sh; /bin/bash
