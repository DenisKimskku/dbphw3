#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
for line in sys.stdin:
    numbers_str = line.strip().split(",")
    print(" ".join(numbers_str))