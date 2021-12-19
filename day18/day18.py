
def convert(ln):
    return [int(s) if s.isdigit() else s for s in ln.rstrip()]


def out(lst):
    return ''.join(str(t) for t in lst)


def add(a, b):
    if not a:
        return b
    return ['['] + a + [','] + b + [']']


def isdigit(k):
    return isinstance(k, int)


def explode(a, n):
    left = a[n + 1]
    right = a[n + 3]

    for nn in range(n - 1, -1, -1):
        if isdigit(a[nn]):
            a[nn] += left
            break

    for nn in range(n + 5, len(a)):
        if isdigit(a[nn]):
            a[nn] += right
            break
    return a[:n] + [0] + a[n + 5:]


def split(a, n):
    val = a[n]
    return a[:n] + ["[", val // 2, ",", (val + 1) // 2, "]"] + a[n + 1:]


def actions(a):
    changed = True
    while changed:
        changed = False

        depth = 0
        for i, c in enumerate(a):
            if c == ']':
                depth -= 1
            elif c == '[':
                depth += 1
                if depth == 5:
                    a = explode(a, i)
                    changed = True
                    break
        if changed:
            continue

        for i, c in enumerate(a):
            if isdigit(c) and c >= 10:
                a = split(a, i)
                changed = True
                break
    return a


def magnitude(a):
    while len(a) > 1:
        for i in range(len(a)):
            if isdigit(a[i]) and isdigit(a[i + 2]):
                a = a[:i - 1] + [a[i] * 3 + a[i + 2] * 2] + a[i + 4:]
                break
    return a[0]


def solve():
    data = open('input.txt').readlines()
    data = [convert(d) for d in data]
    base = []
    for expr in data:
        base = add(base, expr)
        base = actions(base)
    return magnitude(base)


def solve2():
    data = open('input.txt').readlines()
    data = [convert(d) for d in data]
    maxval = 0
    for a in data:
        for b in data:
            if a == b:
                continue
            val = magnitude(actions(add(a, b)))
            if val > maxval:
                maxval = val
    return maxval


if __name__ == "__main__":
    print(solve())
    print(solve2())
