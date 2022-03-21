# opening the file in read mode
file = open("sample.txt", "r")
  
# reading the file
data = file.read()

# moving data lines to list
data_list = data.split(",")

# closing the file
file.close()

data_list = [int(x) for x in data_list]

for days in range(0, 80):
    for timer in range(0, len(data_list)):
        data_list[timer] -= 1
        if data_list[timer] < 0:
            data_list[timer] = 6
            data_list.append(8)
            
print(len(data_list))