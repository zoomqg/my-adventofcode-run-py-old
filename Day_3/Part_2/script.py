ones = 0
zeros = 0

# opening the file in read mode
file = open("sample.txt", "r")
  
# reading the file
data = file.read()

# moving data lines to list
data_list = data.split("\n")

# closing the file
file.close()

oxyGenRating = data_list.copy();
c02ScrubRating = data_list.copy();

# i = row
# y = column

#finding oxyGenRating
for i in range(0, len(oxyGenRating[0])):
    if len(oxyGenRating) == 1:
        break
    for y in range(0, len(oxyGenRating)):
        if oxyGenRating[y][i] == '1':
            ones += 1
        elif oxyGenRating[y][i] == '0':
            zeros += 1
    if ones >= zeros:
        list_object_index = 0
        while list_object_index < len(oxyGenRating):
            if oxyGenRating[list_object_index][i] == '0':
                oxyGenRating.pop(list_object_index)
                list_object_index -= 1
            list_object_index += 1
    elif zeros > ones:
        list_object_index = 0
        while list_object_index < len(oxyGenRating):
            if oxyGenRating[list_object_index][i] == '1':
                oxyGenRating.pop(list_object_index)
                list_object_index -= 1
            list_object_index += 1
    list_object_index = 0
    ones = 0
    zeros = 0

# finding c02ScrubRating
for i in range(0, len(c02ScrubRating[0])):
    if len(c02ScrubRating) == 1:
        break
    for y in range(0, len(c02ScrubRating)):
        if c02ScrubRating[y][i] == '1':
            ones += 1
        elif c02ScrubRating[y][i] == '0':
            zeros += 1
    if ones < zeros:
        list_object_index = 0
        while list_object_index < len(c02ScrubRating):
            if c02ScrubRating[list_object_index][i] == '0':
                c02ScrubRating.pop(list_object_index)
                list_object_index -= 1
            list_object_index += 1
    elif zeros <= ones:
        list_object_index = 0
        while list_object_index < len(c02ScrubRating):
            if c02ScrubRating[list_object_index][i] == '1':
                c02ScrubRating.pop(list_object_index)
                list_object_index -= 1
            list_object_index += 1
    list_object_index = 0
    ones = 0
    zeros = 0
    
#converting binary numbers to decimal and finding final answer
print(int(oxyGenRating[0], 2) * int(c02ScrubRating[0], 2)) 
