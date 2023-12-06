ones = 0
zeros = 0
gamma = ''
epsilon = ''

# opening the file in read mode
file = open("sample.txt", "r")
  
# reading the file
data = file.read()

# moving data lines to list
data_list = data.split("\n")

# closing the file
file.close()


# i = row
# y = column

for i in range(0, len(data_list[0])):
    for y in range (0, len(data_list)):
        if data_list[y][i] == '1':
            ones += 1
        elif data_list[y][i] == '0':
            zeros += 1
    if ones > zeros:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'
    zeros = 0
    ones = 0
    
#converting binary numbers to decimal and finding final answer
print(int(gamma, 2) * int(epsilon, 2))
