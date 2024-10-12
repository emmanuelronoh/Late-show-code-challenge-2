# Late Show Code Challenge

## Overview

This project is a web application that simulates a database of episodes, guests, and their appearances on a fictional late-night show. The application allows users to retrieve, add, and delete episodes and guest appearances through a RESTful API.

## Features

- **API Endpoints**:
  - Get all episodes
  - Get a specific episode by ID
  - Get all guests
  - Create a new appearance
  - Delete an episode by ID

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- PostgreSQL (or your preferred database)
- CSV for seeding data

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip
- PostgreSQL (or your preferred database)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd late-show-code-challenge
2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
4. **Set up your database**:

 Update the *config.py* file with your database connection settings.

5. **Run migrations**:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
6. **Seed the database**:

Make sure to place your seed.csv file in the appropriate directory and run:

    python seeds/seed.py

### Running the Application
To run the application, execute:  
 python app.py

The server will start at http://localhost:5000.

API Usage
You can use tools like Postman or curl to interact with the API.

Example Endpoints
- **Get all episodes**:

    ```bash
    curl http://localhost:5000/api/episodes
- **Get a specific episode**:

   ```bash
   curl http://localhost:5000/api/episodes/1
- **Delete an episode**:

   ```bash
    curl -X DELETE http://localhost:5000/api/episodes/1
- **Get all guests**:

   ```bash
   curl http://localhost:5000/api/guests
- **Create a new appearance**:
   To create a new guest appearance, use the following command:
   ```bash
   curl -X POST http://localhost:5000/api/appearances -H "Content-Type: application/json" -d '{"rating": 5, "episode_id": 1, "guest_id": 1}'

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

