class cliente:

    def __init__(self, nick, pokemon):
        self.nick = nick
        self.pokemon = pokemon

    def get_nick(self):
        return self.nick

    def get_pokemon(self):
        return self.pokemon

    def set_nick(self, new_nick):
        self.nick = new_nick

    def set_pokemon(self, new_pokemon):
        self.pokemon = new_pokemon
