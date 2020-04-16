import bisect
import sys

"""
Searching with bisect
bisect(haystack, needle) does a binary search for needle in haystack—which must be
a sorted sequence—to locate the position where needle can be inserted while maintaining
haystack in ascending order.
"""

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 29, 23, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)  # <1>
        offset = position * '  |'  # <2>
        print(ROW_FMT.format(needle, position, offset))  # <3>
    print(HAYSTACK)


if __name__ == '__main__':

    if sys.argv[-1] == 'left':    # <4>
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)  # <5>
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)
