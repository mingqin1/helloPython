"""
If there is a default value, the annotation goes between the argument name and the = sign.
To annotate the return value, add -> and another expression between the ) and the :
at the tail of the function declaration. The expressions may be of any type.
The most common types used in annotations are classes, like str or int, or strings, like 'int > 0'

"""
def clip(text: str, max_len: 'int > 0' = 80) -> str:

    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # no spaces were found
        end = len(text)
    return text[:end].rstrip()


