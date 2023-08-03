# Use an official Node runtime as a parent image
FROM node:14-alpine

# Set the working directory to /app
WORKDIR /shop_frontend

# Copy package.json and package-lock.json to the container
COPY /shop_frontend/package*.json ./
# Install dependencies
RUN npm install --production

# Copy the rest of the application code to the container
COPY shop_frontend/public/index.html shop_frontend/public/index.html

COPY . /shop_frontend

# Build the production version of the application
RUN npm run build

# Expose port 80 to the outside world (assuming your application listens on port 80)
EXPOSE 80

# Run the command to start the server
CMD ["npm", "start"]
