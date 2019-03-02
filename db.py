from flask_sqlalchemy import SQLAlchemy


import hashlib
import os


db = SQLAlchemy()

association_table = db.Table('association',
                             db.Column('food_id', db.Integer,
                                       db.ForeignKey('user.id')),
                             db.Column('ingredient_id', db.Integer,
                                       db.ForeignKey('ingredient.id'))
                             )


class Food(db.Model):
    __tablename__ = 'food'
    id = db.Column(db.Integer, primary_key=True)
    foodname = db.Column(db.String, nullable=False)
    calory = db.Column(db.Integer, nullable=False)
    emmision_per_serve = db.Column(db.Integer,nullable = False)
    emmision_per_kcal = db.Column(db.Integer,nullable = False)
    ingredients = db.relationship('Ingredient', secondary=association_table)

    def __init__(self, **kwargs):
        self.foodname = kwargs.get('foodname', '')


    def calc_values(self):
        cal = 0
        emi_1 = 0
        emi_2 = 0
        for ingre in ingredients:
            cal = cal+ingre.cal_per_serve
            emi_1 += ingre.emmision_per_serve
            emi_2 += ingre.emmision_per_kcal
        self.calory = cal
        self.emmision_per_serve = emi_1
        self.emmision_per_kcal = emi_2

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'cal_per_serve' = self.cal_per_serve,
            'emmision_per_serve': self.emmision_per_serve,
            'emmision_per_kcal': self.emmision_per_kcal
        }



class Ingredient(db.Model):
    __tablename__ = 'ingredient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, default=0)
    cal_per_serve = db.Column(db.Integer,nullable = False)
    emmision_per_serve = db.Column(db.Integer,nullable = False)
    emmision_per_kcal = db.Column(db.Integer,nullable = False)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.cal_per_serve = kwargs.get('cal_per_serve', '')
        self.emmision_per_serve = kwargs.get('emmision_per_serve', '')
        self.emmision_per_kcal = kwargs.get('emission_per_kcal', '')

        


    