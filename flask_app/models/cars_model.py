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

    @classmethod
    def create_one(cls,data):
        query = """
            INSERT INTO cars (user_id, year, make, model, trim, color, vin, description, file_name)
            VALUES (%(user_id)s, %(year)s, %(make)s, %(model)s, %(trim)s, %(color)s, %(vin)s, %(description)s, %(file_name)s);
        """
        return connectToMySQL( DATABASE ).query_db( query, data )
    
    @classmethod
    def get_all_cars_by_user(cls):
        query = """
            SELECT *
            FROM cars c JOIN users u
            On u.id = c.user_id;
        """
        result = connectToMySQL( DATABASE ).query_db( query )
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

    @classmethod
    def get_one( cls, data ):
        query  = """
            SELECT *
            FROM cars
            WHERE id = %(id)s;
        """
        result = connectToMySQL( DATABASE ).query_db( query, data )
        return cls( result[0] )

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

    @classmethod
    def sold_one( cls, data ):
        query  = """
            UPDATE cars
            SET sold = 1
            WHERE id = %(id)s;
        """
        return connectToMySQL( DATABASE ).query_db( query, data )

    @classmethod
    def api_get_all(cls):
        query = """
            SELECT *
            FROM cars;
        """
        return connectToMySQL( DATABASE ).query_db( query )
