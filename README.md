StaffManager-API
Welcome to the **StaffManager-API**, a RESTful service designed for managing employee data within organizations. This API provides a structured way to perform CRUD operations on employee records while implementing best practices for security and error handling.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Server](#running-the-server)
- [API Endpoints](#api-endpoints)
  - [Authentication](#authentication)
  - [Employee Management](#employee-management)
- [Filtering and Pagination](#filtering-and-pagination)
- [Testing](#testing)
- [Documentation](#documentation)

## Project Overview

The **EmployeeTrackr API** serves as a backend solution for companies looking to efficiently manage their employee records. It supports essential CRUD operations (Create, Read, Update, Delete) and ensures secure access through token-based authentication. This API is designed with RESTful principles in mind, providing a clear and intuitive interface for developers.

## Features

- **CRUD Operations**: Create, retrieve, update, and delete employee records.
- **Token-Based Authentication**: Secure access to API endpoints using JSON Web Tokens (JWT).
- **Filtering**: Easily filter employee records by department or role.
- **Pagination**: Manage large datasets by paginating responses, limiting results to 10 employees per page.
- **Error Handling**: Comprehensive error handling with informative HTTP status codes.

## Technology Stack

- **Python**: The programming language used for building the API.
- **Django**: A high-level Python web framework that promotes rapid development.
- **Django REST Framework (DRF)**: A powerful toolkit for building Web APIs.
- **SQLite** (or **PostgreSQL**): A lightweight database for storing employee data.
- **JSON Web Tokens (JWT)**: A standard for securely transmitting information between parties.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python** (version 3.8 or higher)
- **Pip** (Python package installer)
- **Virtual Environment** (optional but recommended)

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/EmployeeTrackr.git
   cd EmployeeTrackr
   ```
2. **Set Up a Virtual Environment**:

   ```bash
   python3 -m venv env
   source env/bin/activate  # For Windows: env\Scripts\activate
   ```
3. **Install Required Packages**:

   ```bash
   pip install -r requirements.txt   cd EmployeeTrackr
   ```
4. **Create a Superuser (optional)**:

   ```bash
   python manage.py createsuperuser
   ```
5. **Start the Django development server**:

   ```bash
   python manage.py runserver
   ```
### Access the API at http://127.0.0.1:8000/

### API Endpoints
## Authentication
Obtain Token
POST /api/token/

This endpoint allows users to authenticate and receive a JWT token.
**Request Body**:

   ```bash
   {
     "username": "your_username",
     "password": "your_password"
   }

   ```
**Response**:

  ```bash
  {
    "access": "your_jwt_access_token",
    "refresh": "your_jwt_refresh_token"
  }
  ```
## Refresh Token
POST /api/token/refresh/

**Request Body**:

  ```bash
  {
    "refresh": "your_jwt_refresh_token"
  }
  ```

### Employee Management
## 1. Create an Employee
POST /api/employees/

This endpoint allows you to create a new employee record.
**Request Body**:

  ```bash
  {
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "department": "Sales",
  "role": "Developer"
  }
  ```

**Response**:

  ```bash
  {
  "id": 1,
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "department": "Sales",
  "role": "Developer",
  "date_joined": "2024-11-01"
  }
  ```

## 2. List All Employees
GET /api/employees/

Retrieve a list of all employees with pagination.

**Response Example**:

  ```bash
  [
  {
    "id": 1,
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "department": "Sales",
    "role": "Developer",
    "date_joined": "2024-11-01"
  },
  {
    "id": 2,
    "name": "Bob Smith",
    "email": "bob@example.com",
    "department": "Engineering",
    "role": "Manager",
    "date_joined": "2024-11-02"
  }
  ]
  ```

## 3. Retrieve a Single Employee
GET /api/employees/{id}/

Fetch a single employee's details by their ID.

**Response Example**:

  ```bash
  {
  "id": 1,
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "department": "Sales",
  "role": "Developer",
  "date_joined": "2024-11-01"
  }
  ```

## 4. Update an Employee
PUT /api/employees/{id}/

Update an existing employee's information.

**Response Body**:

  ```bash
  {
  "name": "Alice Johnson",
  "email": "alice.new@example.com",
  "department": "Sales",
  "role": "Senior Developer"
  }
  ```

## 5. Delete an Employee
DELETE /api/employees/{id}/

Remove an employee record from the database.

**Response**:

HTTP Status 204 No Content on successful deletion.

## Filtering and Pagination
# Filter Employees: Use query parameters to filter employees by department or role.

GET /api/employees/?department=Sales&role=Developer

# Pagination: Limit results per page to 10 employees with pagination support.

GET /api/employees/?page=2

## Testing
To run the tests for the API, execute the following command:

``` bash
python manage.py test

```
This will run all the unit tests defined for the API endpoints, ensuring that functionality and edge cases are covered.

### Documentation
## Running Locally
1. Clone the repository and follow the installation steps above.
2. Start the server to access the API endpoints.
3. Use tools like Postman to test the API:
* Authenticate to obtain a token.
* Add the token to the Authorization header as Bearer <token> for secured requests.
  
### API Documentation (Optional)
For interactive API documentation, consider using drf-yasg. After installing and configuring it, access the documentation at:

* Swagger UI: http://127.0.0.1:8000/swagger/
* ReDoc: http://127.0.0.1:8000/redoc/

