# Step Calories Calculator

## Overview
The Step Calories Calculator is a web application that helps users estimate the number of steps needed to burn a specific amount of calories. It takes into account the user's weight and walking pace to provide a personalized calculation.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Docker Deployment](#docker-deployment)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- Calculate steps based on calories, weight, and pace
- Responsive web interface
- Dockerized for easy deployment
- Unit tests for core functionality

## Technologies Used
- Python 3.9+
- Flask 3.1.0
- Docker
- pytest 8.3.4

## Prerequisites
- Python 3.9+
- Docker and Docker Compose (for containerized deployment)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/step-calories-calculator.git
   cd step-calories-calculator
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```
   cp .env.example .env
   ```
   Edit the `.env` file and set the appropriate values for your environment.

## Usage

To run the application locally:

```
python -m src.app
```

The application will be available at `http://localhost:5001`.

## Docker Deployment

To run the application using Docker:

1. Build and start the container:
   ```
   docker-compose up --build
   ```

2. The application will be available at `http://localhost:5001`.

To stop the container:

```
docker-compose down
```

## Running Tests

To run the unit tests:

```
python -m pytest tests/
```

## Project Structure
```
project_root/
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── main.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── calculator.py
│   └── utils/
│       ├── __init__.py
│       └── validators.py
├── tests/
│   └── test_calculator.py
├── static/
│   └── styles.css
├── templates/
│   ├── 404.html
│   ├── 500.html
│   └── index.html
├── .dockerignore
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── README.md
└── requirements.txt
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
