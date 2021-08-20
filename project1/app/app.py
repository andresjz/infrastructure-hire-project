# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api
import os

app = Flask(__name__)
api = Api(app)

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', '')
AWS_DEFAULT_REGION = os.getenv('AWS_DEFAULT_REGION', '')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME', '')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world',
        'variables': AWS_ACCESS_KEY_ID + AWS_SECRET_ACCESS_KEY + AWS_DEFAULT_REGION + AWS_BUCKET_NAME
        }

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')