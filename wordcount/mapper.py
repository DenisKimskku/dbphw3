#!/usr/bin/env python3
import sys
import re
# Read each line from STDIN
for line in sys.stdin:
    # Get the words in each line (for English data)
    words = re.findall(r'\b[a-zA-Z]+\b', line)
    # Get the words in each line (for Korean data)
    #words = re.findall(r’\b[가-힣]+\b’, line)
    # Generate the count for each word
    for word in words:
        # Write the key-value pair to STDOUT to be processed by the reducer
        print ('{0}\t{1}'.format(word, 1))
