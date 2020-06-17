import contextlib

# Apply the contextmanager decorator.
@contextlib.contextmanager
def looking_glass():
    import sys
    # Preserve original sys.stdout.write method.
    original_write = sys.stdout.write
    # Define custom reverse_write function; original_write will be available in the closure.

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    #  Create a variable for a possible error message; this is the first change
    msg = ''
    try:
        yield 'JABBERWOCKY'
    #  Handle ZeroDivisionError by setting an error message.
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'
    finally:
        # Undo monkey-patching of sys.stdout.write.
        sys.stdout.write = original_write
        if msg:
            #  Display error message, if it was set.
            print(msg)
