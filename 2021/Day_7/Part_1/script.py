import numpy as np
# opening the file in read mode
file = open("sample.txt", "r")
  
# reading the file
data = file.read()

# moving data lines to list
data_list = data.split(",")

# closing the file
file.close()

positions = np.array(data_list, int)
median = np.median(positions)
answer = 0

for i in range(0, len(positions)):
    answer += abs(positions[i] - median)
print(answer)