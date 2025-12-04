from input_data import data

data = [list(x) for x in data.split('\n')]
board = []
width = len(data[0]) + 2
height = len(data) + 2
board.append(['#' for _ in range(width)])
for i in range(height-2):
    board.append(['#'] + data[i] + ['#'])


board.append(['#' for _ in range(width)])
for i in range(height):
    print(board[i])

def get_num_of_closest_rolls(x, y):
    count = 0
    if board[y-1][x-1] == '@': count += 1
    if board[y][x-1] == '@': count += 1
    if board[y+1][x-1] == '@': count += 1
    if board[y-1][x] == '@': count += 1
    if board[y+1][x] == '@': count += 1
    if board[y-1][x+1] == '@': count += 1
    if board[y][x+1] == '@': count += 1
    if board[y+1][x+1] == '@': count += 1
    return count

ans1 = 0
for y in range(1, height-1):
    for x in range(1, width-1):
        if board[y][x] == '@' and get_num_of_closest_rolls(x, y) < 4:
            ans1 += 1

print(ans1)

ans2 = 0
running = True
while running:
    tmp = 0
    for y in range(1, height-1):
        for x in range(1, width-1):
            if board[y][x] == '@' and get_num_of_closest_rolls(x, y) < 4:
                board[y][x] = 'x'
                ans2 += 1
                tmp += 1
    if tmp == 0: running = False

print(ans2)














