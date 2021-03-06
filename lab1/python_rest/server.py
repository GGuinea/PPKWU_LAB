from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify


app = Flask(__name__)
api = Api(app)

class RevService(Resource):
    def get(self, inputString):
        result = {'data': inputString[::-1]}
        return jsonify(result)

api.add_resource(RevService, '/rev/<inputString>')

if __name__ == '__main__':
    app.run(port='25000')
