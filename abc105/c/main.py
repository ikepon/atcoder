n = int(input())

ans = []

if n % 2 == 1:
    ans.append(1)
else:
    ans.append(0)

for i in range(1, 35):
    a, mod = divmod(n, -2 ** i)
    print(a, mod)
    ans.insert(0, a)
    n = mod

ans_p = ''.join(map(str, ans))

print(int(ans_p))
