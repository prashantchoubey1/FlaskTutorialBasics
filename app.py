## Importing flask library - helps to build API in flask
from flask import Flask, g,render_template
from flask import request

## creating flask application
app = Flask(__name__)

## creating web address
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Print hi function
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
    if(request.method=="POST"):
        ls=[]
        s=""
        num=int(request.args.get('num'))
        for i in range(0,num):
            s=s+","+str(i)
        return s
    else:
       return "No data"

@app.route("/search_form", methods=["GET","POST"])
def database_view():
    if(request.method=="POST"):
        employee_id=int(request.form['employee_id'])
        query="select * from details where id=?"
        data=view_data(query, employee_id)
        return render_template('search.html',data=data)
    else:
       return render_template('search.html')


@app.route("/submit_form", methods=["GET","POST"])
def database_insert():
    if(request.method=="POST"):
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
    else:
       return render_template('home.html')


import sqlite3 as sql
def connect_db():
   # Connecting to database
    print("connection initiating")
    con = sql.connect('database/employee.db')
    print("connection successful")
    # Getting cursor
    c =  con.cursor() 
    print("cursor created")
    return c

def insert_data(query,id,name):  
  try:
    #connect db
    c=connect_db()
    # Adding data
    c.execute(query,(id,name) )
    print("query executed")
    # Applying changes
    c.commit()
    print("query commited")
  except:
    print("An error has occured")

def view_data(query,id):  
  try:
    con=connect_db()
    # Adding data
    g.db = con
    cur = g.db.execute(query, [id])
    data = [dict(id=row[0], name=row[1]) for row in cur.fetchall()]
    g.db.close()
    return data
  except:
    print("An error has occured")


# Main Driver Function 
if __name__ == '__main__':
    # Run the application on the local development server
    app.run(debug=True)