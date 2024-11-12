import random
from Day_11.art import logo
def black_jack():
    print(logo)
    computer_scores = 0
    user_scores = 0

    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "It's Draw"
        elif user_score == 0:
            return "Lose , opponent has BlackJack"
        elif computer_score == 0:
            return "Win with a Black jack "
        elif user_score > 21:
            return "You went over . You lose"
        elif computer_score > 21:
            return "Opponent went over You Win "
        elif user_score > computer_score:
            return "you win!"
        else:
            return "you lose!"

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False

    while not is_game_over:
        user_scores = calculate_score(user_cards)
        computer_scores = calculate_score(computer_cards)
        print(f"you're cards {user_cards}:  current score : {user_scores}")
        print(f"computer's first card  :{computer_cards[0]}")

        if computer_scores == 0 or user_scores == 0 or user_scores > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or Type 'n' to pass :").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
                print()
            else:
                is_game_over = True
    # print(f"you're cards {user_cards}:  current score : {user_scores}")
    while computer_scores != 0 and computer_scores < 17:
        computer_cards.append(deal_card())
        computer_scores = calculate_score(computer_cards)

    result = compare(user_scores, computer_scores)
    print(result)

while input("Do you want to play a game of black jack ? Type 'Y' or 'n'").lower()=='y':
    print("\n"*100)
    black_jack()








