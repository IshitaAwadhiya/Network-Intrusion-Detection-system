# Use Node.js image
FROM node:18

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN npm install

# Build React app
RUN npm run build

# Serve using serve
RUN npm install -g serve
CMD ["serve", "-s", "build", "-l", "3000"]

