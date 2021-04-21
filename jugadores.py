from cliente import cliente

players = [
    {"name": "chelo", "pokemon": "pijazard"},
    {"name": "jhoni", "pokemon": "irza"}
]


def match(player1, player2, pokemon1, pokemon2):
    cliente1 = cliente(player1, pokemon1)
    cliente2 = cliente(player2, pokemon2)


def matchestojson(name, pokemon, name2, pokemon2):
    pelea = [{}]
    player = {"name": name, "pokemon": pokemon}
    player2 = {"name": name2, "pokemon": pokemon2}
    pelea.append(player)
    pelea.append(player2)
    print(pelea)
    return pelea
