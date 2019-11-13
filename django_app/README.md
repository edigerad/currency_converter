# Currency Converter Backend


##  Instructions for use and launch app.

1. Configure virtual environment settings

    1.1 Create virtual environment and activate it
    
    ```bash
    virtualenv -p python3.6 .venv
   source .venv/bin/activate
    ```
    1.2 Install required libraries

    ```bash
    pip install -r requirements/base.txt
    ```
2.  Install Postge SQL and create database
   
       Connect to the mysql server
   
       ```bash
       sudo su - postgres
       psql
       ```
       Create database with user in the shell
   
       ```bash
       CREATE DATABASE cc_db;
       CREATE ROLE cc_user WITH PASSWORD 'cc_password';
       GRANT ALL PRIVILEGES ON DATABASE cc_db to cc_user;
       ALTER ROLE cc_user LOGIN CREATEDB;
       ```


3. Migrate the database and create super user

    ```bash
    ./manage.py migrate
    ```
   
    ```bash
    ./manage.py createsuperuser
    ```


3. Create directory for logs

    ```bash
    mkdir logs
    ```

4. Compile the translation files

    ```bash
    ./manage.py compilemessages
    ```

5. Run the server

    ```bash
    ./manage.py runserver
    ```

6. Run worker manually to be sure that celery is correct and runnable

    ```bash
    celery -A config worker -l info
    ```
7. Test the RESTful API 
 
    ```bash
    ./manage.py test
    ```