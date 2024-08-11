# Django-Database-Application
Project Assignment for CMPE321 - Inroduction to Database Systems at Bogazici University.

- This project is indeed a Django application to create a database managament system for Turkish National Volleybal League.
- The project can be divided into 2 main parts:
  
- **1. Constructing the database**
- This part can be achieved by executing .sql files.
- This project uses MySQL, so MySQL Workbench is used for this part.
- Firstly, begin with add schema "VolleyDB", after refreshing the schema navigator on the left tab, you will be able to see the created shema.
- Right click on the VolleyDB and select is as the default schema.
- Then execute "create_table.sql", after refreshing the schema navigator on the left tab, you will be able to see the created tables.
- After that, execute "inserts.sql", this move will insert the given mock database information into newly created tables.
- Then add triggers to database to meet the requirements in the project description, this step will be achieved by executing "first_trigger.sql" and "second_trigger.sql" consecutively.

  Now the database is completely setted and ready for use in the second part of the application.
  In the Django-application, there will be a connection for "VolleyDB" database.

- **2. Django Application**
  - The application files are located under "code" folder, you may prefer open this folder under an IDE.
  - Then run "pip install -r requirements.txt" command.
  - After that, run "python -m venv env" command to create the virtual environment.
  - Then, activate the virtual environment by "source myvenv/bin/activate" command.
  - Finally run "python manage.py runserver" command.
  - In the IDE output console, you will see the http domain, ctrl + click on that address and the Django-application will be opened.
 
- You can make your first login to the system via the registered username and passwords in the VolleyDB database, then access to the Database Manager / Player / Coach / Jury dashboards and perform related tasks.

Now, you can try the given project requirements and tasks in the project description on your own through the Django-application :)
     
