from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine
import resources

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'whales',
    'host': '127.0.0.1',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)
api = Api(app)

api.add_resource(resources.Locations, '/locations')
api.add_resource(resources.Locations2, '/locations/v2')
api.add_resource(resources.Locations2ById, '/locations/v2/<int:id>')


if __name__ == '__main__':
    app.run()  # run our Flask app
