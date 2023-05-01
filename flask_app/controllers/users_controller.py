from flask import session, render_template, request, redirect
from flask_app import app
from pprint import pprint
from flask_app.models.users_model import User
from flask_app.models import cars_model

# homepage including registration form and login
@app.route('/')
def display_login_registration():
    return render_template('index.html')

# page used to collect, validate, and transfer new user info
@app.route('/process', methods=['POST'])
def register_user():
    new_user = {
        **request.form
    }
    data = {
        'email' : request.form['email']
    }
    if User.check_email(data) == False:
        return redirect( "/" )
    if User.validate_user( new_user ) == False:
        return redirect( "/" )
    else:
        new_user['password'] = User.encrypt_string(new_user['password'])
        user_id = User.create_one( new_user )
        session['user_id'] = user_id
        session['first_name'] = new_user['first_name']
        return redirect( '/my_garage' )
    
# page to check for login credentials
@app.route('/login', methods=['POST'])
def login():
    data = {
        'email' : request.form['email']
    }
    current_user = User.get_one_by_email(data)
    if current_user == None:
        return redirect('/')
    else:
        if User.validate_password(request.form['password'], current_user.password) == False:
            return redirect('/')
        else:
            session['user_id'] = current_user.id
            session['first_name'] = current_user.first_name
            return redirect('/my_garage')

# user logged in and displays garage
@app.route('/my_garage', methods=['POST', 'GET'])
def user():
    if "user_id" not in session:
        return redirect('/smart@$$')
    data = {
        'user_id':session['user_id']
    }
    list_of_cars = cars_model.Car.get_all_cars_by_user(data)
    return render_template('my_garage.html', list_of_cars = list_of_cars)

# research page for comps
@app.route('/research')
def research():
    if "user_id" not in session:
        return redirect('/smart@$$')
    return render_template('research.html')

# page to reset session, used for logging out
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# reroute for no session logged in
@app.route('/smart@$$')
def smart():
    return render_template('no_session.html')