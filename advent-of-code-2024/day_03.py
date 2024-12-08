# https://adventofcode.com/2024/day/3
import re


def main():
    matches = re.finditer(r"mul\((?P<a>\d{1,3}),(?P<b>\d{1,3})\)", open("day_03_input.txt").read())
    print('results :', sum([int(match.group('a')) * int(match.group('b')) for match in matches]))


main()
