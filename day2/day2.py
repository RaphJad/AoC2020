import numpy as np
#read the input
set_data = open("input.txt").readlines()
numbers, policy, password = [[]], [], []

for i in range(len(set_data)):
    data = set_data[i].split()
    numbers[i]

for data in set_data:
    print(data)
    
    #split the data into numbers and policy
    numbers.append(data.split("-")[0])
    policy.append(data.split("-")[1])
    password.append(data.split("-")[2])
    print(numbers)
    print(policy)
    print(password)
