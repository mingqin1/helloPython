class A:
    def ping(self):
        print('ping of A:', self)


class B(A):
    def pong(self):
        print('pong of B:', self)


class C(A):
    def pong(self):
        print('PONG of C:', self)


class D(B, C):

    def ping(self):
        # The recommended way to delegate method calls to superclasses is the super() built-in function,
        super().ping()
        print('ping of D:', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


print('D.__mro__: ', D.__mro__)

print('++++++++++++++++++++++++++++++++++++++++++++')
#  d.pong() on an instance of D
d = D()
#  Simply calling d.pong() causes the B version to run.
print('d.pong(): ', d.pong())

print('++++++++++++++++++++++++++++++++++++++++++++')
# You can always call a method on a superclass directly, passing the instance as an explicit argument.
print('C.pong(d): ', C.pong(d))

print('++++++++++++++++++++++++++++++++++++++++++++')
d = D()
# The ping of D makes two calls
# The first call is super().ping(); the super delegates the ping call to class A; A.ping outputs this line.
# The second call is print('ping of D:', self), which outputs this line.
print('d.ping(): ', d.ping())


print('++++++++++++++++++++++++++++++++++++++++++++')
d = D()
# The five calls made by pingpong
# 1
# Call #1 is self.ping(), which runs the ping method of D, which outputs this line and the next one.

# 2
# Call #2 is super().ping(), which bypasses the ping in D and finds the ping method in A.

# 3
# Call #3 is self.pong(), which finds the B implementation of pong, according to the __mro__.

# 4
# Call #4 is super().pong(), which finds the same B.pong implementation, also following the __mro__.

# 5
# Call #5 is C.pong(self), which finds the C.pong implementation, ignoring the __mro__.

print('d.pingpong(): ', d.pingpong())
