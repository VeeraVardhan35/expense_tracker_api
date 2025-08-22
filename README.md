# Expense Tracker API

A Django REST API for managing personal expenses with authentication and filtering.

## Features
- User authentication (JWT)
- CRUD operations for expenses
- Categories and date-based filtering
- PostgreSQL backend

## Tech Stack
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Docker (optional)

## Setup
```bash
git clone https://github.com/YourUsername/expense-tracker-api.git
cd expense-tracker-api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
