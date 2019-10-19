# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 11:04:02 2019

@author: Igor Geyn
"""

# This is code for a quick, Web-based calculator.

import webbrowser
import math

print("Hello!")
name = input("What is your name? ")
print(f"Nice to meet you, {name}! I hear you have some simple math to take care of.")
task_answer = input("Is that correct? ")
answer_pos = ["Yes","Yeah","Y","Yep","Positive"]
answer_neg = ["No","Nope","Nah","N"]
if any([x in answer_pos for x in task_answer]):
    print("Great! Let's get started. Here are some options")
    print('''
          1) Basic rounding (BR)
          2) Calculate tips (CT))
          3) Figure out when to leave the house (LH)
          4) <OPTION FOUR> <OFr>
          5) <OPTION FIVE> <OFv>
          ''')
    task_assign = input("Which task do you want to work on? ")
    task_rounding = ["Basic rounding","basic rounding","BR","br","Rounding","rounding","Round","round","BR","br"]
    task_tips = ["Calculate tips","calculate tips","Calculate","calculate","Tips","tips","CL","cl"]
    task_lh = ["Figure out when to leave the house","Leave house","leave house","House","house","LH","lh"]
    if any([x in task_assign for x in task_rounding]):
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
    if any([x in task_tips for x in task_assign]):
        print("We are still working on this feature -- check back in later!")
    if any([x in task_lh for x in task_assign]):
        print("We are still working on this feature -- check back in later!")
elif any([x in answer_neg for x in task_answer]):
    print("Gotcha.")
    other_functions = input("Is there anything else you want to do? ")
    if other_functions == "Learn about animals":
        webbrowser.open("https://www.google.com/search?sxsrf=ACYBGNR-yP-q6uoGTApxzQHtDZnX2bB3xQ%3A1571498095002&ei=biirXYzfPOeyggex04GwDQ&q=blue+footed+booby&oq=blue+footed+booby&gs_l=psy-ab.3..0i71l8.0.0..49320...0.2..0.0.0.......0......gws-wiz.T6lW3KHNepA&ved=0ahUKEwiMzt7NzqjlAhVnmeAKHbFpANYQ4dUDCAs&uact=5")
    #notanimals_share = ["Share something","Tell you about myself","Chat with you"]
    #elif any([x in notanimals_share for x in other_functions]):
    elif other_functions == "Share something":
        name = input('What is your name? ')
        fav_color = input('What is your favorite color? ')
        birth_year = input('When were your born? ')
        age = 2019 - int(birth_year)
        weight_lbs = input('I have to ask -- how much do you weigh? ')
        weight_kg = round(int(weight_lbs) / 2.205)
        msg = f'''I see. So...

        -- Your name is {name}, 
        -- Your favorite color is {fav_color}, 
        -- You are {age} years old, and
        -- You weigh approx. {weight_kg} kilos.'''
        print(msg)
        response = input('Is that right? ')
        if response == "Yes":
            print('Great! Glad to hear I got that right.')
        elif response == "No":
            print("I\'m sorry! I\'ll try better next time.")
    else: print("Have a great day!")
else: print("Well, let me know if you decide something!")
        
        