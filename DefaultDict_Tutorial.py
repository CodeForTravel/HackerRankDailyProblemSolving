from collections import defaultdict

indices = defaultdict(list)

n, m = map(int, input().split())

for i in range(1, n + 1):
    word = input().strip()
    indices[word].append(i)

for _ in range(m):
    word = input().strip()
    if word in indices:
        print(" ".join(map(str, indices[word])))
    else:
        print(-1)


# 5 2
# a
# a
# b
# a
# b
# a
# b
