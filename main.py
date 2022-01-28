import random
import art
def deckCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculateScore(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score or (user_score>21 and computer_score>21):
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def playGame():
    is_game_over = False
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deckCard())
        computer_cards.append(deckCard())
    while not is_game_over:
        user_score = calculateScore(user_cards)
        computer_score = calculateScore(computer_cards)
        print(f"Your cards: {user_cards} and Your current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over = True
        else:
            user_should_deal = input("Do you to draw another card. Type yes or no\n").lower()
            if user_should_deal=="yes":
                user_cards.append(deckCard())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score<17:
        computer_cards.append(deckCard())
        computer_score = calculateScore(computer_cards)
    print(f"Your final hand:{user_cards} and your final score={user_score}")
    print(f"Computer's final hand:{computer_cards} and computer's final score={computer_score}")
    print(compare(user_score, computer_score))
while input("Do you want to play a game of BlackJack? Type yes or no\n")== "yes":
    print(art.logo)
    playGame()





















