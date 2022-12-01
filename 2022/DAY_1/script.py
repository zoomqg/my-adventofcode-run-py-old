import numpy as np

# opening the file in read mode
file = open("input.txt", "r")
  
# reading the file
data = file.read()

# moving data lines to list
data_list = data.split("\n")

# closing the file
file.close()

def part_1(input):
    highest_sum = 0
    current_sum = 0
    for i in input:
        if len(i) == 0:
            if current_sum > highest_sum:
                highest_sum = current_sum
            current_sum = 0
        else:
            current_sum += int(i)
    return highest_sum

def part_2(input):
    current_sum = 0
    arr = []
    for i in input:
        if len(i) == 0:
            arr.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(i)
    arr.sort()
    return arr[-1] + arr[-2] + arr[-3]

print(part_2(data_list))