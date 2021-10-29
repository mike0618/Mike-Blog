def check(spot) -> int:
    if spot != '#':
        if type(spot) is int:
            spot += 1
        else:
            spot = 1
    return spot


def num_grid(grid: list) -> list:
    height = len(grid)
    width = len(grid[0])
    for y in range(height):
        for x in range(width):
            if grid[y][x] == '#':
                if x < width - 1:
                    grid[y][x + 1] = check(grid[y][x + 1])
                if x:
                    grid[y][x - 1] = check(grid[y][x - 1])
                if y < height - 1 and x < width - 1:
                    grid[y + 1][x + 1] = check(grid[y + 1][x + 1])
                if y < height - 1 and x:
                    grid[y + 1][x - 1] = check(grid[y + 1][x - 1])
                if y and x:
                    grid[y - 1][x - 1] = check(grid[y - 1][x - 1])
                if y and x < width - 1:
                    grid[y - 1][x + 1] = check(grid[y - 1][x + 1])
                if y < height - 1:
                    grid[y + 1][x] = check(grid[y + 1][x])
                if y:
                    grid[y - 1][x] = check(grid[y - 1][x])
    for y in range(height):
        for x in range(width):
            if grid[y][x] == '-':
                grid[y][x] = '0'
            else:
                grid[y][x] = str(grid[y][x])
    return grid


if __name__ == '__main__':
    print(num_grid([
        ["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]
    ]))
