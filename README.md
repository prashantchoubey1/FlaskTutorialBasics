Flask - framework python

code:
import pandas as pd -- correct (semantic rule)
import pd as pandas -- incorrect

Framework: a framework is a real or conceptual structure intended to serve as a support or 
guide for the building of something that expands the structure into something useful.


Python language:
(Function, Class, Variable ) -> create a UI
Input: text field, button
Output: xyz

Flask:
Python framework used to build API (application programming interface)

Application : 
Backend ----> Middle Ware ----> Front end 
(DBMS)   ----> (API)     ----> (UI)  
(SQL/No SQL) ----> (Py Flask/Py Django/Java Spring boot) ----> (HTML/CSS/JS)  

->API works to take data from backend and sends to frontend and vice versa
->How to build an API which can interact from backend and send data to front end or takes data from front end and send to backend


Before any python project:
Create a virtual environment to make sure the dependencies remain consitent 

Learn today:
1. what is API?
2. What is framework?
3. How to use flask to build basic api to take input and generate output?

Next:
1. Build api to interact with database

Todo:
1. Create an API in python to check if a number is prime or not
2. Create an API in python to check the count of words in sentence

Note:
Always create a virtual env before development
Use flask run to run app
export FLASK_APP=app.py to set flask app

Task:
1. Install sqlite in vscode - Done
2. Create a database - Done
3. Create a table - Done
4. Create a sql query to insert data and view data - Done
5. Create a html form and take input throgh from
5. Create a flask app to query the database

Steps to install sqlite and interact with sqlite:
- Install sqlite from vscode extensions
- Follow step in the link to create a database, create table, insert data into table and select data or view data (https://burkeholland.gitbook.io/vs-code-can-do-that/exercise-7-working-with-data/working-with-sqlite)
- Created html form using chatgpt
- Link the html form with flask application (making sure that the html form name is the web address of flask app, using the input ids in html to be passed in flask)
- Crete queries inside flask functions and run them on db
- Return rows on front end

Todo:
1. Create  a function that takes user input from html form like name, age and weight. Use the above to insert into database
2. Create a function to enter age and filter all students with the same age