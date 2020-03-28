def make_averager():

    """ a closure is a function that retains the bindings of the free variables
     that exist when the function is defined,
     so that they can be used later when the
      function is invoked and the defining scope is no longer available.

    Returns:
        [type] -- [description]
    """
    #  series is the free  variable
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager

"""call  make_averager() to get a callable object avg
"""
avg = make_averager()

print(avg(10))
