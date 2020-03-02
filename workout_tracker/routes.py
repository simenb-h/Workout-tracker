from flask import render_template, url_for, redirect, flash, request
from workout_tracker.forms import AddForm, RegistrationForm, LoginForm, UpdateForm
from workout_tracker.models import Post, User
from workout_tracker import app, db, bcrypt
from sqlalchemy import desc, text
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/", methods = ['GET','POST'])
@app.route("/home", methods = ['GET','POST'])
def home():
    if current_user.is_authenticated:
        form = AddForm()
        if form.validate_on_submit():
            post = Post(exercise=form.exercise.data, weight=form.weight.data, category=form.category.data, author = current_user)
            db.session.add(post) 
            db.session.commit()
            flash('Success', 'success')
            return redirect(url_for('home'))
        #posts = Post.query.filter_by(author = current_user).group_by('exercise').order_by(desc('date_posted'))
        posts = Post.query.filter_by(author = current_user).order_by(desc('date_posted'))
        return render_template('home.html', posts=posts, form=form)
    else:
        return redirect(url_for('login'))

@app.route("/<string:exercise>/<string:category>")
def add(exercise, category):
    form = AddForm()
    post = Post(exercise=exercise, weight=form.weight.data, category=category, author = current_user)
    db.session.add(post) 
    db.session.commit()
    flash('Successful update', 'success')
    return redirect(url_for('home'))

    
@app.route("/register", methods=['GET', 'POST'])
def register():
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        form = RegistrationForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username = form.username.data,email=form.email.data, password = hashed_password)
            db.session.add(user) 
            db.session.commit()
            flash('Success', 'success')
            return redirect(url_for('login'))  
        return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
               
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/home/delete/<int:post_id>", methods = ['POST'])
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash("Deleted", 'danger')
    return redirect(url_for('home'))

@app.route("/home/stats/<int:post_id>", methods = ['POST'])
def stat_delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash("Deleted",'danger')
    return redirect(url_for('stats', exercise=post.exercise ))


@app.route("/stats/<string:exercise>")
def stats(exercise):
    #posts = Post.query.all()  
    posts = Post.query.filter_by(exercise = exercise)
    return render_template('stats.html', legend = exercise, posts=posts)

@app.route("/stats/chart/<string:exercise>")
def exchart(exercise):
    results = Post.query.filter_by(exercise = exercise)
    if results > 0:
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
    else:
        msg = 'No data'
        return render_template('chart.html', msg = msg)


