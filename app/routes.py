from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import Login

@app.route('/')
@app.route('/index')
def index():
    user = { 'username': 'Ashish' }
    return render_template('index.html', title="Some title", user=user)

@app.route('/login' ,methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        flash('Login Requested {}'.format(form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html', form=form)
