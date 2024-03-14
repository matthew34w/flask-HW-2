from flask import Blueprint, render_template

auth = Blueprint('cars', __name__, template_folder='car_templates')