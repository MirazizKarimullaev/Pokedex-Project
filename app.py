import time
import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
# print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

# Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


# Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
# print(data[0]["name"]["english"])
def show_pokemon():
    lan_chose = False
    while lan_chose == False:
        language = input("What language would you like to choose?, please note, I am too lazy to let you change this later because you can just control+c to reset this\n(name or num works)\n1. english\n2. japanese\n3. chinese\n4. french")
    if language == "1" or language == "english":
        lang = english
        lan_chose = True
    elif language == "2" or language == "japanese":
        lang = japanese
        lan_chose = True
    elif language == "3" or language == "chinese":
        lang = chinese
        lan_chose = True
    elif language == "4" or language == "french":
        lang = french
        lan_chose = True
    else:
        print("sorry, I didnt get that, try again")
    print_names = input("would you like me to print all of the pokemons names? (ALOT OF NAMES) y or n?")
    if print_names == "n":
        print("ok")
    elif print_names == "y":
        print("ok this will be alot, gl o7")
        time.sleep(1)
        print("\n3...\n")
        time.sleep(1)
        print("\n2...\n")
        time.sleep(1)
        print("\n1...\n")
        for i in range(len(data)):
            print(data[i]["name"][lang])
show_pokemon()