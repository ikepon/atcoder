a = input()

ans = 0

for s in a:
    if s == "+":
        ans += 1
    else:
        ans -= 1

print(ans)