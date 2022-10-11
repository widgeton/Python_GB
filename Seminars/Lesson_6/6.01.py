actions = {
    "^": lambda x, y: str(float(x) ** float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}

res = "( 10 + 5 ) * 3 - 8 / 2"


def scob(line):
    lst = []
    i = 0
    while i < len(line):
        if line[i] == '(':
            m = line.index(")", i)
            lst.append(line[i + 1:m])
            i = m
        else:
            lst.append(line[i])
        i += 1
    return lst


# print(scob(res.split()))

def in_scob(lst):
    for i in range(len(lst)):
        if isinstance(lst[i], list):
            a, b, c = scob(lst[i])
            lst[i] = actions[b](a, c)
    return lst


def result(lst):
    prior = [i for i, j in enumerate(lst) if j in "*/"]
    while prior:
        t = prior[0]
        a, b, c = lst[t - 1: t + 2]
        lst.insert(t - 1, actions[b](a, c))
        del lst[t: t + 3]
        prior = [i for i, j in enumerate(lst) if j in "*/"]

    while len(lst) > 1:
        a, b, c = lst[: 3]
        del lst[:3]
        lst.insert(0, actions[b](a, c))

    return lst


s2 = '2 - ( 2 + 7 ) * 2'
s3 = '4 * ( 3 - 1 ) / ( 9 - 7 )'
print(in_scob(scob(s3.split())))
print(result(in_scob(scob(s3.split()))))
