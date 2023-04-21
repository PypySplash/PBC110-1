class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def check_A(self):
        A_count = 0
        for card in self.cards:
            if card.rank == 'A':
                A_count += 1
        return A_count

    def check_pair(self):
        pair_dict = {}
        for card in self.cards:
            rank = card.rank
            pair_dict[rank] = pair_dict.get(rank, 0) + 1
        pair_count = 0
        for i in list(pair_dict.values()):
            pair_count += i * (i - 1) // 2
        return pair_count

    def check_flush(self):
        flush_dict = {}
        for card in self.cards:
            suit = card.suit
            flush_dict[suit] = flush_dict.get(suit, 0) + 1
        for i in list(flush_dict.values()):
            if i == 5:
                return True

    def check_straight(self):
        for card in self.cards:
            if card.rank == 'A':
                card.rank = 14
            if card.rank == 'J':
                card.rank = 11
            if card.rank == 'Q':
                card.rank = 12
            if card.rank == 'K':
                card.rank = 13
            else:
                card.rank = int(card.rank)
        self.cards.sort(key=lambda x: x.rank)
        straight_list = [[2, 11, 12, 13, 14], [2, 3, 12, 13, 14], [2, 3, 4, 13, 14], [2, 3, 4, 5, 14]]
        straight_count = 0
        rank_list = [card.rank for card in self.cards]
        for i in range(5 - 1):
            if rank_list == straight_list[i]:
                return True
            if self.cards[i + 1].rank - self.cards[i].rank != 1:
                return False
        return True

    def check_fullhouse(self):
        pair_dict = {}
        for card in self.cards:
            rank = card.rank
            pair_dict[rank] = pair_dict.get(rank, 0) + 1
        fullhouse_count = 0
        for i in list(pair_dict.values()):
            if i == 2:
                fullhouse_count += 2
            if i == 3:
                fullhouse_count += 3
        if fullhouse_count == 5:
            return True

    def check_fourofakind(self):
        pair_dict = {}
        for card in self.cards:
            rank = card.rank
            pair_dict[rank] = pair_dict.get(rank, 0) + 1
        fourofakind_count = 0
        for i in list(pair_dict.values()):
            if i == 4:
                fourofakind_count = 1
            if i == 5:
                fourofakind_count = 5
        return fourofakind_count

    def check_straightflush(self):
        if self.check_straight() and self.check_flush():
            return True

    def point_count(self):
        point = 0
        A_count = self.check_A()
        point += A_count * 5
        pair_count = self.check_pair()
        point += pair_count * 10
        if self.check_flush():
            point += 30
        if self.check_straight():
            point += 50
        if self.check_fullhouse():
            point += 80
        point += self.check_fourofakind() * 100
        if self.check_straightflush():
            point += 300
        return point


suits = input().split(',')
ranks = input().split(',')

cards = []
for suit, rank in zip(suits, ranks):
    card = Card(suit, rank)
    cards.append(card)

# print(cards)

hand = Hand(cards)

print(hand.point_count())
