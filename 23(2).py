def f(x, y, n, m):
    if x == y: return 1
    if x > y: return 0

    if n < 2 and m < 2:
        return f(x + 1, y, n + 1, 0) + f(x * 2, y, 0, m + 1)
    if n >= 2:
        return f(x * 2, y, 0, m + 1)
    if m >= 2:
        return f(x + 1, y, n + 1, 0)


print(f(1, 16, 0, 0))