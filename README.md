# IdentificationLab

## Install python dependencies
```
pip install -r requirements.txt
```

## Run Django
Go to the directory [**source/**](https://github.com/alexauf/IdentificationLab/tree/main/source)
Then run the following commands:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Nice!! Now the server is running, you can stop it with `ctrl+c` and can create an user by doing:
```
python manage.py createsuperuser
```
I suggest you to use simple user and pass.
Maybe a super user is already created: **admin/admin**
To see if it is created you can go to:
```
https://localhost:8000/admin
```
Then introduce the user and password mentioned before.
You can try the login with OAuth2.0 in the following page:
```
http://localhost:8000/accounts/log-in/
```

## NOTES
In this project has been used python3
