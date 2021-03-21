#! /usr/bin/env python3

import sys

current_key = None
sum_cnt = 0
sys.stdin = open(sys.stdin.fileno(), encoding='utf-8')
for line in sys.stdin:
    word, cnt = line.strip().split('\t', 1)
    cnt = int(cnt)
    if not current_key:
        current_key = word
    if word != current_key:
        print('{}\t{}'.format(word.lower(), sum_cnt))
        sum_cnt = 0
        current_key = word
    sum_cnt += cnt
print('{}\t{}'.format(word.lower(), sum_cnt))