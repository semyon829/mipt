#! /usr/bin/env python3

import sys
from imp import reload

current_key = None
sum_cnt = 0
sys.stdin = open(sys.stdin.fileno(), encoding='utf-8')
for line in sys.stdin:
    error, value = line.strip().split('\t', 1)
    value = int(value)
    if not current_key:
        current_key = error
    if error != current_key:
        print('{}\t{}'.format(current_key, sum_cnt))
        current_key = error
        sum_cnt = 0
    sum_cnt += value
if current_key:
    print('{}\t{}'.format(error, sum_cnt))