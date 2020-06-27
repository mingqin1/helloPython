# A coroutine is defined as a generator function: with yield in its body.
def simple_coroutine():
    print('-> coroutine started')
    #  yield is used in an expression; when the coroutine is designed
    # just to receive data from the client it yields None—this is
    #  implicit because there is no expression to the right of the
    # yield keyword.
    x = yield
    print('-> coroutine received:', x)


my_coro = simple_coroutine()

# As usual with generators, you call the function to get a generator object back.
print('my_coro: ', my_coro)

#  The first call is next(…) because the generator hasn’t started so it’s not waiting in a yield and we can’t send it any data initially.
next(my_coro)
#  This call makes the yield in the coroutine body evaluate to 42; now the coroutine resumes and runs until the next yield or termination.
my_coro.send(42)

# In this case, control flows off the end of the coroutine body, which prompts the generator machinery to raise StopIteration, as usual.
