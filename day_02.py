# https://adventofcode.com/2024/day/2

def is_safe(report):
    increasing = all(1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing


def is_safe_with_dampener(report):
    return any(is_safe(report[:i] + report[i + 1:]) for i in range(len(report)))


def count_safe_reports(data, with_dampener=False):
    return sum(is_safe(report) or (with_dampener and is_safe_with_dampener(report)) for report in data)


def main():
    reports = [list(map(int, line.split())) for line in open('day_02_input.txt')]

    print('safe reports :', count_safe_reports(reports))
    print('safe reports with dampener :', count_safe_reports(reports, True))


main()
