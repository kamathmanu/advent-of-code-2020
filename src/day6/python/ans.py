# Ideal python set algorithm solution

s1, s2 = 0, 0

for group in open("../input.txt").read().split("\n\n"):
    s1 += len(set(group.replace("\n", "")))
    s2 += len(set.intersection(
        *map(set, group.split())
    ))

print(s1)
print(s2)