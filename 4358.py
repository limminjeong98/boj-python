# 4358 생태학
import sys
input = sys.stdin.readline

tree_dict = {}
total = 0

while True:
    data = input().rstrip()
    if not data:
        break
    tree_dict[data] = tree_dict.get(data, 0) + 1
    total += 1

tree_dict = sorted(tree_dict.items(), key=lambda x: (x[0]))
for key, value in tree_dict:
    # print(key, round(100 * value / total, 4))
    print('%s %.4f' % (key, 100 * value / total))
