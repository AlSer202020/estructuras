import random
for i in range(1,6):
    for j in range(i):
        n = random.randint(1,9)
        if n % 2 == 0:
            n = "p"
        print(n, end=" ")
    print(" ")