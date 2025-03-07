import numpy as np
def Minimum(list):
    min = np.inf
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
    print(min)


Numbers = [5, 8, 51, 73, 37, 21, -8, 12, 6]

Minimum(Numbers)