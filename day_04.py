# https://adventofcode.com/2024/day/4

matrix = [list(l) for l in open("day_04_input.txt")]
rows = len(matrix)
cols = len(matrix[0])


def search_xmas_word():
    directions = [(dx, dy) for dx in [0, 1, -1] for dy in [0, 1, -1] if not (dx == 0 and dy == 0)]
    word = 'XMAS'

    def search_from(x, y, dx, dy):
        return all(
            0 <= x + i * dx < rows and 0 <= y + i * dy < cols and matrix[x + i * dx][y + i * dy] == word[i]
            for i in range(len(word))
        )

    return sum(search_from(r, c, dx, dy) for r in range(rows) for c in range(cols) for dx, dy in directions)


def search_crossed_mas_word():
    def is_cross_center(x, y):
        if matrix[x][y] != 'A':
            return False
        if not (0 <= x - 1 < rows and 0 <= x + 1 < rows and 0 <= y - 1 < cols and 0 <= y + 1 < cols):
            return False

        directions = [((x + dx, y + dy), (x - dx, y - dy)) for dx, dy in [(i, j) for i in [1, -1] for j in [1, -1]]]

        return 2 <= sum(
            (0 <= x1 < rows and 0 <= y1 < cols and matrix[x1][y1] == 'M') and
            (0 <= x2 < rows and 0 <= y2 < cols and matrix[x2][y2] == 'S')
            for (x1, y1), (x2, y2) in directions
        )

    return sum(is_cross_center(r, c) for r in range(rows) for c in range(cols))


def main():
    print('Search XMAS :', search_xmas_word())
    print('Search X-MAS :', search_crossed_mas_word())


main()
