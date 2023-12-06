curr_sum = 0
prev_sum = 0
answer = 0
# opening the file in read mode
file = open("numbers.txt", "r")
  
# reading the file
data = file.read()

# moving data lines to list
data_list = data.split("\n")

# closing the file
file.close()

# converting string to integers
data_list = [int(i) for i in data_list]

for i in range(0, len(data_list) - 2):
    curr_sum = data_list[i] + data_list [i+1] + data_list[i+2]
    # skipping first index
    if i == 0:
        prev_sum = curr_sum
        continue

    if curr_sum > prev_sum:
        answer+=1
    prev_sum = curr_sum

print(answer)