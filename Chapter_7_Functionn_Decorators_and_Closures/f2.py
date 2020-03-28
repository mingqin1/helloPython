from dis import dis

b = 6


def f2(a):
    print(a)
    print(b)
    b = 9


dis(f2)
