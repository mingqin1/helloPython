#  bounded Arithemtic Progression  of numbers of any type?


class ArithmeticProgression:
    # __init__ requires two arguments: begin and step. end is optional, if it’s None, the series will be unbounded.
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end  # None -> "infinite" series

    def __iter__(self):
        # This line produces a result value equal to self.begin, but coerced to the type of the subsequent additions
        result = type(self.begin + self.step)(self.begin)
        # For readability, the forever flag will be True if the self.end attribute is None, resulting in an unbounded series.
        forever = self.end is None
        index = 0
        # This loop runs forever or until the result matches or exceeds self.end. When this loop exits, so does the function.
        while forever or result < self.end:
            # The current result is produced.
            yield result
            index += 1
            # The next potential result is calculated. It may never be yielded, because the while loop may terminate.
            result = self.begin + self.step * index
