from operator import methodcaller

""" The function( upcase, hiphenate, etc) methodCaller creates calls a method by name on the object given as argument
"""
s = 'The time has come'
upcase = methodcaller('upper')
upcase(s)
print('upcase(s): ', upcase(s))

hiphenate = methodcaller('replace', ' ', '-')
hiphenate(s)
print('hiphenate(s): ', hiphenate(s))


