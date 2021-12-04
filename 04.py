# Read data
data = open('04.txt', 'r')
lines = data.readlines()
boards = list()

### FIRST PART
### SECOND PART

def string_to_2d_array (first, last):
    global boards
    board = list()
    i = first
    while i < last:
        board.append([int(n) for n in lines[i].split()])
        i += 1
    boards.append(board)

def mark_as_called (board, called_number):
    for line in board:
        if called_number in line:
            i = line.index(called_number)
            line[i] = True

def check_bingo(board):
    horizontal, vertical = [0] * 5, [0] * 5
    x, y = 0, 0
    for line in board:
        for num  in line:
            if num == True:
                horizontal[y] += 1
                vertical[x] += 1
            x += 1
        y += 1
        x = 0
    if 5 in horizontal or 5 in vertical:
        return True
    return False

def calculate_score(board, called_number):
    unmarked_sum = 0
    for line in board:
        for num in line:
            if num != True:
                unmarked_sum += num
    score = unmarked_sum * called_number
    return score

called_numbers = [int(n) for n in lines[0].split(',')]

# set up
line_number = 2
while line_number < len(lines):
    string_to_2d_array(line_number, line_number + 5)
    line_number += 6

# run bingo game
first_score = -1
last_score = -1

# TODO: fix skipping issue, remove method seems like the cause
for called_number in called_numbers:
    for board in boards:
        mark_as_called(board, called_number)
        if check_bingo(board):
            score = calculate_score(board, called_number)
            if first_score < 0:
                first_score = score
            if len(boards) == 1:
                last_score = score
            boards.remove(board)

print("FIRST:\tScore\t" + str(first_score))
print("LAST:\tScore\t" + str(last_score))
