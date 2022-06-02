from flask_restful import Resource, reqparse
import pandas as pd
from documents import Location


class Locations(Resource):
    def get(self):
        data = pd.read_csv('locations.csv')
        data = data.to_dict('records')
        return data, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, location='args', required=True)
        parser.add_argument('breed', type=str, location='args', required=True)
        parser.add_argument('pod', type=str, location='args', required=True)
        parser.add_argument('date', type=str, location='args', required=True)
        parser.add_argument('x', type=str, location='args', required=True)
        parser.add_argument('y', type=str, location='args', required=True)
        args = parser.parse_args()

        new_data = pd.DataFrame([{
            'id': args['id'],
            'breed': args['breed'],
            'pod': args['pod'],
            'date': args['date'],
            'x': args['x'],
            'y': args['y']
        }])
        data = pd.read_csv('locations.csv')

        if args['id'] in list(data['id']):
            return {
                'message': f"'{args['id']}' already exists."
            }, 401

        data = data.append(new_data)
        data.to_csv('locations.csv', index=False)
        return data.to_dict('records'), 200

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, location='args', required=True)
        args = parser.parse_args()

        data = pd.read_csv('locations.csv')

        if args['id'] not in list(data['id']):
            return {
                'message': f"'{args['id']}' not found."
            }, 404

        data = data[data['id'] != args['id']]

        data.to_csv('locations.csv', index=False)
        return data.to_dict('records'), 200


class Locations2(Resource):
    def get(self):
        locs = []
        for loc in Location.objects:
            locs.append(loc.to_json())
        return locs, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, location='args', required=True)
        parser.add_argument('breed', type=str, location='args', required=True)
        parser.add_argument('pod', type=str, location='args', required=True)
        parser.add_argument('date', type=str, location='args', required=True)
        parser.add_argument('x', type=float, location='args', required=True)
        parser.add_argument('y', type=float, location='args', required=True)
        args = parser.parse_args()

        id_exists = False
        for loc in Location.objects:
            if loc.get_id() == args['id']:
                id_exists = True
                break

        if id_exists:
            return {
                'message': f"'{args['id']}' already exists."
            }, 401

        loc = Location(_id=args['id'],
                       breed=args['breed'],
                       pod=args['pod'],
                       date=args['date'],
                       x=args['x'],
                       y=args['y'])
        loc.save()
        return loc.to_json(), 200

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, location='args', required=True)
        parser.add_argument('breed', type=str, location='args', required=False)
        parser.add_argument('pod', type=str, location='args', required=False)
        parser.add_argument('date', type=str, location='args', required=False)
        parser.add_argument('x', type=float, location='args', required=False)
        parser.add_argument('y', type=float, location='args', required=False)
        args = parser.parse_args()

        loc = Location.objects(_id=args['id']).first()

        if not loc:
            return {
                'message': f"'{args['id']}' not found."
            }, 404

        if args['breed'] is not None:
            loc.update(breed=args['breed'])

        if args['pod'] is not None:
            loc.update(pod=args['pod'])

        if args['date'] is not None:
            loc.update(date=args['date'])

        if args['x'] is not None:
            loc.update(x=args['x'])

        if args['y'] is not None:
            loc.update(y=args['y'])

        loc.reload()
        return loc.to_json(), 200

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, location='args', required=True)
        args = parser.parse_args()

        loc = Location.objects(_id=args['id']).first()

        if not loc:
            return {
                'message': f"'{args['id']}' not found."
            }, 404

        loc.delete()

        locs = []
        for loc in Location.objects:
            locs.append(loc.to_json())
        return locs, 200


class Locations2ById(Resource):
    def get(self, id):
        loc = Location.objects(_id=id).first()
        return loc.to_json(), 200
