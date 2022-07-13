import numpy as np
#read the input
set_data = open("input.txt").readlines()
numbers, policy, password = [], [], []
for line in set_data:
    split = line.split(' ')
    min, max = int(split[0].split('-')[0]), int(split[0].split('-')[1])
    numbers.append([min,max])
    policy.append(split[1][0])
    password.append(split[2][0:len(split[2])-1])

#part 1
count = 0
for i in range(len(numbers)):
    if password[i].count(policy[i]) >= numbers[i][0] and password[i].count(policy[i]) <= numbers[i][1]:
        count += 1
print(count)



#part 2
count = 0
for i in range(len(numbers)):
    if(password[i][numbers[i][0]-1] == policy[i]):
        if(len(password[i]) >= numbers[i][1]):
            if(password[i][numbers[i][1]-1] != policy[i]):
                print(password[i][numbers[i][0]-1], password[i][numbers[i][1]-1])
                count += 1
            else:
                continue
    else:
        if(len(password[i]) >= numbers[i][1]):
            if(password[i][numbers[i][1]-1] == policy[i]):
                print(password[i][numbers[i][0]-1], password[i][numbers[i][1]-1])
                count += 1
            else:
                continue
print(count)