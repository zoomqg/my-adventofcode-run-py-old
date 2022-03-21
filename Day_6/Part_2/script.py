import numpy as np
# opening the file in read mode
file = open("sample.txt", "r")
  
# reading the file
data = file.read()

# moving data lines to list
data_list = data.split(",")

# closing the file
file.close()

data_list = [int(x) for x in data_list]
fish_counter = np.zeros(9)

for i in range (0, 9):
    fish_counter[i] = data_list.count(i)

past_zero = 0

for days in range(0, 256):
    for i in range(0, 8):
        counter_copy = np.copy(fish_counter)
        fish_counter[i] = counter_copy[i+1]
    fish_counter[6] += past_zero
    fish_counter[8] = past_zero
    past_zero = counter_copy[0]

print(np.sum(fish_counter))