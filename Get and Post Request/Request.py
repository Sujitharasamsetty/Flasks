from crypt import methods
from flask import Flask,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])

def fun ():
    
    if request.method== 'POST' :
        
        return "This is a POST REQUEST"
    return "This is a GET REQUEST"

app.run(debug=True)
    