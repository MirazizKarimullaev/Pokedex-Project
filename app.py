import json
import time
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
types = open("./types.json",encoding="utf8")
moves = open("./moves.json",encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data_pokedexlist = json.load(pokedex)
data_types = json.load(types)
data_moves = json.load(moves)
# changed to data_pokedexlist because yes
# print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

# Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


# Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
# print(name[0]["name"]["english"])

lan_chose = False
while lan_chose == False:
    language = input("What language would you like to choose?, please note, I am too lazy to let you change this later because you can just control+c to reset this\n(name or num works)\n1. english\n2. japanese\n3. chinese\n4. french\n")
    if language == "1" or language == "english":
        lang = "english"
        lan_chose = True
    elif language == "2" or language == "japanese":
        lang = "japanese"
        lan_chose = True
    elif language == "3" or language == "chinese":
        lang = "chinese"
        lan_chose = True
    elif language == "4" or language == "french":
        lang = "french"
        lan_chose = True
    else:
        print("sorry, I didnt get that, try again")
def show_pokemon():
    print_names = input("would you like me to print all of the pokemons names? y or n?\n")
    if print_names == "n":
        print("ok")
    elif print_names == "y":
        for i in range(len(data_pokedexlist)):
            time.sleep(0.01)
            print(data_pokedexlist[i]["name"][lang])
    else:
        print("huh? ill take that as a no")
def show_pokemon_type():
    find_type_rn = "abcdefg"
    im_too_lazy_to_make_this_better_find_type = input("ok sir/ma'am, i'm too lazy to make this better, SO, type the type you want letter for letter, ENGLISH PLEASE AND CAPATALISE THE FIRST LETTER, I KNOW YOU DONT KNOW HOW TO TYPE IN ANY OTHER LANGUAGE, EVEN IF YOU DO, HOW ARE YOU READING THIS???\n")
    if im_too_lazy_to_make_this_better_find_type == "Normal":
        find_type_rn = "Normal"
    elif im_too_lazy_to_make_this_better_find_type == "Fighting":
        find_type_rn = "Fighting"
    elif im_too_lazy_to_make_this_better_find_type == "Flying":
        find_type_rn = "Flying"
    elif im_too_lazy_to_make_this_better_find_type == "Poison":
        find_type_rn = "Poison"
    elif im_too_lazy_to_make_this_better_find_type == "Ground":
        find_type_rn = "Ground"
    elif im_too_lazy_to_make_this_better_find_type == "Rock":
        find_type_rn = "Rock"
    elif im_too_lazy_to_make_this_better_find_type == "Bug":
        find_type_rn = "Bug"
    elif im_too_lazy_to_make_this_better_find_type == "Ghost":
        find_type_rn = "Ghost"
    elif im_too_lazy_to_make_this_better_find_type == "Steel":
        find_type_rn = "Steel"
    elif im_too_lazy_to_make_this_better_find_type == "Fire":
        find_type_rn = "Fire"
    elif im_too_lazy_to_make_this_better_find_type == "Water":
        find_type_rn = "Water"
    elif im_too_lazy_to_make_this_better_find_type == "Grass":
        find_type_rn = "Grass"
    elif im_too_lazy_to_make_this_better_find_type == "Electric":
        find_type_rn = "Electric"
    elif im_too_lazy_to_make_this_better_find_type == "Psychic":
        find_type_rn = "Psychic"
    elif im_too_lazy_to_make_this_better_find_type == "Ice":
        find_type_rn = "Ice"
    elif im_too_lazy_to_make_this_better_find_type == "Dragon":
        find_type_rn = "Dragon"
    elif im_too_lazy_to_make_this_better_find_type == "Dark":
        find_type_rn = "Dark"
    elif im_too_lazy_to_make_this_better_find_type == "Fairy":
        find_type_rn = "Fairy"
    while find_type_rn == "abcdefg":
        print("so, what did you type? did you misspell it :sob:, or did you not capilize it? or a numbeer, or spaces? Either way, try again")
        print("you know what, here is all the types\nNormal\nFighting\nFlying\nPoison\nGround\nRock\nBug\nGhost\nSteel\nFire\nWater\nGrass\nElectric\nPsychic\nIce\nDragon\nDark\nFairy\n")
        im_too_lazy_to_make_this_better_find_type = input("what type?\n")
        if im_too_lazy_to_make_this_better_find_type == "Normal":
            find_type_rn = "Normal"
        elif im_too_lazy_to_make_this_better_find_type == "Fighting":
            find_type_rn = "Fighting"
        elif im_too_lazy_to_make_this_better_find_type == "Flying":
            find_type_rn = "Flying"
        elif im_too_lazy_to_make_this_better_find_type == "Poison":
            find_type_rn = "Poison"
        elif im_too_lazy_to_make_this_better_find_type == "Ground":
            find_type_rn = "Ground"
        elif im_too_lazy_to_make_this_better_find_type == "Rock":
            find_type_rn = "Rock"
        elif im_too_lazy_to_make_this_better_find_type == "Bug":
            find_type_rn = "Bug"
        elif im_too_lazy_to_make_this_better_find_type == "Ghost":
            find_type_rn = "Ghost"
        elif im_too_lazy_to_make_this_better_find_type == "Steel":
            find_type_rn = "Steel"
        elif im_too_lazy_to_make_this_better_find_type == "Fire":
            find_type_rn = "Fire"
        elif im_too_lazy_to_make_this_better_find_type == "Water":
            find_type_rn = "Water"
        elif im_too_lazy_to_make_this_better_find_type == "Grass":
            find_type_rn = "Grass"
        elif im_too_lazy_to_make_this_better_find_type == "Electric":
            find_type_rn = "Electric"
        elif im_too_lazy_to_make_this_better_find_type == "Psychic":
            find_type_rn = "Psychic"
        elif im_too_lazy_to_make_this_better_find_type == "Ice":
            find_type_rn = "Ice"
        elif im_too_lazy_to_make_this_better_find_type == "Dragon":
            find_type_rn = "Dragon"
        elif im_too_lazy_to_make_this_better_find_type == "Dark":
            find_type_rn = "Dark"
        elif im_too_lazy_to_make_this_better_find_type == "Fairy":
            find_type_rn = "Fairy"
    print("ok here are the pokemon with said type")
    time.sleep(1)
    for i in range(len(data_pokedexlist)):
        for yes in range(len(data_pokedexlist[i]["type"])):
            if data_pokedexlist[i]["type"][yes] == find_type_rn:
                print(data_pokedexlist[i]["name"][lang])
                time.sleep(0.01)
def show_pokemon_search_drool():
    while True:
        search = input("ok, so, type any pokemons name and ill find it ")

show_pokemon()
show_pokemon_type()
def find_poke_search():
    while True:
        search_pokemon_not_full_name_this_is_long_because_why_not_yes_frfr = input("ok so im too lazy to do this efficently so just type man\n")
        while True:
            d