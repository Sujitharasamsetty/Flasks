from flask import Flask

app= Flask(__name__)

@app.route('/')

def fun ():
    return "welcome to home page"

@app.route('/<var>')
 
def fun_1(var):
     
    return " you are on {} route ". format(var)


app.run(debug=True)