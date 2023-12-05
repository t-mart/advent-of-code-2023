from typing import Callable

from aoc23.util import get_data

DAY = 2
YEAR = 2023
DATA = get_data(day=DAY, year=YEAR)

type Set = tuple[int, int, int]  # red, green, blue
type Game = tuple[int, list[Set]]  # game_id, sets


def parse_game(line: str) -> Game:
    game_part, sets_part = line.split(": ")
    game_id = int(game_part.split(" ")[1])

    sets = parse_sets(sets_part)
    return (game_id, sets)


def parse_sets(data: str) -> list[Set]:
    return [parse_set(set_) for set_ in data.split("; ")]


def parse_set(set_: str) -> Set:
    colors = [0, 0, 0]  # red, green, blue
    for color_part in set_.split(", "):
        count, color = color_part.split(" ")
        count = int(count)
        if color == "red":
            colors[0] = count
        elif color == "green":
            colors[1] = count
        else:  # color == "blue"
            colors[2] = count
    return (colors[0], colors[1], colors[2])


def solve(part_fn: Callable[[Game], int]) -> int:
    return sum(part_fn(parse_game(line)) for line in DATA.splitlines())


def part_1(game: Game) -> int:
    def valid_set(set_: Set) -> bool:
        return all(color < max_color for color, max_color in zip(set_, (12, 13, 14)))

    game_id, sets = game

    if all(valid_set(set_) for set_ in sets):
        return game_id
    return 0


def part_2(game: Game) -> int:
    _, sets = game
    max_colors: list[int] = [0] * 3
    for set_ in sets:
        for idx in range(3):
            color_count = set_[idx]
            if color_count > max_colors[idx]:
                max_colors[idx] = color_count
    return max_colors[0] * max_colors[1] * max_colors[2]


if __name__ == "__main__":
    print(solve(part_1))
    print(solve(part_2))
