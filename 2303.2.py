string = "01234567890123"

digits_dict = {}

for digit in string:
    if digit in digits_dict:
        digits_dict[digit] += 1
    else:
        digits_dict[digit] = 1

print(digits_dict)