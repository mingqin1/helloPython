def tag(name, *content, cls=None, **attrs):
    """ Generate one or more HTML tags.

    Arguments:
        name {string} -- A single positional argument produces an empty tag with that name.

        *content { tuple } -- Any number of arguments

    Keyword Arguments:
        cls {dict} -- a key argument  (default: {None})
        **attrs {dict} -- key arguments

    Returns:
        [type] -- [description]
    """
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
                         (name, attr_str, _content, name) for _content in content)
    else:
        return '<%s%s />' % (name, attr_str)


# content with no attributs

print("""tag('br'): """, tag('br'))

# contnet with attributs
# print("""tag( 'p','hello',  id=33): """, tag('p', 'hello', id=33))

print("""tag( 'p','hello', 'world,  id=33, name=usa): """,
      tag('p', 'hello', 'world', id=33, er='usa'))

my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
          'src': 'sunset.jpg', 'cls': 'framed'}

"""fixing the my_tag dict with ** passes all its items as separate arguments, which are then bound to the named parameters, with the remaining caught by **attrs.

"""
print('tag(**my_tag): ', tag(**my_tag))
