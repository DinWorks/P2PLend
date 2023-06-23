
from flask import Flask, jsonify
from flask_graphql import GraphQLView
from .models import Message 
from database import db
from schema import schema


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://chroxmxwwrnpsc:0a5d1f66b55416e48b18e2ee701a0434ab257d65c2315571e878afc754418167@ec2-18-205-44-21.compute-1.amazonaws.com:5432/d586kgmbr7n0rk"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all() 

@app.route('/')
def hello_world():
   return 'Hello World!'

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True 
    )
)

if __name__ == '__main__':
    app.run(debug=True)