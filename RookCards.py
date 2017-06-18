import random
from colorama import init, Fore, Back, Style

class Card:
    def __init__(self):
        self.suit = ''
        self.number = ''
        self.int = 0
    def __init__(self, card_string):
        self.number, self.suit = card_string.split(':')
        self.int = int(self.number)
    def points(self):
        if self.number == '16':
            return 20

        elif self.number == '15':
            return 15

        elif self.number == '14' or self.number == '10':
            return 10

        elif self.number == '5':
            return 5
        return 0

    def is_rook(self):
        if self.number == '16':
            return True
        return False
    def __str__(self):
        return str(self.number)+':'+self.suit
    def string(self):
        return str(self.number)+':'+self.suit
    def split(self,character):
        return self.string().split(character)


class Hand:
    def __init__(self, card_list):
        self.cards = card_list
        self.Cards = [Card(card) for card in card_list]
        self.hand_checker = " ".join(self.cards)

    def rebuild(self):
        self.hand_checker = " ".join(self.cards)
        self.Cards = [Card(card) for card in self.cards]
        return self.hand_checker
    def shuffle(self):
        random.shuffle(self.cards)
        return rebuild()
    def total_points(self):
        points_total = 0
        for card in self.Cards:
            points_total += Card(card).points()
        return points_total
    def print(self):
        builder = ''
        for card in self.cards:
            current_card = Card(card)
            number = current_card.int
            builder+= Back.BLACK
            if number == 16:
                number = 'ROOK'
            elif number == 15:
                number = 1
            if current_card.suit == 'GREEN':
                builder += Fore.GREEN
            elif current_card.suit == 'RED':
                builder += Fore.RED
            elif current_card.suit == 'BLACK':
                builder += Fore.BLUE
            elif current_card.suit == 'YELLOW':
                builder += Fore.YELLOW
            builder += (Back.WHITE+' '+current_card.number)
        builder += Fore.WHITE
        builder+= Back.BLACK
        print(builder)





if __name__ == "__main__":
    print(Card('16:ROOK').points())
