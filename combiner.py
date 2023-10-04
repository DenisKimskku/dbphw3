#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
for line in sys.stdin:
    numbers_str = line.split() 
    numbers_int = [int(i) for i in numbers_str]
    print(" ".join([str(i) for i in sorted(numbers_int)]))