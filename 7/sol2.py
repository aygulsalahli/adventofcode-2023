poker_card_strength = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}


class CamelCard:
    def __init__(self, hand, bid):
        self.original_hand = hand
        self.hand = hand
        self.bid = bid
        self.card_amount = {}
        self.handle_card_amount()
        self.handle_poker_cards()
        self.handle_card_amount()

        self.type = ""
        if self.is_five_of_a_kind():
            self.type = "Five of a kind"
        elif self.is_four_of_a_kind():
            self.type = "Four of a kind"
        elif self.is_full_house():
            self.type = "Full house"
        elif self.is_three_of_a_kind():
            self.type = "Three of a kind"
        elif self.is_two_pair():
            self.type = "Two pair"
        elif self.is_one_pair():
            self.type = "One pair"
        elif self.is_high_card():
            self.type = "High card"



    def handle_card_amount(self):
        self.card_amount = {}
        for card in self.hand:
            if card not in self.card_amount:
                self.card_amount[card] = 1
            else:
                self.card_amount[card] += 1

    def handle_poker_cards(self):
        if 'J' not in self.hand:
            return

        if self.is_four_of_a_kind() or self.is_full_house() or self.is_three_of_a_kind() or self.is_two_pair() or self.is_one_pair() or self.is_high_card():
            self.hand = self.hand.replace('J', self.candidat_for_joker())


    def max_num_of_unique_cards(self):
        return max(self.card_amount.values())

    def candidat_for_joker(self):
        max_value = max([v for k, v in self.card_amount.items() if k != 'J'])
        keys = [k for k, v in self.card_amount.items() if v == max_value]
        candidate = max(keys, key=lambda x: poker_card_strength[x])
        return candidate

    def __str__(self):
        return f"Original hand: {self.original_hand}, Hand: {self.hand}, Type: {self.type}"

    def is_five_of_a_kind(self):
        return len(set(self.hand)) == 1

    def is_four_of_a_kind(self):
        return len(set(self.hand)) == 2 and self.max_num_of_unique_cards() == 4

    def is_full_house(self):
        return len(set(self.hand)) == 2 and self.max_num_of_unique_cards() == 3

    def is_three_of_a_kind(self):
        return len(set(self.hand)) == 3 and self.max_num_of_unique_cards() == 3

    def is_two_pair(self):
        return len(set(self.hand)) == 3 and self.max_num_of_unique_cards() == 2

    def is_one_pair(self):
        return len(set(self.hand)) == 4

    def is_high_card(self):
        return len(set(self.hand)) == 5

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, CamelCard):
            return False

        return self.hand == __value.hand

    def compare_hands_lt(self, __value: object) -> bool:
        if not isinstance(__value, CamelCard):
            return False

        num = 0
        for i in range(5):
            if poker_card_strength[self.original_hand[i]] < poker_card_strength[__value.original_hand[i]]:
                return True
            elif poker_card_strength[self.original_hand[i]] > poker_card_strength[__value.original_hand[i]]:
                return False
            else:
                num += 1
        return False

    def __lt__(self, __value: object) -> bool:
        if self.is_five_of_a_kind() and not __value.is_five_of_a_kind():
            return False
        elif self.is_five_of_a_kind() and __value.is_five_of_a_kind():
            return self.compare_hands_lt(__value)
        elif not self.is_five_of_a_kind() and __value.is_five_of_a_kind():
            return True

        if (
            self.is_four_of_a_kind()
            and not __value.is_five_of_a_kind()
            and not __value.is_four_of_a_kind()
        ):
            return False
        elif self.is_four_of_a_kind() and __value.is_four_of_a_kind():
            return self.compare_hands_lt(__value)
        elif not self.is_four_of_a_kind() and __value.is_four_of_a_kind():
            return True

        if (
            self.is_full_house()
            and not __value.is_five_of_a_kind()
            and not __value.is_four_of_a_kind()
            and not __value.is_full_house()
        ):
            return False

        elif self.is_full_house() and __value.is_full_house():
            return self.compare_hands_lt(__value)
        elif not self.is_full_house() and __value.is_full_house():
            return True

        if (
            self.is_three_of_a_kind()
            and not __value.is_five_of_a_kind()
            and not __value.is_four_of_a_kind()
            and not __value.is_three_of_a_kind()
        ):
            return False
        elif self.is_three_of_a_kind() and __value.is_three_of_a_kind():
            return self.compare_hands_lt(__value)
        elif not self.is_three_of_a_kind() and __value.is_three_of_a_kind():
            return True

        if (
            self.is_two_pair()
            and not __value.is_five_of_a_kind()
            and not __value.is_four_of_a_kind()
            and not __value.is_three_of_a_kind()
            and not __value.is_two_pair()
        ):
            return False
        elif self.is_two_pair() and __value.is_two_pair():
            return self.compare_hands_lt(__value)
        elif not self.is_two_pair() and __value.is_two_pair():
            return True

        if (
            self.is_one_pair()
            and not __value.is_five_of_a_kind()
            and not __value.is_four_of_a_kind()
            and not __value.is_three_of_a_kind()
            and not __value.is_two_pair()
            and not __value.is_one_pair()
        ):
            return False
        elif self.is_one_pair() and __value.is_one_pair():
            return self.compare_hands_lt(__value)
        elif not self.is_one_pair() and __value.is_one_pair():
            return True

        if (
            self.is_high_card()
            and not __value.is_five_of_a_kind()
            and not __value.is_four_of_a_kind()
            and not __value.is_three_of_a_kind()
            and not __value.is_two_pair()
            and not __value.is_one_pair()
            and not __value.is_high_card()
        ):
            return False
        elif self.is_high_card() and __value.is_high_card():
            return self.compare_hands_lt(__value)
        elif not self.is_high_card() and __value.is_high_card():
            return True


with open("input") as f:
    lines = f.readlines()

    camel_cards = []
    for line in lines:
        hand, bid = line.strip().replace("\n", "").split(" ")
        camel_card = CamelCard(hand, bid)
        camel_cards.append(camel_card)


    sorted_camel_cards = sorted(camel_cards)
    total = 0
    for i, camel_card in enumerate(sorted_camel_cards):
        total += (i+1) * int(camel_card.bid)

    print(f"Total: {total}")
