letters_list = ['a', 'b', 'c', 'd']
for letter in letters_list:
    print letter

a = 8*7

div2_test values = [1, 58, 9928, 464637]
for number in div2_test_valus:
    print(div2_add20(number))

test_list = list(range(15))
test_list

for number in test_list
    # print (div2_add20(number))
    print("I am making some modifications to",number)

# This was me playing a bit with nestd for-loops, if statemnts, etc. It worked!
for number in test_list:
    # print(div2_add20(number))
    if number == 0:
        print("This is a zero, dummy. What did you think was gonna happen?")
    else:
        print(number)
        if number % 2 == 0:
            print("I am making some modifications to a number I dare you to do something about it! By the way, this number is even.")
        #print("I am making some modifications to",number,"and I dare you to do something about it! By the way, this number is even.")
        elif number % 3 == 0:
            print("I am making some modifications to a number I dare you to do something about it! By the way, this number is not even, but it is divisible by three.")
        #print("I am making some modifications to",number,"and I dare you to do something about it! By the way, this number is not even, but is divisible by three.")
        else: 
            print("I am making some modifications to a number that is neither even nor divisible by three.")
        #print("I am making some modifications to"number,"which is neither even nor divisible by three.")