from flask import session, render_template, request, redirect
from flask_app import app
from pprint import pprint
from flask_app.models.cars_model import Car

# add a car form
@app.route('/garage/add')
def add_a_car():
    return render_template('add_car.html')

# page to validate, collect, and transfer NEW car data
@app.route('/garage/process', methods=['POST'])
def process_car():
    new_car = {
        'user_id' : session['user_id'],
        'year' : request.form['year'],
        'make' : request.form['make'],
        'model' : request.form['model'],
        'trim' : request.form['trim'],
        'color' : request.form['color'],
        'vin' : request.form['vin'],
        'description' : request.form['description']
    }
    car_id = Car.create_one(new_car)
    return redirect('/my_garage')

# edit a single selected car info form
@app.route('/garage/<int:id>/edit')
def display_edit_car_form(id):
    data = {
        'id':id
    }
    current_car = Car.get_one(data)
    return render_template('update_car.html', current_car = current_car)

# process the update of a car
@app.route('/garage/<int:id>/update', methods=['POST'])
def update_car(id):
    data = {
        'id': id,
        **request.form,
        'user_id':session['user_id']
    }
    Car.update_one(data)
    return redirect('/my_garage')

# process the selling of a car
@app.route('/garage/<int:id>/sold', methods=['POST'])
def sold_car(id):
    data = {
        'id': id
    }
    Car.sold_one(data)
    return redirect('/my_garage')