FROM node:16
MAINTAINER cosmos
WORKDIR /usr/src/app
COPY ./app.js /usr/src/app/app.js

COPY ./package.json /usr/src/app/package.json
RUN npm config set strict-ssl false
RUN npm install

ENTRYPOINT [ "node", "app.js" ]
EXPOSE 8000