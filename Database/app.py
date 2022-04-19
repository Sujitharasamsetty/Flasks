import os
from flask import Flask, render_template,request
from flask_sqlalchemy  import SQLAlchemy
from flask_migrate import Migrate
from sklearn.tree import BaseDecisionTree
import sqlalchemy

app=Flask(__name__)


############################## SQL ALCHAMEY CONFIGURATION #############################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHAMEY_DATABASE_URI'] = 'sqlite:/// '+ os.path.join(basedir,'data.sqlite')
app.config['SQLALCHAMEY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
Migrate(app,db)

################################### Create Model #######################################

class sabji(db.Model):
    
    ___tablename__ = "sabjis"
    id=db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    mrp=db.Column(db.Integer)
    
    def __init__(self,name,mrp) :
        
        self.name = name
        self.mrp = mrp
        
    def __repr__(self):
        
       return "Sabji name - {} and mrp - {}".format(self.name,self.mrp)
        
    
    



#############################################################################################
@app.route('/')

def index():
    return render_template("index.html")

@app.route('/add',methods=['GET','POST'])

def add ():
    
    if request.method == 'POST' :
        
        name=request.form.get('in_1')
        mrp=request.form.get('in_2')
        new_sabji = sabji(name.mrp)
        db.session.add(new_sabji)
        db.session.commit()
        
    return render_template("add.html")

@app.route('/search')

def search():
     return render_template("search.html")
 
@app.route('/display')

def display():
     return render_template("display.html")
 
app.run(debug=True)
