#!/usr/bin/python

from flask import Flask
from flask_restful import Resource, Api, fields, marshal_with, reqparse
import hue

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('on', type=bool)
parser.add_argument('saturation', type=int)
parser.add_argument('value', type=int)
parser.add_argument('hue', type=int)

light = hue.get_corner_light()

resource_fields = {
    'name': fields.String,
    'on': fields.Boolean,
    'saturation': fields.Integer,
    'value': fields.Integer(attribute='brightness'),
    'hue': fields.Integer
}

class Light(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return light

    @marshal_with(resource_fields)
    def post(self):
        args = parser.parse_args()
        if(args['on'] != None):
            light.on = args['on']
        if(args['saturation'] != None):
            light.saturation = args['saturation']
        if(args['value'] != None):
            light.brightness = args['value']
        if(args['hue'] != None):
            light.hue = args['hue']
        return light

api.add_resource(Light, '/api/')

if __name__ == '__main__':
    app.run(debug=True)