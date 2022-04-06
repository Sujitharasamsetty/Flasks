from atexit import register
from flask import Flask

app = Flask(__name__)

registered_users=['Suji','Veda','Seku','Mom']

@app.route('/')

def home():
    return "Welcome Home Page"


'''@app.route('/in/Suji')

def fun_user_1():
    return "Welcome {} !".format(registered_users[0])

@app.route('/in/veda')

def fun_user_2():
    return "Welcome {} !".format(registered_users[1])

@app.route('/in/Seku')

def fun_user_3():
    return "Welcome {} !".format(registered_users[2])

@app.route('/in/Mom')

def fun_user_4():
    return "Welcome {} !".format(registered_users[3])

app.run()'''


@app.route('/in/<user_name>')

def user_details(user_name):
    
    if user_name in registered_users :
        
        return "Welcome {} !".format(user_name)
    
    else:
        
        return "Normusukoni.Velli Register Chesuko"
    
app.run(debug=True)


