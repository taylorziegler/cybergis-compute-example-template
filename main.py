i = 1
j = 1

for count in range(1, 10):
    print("%d %d" % (i, j), end=" ")
    i = i + j
    j = i + j

print("%d %d" % (i, j), end=" ")