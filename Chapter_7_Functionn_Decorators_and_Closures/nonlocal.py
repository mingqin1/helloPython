def make_averager():
    """nonlocal lets you flag a variable as a free variable even
        when it is assigned a new value within the function

    Returns:
        [type] -- [description]
    """
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


ave = make_averager()

print(ave(10))
print(ave(11))
