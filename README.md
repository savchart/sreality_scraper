# Sreality Property Scraper and Viewer

This project includes a web scraper that extracts property listings from sreality.cz and stores them in a PostgreSQL database. Additionally, it includes a simple HTTP server that displays the scraped property listings in a web page.

## Table of Contents:
1. Project Structure
2. Installation
3. Usage
4. Configuration

## Project Structure
```
project-root/
│
├── sreality/               # Scraper directory
│   ├── spiders/            # Directory for spiders
│   ├── Dockerfile          # Dockerfile for the scraper
│   ├── requirements.txt    # Python dependencies
│   └── ...
│
├── server/                 # Server directory
│   ├── Dockerfile          # Dockerfile for the server
│   ├── requirements.txt    # Python dependencies
│   └── server.py           # Python script for HTTP server
│
├── db/
│   ├── init.sql            # SQL script to initialize the database
│
├── docker-compose.yml      # Docker Compose file
├── .env                    # Environment variables
└── README.md               # This file
```

## Installation
Before you start, make sure you have Docker and Docker Compose installed on your machine.

1. Clone this repository:
```git clone https://github.com/savchart/sreality_scraper```
2. Navigate to the project directory:
```cd sreality_scraper```
3. Build and run the Docker containers:
```docker-compose up --build```

This will start three containers: PostgreSQL database, scraper, and server.

## Usage
Access the server by opening your web browser and navigating to http://localhost:8080.

To stop the services, press Ctrl+C in the terminal and then run:
```docker-compose down```

## Configuration
Configure the project by setting environment variables in the .env file. Example:

POSTGRES_HOST=localhost
POSTGRES_DB=mydatabase
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
