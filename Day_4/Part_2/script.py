import numpy as np


# opening the file in read mode
file = open("sample.txt", "r")
  
# reading the file
data = file.read()

# moving data lines to list
boards = data.split("\n")

# closing the file
file.close()

# moving numbers to other list
numbers = boards.pop(0).split(',')
# converting string list to int
numbers = [int(x) for x in numbers]
checked_numbers = []

# removing '' strings
boards = [x for x in boards if x != '']

# # reshaping an array
boards = [x.split(' ') for x in boards]
boards = sum(boards, [])
boards = [x for x in boards if x != '']
boards = np.array(boards, int).reshape(100, 5, 5)

break_point = 0
winners = []
for num in range(len(numbers)):
    if break_point == 1:
        break
    checked_numbers.append(numbers[num])
    # marking of all numbers
    checker = np.isin(boards, checked_numbers)
    # checking through all boards
    for brds in range(0, len(checker)):
        if break_point == 1:
            break
        if brds in winners:
            continue
        # checking through all axes
        if np.any(np.all(checker[brds], axis=1)) or np.any(np.all(checker[brds], axis = 0)):
            if len(winners) != 99:
                winners.append(brds)
            else:
                winning_board = np.copy(boards[brds])
                # deleting all marked numbers 
                for delete in range(0, len(checked_numbers)):
                    winning_board = winning_board[winning_board != checked_numbers[delete]]
                #calculating score
                print(np.sum(winning_board) * numbers[num])
                break_point = 1
                break