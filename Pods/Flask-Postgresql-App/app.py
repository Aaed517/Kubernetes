from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField


app = Flask(__name__, template_folder='templates')

app.config['SECRET_KEY'] = 'mVXMEkIrVQVi1yyXeICN81X3xkwXpJ3q'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:passwd@postgres:5432/dbapp'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))


class userform(FlaskForm):
    Name = StringField('Name')
    Surname =  StringField('Surname')


@app.route('/',methods=["GET","POST"])
def flaskapp_main_page():
    form= userform()
    if request.method == "POST":
        if form.is_submitted():
                user_ = User(name=form.Name.data,surname=form.Surname.data)
                db.session.add(user_)
                db.session.commit()
                return redirect(url_for('flaskapp_main_page'))
    users = User.query.all()
    return render_template('FlaskAppMain.html',form=form,users=users)
