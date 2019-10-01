# react-django-template
A project template for creating a React application coupled with a Django backend API

## Initial Setup - Backend

After cloning the repo, you should first set up a Python virtual environment, and install the development requirements. From a command line prompt, navigate to the `backend` directory and run the following commands to create and activate a new virtual environment named `env`:
```
python3 -m venv env
source env/bin/activate
```
After creating the virtual environment, you then need to install all of the package dependencies and apply Django database migrations to set up the database:
```
make installdeps
python manage.py migrate
```
If the installation completed successfull you can start the development server using the command `make run`. If you then open a browser and navigate to [http://localhost:8000/](http://localhost:8000/) you should see the Django welcome page.


## Initial Setup - Frontend
