from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_restful import Api, Resource, reqparse

from resources.item import Item

app = Flask(__name__)
api = Api(app)

api.add_resource(Item, '/items/<string:name>')
