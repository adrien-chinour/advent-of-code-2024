# https://adventofcode.com/2024/day/1

def main():
    left, right = zip(*(map(int, line.split('  ')) for line in open("day_01_input.txt")))

    print('total distance :', sum(abs(a - b) for a, b in zip(sorted(left), sorted(right))))
    print('similarity score :', sum(i * right.count(i) for i in left))


main()
