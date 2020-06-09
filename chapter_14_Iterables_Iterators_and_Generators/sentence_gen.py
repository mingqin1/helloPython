import re
import reprlib

# Sentence implemented using a generator function

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        #  have not been lazy because the __init__ eagerly builds a list of all words in the text, binding it to the self.words attribute. This will entail processing the entire text, and the list may use as much memory as the text itself (probably more; it depends on how many nonword characters are in the text).
        # Most of this work will be in vain if the user only iterates over the first couple words.
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    #  a generator yields or produces values
    def __iter__(self):
        for word in self.words:
            yield word
        return
