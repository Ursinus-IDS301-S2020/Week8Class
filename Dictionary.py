#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:04:54 2020

@author: ctralie

A basic example of dictionaries
"""
import numpy as np
import pickle

chris = {
            'year':'supersenior',
            'major':'ee',
            'brand':'acer',
            'grades':{
                    'audio':95,
                    'image':60,
                    'nbody':100
                    },
            10: [-1, 5, 2, 4]
        }
chris['favassignment'] = 'fractal'
del chris['grades']

keys = list(chris.keys())
values = list(chris.values())
for myvar in chris.keys():
    print(myvar, " value is ", chris[myvar])