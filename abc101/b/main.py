str = input()

ans = 0

for s in str:
    ans += int(s)

if int(str) % ans == 0:
    print('Yes')
else:
    print('No')
