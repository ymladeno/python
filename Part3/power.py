#!/usr/bin/python3

L = []
for i in range(7): L.append(2**i)

X = 5

i = 2**X
if i in L:
    print('at index', L.index(i))
else:
    print(X, 'not found')

# for i in L:
    # if 2**X == i:
        # print('at index', L.index(i))
        # break;
    # else:
        # i = i + 1
# else:
    # print(X, 'not found')

# i = 0
# while i < len(L):
    # if 2**X == L[i]:
        # print('at index',i)
        # break;
    # else:
        # i = i + 1
# else:
    # print(X, 'not found')