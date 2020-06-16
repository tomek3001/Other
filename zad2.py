input_data = "[2,3,7,4,9], 10"

input_data = input_data.replace('[', '').replace(']', '').replace(' ', '')
input_data = [int(x) for x in input_data.split(",")]

input_list, lim = input_data[:-1], input_data[-1]

missing_numbers = [x for x in range(lim + 1) if x not in input_list]

print(missing_numbers)
