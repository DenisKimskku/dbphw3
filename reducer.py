#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
merged_numbers = []
for line in sys.stdin:
    numbers_str = line.split()
    numbers_int = [int(i) for i in numbers_str]
    if len(merged_numbers) == 0:
        merged_numbers = numbers_int
    else:
        l1 = merged_numbers
        l2 = numbers_int
        new_merged_numbers = []
        index1 = 0
        index2 = 0
        while index1 < len(l1) and index2 < len(l2):
            a = l1[index1]
            b = l2[index2]
            if a < b:
                new_merged_numbers.append(a)
                index1 += 1
            else:
                new_merged_numbers.append(b)
                index2 += 1
        if index1 == len(l1) and index2 < len(l2):
            new_merged_numbers.extend(l2[index2: ])
        if index1 < len(l1) and index2 == len(l2):
            new_merged_numbers.extend(l1[index1: ])
        merged_numbers = new_merged_numbers
print(" ".join([str(i) for i in merged_numbers]))
