#! /usr/bin/env python3

import sys
import re

sys.stdin = open(sys.stdin.fileno(), encoding='utf-8')

for line in sys.stdin:
    try:
        article_id, text = line.strip().split('\t', 1)
    except ValueError as e:
        continue
    words = re.split('\W*\s+\W*', text)
    for word in words:
        word = re.sub('\W', '', word)
        if (6 <= len(word) <= 9 and word[0].isupper()
                and word[1:].islower() and word.lower() not in words):
            print('{}\t1'.format(word))