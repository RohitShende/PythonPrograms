from flask import Flask, url_for, jsonify, request, abort

app = Flask(__name__)
app.config['DEBUG'] = True

pokemons = {}


@app.route("/")
def hello_world():
    return f"""<h1>Hello, Pokemon Fans!</h1> <br><br>
    <b>GET</b> - For getting Pokemon by ID - {url_for('get', pokemon_id=1)} <br>
    <b>POST</b> - For creating / adding a new Pokemon - {url_for('post', pokemon_id=1)} <br>
    <b>PUT</b> - For updating / changing an existing Pokemon - {url_for('put', pokemon_id=1)} <br>
    <b>PATCH</b> - For updating / changing an existing Pokemon - {url_for('patch', pokemon_id=1)} <br>
    <b>DELETE</b> - For deleting an existing Pokemon - {url_for('delete', pokemon_id=1)} <br>
    <b>GET</b> - For getting all Pokemons - {url_for('get_all')} <br>"""


@app.route('/pokemon/<int:pokemon_id>', methods=["GET"])
def get(pokemon_id):
    if pokemon_id in pokemons:
        return jsonify(pokemons[pokemon_id]), 200
    else:
        return jsonify({"message": "Not Found"}), 404


@app.route('/pokemons')
def get_all():
    return jsonify(pokemons), 200


@app.route('/pokemon/<int:pokemon_id>', methods=["POST"])
def post(pokemon_id):
    if pokemon_id in pokemons:
        return jsonify({"message": f"Pokemon Already Exists with id {pokemon_id}"}), 500
    else:
        data = request.get_json()
        print(data)
        pokemons[pokemon_id] = data
        return jsonify({"message": "Pokemon Added !"}), 201


@app.route('/pokemon/<int:pokemon_id>', methods=["PUT"])
def put(pokemon_id):
    if pokemon_id in pokemons:
        data = request.get_json()
        print(data)
        pokemons[pokemon_id] = data
        return jsonify({"message": f"Updated Pokemon {pokemon_id}"}), 200
    else:
        return jsonify({"message": "Not Found"}), 404


@app.route('/pokemon/<int:pokemon_id>', methods=["DELETE"])
def delete(pokemon_id):
    if pokemon_id in pokemons:
        del pokemons[pokemon_id]
        return jsonify({"message": f"Deleted Pokemon {pokemon_id}"}), 200
    else:
        return jsonify({"message": "Not Found"}), 404


@app.route('/pokemon/<int:pokemon_id>', methods=["PATCH"])
def patch(pokemon_id):
    if pokemon_id in pokemons:
        data = request.get_json()
        print(data)
        for k, v in data.items():
            pokemons[pokemon_id][k] = v
        return jsonify({"message": f"Updated Pokemon {pokemon_id} with partial data"}), 200
    else:
        return jsonify({"message": "Not Found"}), 404


if __name__ == '__main__':
    app.run(host='localhost', port=9000)
