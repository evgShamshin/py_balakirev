def fact_rec(n, comp=1, step=1, l = []):
    if n == 0:
        return 1
    elif step <= n:
        comp *= step
        l.append(comp)
        step += 1
        fact_rec(n, comp, step)
    return l[-1]


print(fact_rec(int(input())))