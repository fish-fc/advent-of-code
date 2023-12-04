"""Advent of Code 2023 - Day Four :-)
Input: .txt with each line containing containing the following scratchcard with a card number, winning number, and your numbers
    Card {id}: {winning_nums} | {given_nums}

Silver:
    Return: Sum of the doubled number of matches of each card 
    Answer: 23847

Gold:
    Return: Total number of cards when each winning number adds to the card count
    Answer: 8570000
"""
import re
from pydantic import BaseModel


class Card(BaseModel):
    """A class representation of a card

    Attr:
        id (int): the identifier of the card taken from "Card {id}:"
        winning_numbers set(int): a set of winning numbers taken from the left side of a card
        given_numbers set(int): a set of given numbers taken from the right side of a card
    """

    id: int
    winning_numbers: set[int]
    given_numbers: set[int]

    @classmethod
    def parse_string(cls, card_string: str):
        """Creates a Card object from a string (line from input.txt)"""
        id, winning_numbers, given_numbers = re.match(
            r"Card\s+(\d+): ([\d\s]+?) \| ([\d\s]+)", card_string
        ).groups()

        return Card(
            id=int(id),
            winning_numbers={int(n) for n in winning_numbers.split()},
            given_numbers={int(n) for n in given_numbers.split()},
        )

    def count_matching(self):
        """Return the length of the intersection of winning numbers and the given numbers"""
        return len(self.winning_numbers & self.given_numbers)

    def calculate_silver(self):
        """Return the 2^{matching_numbers}"""
        match_count = self.count_matching()
        return 2 ** (match_count - 1) if match_count > 0 else 0


def calculate_gold(cards):
    """Calculate the number of cards and their copies"""
    # initialize a list of copies of each card to 1
    copies = [1] * len(cards)
    for i, card in enumerate(cards):
        # for each card, loop from the initial card id to the last copy obtained by wins
        for j in range(card.id, card.id + card.count_matching()):
            # add the number of copies of the current card to the copies of the next cards
            copies[j] += copies[i]
    return sum(copies)


if __name__ == "__main__":
    silver_sum = 0
    gold_sum = 0

    with open("input.txt") as file:
        cards = [Card.parse_string(line) for line in file]
        for card in cards:
            silver_sum += card.calculate_silver()
        gold_sum = calculate_gold(cards)

    print("Silver Star Sum: " + str(silver_sum))
    print("Gold Star Sum: " + str(gold_sum))
