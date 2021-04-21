from flask import Flask, jsonify, request, render_template, json
from jugadores import *
from cliente import cliente

app = Flask(__name__)

matches = []

k = 0


@app.route('/')
def hello_world():
    return 'Hello World!'


"""Lista todos los jugadores conectados"""


@app.route("/players")
def getPlayers():
    for n in range(len(players)):
        print("jugador:", players[n]["name"], "pokemons:", players[n]["pokemon"])
    return jsonify({"jugadores": players})


@app.route("/players/matches")
def seematces():
    fights = []
    for n in range(len(matches)):
        x = matchestojson(matches[n][1].get_nick(), matches[n][1].get_pokemon(),
                          matches[n][2].get_nick(), matches[n][2].get_pokemon())
        print(x)
        print(matches[n][1].get_nick(), matches[n][1].get_pokemon())
        print(matches[n][2].get_nick(), matches[n][2].get_pokemon())
    print(len(matches))
    return jsonify({"jugadores": fights})


def getPlayers():
    for n in range(len(players)):
        print("jugador:", players[n]["name"], "pokemons:", players[n]["pokemon"])
    return jsonify({"jugadores": players})


"""busca un player en particular"""


@app.route("/players/<string:player_name>")
def getPlayer(player_name):
    playerFound = [player for player in players if player["name"] == player_name]
    if len(playerFound) > 0:
        print("jugador:", playerFound[0]["name"], "pokemons:", playerFound[0]["pokemon"])
        return jsonify({"player": playerFound[0]})
    return jsonify({"message": "player not found"})


"""permite a un cliente unirse como jugador"""


@app.route("/players", methods=["POST"])
def addPlayer():
    new_player = {
        "name": request.json["name"],
        "pokemon": request.json["pokemon"]
    }
    print(len(matches))
    players.append(new_player)
    pelea = []
    if len(players) > 1:
        jugador1 = {"name": players[0]["name"], "pokemon": players[0]["pokemon"]}
        jugador2 = {"name": players[1]["name"], "pokemon": players[1]["pokemon"]}
        pelea.append(jugador1)
        pelea.append(jugador2)
        players.remove(players[0])
        players.remove(players[0])
        matches.append(pelea)
        print("matches", matches)
        print("esperando", players)
        return jsonify({"peleando": matches[0], "esperando": players})

    # corregir reenviar info server actualizada


"""permite a un cliente eliminar a un jugador """


@app.route("/players/<string:player_name>", methods=["DELETE"])
def deleteProduct(player_name):
    playerFound = [player for player in players if player["name"] == player_name]
    if len(playerFound) > 0:
        players.remove(playerFound[0])
        return jsonify()


if __name__ == '__main__':
    app.run()
