def f(a, *, b):
    """

    Arguments:
        a {[type]} -- [description]
        b {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    return a, b


print('f( 1, c=2): ', f(1, b=2))
