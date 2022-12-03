import string
import numpy as np
import pandas as pd

# opening the file in read mode
file = open("input.txt", "r")
  
# reading the file
data = file.read()

# moving data lines to list
data_list = data.split("\n")

# closing the file
file.close()

chars_arr = list(string.ascii_lowercase) + list(string.ascii_uppercase)

num_arr = list(range(1, 53))

aplhabet_series = pd.Series(data=num_arr, index=chars_arr)

def part_1(data):
    sum = 0
    splited_arr = []
    for string_to_split in data:
        s1 = string_to_split[:len(string_to_split)//2]
        s2 = string_to_split[len(string_to_split)//2:]
        splited_arr.append(s1)
        splited_arr.append(s2)
    
    final_data = np.array(splited_arr)
    final_data = np.reshape(final_data, (int(len(final_data) / 2), 2))
    
    for i in final_data:
        char = ''.join(set(i[0]).intersection(i[1]))
        sum += aplhabet_series[char]
    return(sum)
    
def part_2(data):
    sum = 0
    data_list = np.array(data)
    data_list = np.reshape(data_list, (int(len(data_list) / 3), 3))
    
    for i in data_list:
        first_comparison = ''.join(set(i[0]).intersection(i[1]))
        final_comparison = ''.join(set(first_comparison).intersection(i[2]))
        sum += aplhabet_series[final_comparison]
    return sum

print(part_2(data_list))