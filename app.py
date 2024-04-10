## Importing flask library - helps to build API in flask
from flask import Flask, render_template
from flask import request

## creating flask application
app = Flask(__name__)

## creating web address
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hi")
def abc():
    return "<p>hello guddu</p>"


## Create a python api to find whether a number is even or odd
@app.route("/even_validation", methods=["GET","POST"])
def even_odd():
    num=int(request.args.get('num'))
    if(num%2==0):
        return "Even"
    else:
        return "Odd"
    
@app.route("/loop", methods=["GET","POST"])
def loop_func():
    ls=[]
    s=""
    num=int(request.args.get('num'))
    for i in range(0,num):
        s=s+","+str(i)
    return s

# @app.route("/search_form", methods=["GET","POST"])
# def database_view():
#     employee_id=int(request.form['employee_id'])
#     query="select * from details where id=?"
#     data=view_data(query, employee_id)
#     return render_template('search.html', sql_query=query,data=data)

@app.route("/submit_form", methods=["GET","POST"])
def database_insert():
    employee_id=int(request.form['employee_id'])
    employee_name=str(request.form['employee_name'])
    query="INSERT INTO details (id, name) VALUES(?,?)"
    status=insert_data(query, employee_id,employee_name)
    print(status)
    return render_template('home.html', 
                           employee_id=employee_id, 
                           employee_name=employee_name, 
                           sql_query=query,
                           status=status)


import sqlite3 as sql
def insert_data(query,id,name):  
  try:
    # Connecting to database
    print("connection initiating")
    con = sql.connect('database/employee.db')
    print("connection successful")
    # Getting cursor
    c =  con.cursor() 
    print("cursor created")
    # Adding data
    c.execute(query,(id,name) )
    print("query executed")
    # Applying changes
    con.commit()
    print("query commited")
  except:
    print("An error has occured")

def view_data(query,id):  
  try:
    # Connecting to database
    print("connection initiating")
    con = sql.connect('database/employee.db')
    print("connection successful")
    # Getting cursor
    c =  con.cursor() 
    print("cursor created")
    # Adding data
    c.execute(query,id)
    rows = c.fetchall()
    print("query executed")
    return rows
  except:
    print("An error has occured")
    

# Main Driver Function 
if __name__ == '__main__':
    # Run the application on the local development server
    app.run(debug=True)