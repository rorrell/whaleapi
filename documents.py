import mongoengine as me


class Location(me.Document):
    _id = me.IntField(primary_key=True)
    breed = me.StringField()
    pod = me.StringField()
    date = me.DateField()
    x = me.FloatField()
    y = me.FloatField()

    def to_json(self):
        return {'_id': self._id,
                'breed': self.breed,
                'pod': self.pod,
                'date': str(self.date),
                'x': self.x,
                'y': self.y}

    def get_id(self):
        return self._id
