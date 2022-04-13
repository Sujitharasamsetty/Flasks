from distutils.log import debug
from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')

def fun_1():
    return render_template('index.html')

@app.route('/about')

def fun_2():
    
    # we dont know how to fetch data from database
    # So,we will store something inside a variable
    
   # vegatables_list = ['Aloo','Mushrooms','Bindi','lemon']
    
    vegetables_dict = {'Aloo' :30,'Mushrooms':100,'Bindi':40,'lemon':200}
    return render_template('about_us.html',input = vegetables_dict)


app.run(debug=True)