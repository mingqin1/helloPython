class LookingGlass:

    # python invokes __enter__ with no arguments besides self.
    def __enter__(self):
        import sys
        # Hold the original sys.stdout.write method in an instance attribute for later use.
        self.original_write = sys.stdout.write
        #  Monkey-patch sys.stdout.write, replacing it with our own method.
        sys.stdout.write = self.reverse_write
        # Return the 'JABBERWOCKY' string just so we have something to put in the target variable what.
        return 'JABBERWOCKY'

    #  Our replacement to sys.stdout.write reverses the text argument and calls the original implementation.
    def reverse_write(self, text):
        self.original_write(text[::-1])

    #  Python calls __exit__ with None, None, None if all went well; if an exception is raised,
    # the three arguments get the exception data, as described next.
    def __exit__(self, exc_type, exc_value, traceback):
        # It’s cheap to import modules again because Python caches them.
        import sys
        # Restore the original method to sys.stdout.write
        sys.stdout.write = self.original_write
        #  If the exception is not None and its type is ZeroDivisionError, print a message
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            #   …and return True to tell the interpreter that the exception was handled.
            #  If __exit__ returns None or anything but True, any exception raised in the with block will be propagated.
            return True
