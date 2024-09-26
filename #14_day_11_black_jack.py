import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    score= sum(cards)
    return score
user_cards = []
dealer_cards =[]
for i in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())
print((user_cards,dealer_cards))
user_score = calculate_score(user_cards)
dealer_score = calculate_score(dealer_cards)
