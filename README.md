# IdentificationLab
## Install Django
I think the only thing needed to run a django server is to install Django, if you are a pussy and have Windows as OS you can do:
```
py -m pip install Django
```
If there is any error or when you try to run it shows that does not exist any dependency is normally so fucking easy to install it, if you are lucky you will solve it with:
```
py -m pip install whateverTheShitThatTheTerminalSaysItIsNotFound
```

## Run Django
Go to the directory [**clientServer/**](https://github.com/alexauf/IdentificationLab/tree/main/clientServer)
Then for runing the server you should do:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Nice!! Now the server is running, you can stop it with `ctrl+c` and can create an user by doing:
```
python manage.py createsuperuser
```
I suggest you to use simple user and pass as: **admin/admin**

Now, everything is working, you can start searching the OpenID connect bullshit to implement it in login function.

## Programming in Django
In this case all the logic must go in the login function inside [**clientServer/clientApp/views.py**](https://github.com/alexauf/IdentificationLab/blob/main/clientServer/clientApp/views.py)

## Problems with Github
I don't know what exactly have happened with git and github, but now you can't use git in terminal to do git clone directly by putting your user and password and have to create a token, to do that go to [**settings/tokens**](https://github.com/settings/tokens), then click **generate new token** and put the name that you want, then tick all the boxes, i don't even fucking understand what all them are for but if you wanna do all shit like a fucking git beast you should tick them all. Once generated you need to copy your token, don't be a noob and forget to copy it because it will only be shown once you fucking stupid bitch.
Finally when you are doing git clone, enter your user, and for the password paste your token.
And well, thats all. If you have not Django running in your computer after all this, you really are useless, drop the master and go work selling _gelati_
