import copy

def get_random_numbers(file):
    with open(file, "r") as f:
        random_numbers = f.readline().replace("\n", "").split(",")
        random_numbers = [int(x) for x in random_numbers]

        return random_numbers

def get_board_array(arr):
    board = []

    for row in range(len(arr)):
        line_list = []
        for i in range(0, len(arr[row]), 3):
            line_list.append(int(arr[row][i:i+2].strip()))
        board.append(line_list)

    return board

def get_boards(file):
    boards = []

    with open(file, "r") as f:
        lines = f.readlines()

        for i in range(2, len(lines), 6):
            board_array = lines[i:i+5]
            board = get_board_array(board_array)
            boards.append(board)

    return(boards)

def print_board(board):
    for row in board:
        print(row)

def print_boards(boards):
    for board in boards:
        print_board(board)
        print()

def empty_board():
    return [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

def empty_boards(num):
    boards = []

    for i in range(num):
        boards.append(empty_board())

    return boards

def mark_number(number, board, board_number, marked_boards):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == number:
                marked_boards[board_number][row][col] = 1
                if check_bingo(marked_boards[board_number]):
                    return board_number
    return marked_boards

def check_bingo(marked_board):
    for row in range(len(marked_board)):
        marked = 0
        for col in range(len(marked_board[row])):
            if marked_board[row][col] == 1:
                marked += 1
        if marked == 5:
            return True
    for col in range(len(marked_board[0])):
        marked = 0
        for row in range(len(marked_board)):
            if marked_board[row][col] == 1:
                marked += 1
        if marked == 5:
            return True
    return False

def check_bingos(marked_boards):
    for i, board in enumerate(marked_boards):
        if check_bingo(board):
            return i
    return -1

def find_winning_board_number(random_numbers, boards, marked_boards):
    for number in random_numbers:
        for i, board in enumerate(boards):
            if mark_number(number, board, i, marked_boards) == i:
                return [number, i]
    return -1

def calculate_final_score(boards, marked_boards, board_number, last_number):
    sum_unmarked = 0
    for row in range(len(marked_boards[board_number])):
        for col in range(len(marked_boards[board_number][row])):
            if marked_boards[board_number][row][col] == 0:
                sum_unmarked += boards[board_number][row][col]

    return sum_unmarked * last_number

def part1(file="day4input.txt"):
    random_numbers = get_random_numbers(file)
    boards = get_boards(file)
    marked_boards = empty_boards(len(boards))
    winning_number = find_winning_board_number(random_numbers, boards, marked_boards)[0]
    winning_board_number = find_winning_board_number(random_numbers, boards, marked_boards)[1]

    return calculate_final_score(boards, marked_boards, winning_board_number, winning_number)

def part2(file="day4input.txt"):
    random_numbers = get_random_numbers(file)
    boards = get_boards(file)
    marked_boards = empty_boards(len(boards))
    last_number = 0

    while len(boards) > 1:
        winning_board_number = find_winning_board_number(random_numbers, boards, marked_boards)[1]
        boards.pop(winning_board_number)
        marked_boards.pop(winning_board_number)

    while check_bingo(marked_boards[0]) != True:
        last_number = find_winning_board_number(random_numbers, boards, marked_boards)[0]

    return calculate_final_score(boards, marked_boards, 0, last_number)

def main():
    print(part1())
    print(part2())

if __name__ == "__main__":
    main()