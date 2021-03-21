#! /usr/bin/env python3

import sys
import re

sys.stdin = open(sys.stdin.fileno(), encoding='utf-8')
error_flag = 0
error = None
for line in sys.stdin:
    if re.match('\[', line):
        date, thread_name, line = re.split('\W+\s+', line.strip(), maxsplit=2)
        if error:
            print('{}\t{}'.format(error.split('(')[0], 1))
        error = None
        stacktrace = 0
        error_flag = 0
    if "ERROR" in thread_name:
        error_flag = 1
    if error_flag:
        if "Caused by" in line:
            stacktrace = 1
    if error_flag:
        if re.match('\s*at\s+', line):
            error = re.sub('\s*at\s+', '', line)
if error:
    print('{}\t{}'.format(error.split('(')[0], 1))
