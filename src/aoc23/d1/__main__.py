from aoc23.util import get_data

DAY = 1
YEAR = 2023

DIGIT_MAP = {str(i): i for i in range(1, 10)}
DIGIT_AND_WORD_MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
} | DIGIT_MAP


def first_last_number(line: str, digit_map: dict[str, int]) -> tuple[int, int]:
    idx = 0
    numbers: list[int] = []
    while idx < len(line):
        substr = line[idx:]
        for word, number in digit_map.items():
            if substr.startswith(word):
                numbers.append(number)
                break
        idx += 1
    return numbers[0], numbers[-1]


def solve(digit_map: dict[str, int]) -> int:
    total = 0
    lines: list[str] = get_data(day=DAY, year=YEAR).splitlines()
    for line in lines:
        first, last = first_last_number(line, digit_map)
        addend = first * 10 + last
        total += addend
    return total


if __name__ == "__main__":
    print(solve(DIGIT_MAP))
    print(solve(DIGIT_AND_WORD_MAP))