FROM node:16
WORKDIR /usr/src/app
COPY ./server.js /usr/src/app/server.js

COPY ./package.json /usr/src/app/package.json
RUN npm install

ENTRYPOINT [ "node", "server.js" ]
EXPOSE 3000