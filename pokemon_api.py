import requests as r

class Pokemon():

    def __init__(self, pokemon):
        self.pokemon = pokemon

    def get_pokemon(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon}"
        response = r.get(url)
        if response.ok:
            data = response.json()
            # get pokemon name 
            # at least one ability 
            # base_experience
            # and the url for its sprite 'front_shiny'
            self.name = data['name']
            self.ability_name = data['abilities'][0]['ability']['name']
            self.base_experience = data['base_experience']
            self.sprite = data['sprites']['front_shiny']
            self.print_info()
        else:
            print(f">>> '{self.pokemon.upper()}' NOT FOUND <<<")

    def print_info(self):
        print(f"POKEMON INFO".center(50, '-'))
        print(f"ABILITY: {self.ability_name.title()}")
        print(f"BASE EXPERIENCE: {self.base_experience}")
        print(f"IMAGE SPRITE: {self.sprite}")



# main
print("POKEMON".center(52, '-'))
pokemon = input("Enter the name of a Pokemon or enter 'Q' to Quit: ")
while True:
    while not pokemon.replace(" ", "").isalpha():
        print("\n>>> INVALID INPUT <<<")
        pokemon = input("Enter the name of a Pokemon or 'Q' to Quit: ")
    pokemon = pokemon.lower()
    if pokemon.upper() == 'Q':
        break
    else:
        print(f"\nRetrieving stats for ---------------> {pokemon.upper()}")
        poke = Pokemon(pokemon)
        poke.get_pokemon()
        pokemon = input("\nEnter the name of a Pokemon or 'Q' to Quit: ")