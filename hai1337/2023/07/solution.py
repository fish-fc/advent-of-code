"""Advent of Code Day 7


Silver: given multiple hands of cards, rank them and multiply their bids by their rank
    Answer: 250058342

Gold: now include jokers as the same as the highest ranked card but when comparing for a tie, use as the lowest rank
    Answer: 250506580
"""
from pydantic import BaseModel, Field
from functools import cmp_to_key
from collections import Counter

SILVER_CARDS = "23456789TJQKA"
GOLD_CARDS = "J23456789TQKA"


class Hand(BaseModel):
    """A class representation of a hand of cards

    Attr:
        cards (str): the cards of a hand
        bid (int): the bid amount of a hand
        silver_type (int): the type of hand given silver rules
        gold_type (int): the type of hand given gold rules
    """

    cards: str = ""
    bid: int = 0
    silver_type: int = 0
    gold_type: int = 0

    @classmethod
    def parse_silver(cls, hand_str: str):
        """Creates a Hand object from a string"""
        cards, bid = hand_str.split(" ")
        return Hand(
            cards=cards,
            bid=int(bid),
            silver_type=cls.get_type(cards, silver=True),
            gold_type=cls.get_type(cards, silver=False),
        )

    def get_type(cards: str, silver: bool):
        """Gets the type of the hand"""
        if silver:
            joker_count = 0
        else:
            joker_count = cards.count("J")
            cards = [card for card in cards if card != "J"]
        occurences = sorted(Counter(cards).values(), reverse=True)

        if not occurences:
            occurences = [0]
        if occurences[0] + joker_count == 5:
            return 6
        if occurences[0] + joker_count == 4:
            return 5
        if occurences[0] + joker_count == 3 and occurences[1] == 2:
            return 4
        if occurences[0] + joker_count == 3:
            return 3
        if occurences[0] == 2 and (joker_count or occurences[1]) == 2:
            return 2
        if occurences[0] == 2 or joker_count:
            return 1
        return 0


def create_compare_hands(silver: bool):
    def compare_hands(hand1: Hand, hand2: Hand):
        hand1_type = hand1.silver_type if silver else hand1.gold_type
        hand2_type = hand2.silver_type if silver else hand2.gold_type

        # if the first hand has a higher type than the second, return 1
        if hand1_type > hand2_type:
            return 1
        # if the second hand has a higher type than the first, return -1
        if hand2_type > hand1_type:
            return -1
        # if they are equal types, compare each card until one is higher
        for hand1_card, hand2_card in zip(hand1.cards, hand2.cards):
            if hand1_card == hand2_card:
                continue
            hand1_wins = (
                SILVER_CARDS.index(hand1_card) > SILVER_CARDS.index(hand2_card)
                if silver
                else GOLD_CARDS.index(hand1_card) > GOLD_CARDS.index(hand2_card)
            )
            return 1 if hand1_wins else -1

    return compare_hands


def calculate(hands: list[Hand], silver: bool):
    # sort the list by rank after comparing each card
    if silver:
        silver_hands = hands.copy()
        silver_hands.sort(key=cmp_to_key(create_compare_hands(silver=True)))
    else:
        gold_hands = hands.copy()
        gold_hands.sort(key=cmp_to_key(create_compare_hands(silver=False)))

    sum = 0
    for hand_rank, hand in enumerate(silver_hands if silver else gold_hands, start=1):
        sum += hand_rank * hand.bid
    return sum


if __name__ == "__main__":
    silver_sum = 0
    gold_sum = 0

    with open("input.txt") as file:
        hands = [Hand.parse_silver(line) for line in file]

    silver_sum = calculate(hands, silver=True)
    gold_sum = calculate(hands, silver=False)

    print("Silver Star Sum: " + str(silver_sum))
    print("Gold Star Sum: " + str(gold_sum))
