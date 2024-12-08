# https://adventofcode.com/2024/day/3
import re


def sum_multiplied_pairs(content, enabled=False):
    if enabled: content = re.sub(r"don\'t\(\).+?do\(\)", "", content, flags=re.DOTALL)
    multiply_regex = r"mul\((?P<a>\d{1,3}),(?P<b>\d{1,3})\)"
    return sum([int(match.group('a')) * int(match.group('b')) for match in re.finditer(multiply_regex, content)])


def main():
    content = open("day_03_input.txt").read()

    print('multiplications :', sum_multiplied_pairs(content))
    print('enabled multiplications :', sum_multiplied_pairs(content, True))

main()
