# Step Calories Calculator

## Overview
The Step Calories Calculator is a web application that helps users estimate the number of steps needed to burn a specific amount of calories. It takes into account the user's weight and walking pace to provide a personalized calculation.

## Features
- Calculate steps based on calories, weight, and pace
- Responsive web interface
- Dockerized for easy deployment
- Prepared for cloud deployment (Hetzner Cloud)

## Technologies Used
- Python 3.9
- Flask
- Docker
- Gunicorn

## Setup and Installation

### Prerequisites
- Docker
- Docker Compose

### Local Development
1. Clone the repository:
   ```
   git clone https://github.com/hheydaroff/step-calories-calculator.git
   cd step-calories-calculator
   ```

2. Create a `.env` file in the project root and add the following:
   ```
   SECRET_KEY=your_secret_key_here
   FLASK_ENV=development
   ```

3. Build and run the Docker container:
   ```
   docker-compose up --build
   ```

4. Access the application at `http://localhost:5001`

## Usage
1. Enter the number of calories you want to burn
2. Input your weight in kilograms
3. Select your walking pace (Slow, Moderate, or Brisk)
4. Click "Calculate Steps" to see the estimated number of steps required

## Deployment
This application is prepared for deployment on Hetzner Cloud. Refer to the `deployment_plan.md` in the `cline_docs` directory for detailed deployment instructions.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
[MIT License](LICENSE)
