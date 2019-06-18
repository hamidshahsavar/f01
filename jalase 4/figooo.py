def f(n):
    if n in (0, 1):
        return 1

    return f(n - 1) + f(n - 2)


for i in range(0, 10):
    print(f(i), end=', ')

print()
for b in range(0, 20):
    print(f(b), end=', ')
