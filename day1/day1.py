#read the input
set_data = open("input.txt").readlines()
input_values = []
for data in set_data:
    input_values.append(int(data))



#part 1
val1, val2 = 0, 0
for value1 in input_values:
    for value2 in input_values:
        if( (value1+value2) == 2020 ):
            val1, val2 = value1, value2
            break

print(val1*val2)

#part 2
val1, val2, val3 = 0, 0, 0
for value1 in input_values:
    for value2 in input_values:
        for value3 in input_values:
            if( (value1+value2+value3) == 2020 ):
                val1, val2, val3 = value1, value2, value3
                break
print(val1*val2*val3)