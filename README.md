# Simple API

A lightweight and easy-to-use RESTful API built with Flask. This API provides basic functionality to retrieve, add, and manage a list of items, serving as a foundational implementation for learning or small-scale projects.

## Features

- **GET /**: Displays a welcome message.
- **GET /items**: Retrieves a list of predefined items.
- **POST /items**: Allows adding a new item by sending JSON data.

## Installation

### Prerequisites
- Python 3.7 or higher
- `pip` (Python package installer)

### Steps to Set Up Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/kylelknight/simple-API.git
   cd simple-API
2. Install Dependencies
   ```bash
   pip install flask
3. Run the application:
   ```bash
   python3 api.py
The API will run locally at http://127.0.0.1:5000.


## Endpoints

### **GET /** - Welcome Message
- **Description**: Returns a JSON response with a welcome message.
- **Example Request**:
  ```bash
  curl http://127.0.0.1:5000/

**Example Response**
  ```json
[
    {"id": 1, "name": "Item One"},
    {"id": 2, "name": "Item Two"},
    {"id": 3, "name": "Item Three"}
]



