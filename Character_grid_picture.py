
grid = []

WIDTH = 6
HEIGHT = 9

for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        column.append('#')
    grid.append(column)

for y in range(HEIGHT):
    for x in range(WIDTH):
        print(grid[x][y], end='')
    print()

print('------------------------')
print()

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print(len(grid))


def draw_rotated_grid(matrix):
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            print(grid[y][x], end=' ')
        print()

draw_rotated_grid(grid)