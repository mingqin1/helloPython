import inspect
from clip import clip
from tag import tag
from inspect import signature

sig = signature(clip)
print(str(sig))

for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)


sig = inspect.signature(tag)

my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
          'src': 'sunset.jpg', 'cls': 'framed'}
bound_args = sig.bind(**my_tag)

for name, value in bound_args.arguments.items():
    print(name, '=', value)


del my_tag['name']

bound_args = sig.bind(**my_tag)
