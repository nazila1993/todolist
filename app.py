from flask import Flask, render_template, redirect, url_for, request
import mongoengine as me
import yaml 
from settings import DB

me.connect(host=DB)


class Task(me.Document):
    title = me.StringField()
    priority = me.IntField()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/tasks/')
def tasks():
  
     data = dict(
         tasks=Task.objects, 
         )
     return render_template("tasks.html", data=data)

@app.route('/rm/<string:_id>/')
def remove(_id):
    Task.objects.get(id=_id).delete()
    return redirect(url_for('tasks'))

@app.route('/new/', methods=['Post'])
def new():
    Task(
        title=request.form.get("title"),
        priority=request.form.get("priority")
     ).save()
    return redirect(url_for('tasks'))

@app.route("/cv/")
def cv():
    with open('data.yaml') as f:
        data = yaml.safe_load(f)
    return render_template('cv.html', data=data)

    




