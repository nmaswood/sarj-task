# client/Dockerfile
FROM node:20-alpine

WORKDIR /app

# Copy package files
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application
COPY . .

# Build Next.js application for production
RUN npm run build --clear-cache

CMD ["npm", "run", "start"]
