"""Advent of Code Day 6


Silver: multiply the number of ways to win for each race
    Answer: 6209190

Gold: multiple the number of ways to win for the single, long race
    Answer: 28545089
"""
from pydantic import BaseModel


class Race(BaseModel):
    """A class representation of a race

    Attr:
        time (int): the total duration of a race in ms
        dist (int): the record distance of a race
    """

    time: int
    dist: int

    def ways_to_win(self):
        """Count and return the number of ways to win a race given its duration and record distance"""
        wins = 0

        i = 1
        while i <= self.time:
            time_left = self.time - i
            if time_left * i > self.dist:
                wins += 1
            i += 1

        return wins


def calculate_silver(text):
    answer = 1

    # parse the input into a list of ints
    time = [int(s) for s in text[0].split(":")[1].split()]
    dist = [int(s) for s in text[1].split(":")[1].split()]

    # create a list of races with a given time and distance
    races: list[Race] = []
    for idx, num in enumerate(time):
        races.append(Race(time=time[idx], dist=dist[idx]))

    # for each race, multiple the numbers of ways to win
    for race in races:
        answer *= race.ways_to_win()

    return answer


def calculate_gold(text):
    # parse the input into a single time and dist value by removing white space between the ints
    time = text[0].split(":")[1].replace(" ", "")
    dist = text[1].split(":")[1].replace(" ", "")

    # create a single race
    race = Race(time=time, dist=dist)

    return race.ways_to_win()


if __name__ == "__main__":
    with open("input.txt") as file:
        text = file.read().split("\n")

    silver_answer = calculate_silver(text)
    gold_answer = calculate_gold(text)

    print("Silver Star Answer: " + str(silver_answer))
    print("Gold Star Answer: " + str(gold_answer))
