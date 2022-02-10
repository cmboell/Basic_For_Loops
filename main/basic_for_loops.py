"""
Assignment: Basic For Loops Assignment
Program: basic_for_loops.py
Author: Colby Boell
Last date modified: 02/10/2022

The purpose of this program is to demonstrate basic for loops. The first loop will
print out a list of floating numbers. The second for loop will print out the odd numbers
between 99 and 33 (including 99 and 33). One for loop uses list and one uses range.
"""

# declaring list
floating_numbers = [1.2, 5.6, 7.7, 10.3]
# for loop to print out the numbers in the list
for number in floating_numbers:
    print(number)

# for loop that uses range to print out the odd numbers between 99, 32 (to include both 99 and 33)
for number in range(99, 32, -2):
    print(number)

"""
Results:
From first loop:
1.2
5.6
7.7
10.3

From second loop:
99
97
95
93
91
89
87
85
83
81
79
77
75
73
71
69
67
65
63
61
59
57
55
53
51
49
47
45
43
41
39
37
35
33

"""
