def LevenshteinOriginal(a, b):
    if len(b) == 0:
        return len(a)
    if len(a) == 0:
        return len(b)
    if a[0] == b[0]:
        return LevenshteinOriginal(a[1:], b[1:])

    return 1 + min(
        LevenshteinOriginal(a[1:], b),
        LevenshteinOriginal(a, b[1:]),
        LevenshteinOriginal(a[1:], b[1:])
    )


def WagnerFischer(a, b):
    arr = [[0 for _ in range(len(a) + 1)] for _ in range(len(b) + 1)]

    for i in range(len(a) + 1):
        arr[0][i] = i

    for i in range(len(b) + 1):
        arr[i][0] = i

    for c in range(1, len(a) + 1):
        for r in range(1, len(b) + 1):
            substitute = arr[r - 1][c - 1]

            if a[c - 1] != b[r - 1]:
                insert = arr[r - 1][c]
                delete = arr[r][c - 1]
                arr[r][c] = 1 + min(insert, delete, substitute)
            else:
                arr[r][c] = substitute

    return arr[-1][-1]
