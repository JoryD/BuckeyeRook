from RookCards import Card, Hand

cards = ['5','6','7','8','9','10','11','12','13','14','15']
colors = ['GREEN','RED','BLACK','YELLOW']

def suit(card):
    return card.split(':')[1]

def number(card):
    return card.split(':')[0]

def number_int(card):
    return int(card.split(':')[0])

def bid_round(x, base=5):
    return int(base * round(float(x)/base))
    # Credit: https://stackoverflow.com/questions/2272149/round-to-5-or-other-number-in-python @ Alok Singhal Retrieved 6/3/2017 10:51 PM EDT

def suits_in_hand(hand):
    suits = list()
    for card in hand:
        suits.append(Card(card).suit)
    if suits.count('ROOK') > 0:
        suits.remove('ROOK')
    return suits, list(set(suits))

def hand_value(list):
    hand_checker = " ".join(list)
    current_bid = float(0.0)
    current_bid += 40 # for partner
    current_bid += 10 # for nest

    if hand_checker.count("ROOK") == 1:
        current_bid +=35

    for color in colors:
        if '15:'+color in list:
            current_bid += 25
        if hand_checker.count(color) == 0:
            current_bid +=20
        if hand_checker.count(color) == 1:
            current_bid +=7
            if '14:'+color in list:
                current_bid -= 13
            if '10:'+color in list:
                current_bid -= 11
            if '5:'+color in list:
                current_bid -= 5
        if hand_checker.count(color) > 3:
            current_bid += 10
            if hand_checker.count(color) > 4:
                current_bid += 10
                if hand_checker.count(color) > 5:
                    current_bid += 10
                    if hand_checker.count(color) > 6:
                        current_bid += 10
                        if hand_checker.count(color) > 7:
                            current_bid += 180

    for card in list:
        checker = card.split(':')[0]
        if checker == '6':
            current_bid -= 2
        if checker == '7':
            current_bid -= 1.5
        if checker == '8':
            current_bid -= 1
        if checker == '9':
            current_bid -= .5
        if checker == '10':
            current_bid += 1
        if checker == '11':
            current_bid += 2
        if checker == '12':
            current_bid += 3
        if checker == '13':
            current_bid += 5
        if checker == '14':
            current_bid += 10
    return current_bid
