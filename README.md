# LAB - Class 31

## Project: Books API

### Author: Harper Foley

### Links and Resources

* [Repo](https://github.com/hfoley2013/django_books_api)
* [Django REST Framework](https://www.django-rest-framework.org/)

#### Setup

* Create a new project folder on your local machine
  * `mkdir new_project && cd new_project`
* Clone the repo into your new folder
  * `git clone https://github.com/hfoley2013/django_books_api.git`
* Create a virtual environment to hold the project requirements
  * `python -m venv .venv`
* Install the `requirements.txt` file
  * `pip install -r requirements.txt`
* The application is now successfully cloned and able to run on your local machine

#### How to initialize/run your application (where applicable)

* To run the application
  * `python manage.py runserver`
* This will open the server in your local host
* Navigate to the `/api/v1/books/` endpoint to see the list of books available in the database
* To go to a specific book, you can enter the book `id` at the end of the url
  `/api/v1/books/1` will take you to *Web Development with Node.js and Express*
* You can add books from the list view
* You can update books from the details view
* You can delete books from the details view

#### Tests

* Tests are internal to Django and can be run by entering:
  * `python manage.py test books` while the server is running
