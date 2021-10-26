FROM node
COPY package.json .
RUN npm install
COPY app.js .
COPY index.html .
EXPOSE 8001
CMD [ "npm", "start", "--port", "8001" ]