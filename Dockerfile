FROM python:3.8.10-alpine3.12

# Create app directory
WORKDIR /app

# Install app dependencies
# COPY package*.json .
COPY . .
RUN pip install -r requirements.txt

# Copy app source
COPY . .

# Expose port
EXPOSE 80

# Run application
CMD ["python3", "/app/app.py"]
