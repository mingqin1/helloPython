# test runner for Tombola subclasses


import doctest

from tombola import Tombola

# Import modules containing real or virtual subclasses of Tombola for testing.
# modules to test
import bingo
import lotto
import tombolist
# import drum

TEST_FILE = 'tombola_tests.rst'
TEST_MSG = '{0:16} {1.attempted:2} tests, {1.failed:2} failed - {2}'


def main(argv):
    verbose = '-v' in argv
    # __subclasses__() lists the direct descendants that are alive in memory. That’s why we imported the modules to test,
    # even if there is no further mention of them in the source code: to load the classes into memory.
    real_subclasses = Tombola.__subclasses__()
    # Build a list from _abc_registry (which is a WeakSet)
    # so we can concatenate it with the result of __subclasses__().
    virtual_subclasses = list(Tombola._abc_registry)

    #  Iterate over the subclasses found, passing each to the test function.
    for cls in real_subclasses + virtual_subclasses:
        test(cls, verbose)


def test(cls, verbose=False):

    res = doctest.testfile(
        TEST_FILE,
        #  The cls argument—the class to be tested—is bound to the name ConcreteTombola
        # in the global namespace provided to run the doctest.
        globs={'ConcreteTombola': cls},
        verbose=verbose,
        optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
    tag = 'FAIL' if res.failed else 'OK'
    #  The test result is printed with the name of the class, the number of tests attempted, tests failed,
    #  and an 'OK' or 'FAIL' label.
    print(TEST_MSG.format(cls.__name__, res, tag))


if __name__ == '__main__':
    import sys
    main(sys.argv)
