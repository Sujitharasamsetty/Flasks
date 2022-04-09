from flask import Flask , render_template

app= Flask(__name__)

@app.route('/')

def fun():
    return render_template("index.html")

@app.route('/<var>')


def fun_1(var):
    
    return render_template("user.html" , input = var)



app.run(debug=True)