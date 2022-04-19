from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')

def fun ():
    
    return render_template ("index.html")

@app.route('/about_us')

def fun_1 ():
    
    return render_template ("about.html")

@app.route('/contact_us')

def fun_2 ():
    
    return render_template("contact.html")


app.run(debug=True)