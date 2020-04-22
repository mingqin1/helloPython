import array as array

numbers = array.array('h', [-2, -1, 0, 1, 2])
mem = memoryview(numbers)
len(mem)

mem[0]

mem_oct = mem.cast('B')


print(mem_oct.tolist())

mem_oct[5] = 4
print(numbers)
