import random

r = int(random.randrange(20, 50))
print(r)

for i in range(r):
    if (i+1) % 10 == 0:
        if (i+1) // 10 in(3,6,9):
            print(((i + 1) // 10) * '뽀', '숑짝', sep='')
        else:
            print(((i + 1) // 10) * '뽀', '숑', sep='')
    elif (i+1) % 10 in(3,6,9):
        if (i+1) // 10 in(3,6,9):
            print('짝짝')
        else:
            print('짝')
    elif (i+1) // 10 in(3,6,9):
        print('짝')
    else:
        print(i+1)

