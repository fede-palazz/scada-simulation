# Base image
FROM node:16

# Set working directory inside the container
WORKDIR /app

# Copy the package.json file inside the container
COPY package.json .

# Install the dependecies (express, ecc...)
RUN npm install

# Copy all the project files within the container
COPY . ./

# Run the entrypoint
CMD ["node", "index.js"]