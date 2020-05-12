from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Netid~6313@localhost/height_collector'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://acbtlctazfbytw:b12e304d817b8cd79adc3daafbbff6db79972d4b8603d9e8e6a4842c454a3217@ec2-54-157-78-113.compute-1.amazonaws.com:5432/d2qv82r63jum92?sslmode=require'
db=SQLAlchemy(app)


class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer,primary_key=True)
    email_=db.Column(db.String(120),unique=True)
    height_=db.Column(db.Integer)

    def __init__(self,email_,height_):
        self.email_=email_
        self.height_=height_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success",methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height_name"]
        if db.session.query(Data).filter(Data.email_==email).count() == 0:
            data=Data(email,height)
            db.session.add(data)
            db.session.commit()
            avg_height=db.session.query(func.avg(Data.height_)).scalar()
            avg_height=round(avg_height,1)
            count=db.session.query(Data.height_).count()
            send_email(email,height,avg_height,count)
            return render_template("success.html")
        else:
            return render_template("index.html",text="Seems like this email is already registered!")


if __name__=='__main__':
    app.debug=True
    app.run()
