from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import requests




## write a script to return the top 50 tallest and heaviest pokemon

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class PokemonModel(db.Model):
    l_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    region = db.Column(db.String, nullable = False)
    game_index = db.Column(db.String, nullable = False)

    def __repr__(self):
        return f"Pokemon(name = {name}, views = {view}, likes= {likes})"

pokemon_args = reqparse.RequestParser()
pokemon_args.add_argument("name", type = str, help = "Name is required", required = True)
pokemon_args.add_argument("region", type = str, help = "Type is required", required = True)
pokemon_args.add_argument("game_index", type = int, help = "power level is required", required = True)

db.create_all()



# @app.route("/pokemon/<int:id>")
# def get_location(id):
#     url = "https://pokeapi.co/api/v2/location/" + str(id)
#     print(url)
#     r = requests.get(url).json()
#     return r


# # def post_location("")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'region': fields.String,
    'game_index': fields.Integer

}



class Pokemon_locations(Resource):

    def get_process_store(id):
        return

    def get_location(id):
        url = url = "https://pokeapi.co/api/v2/location/" + str(id)
        print(url)
        r = requests.get(url).json()
        return r


    @marshal_with(resource_fields)
    def post(self, id):
        args = pokemon_args.parse_args()
        loc = PokemonModel(l_id = id, name = args["name"], region = args["region"], game_index = args["game_index"])
        db.session.add(loc)
        db.session.commit()
        return loc, 201





api.add_resource(Pokemon_locations, "/location/<int:id>")



if __name__ == "__main__":
    app.run(debug=True)
