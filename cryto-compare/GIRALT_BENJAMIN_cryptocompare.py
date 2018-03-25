#!/usr/bin/env python3.5 
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------------------------------------  
# 	purpose		| simple script using cryptocompy api 
#      			|   type list to get the list of all crypto currencies available
#      			|   type price to get the exchange rate of a given cryptocurrency in euros
# 	author		| Benjamin GIRALT - B2A 
# 	date		| 26/03/18
# 	version		| 01.0
# --------------------------------------------------------------------------------------------------------- 

from cryptocompy import coin, price 
import os
import sys
import ansi_colors as colors


list_cryptocurrencies = coin.get_coin_list()


def clear_screen() -> None:
    
    os.system('cls' if os.name == 'nt' else 'clear')



def get_list_cryptocurrencies(list):

    l = ''
    for key, value in list.items():
        print(value.get('CoinName') ,'- (',value.get('Name'),')')
    
    print('\n{}{} crypto currencies found.{}\n'.format(colors.GREEN, len(list), colors.ESCAPE))



def get_selling_price(cryptocurrency, currency):

    p = price.get_current_price(cryptocurrency, ["EUR"])
    selling_price = p[cryptocurrency][currency]
    
    return ('\n{} = {} {}\n'.format(cryptocurrency, selling_price, currency))



def process_user_choice(user_choice):

    if user_choice == 'list':
        print('\n')
        get_list_cryptocurrencies(list_cryptocurrencies)

    elif user_choice == 'quit':
        # TODO print(successfully exited with code 0)
        exit
    
    elif user_choice == 'price':

        while True:
            print('\n{}Please enter the desired cryptocurrency. e.g : BTC for Bitcoin{}'.format(colors.YELLOW, colors.ESCAPE))
            crypto = str.upper((input(' > ')))

            try:
                print(get_selling_price(crypto, "EUR"))
                break
            except:
                print('{}\nInvalid cryptocurrency, please enter a correct one{}'.format(colors.RED, colors.ESCAPE))
                

    else :
        print('Syntax Error.')



def main():
    
    clear_screen() 
    possible_inputs = ['list', 'price', 'quit']

    # print('{}Number of cryptocurrencies available : {}{}\n'.format(colors.YELLOW, len(list_cryptocurrencies), colors.ESCAPE))
    print('{}\nlist -> {}Get the list of all available cryptocurrencies\n'.format(colors.YELLOW, colors.ESCAPE))
    print('{}price -> {}Get the price in EUROS of a given cryptocurrency\n'.format(colors.YELLOW, colors.ESCAPE))
    print('{}\nquit -> {}Exit the program\n'.format(colors.YELLOW, colors.ESCAPE))

    while True:
        user_choice = (input('\n{}Your choice :{} \n > '.format(colors.CYAN, colors.ESCAPE)))

        if not user_choice in possible_inputs:

            print('{}\nSyntax error. Please enter your choice again{}'.format(colors.RED, colors.ESCAPE))
        
        else:

            process_user_choice(user_choice)
            break


main()
