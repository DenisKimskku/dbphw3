#!/usr/bin/env python3

sorted_list = []

with open('./output/part-00000', 'r') as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        string, number = line.split("\t")
        number = int(number)
        sorted_list.append((string, number))

sorted_list.sort(key=lambda x: x[1], reverse = True)

for i in range(30):
    print(sorted_list[i])
