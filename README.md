# YoungDev_Interns_Tasks
This repository showcases my work on various tasks. To run each file, please follow these steps:
## Digital Resume
1. Install the required library: pip install streamlit
2. Run the file in terminal: streamlit run digital_resume.py.

## My Portfolio
1. Install Django: `pip install django`
2. Navigate to the project directory and run the development server: python manage.py runserver
3. Open a web browser and navigate to `http://localhost:8000/` to view the website.

## Sine and Cosine Graph
1. Install the required libraries: pip install matplotlib numpy
2. Run this file to open a window displaying the sine and cosine graph.

## E-Commerce Website
#For Intermediate task 1
1. Install Django: `pip install django`
2. Navigate to the project directory and run the development server: python manage.py runserver
3. Open a web browser and go to:
http://localhost:8000/ → Client side,
http://localhost:8000/admin → Admin side (login with superuser)
Use the following login credentials for admin access:
Username: Maryam
Password: ecommerce123 (Or create your own superuser)
5. To create a superuser: run `python manage.py createsuperuser` in the terminal and follow the prompts.

#For Intermediate task 2
This task adds two major features:
Admin can perform CRUD operations on products & Admin can assign roles
**Note**: Only the db.sqlite3 file has been updated in this task.
To view the new functionality:
1. Use the existing project files from Task 1
2. Replace the old db.sqlite3 with the updated one provided for Task 2
3. Run the project as before using python manage.py runserver.

#For Intermediate task 3
This task adds a new feature to the E-Commerce website:
Admin can now accept payment of purchases placed by customers
**Changes**:
. The `Order` model has been updated to include an `is_paid` boolean field
. Admin can view all orders from the admin panel and mark them as paid
. Customer receives a success message on placing an order
. The order form automatically hides and redirects after successful submission
To view the new functionality:
1. Use the project folder (`ecommerce_project`) 
2. Run the server with: `python manage.py runserver`
3. Go to:
   http://localhost:8000/ → Client side
   http://localhost:8000/admin → Admin side (login with superuser)


