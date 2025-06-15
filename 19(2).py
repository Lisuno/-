# def f(x, y, h):
#     if x + y >= 75 and h == 2: return True
#     if x + y < 75 and h == 2: return False
#     if x + y >= 75: return False
#
#     return f(x + 1, y, h + 1) or f(x + x, y, h + 1) or f(x, y + 1, h + 1) or f(x, y + y, h + 1)
#
# for s in range(1, 68):
#     if f(s, 7, 0):
#         print(s)

# def f(x, y, h):
#     if x + y >= 75 and h == 3: return True
#     if x + y < 75 and h == 3: return False
#     if x + y >= 75: return False
#
#     if h % 2 != 0:
#         return f(x + 1, y, h + 1) and f(x + x, y, h + 1) and f(x, y + 1, h + 1) and f(x, y + y, h + 1)
#     else:
#         return f(x + 1, y, h + 1) or f(x + x, y, h + 1) or f(x, y + 1, h + 1) or f(x, y + y, h + 1)
#
# for s in range(1, 68):
#     if f(s, 7, 0):
#         print(s)

# def f(x, y, h):
#     if x + y >= 75 and h == 3: return True
#     if x + y < 75 and h == 3: return False
#     if x + y >= 75: return False
#
#     if h % 2 != 0:
#         return f(x + 1, y, h + 1) and f(x + x, y, h + 1) and f(x, y + 1, h + 1) and f(x, y + y, h + 1)
#     else:
#         return f(x + 1, y, h + 1) or f(x + x, y, h + 1) or f(x, y + 1, h + 1) or f(x, y + y, h + 1)
#
# for s in range(1, 68):
#     if f(s, 7, 0):
#         print(s)

def f(x, y, h):
    if x + y >= 75 and h == 2: return True
    if x + y < 75 and h == 2: return False
    if x + y >= 75: return False

    if h % 2 == 0:
        return f(x + 1, y, h + 1) and f(x + x, y, h + 1) and f(x, y + 1, h + 1) and f(x, y + y, h + 1)
    else:
        return f(x + 1, y, h + 1) or f(x + x, y, h + 1) or f(x, y + 1, h + 1) or f(x, y + y, h + 1)

for s in range(1, 68):
    if f(s, 7, 0):
        print(s)
print()

def f(x, y, h):
    if x + y >= 75 and (h == 2 or h == 4): return True
    if x + y < 75 and h == 4: return False
    if x + y >= 75: return False

    if h % 2 == 0:
        return f(x + 1, y, h + 1) and f(x + x, y, h + 1) and f(x, y + 1, h + 1) and f(x, y + y, h + 1)
    else:
        return f(x + 1, y, h + 1) or f(x + x, y, h + 1) or f(x, y + 1, h + 1) or f(x, y + y, h + 1)

for s in range(1, 68):
    if f(s, 7, 0):
        print(s)