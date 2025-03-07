def Maximimum(list):
    max = 0
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    return max



Numbers = [4, 52, 21, 95, 8, 25, 81]
print(Maximimum(Numbers))