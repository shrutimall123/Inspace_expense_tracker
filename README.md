# Inspace_expense_tracker

# Expense Tracker

An Expense Tracker application built with Django to help users manage and track their expenses. The app allows users to add, view, and filter expenses by category and date. The filtering feature lets users narrow down their expense lists for easier tracking and analysis.

## Features

- **User Registration**: Users can sign up for an account to securely track their expenses.
- **Expense Management**: Add, edit, and delete expenses.
- **Filtering**: Filter expenses by category and date to get a clearer view of specific expenses.
- **Responsive Design**: Mobile-friendly user interface with clean and modern styling.
- **Authentication**: Secure user authentication for protecting personal financial data.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default Django database)

## Project Setup

### Prerequisites

To run this project, you will need:

- Python 3.8 or higher
- Django 3.x or higher
- Bootstrap 4 or higher (for styling)
- FontAwesome (for icons)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/expense-tracker.git
    ```

2. Navigate into the project directory:

    ```bash
    cd expense-tracker
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

  

    - On macOS/Linux:
    
        ```bash
        source venv/bin/activate
        ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser to access the Django admin panel (optional but recommended for managing data):

    ```bash
    python manage.py createsuperuser
    ```

8. Run the development server:

    ```bash
    python manage.py runserver
    ```

9. Open your browser and navigate to `http://127.0.0.1:8000` to view the app.

## How to Use

### Register and Login

- First, register an account to start using the app.
- Once registered, you can log in and manage your expenses.

### Add Expenses

- Navigate to the "Add Expense" page.
- Fill out the expense details, including category, amount, and date.
- Submit the form to add the expense to your list.

### Filter Expenses

- Use the filter form to filter your expenses by **category** or **date**.
- Click the "Filter" button to see the filtered results.
- Use the "Clear" button to reset the filters and see the full list again.

## Folder Structure

```plaintext
expense-tracker/
│
├── expense_tracker/            # Main Django project directory
│   ├── settings.py             # Django settings file
│   ├── urls.py                 # Project-wide URL routes
│   ├── wsgi.py                 # WSGI config for deployment
│   └── ...
│
├── expenses/                   # Expenses app
│   ├── migrations/             # Database migrations for expenses
│   ├── templates/              # HTML templates
│   │   └── expenses/           # Templates for expenses app
│   ├── views.py                # Views for managing expenses
│   ├── models.py               # Expense model definition
│   ├── forms.py                # Forms for adding/editing expenses
│   ├── urls.py                 # URL routes for expenses app
│   └── ...
│
├── static/                     # Static files (CSS, JS, images)
│
├── templates/                  # Base templates
│   └── base.html               # Base template for all pages
│
├── manage.py                   # Django's CLI entry point
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies
