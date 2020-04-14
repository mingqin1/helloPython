#!/usr/bin/env python3
l = [10, 20, 30, 40, 50, 60]
print(l[:2])  # split at 2

print(l[2:])

"""
slicing objects

s[a:b:c] can be used to specify a stride or step c,
causing the resulting slice to skip items. The stride can also be negative,
returning items in reverse.

slice [start:stop:step],
"""

s = 'bicycle'
print(s[::3])
print(s[0:6:3])

print(s[::-1])

print(s[6:0:-2])
