s = input()
k = int(input())

ans = False

for n in range(0, k):
    str = s[n]
    int_str = int(str)
    if int_str != 1:
        print(str)
        ans = True
        break

if ans == False:
    print(1)
