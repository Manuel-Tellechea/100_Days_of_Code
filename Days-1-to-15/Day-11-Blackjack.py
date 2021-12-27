"""
############### Our Blackjack House Rules #####################

- The deck is unlimited in size.
- There are no jokers.
- The Jack/Queen/King all count as 10.
- The the Ace can count as 11 or 1.
- Use the following list as the deck of cards:
- cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
- The cards in the list have equal probability of being drawn.
- Cards are not removed from the deck as they are drawn.
- The computer is the dealer.

"""
import random
from Files.art11 import logo


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = random.choice(cards)
    return player_cards


def check_score(player_cards):
    total_score = sum(player_cards)

    if total_score == 21 and len(player_cards) == 2:
        return 0
    elif total_score > 21:
        if 11 in player_cards:
            player_cards.remove(11)
            player_cards.append(1)
            total_score = sum(player_cards)
        return total_score
    else:
        return total_score


def compare_cards(player_score, dealer_score):
    if player_score > 21 and dealer_score > 21:
        return "You went over. You lose 😤"
    elif dealer_score > 21:
        return "Opponent went over. You win 😁"
    elif player_score == dealer_score:
        return "Draw 🙃"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif player_score == 0:
        return "Win with a Blackjack 😎"
    elif player_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def game():
    print(logo)
    player_cards = []
    dealer_cards = []

    for _ in range(2):
        player_cards.append(deal_cards())
        dealer_cards.append(deal_cards())

    is_game_over = False

    while not is_game_over:
        player_score = check_score(player_cards)
        dealer_score = check_score(dealer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {dealer_cards[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                player_cards.append(deal_cards())
                print(player_cards)
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_cards())
        dealer_score = check_score(dealer_cards)

    print(f"   Your final hand: {player_cards}, final score: {player_score}")
    print(f"   Computer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare_cards(player_score, dealer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    game()
