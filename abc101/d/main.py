k = input()


def sk(n):
    ans = 0
    for s in n:
        ans += int(s)

    return ans


n = 1
ans_arr = []

for _ in range(0, 10 ** 15):
    condition_ok = True
    for m in range(1, 100):
        if n / sk(str(n)) > (n + m) / sk(str(n + m)):
            condition_ok = False
            break

    if condition_ok:
        ans_arr.append(n)
    if len(ans_arr) >= int(k):
        break
    n += 1

for ans in ans_arr:
    print(ans)
