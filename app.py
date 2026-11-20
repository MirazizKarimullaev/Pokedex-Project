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
    language = input("What language would you like to choose?, please note, I am too lazy to let you change this later because you can just control+c to reset this\n(name only)\n1. english\n2. japanese\n3. chinese\n4. french\n")
    if language in "english , japanese , chinese , french":
        lang = language
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
    finding_check = False
    while finding_check == False:
        finding = input("find pokemon from type: ")
        for types_7 in data_types:
            if finding.lower() == types_7['english'].lower():
                finding_check = True
                find_type_rn = finding.title()
    print("ok here are the pokemon with said type")
    time.sleep(1)
    for i in data_pokedexlist:
        if find_type_rn in i["type"]:
            print(i["name"][lang])
            time.sleep(0.01)
def show_pokemon_search_drool():
    print("ok, so, type any pokemons name and ill find it if you want, type it partially plz, english and im lazy and dum")
    while True:
        amount_found = 0
        search = input("name?/partial name?\n")
        for idk_bro_help_me_i_dont_wana in range(len(data_pokedexlist)):
            search = search.title()
            name_2 = data_pokedexlist[idk_bro_help_me_i_dont_wana]["name"][lang]
            if search in name_2:
                amount_found +=1
                print(data_pokedexlist[idk_bro_help_me_i_dont_wana]["name"][lang])
        if amount_found == 0:
            print("sry i find no pokemon of your search")
        done_search_name_check = "qwerty"
        while done_search_name_check == "qwerty":
            done_search_name = input("wanna search again?, y if again, n if no more?\n")
            if done_search_name == "y":
                done_search_name_check = "yes"
            elif done_search_name == "n":
                done_search_name_check = "no"
                break
            else:
                continue
            break
        break
def show_pokemon_moves_from_type_droororoororol():
    while True:
        amount_found = 0
        search = input("name?/partial name?\n")
        for idk_bro_help_me_i_dont_wana in range(len(data_pokedexlist)):
            search_2 = search.lower()
            name_2 = data_pokedexlist[idk_bro_help_me_i_dont_wana]["name"][lang].lower()
            if search_2 in name_2:
                amount_found +=1
                print(data_pokedexlist[idk_bro_help_me_i_dont_wana]["name"][lang])
        if amount_found == 0:
            print("sry i find no pokemon of your search")
        elif amount_found == 1:
            print("hm i only found 1")
            while True:
                pokemon_choose_find_moves = input("do you want to use this pokemon? y or n \n")
                if pokemon_choose_find_moves == "y":
                    for idk_bro_help_me_i_dont_wana in range(len(data_pokedexlist)):
                        search_2 = search.lower()
                        name_2 = data_pokedexlist[idk_bro_help_me_i_dont_wana]["name"][lang].lower()
                        if search_2 in name_2:
                            data_pokemon_move_find = idk_bro_help_me_i_dont_wana
                            break
                            return
                    return
                elif pokemon_choose_find_moves != "n" and pokemon_choose_find_moves != "y":
                    x=1
                else:
                    print("ok")
                    return
    print("so you found your pokemon")


show_pokemon_type()
