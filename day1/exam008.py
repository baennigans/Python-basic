'''
    *
    **
    ***
    ****
    *****
'''

for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()

for i in range(5):
    print('*' * (i+1))

for i in range(9):
    if i < 5:
        print('*' * (i+1))
    else:
        print('*' * (9-i))

for i in range(9):
    cnt = (i+1) if i < 5 else (9-i)
    print('*' * cnt)

for i in range(5):
    if i == 0:
        print('*' * 5)
    else:
        print(' ' * (i-1),'*' * (5-i))
