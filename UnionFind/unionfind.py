p = [i for i in range(n+1)]
r = [1 for i in range(n+1)]


def find(x):
    if p[x] == x:
        return x
    else:
        return find(p[x])

def union(x,y):
    p_x = find(x)
    p_y = find(y)

    if p_x == p_y:
        return False

    if r[p_x] > r[p_y]:
        p[p_y] = p_x
        r[p_x] += r[p_y]  
    else:
        p[p_x] = p_y
        r[p_y] += r[p_x] 

    return True