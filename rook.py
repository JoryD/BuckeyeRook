import random
import itertools
from rooklib import *
from RookCards import Card, Hand
from colorama import init, Fore, Back, Style



cards = ['5','6','7','8','9','10','11','12','13','14','15']
colors = ['GREEN','RED','BLACK','YELLOW']
optimization = False
init()
for i in range(1,100):
    rounds_played = 0
    player_scores = [0,0,0,0]
    dealer=random.randint(0,3)
    while 1:
        partner_card = None
        partner_is_self = False
        del partner_card
        teams = [[-1,-1],[-1,-1]]
        dealer +=1
        if dealer == 4:
            dealer = 0
        elif dealer == 5:
            dealer = 1
        elif dealer == 6:
            dealer = 2
        elif dealer == 7:
            dealer = 3
        deck = list(); deck.append('16:ROOK')
        table = list()
        hands = list()
        hand_table = ['','','','']
        taken_hands = list()
        nest = list()
        bids = list()

        for card in cards:
            for color in colors:
                deck.append(card+':'+color)

        random.shuffle(deck)

        for i in range(0,4):
            hands.append(list())
            taken_hands.append(list())

        for i in range(0,5):
            nest.append(deck[0])
            deck.pop(0)


        for i in range(0,10):
            hands[0].append(deck[0])
            deck.pop(0)
            hands[1].append(deck[0])
            deck.pop(0)
            hands[2].append(deck[0])
            deck.pop(0)
            hands[3].append(deck[0])
            deck.pop(0)

        for i in range(0,4):
            current_bid = hand_value(hands[i])
            current_bid = bid_round(int(current_bid))
            if current_bid > 180:
                current_bid = 180

            bids.append(current_bid)
        bid_winner = dealer
        bid_incrementer = dealer
        bid_set = bids[bid_winner] - 20
        #print(dealer)
        while 1:
            bid_incrementer += 1
            if bid_incrementer == 4:
                bid_incrementer = 0
            if bid_incrementer != bid_winner:
                if bid_set >= bids[bid_incrementer]:
                    pass
                elif bid_set + 10 == bids[bid_incrementer]:
                    bid_winner = bid_incrementer
                    bid_set = bid_set + 10
                else:
                    bid_winner = bid_incrementer
                    bid_set = bid_set + 5
            else:
                break
        print("WINNING BID: "+str(bid_set))
        last_taken = bid_winner
        teams[0][0] = bid_winner

        hands[last_taken] += nest
        powers = [0,0,0,0]

        for card in hands[last_taken]:
            power, suit = card.split(':')
            power = int(power)
            for color in colors:
                index = colors.index(color)
                if suit == color:
                    powers[index] += 5
                    if power == 15:
                       powers[index] += 25
                    elif power == 14:
                       powers[index] += 15
                    elif power == 13:
                       powers[index] += 10
                    elif power == 12:
                       powers[index] += 5
                    elif power == 10:
                       powers[index] += 10
        trump = colors[powers.index(max(powers))]

        new_hand = []
        junk = []
        for card in hands[last_taken]:
            power, suit = card.split(':')
            power = int(power)
            if power == 15 or power == 16:
                new_hand.append(card)
            elif suit == trump:
                new_hand.append(card)
            else:
                junk.append(card)
        while 1:
            if len(new_hand) > 10:
                new_hand.pop(0)
            else:
                break
        combos = itertools.combinations(junk, 10-len(new_hand))
        combos_list = list()
        combols = list()
        for combo in combos:
            combos_list.append(int(hand_value(new_hand+list(combo))))
            combols.append(list(combo))

        new_index = combos_list.index(max(combos_list))
        hand_finder = list(new_hand + combols[combos_list.index(max(combos_list))])
        hand_checker = " ".join(hand_finder)
        hands[last_taken] = hand_finder
        partner_card = True
        if hand_checker.find('16:ROOK') > -1:
            if hand_checker.find('15:'+trump) > -1:
                if hand_checker.find('14:'+trump) > -1:
                    number_sih, sih = suits_in_hand(hand_finder)
                    for suit in sih:
                        if suit == trump:
                            pass
                        else:
                            if number_sih.count(suit) == 1 and not hand_checker.find('15:'+suit) > -1:
                                partner_card = '15:'+suit
                                break
                    if partner_card:
                        for suit in colors:
                            if not hand_checker.find('15:'+suit) > -1:
                                partner_card = '15:'+suit
                                break


                else: partner_card = '14:'+trump
            else:
                partner_card = '15:'+trump

        else:
            partner_card = '16:ROOK'

        suit_required =''
        rounds_played += 1
        if partner_card == True:
            partner_card = '16:ROOK'
        if hand_checker.find(partner_card) > -1:
            partner_is_self = True
            teams[0]=[last_taken]
            teams[1] = [0,1,2,3]
            teams[1].remove(last_taken)
        else:
            for hand in hands:
                if partner_card in hand:
                    teams[0][1] = hands.index(hand)
            teams[1]=[0,1,2,3]
            try:
                teams[1].remove(teams[0][0])
                teams[1].remove(teams[0][1])
            except:
                print(hand_checker)
                input(partner_card)

        for trick in range(0,len(hands[last_taken])):
            hand_table = ['','','','']
            table = list()
            random.shuffle(hands[last_taken])
            played_card = hands[last_taken][0] # edit out
            if len(hands[last_taken]) == 10:
                partner_suit = partner_card.split(':')[1]
                if partner_suit == 'ROOK':
                    partner_suit = trump
                if '10:'+partner_suit in hands[last_taken]:
                    played_card = '10:'+partner_suit

                else:
                    for jokar in range(14,4,-1):
                        print(str(jokar)+':'+partner_suit)
                        if str(jokar)+':'+partner_suit in hands[last_taken]:
                            played_card = str(jokar)+':'+partner_suit
            else:
                played_card = hands[last_taken][0]
            #print(played_card)
            table.append(played_card)
            hand_table[last_taken] = played_card
            suit_required = played_card.split(':')[1]
            Hand(hands[last_taken]).print()
            hands[last_taken].pop(hands[last_taken].index(played_card))
            if suit_required == 'ROOK':
                suit_required = trump
            if last_taken == 0:
                hands_left = [1,2,3]
            elif last_taken == 1:
                hands_left = [2,3,0]
            elif last_taken == 2:
                hands_left = [3,0,1]
            elif last_taken == 3:
                hands_left = [0,1,2]
            for player in hands_left:
                hand_checker = " ".join(hands[player])
                if hand_checker.find(suit_required) > -1 or (suit_required==trump and hand_checker.find('ROOK') > -1):
                    while 1:
                        random.shuffle(hands[player])
                        played_card = hands[player][0]
                        suit_attempt = played_card.split(':')[1]
                        if suit_attempt == suit_required or (suit_required==trump and suit_attempt=='ROOK'):
                            table.append(played_card)
                            hands[player].pop(0)
                            hand_table[player] = played_card
                            break
                else:
                    random.shuffle(hands[player])
                    played_card = hands[player][0]
                    table.append(played_card)
                    hand_table[player] = played_card

                    hands[player].pop(0)
            current_winner = last_taken
            winning_card = Card(hand_table[last_taken])
            for card in hand_table:
                card = Card(card)
                suit_attempt = card.suit
                if suit_attempt == trump or suit_attempt=='ROOK':
                    if winning_card.suit == trump or winning_card.is_rook():
                        if winning_card.int < card.int:
                            current_winner = hand_table.index(card.string())
                            winning_card = card
                elif suit_attempt == suit_required:
                    if winning_card.suit == trump or winning_card.is_rook():
                        continue
                    elif winning_card.int < card.int:
                            current_winner = hand_table.index(card.string())
                            winning_card = card
            last_taken = current_winner
            taken_hands[current_winner] += hand_table
        taken_hands[current_winner] += nest
        round_scores = [0,0,0,0]
        for hand in taken_hands:
            round_scores[taken_hands.index(hand)] += Hand(hand).total_points()
        print(teams)
        print(partner_is_self)
        for team in teams:
            team_value = 0
            for member in team:
                team_value += round_scores[member]
            for member in team:
                player_scores[member] += team_value
                print(team_value)
        if partner_is_self:
            input()            
        if max(player_scores) >= 500:
            #print("Winner is Player "+str(player_scores.index(max(player_scores))))
            #print(max(player_scores))
            #print(rounds_played)
            break
