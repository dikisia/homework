my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

first_key = list(my_dict.keys())[0]
last_key = list(my_dict.keys())[-1]
my_dict[last_key], my_dict[first_key] = my_dict[first_key], my_dict[last_key]

del my_dict[list(my_dict.keys())[1]]

my_dict['new_key'] = 'new_value'

print(my_dict)