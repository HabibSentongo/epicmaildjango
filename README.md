# epicmaildjango
Django version of EpicMail by A21 Team


## Projec Overview
This is an application that enables exchange of information through messages.

## Getting started
 These instructions will get you acopy of the project up and running on your local machine for development and testing purposes.

 ## Prerequisties
Inorder  to run this application you need the following;
you need to have [python3](https://www.python.org/downloads/)  installed on your machine.

You need to have [Django](https://docs.djangoproject.com/en/2.2/topics/install/) installed on your machine.

The application is bulit with a python flamework called [Django](https://docs.djangoproject.com/en/2.2/).
 
 ## Installing 

> - To clone this appplication;

 ```
  $ git clone : https://github.com/HabibSentongo/epicmaildjango
```


 > - Then change directory 
```
 $ cd <app directory>
```

 Extract and open this application in a text editor Vscode or any other editor
 for Vscode run this 
 ```
 $ code .
 ``` 
  
> - You have to install a virutualenvirnoment, 
```
  $ pip3 install virtualenv
```

> - Create the virtual envirnoment
```
  $ virtualenv env
```

> - Activate your virtualenv to start working.
 ```
 $ source env/bin/activate
 ```

> - Install  django 
```
$ pip install django
```

> - Install  django Rest Framework
```
$ pip install djangorestframework
```
 Good then install the app dependencies,these are found in the `requirements.txt`
 ```
 $ pip install -r requiremnets.txt
 ```

 Then Create  a project for the application 
 > - Run the following command 
```
$ django-admin  startproject Epicmail .
```
Note the trailing '.' character

 Then change directory 
 ```
 $ cd Epicmail
```

After this go ahead and create the application
```
$ django-admin  startapp the_epicmail 
```

 

