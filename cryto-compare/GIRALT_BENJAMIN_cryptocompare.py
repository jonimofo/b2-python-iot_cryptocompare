#!/usr/bin/env python3.5 
# -*- coding: utf-8 -*-@

# 1. Demande à l'utilisateur la crypto dont il veut le prix 
    #  ou s'il veut la liste des cryptos disponibles.

# 2. Cherche la liste des cryptos et les affiches. 
    # Ou cherche le prix via l'API de cryptocompare.com et l'affiche

# 3. Retour au n°1


from cryptocompy import coin
import os
import sys
import colors


list_crypto = coin.get_coin_list()



def clear_screen() -> None:
    
    os.system('cls' if os.name == 'nt' else 'clear')



def get_list_crypto(list_crypto):
    
    for key, value in list_crypto.items():
        return (value.get('FullName'))



def process_user_choice(user_choice):

    if user_choice == 1:

        get_list_crypto()

    if user_choice == 0:

        # TODO print(successfully exited with code 0)
        exit

    else :

        print('toto')



def main():
    
    clear_screen()

    print('Number of cryptocurrencies available : {}'.format(len(list_crypto)))
    print('{}Enter 1 to get a list of all available cryptocurrencies{}\n'.format(colors.CYAN, colors.ESCAPE))
    print('{}Enter exit to quit the program{}'.format(colors.CYAN, colors.ESCAPE))

    # TODO : verifier valeurs / unwanted values pour ne pas quitter si mauvais choix
    try:

        user_choice = int(input('\nYour choice \n > ').format(colors.CYAN, colors.ESCAPE))

    except ValueError:

        sys.stderr.write("Error : Undefined choice\n")
        sys.exit(1)

    process_user_choice(user_choice)



main()


