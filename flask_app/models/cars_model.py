from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from pprint import pprint
from flask_app.models import users_model

class Car:
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.year = data['year']
        self.make = data['make']
        self.model = data['model']
        self.trim = data['trim']
        self.color = data['color']
        self.vin = data['vin']
        self.description = data['description']
        self.file_name = data['file_name']
        self.sold = data['sold']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    # adds a single car to the database
    @classmethod
    def create_one(cls,data):
        query = """
            INSERT INTO cars (user_id, year, make, model, trim, color, vin, description, file_name)
            VALUES (%(user_id)s, %(year)s, %(make)s, %(model)s, %(trim)s, %(color)s, %(vin)s, %(description)s, %(file_name)s);
        """
        print("create_one")
        return connectToMySQL( DATABASE ).query_db( query, data )
    
    # grabs all cars currently under the logged in user
    @classmethod
    def get_all_cars_by_user(cls, data):
        query = """
            SELECT *
            FROM cars c JOIN users u
            ON u.id = c.user_id
            WHERE c.user_id = %(user_id)s;
        """
        result = connectToMySQL( DATABASE ).query_db( query,data )
        list_of_cars = []

        for row in result:
            current_car = cls(row)
            user = {
                'id': row['u.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['u.created_at'],
                'updated_at': row['u.updated_at']
            }
            current_user = users_model.User(user)
            current_car.user = current_user
            list_of_cars.append(current_car)
        return list_of_cars

    # gets a single car, used for update form
    @classmethod
    def get_one(cls, data):
        query = """
            SELECT *
            FROM cars
            WHERE id = %(id)s;
        """
        if isinstance(data, int):  # Check if data is just the id
            data = {'id': data}

        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0]) if result else None  # Return None if no car is found


    # updates a single car in the database
    @classmethod
    def update_one( cls, data ):
        query  = """
            UPDATE cars
            SET user_id = %(user_id)s,
                year = %(year)s,
                make = %(make)s,
                model = %(model)s,
                trim = %(trim)s,
                color = %(color)s,
                vin = %(vin)s,
                description = %(description)s,
                file_name = %(file_name)s
            WHERE id = %(id)s;
        """
        return connectToMySQL( DATABASE ).query_db( query, data )

    # marks sold boolean in the cars table to TRUE by setting to 1
    @classmethod
    def sold_one( cls, data ):
        query  = """
            UPDATE cars
            SET sold = 1
            WHERE id = %(id)s;
        """
        return connectToMySQL( DATABASE ).query_db( query, data )

    # JSON API
    @classmethod
    def api_get_all(cls):
        query = """
            SELECT *
            FROM cars;
        """
        print("api_get_all")
        return connectToMySQL( DATABASE ).query_db( query )
