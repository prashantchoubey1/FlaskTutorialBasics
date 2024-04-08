## Importing flask library - helps to build API in flask
from flask import Flask

## creating flask application
app = Flask(__name__)

## creating web address
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hi")
def abc():
    return "<p>hello guddu</p>"

from flask import request
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
    

# Main Driver Function 
if __name__ == '__main__':
    # Run the application on the local development server
    app.run(debug=True)