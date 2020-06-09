import re
import reprlib

RE_WORD = re.compile('\w+')

#  Sentence is a sequence,
#  Why Sequences Are Iterable: The iter Function
class Sentence:

    def __init__(self, text):
        self.text = text
        # re.findall returns a list with all nonoverlapping matches of the regular expression, as a list of strings.
        self.words = RE_WORD.findall(text)

    # an object is considered iterable not only when it implements the special method __iter__, but also when it implements __getitem__,
    # as long as __getitem__ accepts int keys starting from 0.
    def __getitem__(self, index):
        return self.words[index]

    # To complete the sequence protocol, we implement __len__—but it is not needed to make an iterable object.
    def __len__(self):
        return len(self.words)

    # reprlib.repr is a utility function to generate abbreviated string representations of data
    # structures that can be very large.

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
