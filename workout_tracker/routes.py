from flask import render_template, url_for, redirect, flash
from workout_tracker.forms import AddForm
from workout_tracker.models import Post
from workout_tracker import app, db

@app.route("/", methods = ['GET','POST'])
@app.route("/home", methods = ['GET','POST'])
def home():
    form = AddForm()
    if form.validate_on_submit():
        post = Post(exercise=form.exercise.data, weight=form.weight.data)
        db.session.add(post) 
        db.session.commit()
        flash('Success')
        return redirect(url_for('home'))  
    posts = Post.query.all()  
    return render_template('home.html', posts=posts, form=form)
