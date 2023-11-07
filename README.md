# Programming Exercise for Greenbone Networks

### Computer Tracking System - A Django Project


### Important Note
```markdown

1. The user signup/login and authentication mechanism for APIs was not implemented as it was not
   defined in the scope of requirements.

2. Minimum implementation of Docker configuration added to run the application.

3. SQLite database is used for assignment purpose for production recommend using PostgreSQL.
```

Instructions for setting up and running the project:

```markdown
This is a Django project for a computer tracking system designed for system administrators.
The project allows the tracking of computers issued by the company, management of computer 
records, and assignment of computers to employees.
```

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Unit Tests](#unit-tests)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)

## Features

The project includes the following features:

- Storing computer details in a database, including MAC address, computer name, IP address, and optional employee assignment and description.
- RESTful API endpoints for Create, Read, Update, and Delete (CRUD) operations for computers.
- Listing all computers.
- Listing computers assigned to a specific employee.
- Assigning a computer to an employee.
- Automatic notification when an employee is assigned 3 or more computers.

## Getting Started

### Prerequisites

Before you start, ensure you have the following:

- Python (3.6 or higher)
- Pip (Python package manager)
- Django (install with `pip install Django`)
- Django Rest Framework (install with `pip install djangorestframework`)
- Factory Boy (for testing, install with `pip install factory_boy`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/asadmanzoor93/greenbone_networks.git
   cd greenbone_networks/hardware_tracking
   
   # adjust the settings for environment
    cp deployment.template.py deployment.py
    vim deployment.py
   ```

2. Run the Docker container using Docker Compose:

   ```bash
   docker-compose up
   ```

3. Open your web browser and access the Django application running locally at [http://localhost:8000](http://localhost:8000).


4. To stop the application and remove the containers, use the following command:

   ```bash
   docker-compose down
   ```

## Project Structure

- `Dockerfile`: Defines the Docker image for the Django project.
- `docker-compose.yml`: Configuration for running the Django application and an SQLite database.
- `requirements.txt`: Lists the project's Python dependencies.
- `hardware_tracking/`: Application source code.
- `hardware_tracking/settings.py`: Application settings, including the database configuration.
- `manage.py`: Django management script.
- `.github/workflows/`: Github configuration for running unit tests and quality check on Pull Requests.

## Usage

- Detailed documentation is available at http://localhost:8000/docs/
- Access the admin panel to manage computers and employees: http://localhost:8000/admin/

## API Endpoints
- Use the API endpoints for CRUD operations on computers. The available endpoints are:
  - `/api/computers/`
  - `/api/computers/<computer_id>/`
  - `/api/computers/create/`
  - `/api/computers/<computer_id>/update/`
  - `/api/computers/<computer_id>/delete/`
  - `/api/computers/employee/<employee_abbreviation>/`
  - `/api/computers/<computer_id>/assign/`

## Unit Tests

To run unit tests for the project, use the following command:

```bash
python manage.py test
```

This will execute the unit tests for your views, models and signal.

## Contributing

If you'd like to contribute to this project, please follow the standard GitHub flow:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Create a pull request.
