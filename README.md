# django_image_blog

This is a project created for a university assignment. It's a simpler version of Instagram, a blog created with Django Python in which you can create a user account and a profile and make new posts by uploading images. There is also an admin page, in which anyone with admin credentials can login and manage the blog. 

I have listed the commands i used for installing Django and Python and for developing this project. I have also listed the commands that someone needs to run in order, for the project, to work in his system.

It was developed in Ubuntu Linux, so the following terminal commands will work in Linux and probably MacOS but not in Windows. The installation of Django and Python in Windows might be different.

For code writing and editing i used Visual Studio Code.





---------->     TERMINAL COMMANDS     <----------

○ update the local APT repository 
    
    ~$ sudo apt-get update && sudo apt-get -y upgrade

○ install python3

    ~$ sudo apt-get install python3

○ check if python was successfully installed

    ~$ python3 -V

it shows the version of installed python

○ install pip with root command
    
    ~$ sudo apt-get install -y python3-pip

○ check if pip was successfully installed
    
    ~$ pip3 -V

○ install a virtual environment to contain all Python packages and software including django

    ~$ pip3 install virtualenv

○ check if virtualenv was successfully installed
    
    ~$ virtualenv --version

○ create a django-apps directory 

    ~$ cd Home 
    ~$ mkdir django-apps 
    ~$ cd django-apps

○ inside django-apps directory create a virtual environment 

    ~$ virtualenv env

○ activate the virtual env 
    
    ~$ . env/bin/activate

now the prefix is changed to (env)

○ inside the env install django

    ~$ pip3 install django

○ check if django was successfully installed

    ~$ django-admin --version

○ open the port we’ll be using in our server’s firewall to view the django project 

    ~$ sudo ufw allow 8000

○ start a new django project 

    ~$ django-admin startproject django_pikpok(project name)

<---------------------------------------------------------->

○ create a MySQL database for the django project 

    ~$ sudo apt install mysql-server

○ go inside your virtual environment, activate it and create a connector to MySQL database 
    
    ~$ cd django-apps 
    ~$ . env/bin/activate

○ make sure you have python3-dev installed

    ~$ sudo apt install python3-dev

○ install the necessary Python and MySQL development headers and libraries 

    ~$ sudo apt install python3-dev libmysqlclient-dev default-libmysqlclient-dev

○ install the mysqlclient library from PyPi 

    ~$ pip3 install mysqlclient

○ create the database

○ configure Django backend for MySQL compatibility

○ log in via the MySQL root 

    ~$ sudo mysql -u root
    mysql> SHOW DATABASES;

○ if you havent created any databases yet then the output should be like
    
    +--------------------+
    | Database |
    +--------------------+
    | information_schema |
    | mysql |
    | performance_schema |
    | sys |
    +--------------------+
    4 rows in set (0.00 sec)

○ create a database in MySQL

    mysql> CREATE DATABASE blog_data;

○ verify that the database is now listed in your list of available databases 

    ~$ SHOW DATABASES;

○ create a separate MySQL user account (djangouser) to operate the new database

    mysql> CREATE USER 'djangouser'@'%' IDENTIFIED WITH mysql_native_password BY 'password';

○ give djangouser complete access to the database

    mysql> GRANT ALL ON blog_data.* TO 'djangouser'@'%';

○ flush the privileges for the database and the user account made for django

    mysql> FLUSH PRIVILEGES;

type CTRL + D to exit

○ go to django project in settings.py and in DATABASES
config and make changes so that it will use MySQL as database

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'read_default_file': '/etc/mysql/my.cnf',
            },
        }
    }

○ activate virtualenv and run

    ~$ sudo nano /etc/mysql/my.cnf

○ add the following lines at the end of my.cnf file

    [client]
    database = blog_data
    user = djangouser
    password = password
    default-character-set = utf8

○ restart MySQL 

    ~$ sudo systemctl daemon-reload
    ~$ sudo systemctl restart mysql

○ we make the migrations, we run the server and the database is ready 

    ~$ python3 manage.py makemigrations 
    ~$ python3 manage.py migrate 
    ~$ python3 manage.py runserver

stop the server from running with CTRL + C

<---------------------------------------------------------->

○ inside your virtualenv

○ install crispy forms to make your templates look nicer 

    ~$ pip3 install django-crispy-forms

○ install GitHub
    
    ~$ sudo apt-get install git

○ install Bootstrap using NPM

○ create a clone of Bootstrap project from GitHub

    ~$ git clone https://github.com/twbs/bootstrap.git

○ install NPM

    ~$ apt-get install npm
    ~$ npm install bootstrap

○ install Pillow to user ImageField in django and upload images 

    ~$ pip3 install Pillow

○ to start a new app within the django project 

    ~$ cd django_pikpok 
    ~$ python3 manage.py startapp image_blog(new app name)

○ everytime you make changes you need to make migrations within the django project apps 

    ~$ python3 manage.py makemigrations 
    ~$ python3 manage.py migrate

○ to run the server and check your project 

    ~$ python3 manage.py runserver

go to your browser and type http://your-server-ip:8000/ or localhost:8000/

○ create an admin account to make administrative changes 

    ~$ python3 manage.py createsuperuser

○ to make a new folder inside the project 

    ~$ mkdir (foldername)

○ to create a new file 

    ~$ touch (filename.filetype)

○ to make any changes via terminal in your django project : runserver,migrate,create new directory or file 

    ~$ cd django-apps 
    ~$ . env/bin/activate 
    ~$ cd django_pikpok

**when you are done with your django project exit the virtual env with command

    ~$ deactivate

**deleting superuser
go to terminal and type 

    ~$ python3 manage.py shell
    >>> from django.contrib.auth.models import User
    >>> User.objects.get(username="joebloggs", is_superuser=True).delete()
    >>> exit()




    
                        
---------->     TERMINAL COMMANDS YOU NEED TO RUN TO CHECK THIS PROJECT IN YOUR SYSTEM     <----------

○ update the local APT repository 

    ~$ sudo apt-get update && sudo apt-get -y upgrade

○ install python3

    ~$ sudo apt-get install python3

○ check if python was successfully installed

    ~$ python3 -V

it shows the version of installed python

○ install pip with root command

    ~$ sudo apt-get install -y python3-pip

○ check if pip was successfully installed
    
    ~$ pip3 -V

○ install a virtual environment to contain all Python packages and software including django

    ~$ pip3 install virtualenv

○ check if virtualenv was successfully installed

    ~$ virtualenv --version

○ create a django-apps directory 

    ~$ cd Home
    ~$ mkdir django-apps 
    ~$ cd django-apps

○ inside django-apps directory create a virtual environment 

    ~$ virtualenv env

○ activate the virtual env 

    ~$ . env/bin/activate

now the prefix is changed to (env)

○ inside the env install django
    
    ~$ pip3 install django

○ check if django was successfully installed
    
    ~$ django-admin --version

○ open the port we’ll be using in our server’s firewall to view the django project 
    
    ~$ sudo ufw allow 8000

move the django_pikpok directory inside the django-apps directory

○ create a MySQL database for the django project 
    
    ~$ sudo apt install mysql-server

○ go inside your virtual environment, activate it and create a connector to MySQL database 

    ~$ cd django-apps 
    ~$ . env/bin/activate

○ make sure you have python3-dev installed

    ~$ sudo apt install python3-dev

○ install the necessary Python and MySQL development headers and libraries 

    ~$ sudo apt install python3-dev libmysqlclient-dev default-libmysqlclient-dev

○ install the mysqlclient library from PyPi 
    
    ~$ pip3 install mysqlclient

○ log in via the MySQL root 
    
    ~$ sudo mysql -u root

○ create a new database to load the files from our django database

○ Enter the MySQL shell 

    ~$ mysql
    > CREATE DATABASE newdatabase;

○ create a separate MySQL user account (djangouser) to operate the new database

    mysql> CREATE USER 'username'@'%' IDENTIFIED WITH mysql_native_password BY 'password';

○ give djangouser complete access to the database

    mysql> GRANT ALL ON newdatabase.* TO 'username'@'%';

○ flush the privileges for the database and the user account made for django

    mysql> FLUSH PRIVILEGES;

type CTRL + D to exit

○ exit the MySQL shell and type 

    ~$ mysql -u [username] -p newdatabase < blog_data.sql

○ go back to MySQL shell and flush the privileges for the database and the user account made for django

    mysql> FLUSH PRIVILEGES;

type CTRL + D to exit

○ make database migrations inside the django-apps directory

    ~$ python3 manage.py makemigrations 
    ~$ python3 manage.py migratemysql

○ restart MySQL 

    ~$ sudo systemctl daemon-reload
    ~$ sudo systemctl restart mysql

○ make the migrations, run the server and the database is ready 

    ~$ python3 manage.py makemigrations 
    ~$ python3 manage.py migrate 
    ~$ python3 manage.py runserver

stop the server from running with CTRL + C

○ inside your virtualenv install crispy forms to make your templates look nicer 
    
    ~$ pip3 install django-crispy-forms

○ install GitHub

    ~$ sudo apt-get install git

○ install Bootstrap using NPM

○ create a clone of Bootstrap project from GitHub

    ~$ git clone https://github.com/twbs/bootstrap.git

○ install NPM

    ~$ apt-get install npm
    ~$ npm install bootstrap

○ install Pillow to use ImageField in django and upload images 

    ~$ pip3 install Pillow

○ create an admin account to make administrative changes and login to the admin page 

    ~$ python3 manage.py createsuperuser

○ run the server 

    ~$ python3 manage.py runserver

View the project by going to your browser and typing http://your-server-ip:8000/ or localhost:8000/

○ to make any changes via terminal in your django project : runserver,migrate,create new directory or file 

    ~$ cd django-apps 
    ~$ . env/bin/activate 
    ~$ cd django_pikpok

**when you are done with your django project exit the virtual env with command

    ~$ deactivate
