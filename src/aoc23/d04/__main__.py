from __future__ import annotations

from dataclasses import dataclass, field

from aoc23.util import get_data

DAY = 4
YEAR = 2023
DATA = get_data(day=DAY, year=YEAR)
# DATA = """\
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

type Ticket = set[int]


@dataclass
class Card:
    number: int
    winning: Ticket
    chosen: Ticket
    copies: int = field(default=1, init=False)

    @property
    def match_count(self) -> int:
        return len(self.winning & self.chosen)

    def add_copies(self, copies: int) -> None:
        self.copies += copies


def parse_ticket(numbers_str: str) -> Ticket:
    return set(int(num) for num in numbers_str.split(None))


def parse_card(line: str) -> Card:
    card_no_part, tickets_part = line.split(": ")
    card_no = int(card_no_part.split(None)[1])
    winning, chosen = [
        parse_ticket(ticket_str) for ticket_str in tickets_part.split(" | ")
    ]
    return Card(card_no, winning, chosen)


def silver() -> int:
    total = 0
    for line in DATA.splitlines():
        card = parse_card(line)
        total += int(2 ** (card.match_count - 1))
    return total


def gold() -> int:
    card_map: dict[int, Card] = {}
    card_count = 0
    for line in DATA.splitlines():
        card = parse_card(line)
        card_map[card.number] = card
        card_count += 1

    for card_number in range(1, card_count + 1):
        card = card_map[card_number]
        for card_number_offset in range(1, card.match_count + 1):
            next_card_number = card_number + card_number_offset
            next_card = card_map[next_card_number]
            next_card.add_copies(card.copies)

    return sum(card.copies for card in card_map.values())


if __name__ == "__main__":
    print(silver())
    print(gold())
