FROM node:lts-alpine
WORKDIR /appcode

COPY package.json package-lock.json ./
RUN npm install

COPY . .
EXPOSE 3000
CMD ["npm", "run", "dev"]
