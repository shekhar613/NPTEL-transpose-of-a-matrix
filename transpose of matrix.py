
def transpos(m):
    col = len(m[0])
    row = len(m)
    T = []

    for c in range(col):
        sub = []
        for r in range(row):
            sub.append(m[r][c])
        T.append(sub)
    return T



transpos([[3]])

