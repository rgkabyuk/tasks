a = [0, 1, 0, 0, 4, 5, 6, 7, 0, 8, -4, 0]
l = len(a)
for i in range(l):
    for j in range(l - i - 1):
        if a[j] < abs(a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]

for i in range(l):
  if a[i] == 0:
    a = a[:i]
    break

a
