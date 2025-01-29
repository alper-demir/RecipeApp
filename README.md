# RecipeApp

## Project Description

RecipeApp is a web application developed using Django, featuring a robust database backend and interactive frontend functionality powered by jQuery. This project allows users to manage and explore recipes with an intuitive and user-friendly interface.

## Technologies Used

- **Backend**: Django (Python Web Framework)
- **Frontend**: HTML, CSS, jQuery
- **Database**: SQLite

## Features

- Recipe management
- Interactive user interface
- Database-driven recipe storage and retrieval

## Prerequisites

- Python 3.8+
- Django
- pip (Python Package Manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/alper-demir/RecipeApp.git
   ```

2. Navigate to the project directory:
   ```bash
   cd RecipeApp
   ```

3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

2. Start the development server:
   ```bash
   python manage.py runserver
   ```

3. Open your browser and navigate to `http://127.0.0.1:8000/`

## Project Structure

```
RecipeApp/
│
├── djangoProject/     # Django project configuration
├── recipeapp/         # Main application directory
├── static/            # Static files (CSS, JavaScript)
├── templates/         # HTML templates
├── db.sqlite3         # SQLite database
└── manage.py          # Django management script
```
