from dis import dis

b = 6


def f3(a):
    global b
    print(a)
    print("insdie function ")
    print(b)
    b = 9


"""f3 return None
"""
print('f3(3): ', f3(3))

print(b)

dis(f3)
