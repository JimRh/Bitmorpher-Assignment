# Bitmorpher-Assignment
 
This repository contains the code for the Bitmorpher assignment. It includes the setup for a Django project with custom middleware and API endpoints. Follow the instructions below to clone and set up the project on your local machine.



Prerequisites
Before setting up the project, ensure you have the following software installed on your local machine:

Python (version 3.8 or higher)
pip (Python package installer)
virtualenv (for creating isolated Python environments)
Git (for cloning the repository)
Database (such as PostgreSQL, MySQL, or SQLite)
Installation
Follow these steps to clone the repository and set up the project locally:

Step 1: Clone the Repository
Open your terminal and run the following command to clone the repository:

git clone https://github.com/JimRh/Bitmorpher-Assignment.git

Navigate to the project directory:

cd Bitmorpher-Assignment

Step 2: Create and Activate a Virtual Environment



python -m venv venv:



Activate the virtual environment:

On Windows:

venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

Step 3: Install Dependencies

Install the required Python packages using pip:

pip install -r requirements.txt



Step 4: Set Up the Database

Make sure you have your database configured and accessible. Create the necessary database tables by running the migrations:

python manage.py migrate

Step 6: Create a Superuser

Create a superuser account to access the Django admin interface:

python manage.py createsuperuser

Follow the prompts to set up your admin account.

Running the Project:

Start the Django development server to run the project locally:

python manage.py runserver

Open your browser and navigate to http://127.0.0.1:8000 to see the project in action.

Access the Django admin interface at http://127.0.0.1:8000/admin using the superuser credentials you created earlier.

Use the provided postman collection to test the api endpoints