a = input()
if int(a[-1]) % 2 == 0:
    if sum(map(int, str(a))) % 3 == 0:
        print("ес")
else:
    print("неа")