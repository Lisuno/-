# def f(s, h):
#     if s >= 68 and h == 2: return True
#     if s < 68 and h == 2: return False
#     if s >= 68: return False
#
#     return f(s + 1, h + 1) or f(s + 4, h + 1) or f(s * 5, h + 1)
#
# for s in range(1, 68):
#     if f(s, 0):
#         print(s)

# def f(s, h):
#     if s >= 68 and h == 3: return True
#     if s < 68 and h == 3: return False
#     if s >= 68: return False
#
#     if h % 2 != 0:
#         return f(s + 1, h + 1) and f(s + 4, h + 1) and f(s * 5, h + 1)
#     else:
#         return f(s + 1, h + 1) or f(s + 4, h + 1) or f(s * 5, h + 1)
#
# for s in range(1, 68):
#     if f(s, 0):
#         print(s)

def f(s, h):
    if s >= 68 and (h == 2 or h == 4): return True
    if s < 68 and h == 4: return False
    if s >= 68: return False

    if h % 2 == 0:
        return f(s + 1, h + 1) and f(s + 4, h + 1) and f(s * 5, h + 1)
    else:
        return f(s + 1, h + 1) or f(s + 4, h + 1) or f(s * 5, h + 1)

for s in range(1, 68):
    if f(s, 0):
        print(s)
print()
def f(s, h):
    if s >= 68 and (h == 2): return True
    if s < 68 and h == 2: return False
    if s >= 68: return False

    if h % 2 == 0:
        return f(s + 1, h + 1) and f(s + 4, h + 1) and f(s * 5, h + 1)
    else:
        return f(s + 1, h + 1) or f(s + 4, h + 1) or f(s * 5, h + 1)

for s in range(1, 68):
    if f(s, 0):
        print(s)