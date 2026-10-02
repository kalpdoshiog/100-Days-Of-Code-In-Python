import random
from art import logo
print(logo)

start_again = True

while start_again:

    def deal_card():
        """Returns a random card from the deck."""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    def calculate_score(cards):
        """It takes the list of cards and Returns a total score (Calculated Score)."""
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(u_score, comp_score):
        if u_score == comp_score:
            return "Draw 🙃"
        elif comp_score == 0:
            return "Lost, opponent has Blackjack 😩"
        elif u_score == 0:
            return "Win with a Blackjack 😊"
        elif u_score > 21:
            return "You went over. You Lose 😒"
        elif comp_score > 21:
            return "opponent went over. You Win 😎"
        elif u_score > comp_score:
            return "You Win 😁"
        else:
            return "You Lose 😭"



    user_cards = []
    computer_cards = []

    user_score = -1
    computer_score = -1

    is_game_over = False


    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            continue_game = input("Do you want to play another round? Type 'y' or 'n'.").lower()
            if continue_game == "y":
                user_cards.append(deal_card())
            elif continue_game == "n":
                is_game_over = True



    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your Final Hand: {user_cards}, final score: {user_score}")
    print(f"Computer's Final Hand: {computer_cards}, final score: {computer_score}")
    print(compare(u_score=user_score, comp_score=computer_score))
    start_again = False

    wanna_play_again = input("Do you want to start new game? Type 'y' or 'n' ")

    if wanna_play_again == "y":
        print("\n" * 50)
        print(logo)
        start_again = True
    else:
        start_again = False