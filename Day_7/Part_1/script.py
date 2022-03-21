# opening the file in read mode
file = open("sample.txt", "r")
  
# reading the file
data = file.read()

# moving data lines to list
data_list = data.split(",")

# closing the file
file.close()

data_list = [int(x) for x in data_list]

lowest_answer = 0

for subtrahend in range(0, len(data_list)):
    answer = 0
    for i in range(0, len(data_list)):
        answer += abs(data_list[i] - data_list[subtrahend])
    print(answer)
    if answer < lowest_answer or lowest_answer == 0:
        lowest_answer = answer
print(lowest_answer)