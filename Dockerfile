FROM node:10-alpine
ADD . ./app
WORKDIR /app

RUN apk add --no-cache curl
RUN apk add --no-cache wget
RUN apk add --no-cache bash

RUN chmod +x .scripts/install.sh
RUN chmod +x .scripts/build.sh
RUN chmod +x .scripts/deploy.sh

RUN .scripts/install.sh
RUN .scripts/build.sh

RUN export PR_NUMBER=$(echo ${REF} | cut -d'/' -f3)

RUN .scripts/deploy.sh
