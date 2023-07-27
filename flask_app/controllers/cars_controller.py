import os
from flask import session, render_template, request, redirect, flash
from flask_app import app
from pprint import pprint
from flask_app.models.cars_model import Car
from werkzeug.utils import secure_filename
from flask_app.models.files_model import FileTest

# image asset folder directory and extension settings(add more as needed)
UPLOAD_FOLDER = 'flask_app\\static\\img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = { 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif' }

# function to check file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# add a car form
@app.route('/garage/add')
def add_a_car():
    if "user_id" not in session:
        return redirect('/smart@$$')
    return render_template('add_car.html')

# page to validate, collect, and transfer NEW car data
@app.route('/garage/process', methods=['POST'])
def process_car():
    # check if the post request has a file part
    if 'file' not in request.files:
        flash('No file part')
        filename = 'none'
        

    # if file part exists in form, save to variable
    file = request.files['file']

    # if the user does not select a file, browser submits an empty part without filename
    if file.filename == '':
        flash('No selected file')
        filename = 'none'

    # if valid file submitted, save into local folder (does *NOT* save in database!)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        # saves the image into the static/img folder
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    if filename == 'none':
        new_car = {
            'user_id' : session['user_id'],
            'year' : request.form['year'],
            'make' : request.form['make'],
            'model' : request.form['model'],
            'trim' : request.form['trim'],
            'color' : request.form['color'],
            'vin' : request.form['vin'],
            'description' : request.form['description'],
            'file_name' : ''
        }
    else:
        new_car = {
            'user_id' : session['user_id'],
            'year' : request.form['year'],
            'make' : request.form['make'],
            'model' : request.form['model'],
            'trim' : request.form['trim'],
            'color' : request.form['color'],
            'vin' : request.form['vin'],
            'description' : request.form['description'],
            'file_name' : filename
        }
    car_id = Car.create_one(new_car)
    return redirect('/my_garage')

# edit a single selected car info form
@app.route('/garage/<int:id>/edit')
def display_edit_car_form(id):
    if "user_id" not in session:
        return redirect('/smart@$$')
    data = {
        'id':id
    }
    current_car = Car.get_one(data)
    return render_template('update_car.html', current_car = current_car)

# process the update of a car
@app.route('/garage/<int:id>/update', methods=['POST'])
def update_car(id):
    # check if the post request has a file part
    if 'file' not in request.files:
        flash('No file part')
        filename = 'none'

    # if file part exists in form, save to variable
    file = request.files['file']

    # if the user does not select a file, browser submits an empty part without filename
    if file.filename == '':
        flash('No selected file')
        filename = 'none'

    # Get the current file name from the database for the car being updated
    current_car = Car.get_one(id)
    current_file_name = current_car.file_name if current_car else ''

    # if valid file submitted, save into local folder (does *NOT* save in database!)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        # saves the image into the static/img folder
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    else:
        filename = current_file_name

    # Prepare the data for updating the car
    data = {
        'id': id,
        'year': request.form['year'],
        'make': request.form['make'],
        'model': request.form['model'],
        'trim': request.form['trim'],
        'color': request.form['color'],
        'vin': request.form['vin'],
        'description': request.form['description'],
        'file_name': filename,
        'user_id': session['user_id']
    }

    # Update the car using the prepared data
    Car.update_one(data)

    return redirect('/my_garage')


# process the selling of a car
@app.route('/garage/<int:id>/sold', methods=['POST', 'GET'])
def sold_car(id):
    data = {
        'id': id
    }
    Car.sold_one(data)
    return redirect('/my_garage')