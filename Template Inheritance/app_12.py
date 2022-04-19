import re
from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')

def fun():
    
    return render_template("index.html")


@app.route('/registerpage',methods=['GET','POST'])

def fun_3():
    
    if request.method == 'POST' :
        
       Email= request.form.get('in_1')
       Password =request.fomr.get('in_2')
       
       
    return render_template("register.html")
    
    
@app.route('/about_us')

def fun_1 ():
    
    return render_template("about.html")

@app.route('/contact_us')

def fun_2 ():
    
    return render_template("context.html")

app.run(debug=True)

