from clip import clip
from inspect import signature
sig = signature(clip)
str(sig)
print('str(sig): ', str(sig))

for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)
