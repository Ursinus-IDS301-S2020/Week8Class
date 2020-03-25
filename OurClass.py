#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 11:42:19 2020

@author: ctralie
"""

import pickle

students = pickle.load(open("students.dat", "rb"))
# Create a dictionary whose key is
# a class year, and whose value is a count
# of how many students are in that year
classyears = {}
for name in students:
    student = students[name]
    year = student['year']
    if not (year in classyears):
        classyears[year] = 1
    else:
        classyears[year] += 1
print(classyears)