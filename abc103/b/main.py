a = input()
b = input()

compare = a

right = False
for str in reversed(a):
    compare = str + compare[:-1]
    if compare == b:
        right = True
        break

if right:
    print('Yes')
else:
    print('No')
