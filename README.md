# Introduction 
The project entails building a microblog to test Python Django skills.

#Prerequisites
Ensure you have python3 installed on your environment.

#### How to setup the project
- Download the source code but running ''git clone command''.
- Install mysql or any other RDBMS i.e sqlite and create a DB with the name 'blog'. Make necessary database changes on the config.
''NB: I used mysql for my case''
- Open the cli and navigate to the directory of the source code downloaded and run the command ''pip intall -r requirements'' to install dependencies.
- Run the migrations by running the commands below.
1. ''python3 manage.py makemigrations''
2. ''python3 manage.py migrate''

#### How to run the project
- Open cli and navigate to the path where your source code is located and run the command ''python3 manage.py runserver''.
- Open the your browser and browse ''localhost:8000''. This will open the swagger-ui to the project. Alternative import the postman collection inside the source code.



