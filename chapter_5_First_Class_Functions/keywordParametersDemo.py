"""
 use of * and ** to “explode” iterables and mappings into separate arguments when we call a function
"""

# a keyword-only argument cls is used to pass “class” attributes
# To specify keyword-only arguments when defining a function, name them after the argument prefixed with *


def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


# A single positional argument produces an empty tag with that name.
print(tag('br'))

#  Any number of arguments after the first are captured by *content as a tuple.
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))

# Keyword arguments not explicitly named in the tag signature are captured by **attrs as a dict.
print(tag('p', 'hello', id=33))

# The cls parameter can only be passed as a keyword argument.
print(tag('p', 'hello', 'world', cls='sidebar'))

# Even the first positional argument can be passed as a keyword when tag is called.
print(tag(content='testing', name="img"))

my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
          'src': 'sunset.jpg', 'cls': 'framed'}

# Prefixing the my_tag dict with ** passes all its items as separate arguments,
# which are then bound to the named parameters, with the remaining caught by **attrs.
print(tag(**my_tag))


# If you don’t want to support variable positional arguments but still want keyword-only arguments,
#  put a * by itself in the signature

"""
Note that keyword-only arguments do not need to have a default value:
 they can be mandatory, like b in the following example.
"""
def f(a, *, b):
    return a, b

f(1, b=2)
