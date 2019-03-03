import json
import re
from db import db, Stop, Supplychain
from flask import Flask, request
import helpers

db_filename = "todo.db"
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def hello_world():
    return json.dumps({'message': 'Hello, World!'})


@app.route('/api/')
def hello_world_again():
    return json.dumps({'message': 'Hello, World!'})


@app.route('/api/<int:id>/change/', methods=['POST'])
def post_test_events(id):
    chain = Supplychain.query.filter_by(id = id).first()
    if chain is not None:
        post_body = json.loads(request.data)
        name = post_body.get('username')
        persona = post_body.get('persona')
        emission = helpers.calc_emission(persona)
        stop = Stop(username = name, persona = persona, emission = emission, chain_id = id)
        chain.stops.append(stop)
        chain.total_emission = chain.total_emission + emission
        chain.current_owner = name
        db.session.add(stop)
        db.session.commit()
        return json.dumps({'success': True, 'data': stop.serialize()})
    else:
        return json.dumps({'success': False, 'error': 'No chain found'}), 404


@app.route('/api/create/',methods = ['POST'])
def create_link():
    post_body = json.loads(request.data)
    name = post_body.get('username')
    persona = post_body.get('persona')
    emission = helpers.calc_emission(persona)
    if persona != 'Farmer/Producer':
        return json.dumps({'success': False, 'error': 'you cannot initiate a chain'}), 404
    else:
        chain = Supplychain(name = 'tomato')
        db.session.add(chain)
        db.session.commit()
        stop = Stop(username = name, persona = persona, emission = emission, chain_id = chain.id)
        chain.current_owner = stop.username
        chain.total_emission = chain.total_emission + emission
        db.session.add(stop)
        db.session.commit()
        return json.dumps({'success': True,'Supplychain': chain.id})

    
@app.route('/api/<int:id>/',methods = ['GET'])
def display(id):
    chain = Supplychain.query.filter_by(id = id).first()
    if chain is not None:
        return json.dumps({'success': True, 'data': [stop.serialize() for stop in chain.stops],'total_emission':chain.total_emission})
    else:
        return json.dumps({'success': False, 'error': 'No chain found'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
