# Use an official Node.js runtime as a parent image
FROM node:20-alpine

# Define build argument for VITE_API_BASE_URL
ARG VITE_API_BASE_URL

# Set the working directory in the container
WORKDIR /app/frontend

# Copy package.json and package-lock.json to the working directory
COPY frontend/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY frontend/ .

# Build the Vue application, passing VITE_API_BASE_URL as an environment variable
RUN VITE_API_BASE_URL=$VITE_API_BASE_URL npm run build

# Serve the built application with a simple HTTP server
FROM nginx:alpine
COPY --from=0 /app/frontend/dist /usr/share/nginx/html
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]