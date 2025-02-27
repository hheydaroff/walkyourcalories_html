# Codebase Summary

## Key Components
- src/app.py: Main application file (contains Flask application setup)
- src/config.py: Configuration file for the application
- src/routes/main.py: Contains route handlers for the web application
- src/services/calculator.py: Contains the step calculation logic
- src/utils/validators.py: Contains input validation functions
- static/styles.css: CSS file for styling the web application
- templates/: Directory containing HTML templates
  - 404.html: Custom 404 error page
  - 500.html: Custom 500 error page
  - index.html: Main page of the web application
- tests/test_calculator.py: Unit tests for the calculator service

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

## Data Flow
1. User sends request to the Flask application (src/app.py)
2. The request is routed to the appropriate function in src/routes/main.py
3. Input validation is performed using functions from src/utils/validators.py
4. The calculation is performed using the calculate_steps function in src/services/calculator.py
5. The result is sent back to the user through the appropriate route handler

## External Dependencies
- Flask: Web framework
- pytest: Testing framework
- gunicorn: WSGI HTTP Server for running Flask in production

## Recent Significant Changes
- [2025-02-27] Reorganized project structure for better modularity and maintainability
- [2025-02-27] Updated Docker configuration for the new project structure
- [2025-02-27] Implemented input validation
- [2025-02-27] Added error handling and custom error pages
- [2025-02-27] Created and updated unit tests
- [2025-02-27] Implemented health check endpoint

## Potential Improvements
- Implement user authentication and user profiles
- Add a database to store user data and calculation history
- Implement more advanced step calculation algorithms
- Add more comprehensive tests for routes and validators
- Implement continuous integration and continuous deployment (CI/CD) pipeline
- Add type hinting and improve documentation with docstrings