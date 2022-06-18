a = input()

if a[0] == 'A' and ('C' in a[2:-1]) and a[2:-1].count('C') == 1:
    str = a[1:2] + a[3:].replace('C', '')
    if str.islower():
        print('AC')
        quit()

print('WA')
