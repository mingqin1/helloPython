
from clip_annot import clip
from inspect import signature
sig = signature(clip)
sig.return_annotation
print('sig.return_annotation: ', sig.return_annotation)

for param in sig.parameters.values():
    note = repr(param.annotation).ljust(13)
    print(note, ':', param.name, '=', param.default)
