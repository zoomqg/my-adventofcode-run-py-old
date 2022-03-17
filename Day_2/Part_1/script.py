movement = []
horizontalPosition = 0;
depth = 0;
# opening the file in read mode
file = open("sample.txt", "r")
  
# reading the file
data = file.read()

# moving data lines to list
data_list = data.split("\n")

# closing the file
file.close()

for i in range(0, len(data_list)):
    movement = data_list[i].split(' ')
    match movement[0]:
        case 'forward':
            horizontalPosition += int(movement[1])
        case 'up':
            depth -= int(movement[1])
        case 'down':
            depth += int(movement[1])

print('answer: ' + str(horizontalPosition * depth))