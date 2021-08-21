### Steps to create a django project:

1. Create a virtual environment
2. Activate virtual environment
3. Upgrade pip if needed:
    ```python -m pip install --upgrade pip```

4. Install Django: 
    ```pip install django```

5. Create a project: 
    ```django-admin startproject {project name} . ```  <<< --- There's Dot!

6. Create the DB:
 ``` python manage.py migrate ```

7. Start a Dev server in a separate terminal session: 
    ``` python manage.py runserver``` 
verify that server is alive by opening: http://localhost:8000

8. Create an app in the project: 
    ``` python manage.py startapp {app name} ```