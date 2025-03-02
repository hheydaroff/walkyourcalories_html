# Walk Your Calories

## Overview
Walk Your Calories is a web application that helps users estimate the number of steps needed to burn a specific amount of calories. It takes into account the user's weight and walking pace to provide a personalized calculation. The application is currently undergoing a major frontend redesign and feature expansion to enhance user experience and provide more comprehensive information about the benefits of walking.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Docker Deployment](#docker-deployment)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [Frontend Implementation Timeline](#frontend-implementation-timeline)
- [Contributing](#contributing)
- [License](#license)

## Features
- Calculate steps based on calories, weight, and pace
- Responsive web interface
- Multiple informational pages (Home, How It Works, Benefits, FAQ, About Us)
- Reusable calculator widget across pages
- Dockerized for easy deployment
- Unit tests for core functionality

## Technologies Used
- Backend:
  - Python 3.9+
  - Flask 3.1.0
  - pytest 8.3.4
- Frontend:
  - HTML5 (semantic elements)
  - CSS3 (BEM methodology, CSS Grid, Flexbox)
  - JavaScript (ES6+, Vanilla JS)
- DevOps:
  - Docker
  - Docker Compose

## Prerequisites
- Python 3.9+
- Docker and Docker Compose (for containerized deployment)
- Node.js and npm (for frontend development)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/walk-your-calories.git
   cd walk-your-calories
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
│   ├── styles.css
│   ├── js/
│   │   └── main.js
│   └── images/
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── how_it_works.html
│   ├── benefits.html
│   ├── faq.html
│   ├── about_us.html
│   ├── calculator.html
│   ├── 404.html
│   └── 500.html
├── cline_docs/
│   ├── projectRoadmap.md
│   ├── currentTask.md
│   ├── techStack.md
│   ├── codebaseSummary.md
│   └── frontend_implementation_timeline.md
├── .dockerignore
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── README.md
└── requirements.txt
```

## Frontend Implementation Timeline

We are currently in the process of implementing a new frontend design and structure. The implementation is planned to be completed over a 10-week period, divided into 5 sprints. Each sprint is 2 weeks long and focuses on specific aspects of the frontend development. For more details, please refer to the [Frontend Implementation Timeline](cline_docs/frontend_implementation_timeline.md).

Key milestones:
1. End of Sprint 1 (Week 2): Basic structure and calculator widget completed
2. End of Sprint 2 (Week 4): All main pages implemented with integrated calculator widget
3. End of Sprint 3 (Week 6): Fully responsive and optimized frontend
4. End of Sprint 4 (Week 8): Thoroughly tested and refined frontend
5. End of Sprint 5 (Week 10): Production-ready frontend prepared for launch

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
