# Use an official Node.js runtime as a parent image, with a version compatible with Next.js
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to leverage Docker cache layers
COPY package*.json ./

# Install any needed packages specified in package.json
RUN npm install

# Bundle the app source inside the Docker image
COPY . .

# Build the application for development (if necessary, some projects may not require a build step in development)
RUN npm run build

# Expose the port the app runs on
EXPOSE 3000

# Define environment variable for development
ENV NODE_ENV development

# Run the app when the container launches using the development command
CMD ["npm", "run", "dev"]
