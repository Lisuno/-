def f(x, y):
    if x == y: return 1
    if x < y: return 0
    if x == 12: return 0

    return f(x - 2, y) + f(x // 2, y)

print(f(42, 26) * f(26, 1))
