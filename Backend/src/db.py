from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String, nullable=False)
    persona = db.Column(db.String, nullable = False)
    emission = db.Column(db.String, nullable = False)
    chain_id = db.Column(db.Integer, db.ForeignKey(supplychain.id),nullable = False)

    def __init__(self, **kwargs):
        self.username = kwargs.get('username','')
        self.persona = kwargs.get('persona','')
        self.emission = kwargs.get('emission','')
        self.chain_id = kwargs.get('chain_id','')

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'persona': self.persona,
            'chain_id': self.chain_id
        }


class Supplychain(db.Model):
    __tablename__ = 'supplychain'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, default=0)
    current_owner = db.Column(db.String, default=0)
    total_emission = db.Column(db.Integer, nullable=False)
    stops = db.relationship('Stop')
    


    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')


    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'current_owner' : self.current_owner,
            'total_emission': self.total_emission
        }
