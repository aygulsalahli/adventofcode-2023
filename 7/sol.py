card_strength = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


class CamelCard:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        self.card_amount = {}
        for card in self.hand:
            if card not in self.card_amount:
                self.card_amount[card] = 1
            else:
                self.card_amount[card] += 1


    def max_num_of_unique_cards(self):
        return max(self.card_amount.values())

    def __str__(self):
        return f"Hand: {self.hand} Bid: {self.bid}"

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
            if card_strength[self.hand[i]] < card_strength[__value.hand[i]]:
                return True
            elif card_strength[self.hand[i]] > card_strength[__value.hand[i]]:
                # print(f"Card {self.hand} is greater than {__value.hand}")
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
