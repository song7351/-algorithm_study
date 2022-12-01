a = list(input())
worda = []
wordb = []
for x in a:
    if not x.isdigit():
        worda.append(x)
    else:
        wordb.append(int(x))

worda.sort()
wordb.sort()
wordb = list(map(str, wordb))
print(''.join(worda) + ''.join(wordb))