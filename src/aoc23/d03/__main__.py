from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field

from aoc23.util import get_data

DAY = 3
YEAR = 2023
DATA = get_data(day=DAY, year=YEAR)

type Coord = tuple[int, int]
type Thing = Symbol | Part | None
type Grid = dict[Coord, Thing]

part_id_counter = 0


def next_part_id() -> int:
    global part_id_counter
    part_id_counter += 1
    return part_id_counter


@dataclass(eq=True, frozen=True)
class Part:
    number: int = field(compare=False)
    # we need to have an id field so that we don't double count parts
    id_: int = field(default_factory=next_part_id)

    @classmethod
    def insert_from_right(cls, coord: Coord, number: int, grid: Grid) -> None:
        num_len = len(str(number))
        left_coord = (coord[0] - num_len + 1, coord[1])
        part = cls(number)
        for x in range(num_len):
            coord = (left_coord[0] + x, left_coord[1])
            grid[coord] = part


@dataclass
class Symbol:
    symbol: str
    parts: set[Part] = field(default_factory=set)

    def gear_ratio(self) -> int:
        if self.symbol == "*" and len(self.parts) == 2:
            gears = [part.number for part in self.parts]
            return gears[0] * gears[1]
        return 0


def parse_grid() -> Grid:
    grid: Grid = defaultdict()
    for y, line in enumerate(DATA.splitlines()):
        cur_part_num: int | None = None
        for x, char in enumerate(line):
            if char.isdigit():
                if cur_part_num is None:
                    cur_part_num = int(char)
                else:
                    cur_part_num = cur_part_num * 10 + int(char)
            else:
                if cur_part_num is not None:
                    Part.insert_from_right((x - 1, y), cur_part_num, grid)
                    cur_part_num = None
                if char != ".":
                    grid[(x, y)] = Symbol(char)
        if cur_part_num is not None:
            Part.insert_from_right((len(line) - 1, y), cur_part_num, grid)
    return grid


def surrounding_coords(coord: Coord) -> list[Coord]:
    x, y = coord
    return [
        # fmt: off
        (x-1, y-1), (x, y-1), (x+1, y-1),
        (x-1, y  ),           (x+1, y  ),
        (x-1, y+1), (x, y+1), (x+1, y+1),
        # fmt: on
    ]


def silver():
    grid = parse_grid()
    total = 0
    for coord, symbol in grid.items():
        match symbol:
            case Symbol(_):
                for coord in surrounding_coords(coord):
                    part = grid.get(coord)
                    match part:
                        case Part(_):
                            if part not in symbol.parts:
                                symbol.parts.add(part)
                                total += part.number
                        case _:
                            pass
            case _:
                pass
    return total


def gold():
    grid = parse_grid()
    for coord, symbol in grid.items():
        match symbol:
            case Symbol(_):
                for coord in surrounding_coords(coord):
                    part = grid.get(coord)
                    match part:
                        case Part(_):
                            if part not in symbol.parts:
                                symbol.parts.add(part)
                        case _:
                            pass
            case _:
                pass

    total = 0
    for coord, symbol in grid.items():
        match symbol:
            case Symbol(_):
                total += symbol.gear_ratio()
            case _:
                pass
    return total


if __name__ == "__main__":
    print(silver())  # 530495
    print(gold())
