FROM node:20.17-alpine AS builder

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

FROM node:20.17-alpine

WORKDIR /app

COPY --from=builder /app/.output /app/.output

CMD ["node", ".output/server/index.mjs"]
