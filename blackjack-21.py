"""
    Assignment 5: Blackjack / Twenty-one
"""
from random import random

def main():
    """
        Main function
    """
    print("Welcome to Blackjack\n")

    while True:
        while True:
            start_game = input("\nDo you wish to start a new game? \'y\' or \'n\')")
            start_game = start_game.lower()
            if start_game == "n":
                exit()
            elif start_game == "y":
                break
            else:
                print("\nValid response is \'y\' for yes or \'n\' for no")


        #create  player and dealer hands
        dealer_cards = deal_two_cards()
        player_cards = deal_two_cards()

        print(f"\nDealer cards are [{dealer_cards[0]}, XXX]")
        print(f"\nPlayer cards are {player_cards}")
        print(f"\nFor a total of {sum_cards(*player_cards)}")

        #is player or dealer busted
        player_busted = False
        dealer_busted = False

        #Hit or Stay loop
        while True:
            response = input("\nShould player Hit or Stay? (\'h\' or \'s\')")
            response = response.lower()
            if response == "h":
                new_card = deal_new_card()
                player_cards.append(new_card)
                print(f"\nPlayer draws {new_card}")
                print(f"\nPlayer now has {player_cards}")
                player_sum = sum_cards(*player_cards)
                print(f"\nFor a total of {player_sum}")
                if player_sum > 21:
                    print("\nPlayer is busted. Player loses :(")
                    player_busted = True
                    break
                elif player_sum == 21:
                    break
            elif response == "s":
                player_sum = sum_cards(*player_cards)
                break
            else:
                print("\nValid response is \'h\' for Hit or \'s\' for Stay")
        #start new game if busted
        if player_busted:
            continue
        #show dealer's hand
        while True:
            dealer_sum = sum_cards(*dealer_cards)
            print(f"\nThe dealer\'s hand is now {dealer_cards}")
            print(f"\nFor a total of {dealer_sum}")

            if dealer_sum < 17:
                print("\nDealer must draw")
                new_card = deal_new_card()
                dealer_cards.append(new_card)
                print(f"\nDealer draws {new_card}")
            elif dealer_sum > 21:
                dealer_busted = True
                print("\nDealer Busted Player wins!!!! :)")
                break
            else:
                break
        if dealer_busted:
            continue

        #evaluate both hands
        if player_sum == dealer_sum:
            print(f"\nBoth Dealer and Player have {player_sum} so Dealer wins sorry :/")
        elif player_sum > dealer_sum:
            print(f"\nPlayer has {player_sum} and Dealer has {dealer_sum} so Player wins!!! :)")
        else:
            print(f"\nDealer has {dealer_sum} and Player has {player_sum} so Dealer Wins!!!! Sorry :/")

def deal_two_cards():
    """
        Deal 2 cards
    """
    cards = [ int(random()*10+1), int(random()*10+1) ]
    return cards
def deal_new_card():
    """
        Deal 1 card
    """
    return int(random()*10+1)

def sum_cards(*args):
    """
        add all cards in hand
    """
    total_cards = 0
    for arg in args:
        total_cards += arg
    return total_cards

if __name__ == "__main__":
    main()
