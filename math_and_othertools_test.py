# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 11:32:52 2019

@author: Igor Geyn
"""

import webbrowser
import math

input_val = input("Which number would you like to round? ")
input_task = input("Would you like to round up or down? ")
task_rdup = ["Up","up","U","u","P","p"]
task_rddn = ["Down","down","D","d","N","n"]
if any([x in input_task for x in task_rdup]):
    #print(f"Thanks for letting me know that you would like to round {input_val}.")
    answer = (math.ceil(float(input_val)))
    print("The answer is " + str(math.ceil(float(input_val))) + ".")
elif any([x in input_task for x in task_rddn]):
    answer = (math.floor(float(input_val)))
    print("The answer is " + str(math.floor(float(input_val))) + ".")
else: print("Well, let me know if you change your mind!")