
from flask import Flask,render_template , request

app=Flask(__name__)


@app.route("/")

def fun_1():
    return render_template("index.html")


'''@app.route('/thankyou')

def fun_2():
    return "Thanks For Registering (GET)"


@app.route('/thankyou',methods=['POST'])

def fun_3():
    return "Thanks For Regsitering (POST)" '''
    
    
    
@app.route('/thankyou' ,methods= ['GET','POST'])

def fun_2():
    
    if request.method == 'GET' :
        return "Thanks For Registering (GET)"
    return "Thanks For Registering (POST)"
        



app.run(debug=True)