from crypt import methods
from flask import Flask,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])

def fun ():
    
    if methods == 'GET' :
        
        return "This is a GET REQUEST"
    return "This is a POST REQUEST"

app.run(debug=True)
    