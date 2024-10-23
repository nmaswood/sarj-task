# client/Dockerfile
FROM node:20.15.0-slim

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy the rest of the application
COPY . .

# Build Next.js application for production
RUN npm run build

EXPOSE 3000

CMD ["npm", "run", "start"]
