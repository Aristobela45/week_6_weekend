from flask import Blueprint, render_template, request, print, redirect, url_for
from marvel_collection.forms import addMarvel
from marvel_collection.models import User, Character, db
from flask_login import login_required, current_user

site = Blueprint('site',__name__,template_folder='site_templates')

@site.route('/home')
def home():
    return render_template('index.html')

@site.route('/collection')
def collection():
    return render_template('collection.html')

@site.route('/collection/add', methods = ['GET','POST'])
@login_required
def addcharacter():
    form = addMarvel()
    
    try:
        if request.method == 'POST' and form.validate_on_submit():
            name = form.name.data
            description = form.description.data
            comics_appeared_in = form.comics_appeared_in.data
            super_power = form.super_power.data
            user_token = current_user.token
            print("Character: ", name, description, comics_appeared_in, super_power)
            print("For User #", user_token)

            character = Character(name = name, description = description, comics_appeared_in = comics_appeared_in, super_power = super_power, user_token = user_token)

            logged_user = User.query.filter(User.token == user_token).first()

            if logged_user:
                db.session.add(character)
                db.session.commit()
                print(f"The character have successfully added {character.name} to {logged_user.name}'s Collection!", 'add-success')
                return redirect(url_for('site.addcharacter'))
            else:
                print('Please enter valid token', 'token-failed')
                
            return redirect(url_for('site.addcharacter'))
    except:
        raise Exception('Invalid: Please Check Your Form')

    return render_template('add.html', form = form)

@site.route('/site profile')
@login_required
def profile():
    logged_user = User.query.filter(User.token == current_user.token).first()
    usercollection = Character.query.filter(Character.user_token == logged_user.token).all()
    return render_template('profile.html', entries = usercollection)