from flask import Blueprint, render_template, redirect, url_for, flash
from auth.forms import SignupForm
from __init__ import db
from auth.models import User


auth = Blueprint('auth', __name__, template_folder='auth_templates')



@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('auth.login'))  
    return render_template('signup.html', form=form)