from flask import render_template, url_for, redirect, flash
from workout_tracker.forms import AddForm
from workout_tracker.models import Post
from workout_tracker import app, db
from sqlalchemy import desc

@app.route("/", methods = ['GET','POST'])
@app.route("/home", methods = ['GET','POST'])
def home():
    form = AddForm()
    if form.validate_on_submit():
        post = Post(exercise=form.exercise.data, weight=form.weight.data, category=form.category.data)

        db.session.add(post) 
        db.session.commit()
        flash('Success')
        return redirect(url_for('home'))  
    #posts = Post.query.filter_by(weight = 20)
    #posts = Post.query.order_by('date_posted').limit(1)  
    posts = Post.query.group_by('exercise').order_by(desc('date_posted'))
    #posts = Post.query.all()  
    return render_template('home.html', posts=posts, form=form)

@app.route("/home/delete/<int:post_id>", methods = ['POST'])
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash("Deleted")
    return redirect(url_for('home'))

@app.route("/stats/<string:exercise>")
def stats(exercise):
    #posts = Post.query.all()  
    posts = Post.query.filter_by(exercise = exercise)

    return render_template('stats.html', legend = exercise, posts=posts)

@app.route("/stats/chart/<string:exercise>")
def exchart(exercise):
    #labels = Post.query.all()
    #labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    #values = labels = Post.query.all()
    results = Post.query.filter_by(exercise = exercise)
    #if results > 0:
    dates = []
    weights = []
    for result in results: 
        x = int(result.date_posted.strftime('%d%m%Y'))
        y = result.weight
        dates.append(x)
        dates.sort()
        #Hvorfor matches ikke weight med date? 
        weights.append(y)
    print(weights)
    print(dates)
    return render_template('chart.html', dates = dates, weights = weights, legend=exercise)
    #else:
     #   msg = 'No data'
      #  return render_template('chart.html', msg = msg)



@app.route("/stats/chart")
def chart():
    legend = 'Monthly Data'
    #labels = Post.query.all()
    #labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    #values = labels = Post.query.all()
    results = Post.query.all()

    #if results > 0:
    dates = []
    weights = []
    for result in results: 
        #x = result.date_posted.strftime('%d')
        x = int(result.date_posted.strftime('%d%m%Y'))
        #x = result.exercise
        y = result.weight
        dates.append(x)
        weights.append(y)
    print(weights)
    print(dates)
    return render_template('chart.html', dates = dates, weights = weights, legend=legend)
    #else:
     #   msg = 'No data'
      #  return render_template('chart.html', msg = msg)