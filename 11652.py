# 11652 카드
import sys
input = sys.stdin.readline

cdict = {}
n = int(input().rstrip())
for _ in range(n):
    card = int(input().rstrip())
    cdict[card] = cdict.get(card, 0) + 1

cdict = sorted(cdict.items(), key=lambda x: (x[1], -x[0]))
print(cdict[-1][0])
