#got the formula from here https://xn----8sbanwvcjzh9e.xn--p1ai/raznoe/formula-summy-chisel-ot-1-do-n-summa-chisel-ot-1-do-n-formula.html#_1_n

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
answer = 0
lowest_answer = 0
for lowest_integer in range(np.min(positions), np.max(positions)):
        for i in range(0, len(positions)):
            steps = abs(lowest_integer - positions[i])
            answer += steps * (steps+1) / 2
        if lowest_answer > answer or lowest_answer == 0:
            lowest_answer = answer
        answer = 0
print(lowest_answer)