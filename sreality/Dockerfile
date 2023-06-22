# Use the official Python image as base lightweight image
FROM python:3.9-slim

# Set the working directory
WORKDIR /scraper

# Copy the current directory contents into the container at /app
COPY . /scraper

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run the Scrapy spider
CMD ["scrapy", "crawl", "sreality_spider"]