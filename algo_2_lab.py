from queue import Queue


def flood_fill(matrix: list[list[str]], x: int, y: int, new_color: str):
    if not matrix:
        return

    row = len(matrix)
    col = len(matrix[0])

    old_color = matrix[x][y]
    if old_color == new_color:
        return
    q = Queue()
    q.put((x, y))
    while not q.empty():
        x, y = q.get()
        if x < 0 or x >= row or y < 0 or y >= col or matrix[x][y] != old_color:
            continue
        else:
            matrix[x][y] = new_color
            q.put((x + 1, y)) #down
            q.put((x - 1, y)) #up
            q.put((x, y + 1)) #right
            q.put((x, y - 1)) #left


if __name__ == '__main__':

    matrix = [
        ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
        ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
        ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
        ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
        ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
        ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
        ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
        ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
        ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
        ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ]

    x = 3
    y = 9

    new_color = 'III'

    flood_fill(matrix, x, y, new_color)

    for r in matrix:
        print(r)
