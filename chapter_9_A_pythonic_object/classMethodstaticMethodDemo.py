class Demo:
    @classmethod
    def klassmeth(*args):
        #  klassmeth just returns all positional arguments.
        return args




print(Demo.klassmeth())
print(Demo.klassmeth('spam'))
