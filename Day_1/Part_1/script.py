answer = 0
# opening the file in read mode
file = open("numbers.txt", "r")
  
# reading the file
data = file.read()

# moving data lines to list
data_list = data.split("\n")

# closing the file
file.close()

#data_list = [int(i) for i in data_list]

for i in range(0, len(data_list)):
    # converting array values from string to numbers
    data_list[i] = int(data_list[i])
    # skipping first index
    if i == 0:
        continue
    if data_list[i] > data_list[i-1]:
        answer += 1

print(answer)