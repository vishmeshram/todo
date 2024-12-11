# todo
# Django To-Do List Application

This is a simple to-do list application built with Django, allowing users to manage their tasks. You can add new tasks, view the list of tasks, and use the admin panel to manage tasks.

## **Features**
- Add new tasks to the to-do list.
- View the list of all tasks.
- Simple and intuitive user interface.

---

## **1. Setup Instructions**

Follow these steps to set up the project locally:

### **Install Dependencies**
First, create a virtual environment and install the required dependencies:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# For Windows
venv\Scripts\activate
# For MacOS/Linux
source venv/bin/activate


# Apply database migrations
python manage.py migrate

# Start the development server
python manage.py runserver

todo_project/
├── tasks/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       
│           ├── base.html
│           ├── task_list.html
│           └── add_task.html
├── manage.py
├── todo_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── requirements.txt


