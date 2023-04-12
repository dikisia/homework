t1 = int(input())
t2 = int(input())
t3 = int(input())
if t1 < t2 < t3:
    print("Акция! ", (t1 + t2 + t3)/2)
elif t1 > t2 > t3:
    print("Акция! ", (t1 + t2 + t3)/3)
else:
    print(t1 + t2 + t3)