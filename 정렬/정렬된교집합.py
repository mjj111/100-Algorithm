def intersection(a, b,c):
    i = j = 0
    n = len(a)
    m = len(b)
    
    while i < n and j < m:
        if a[i] == b[j]:
            c.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    
    return c