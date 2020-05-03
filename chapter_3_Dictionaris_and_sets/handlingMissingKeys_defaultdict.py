"""Build an index mapping word -> list of occurrences"""

import sys
import re
import collections

WORD_RE = re.compile(r'\w+')

# Create a defaultdict with the list constructor as default_factory.
index = collections.defaultdict(list)
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # If word is not initially in the index, the default_factory is called to produce the missing value,
            # which in this case is an empty list that is then assigned to index[word] and returned,
            # so the .append(location) operation always succeeds.
            index[word].append(location)

# print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])
