'''
Question: 1
A Special Number is a number when the sum of the factorial of digits is 
equal to the original number (given number). For example, 145 is a Special 
Number because 145 = 1! + 4! + 5!.

Your task is to write a Python code that takes some numbers as user input 
(separated by a comma) in a single line and groups the Special & 
Non-Special numbers in a dictionary. Note that the values corresponding to 
the keys in that dictionary must be in tuple format.

Sample Input 1:
145, 346, 2, 83221, 7999888
Sample Output 1:
{'Special': (145, 2), 'Non-Special': (346, 83221, 7999888 )}
-----------------------------------------------------------------
Sample Input 2:
1431, 69716, 353, 7969828
Sample Output 2:
{'Special': (), 'Non-Special': (1431, 69716, 353, 7969828)}
'''

import math

nums = list(map(int, input().split(", ")))
count = 0
dict = {"Special": [],  'Non-Special': []}
for num in nums:
    fact = 0
    number = num
    while(num>0):
        mod = num % 10
        fact += math.factorial(mod)
        # print(mod, fact)
        num=num//10
    
    if number == fact:
        dict["Special"].append(number)
    else:
        dict["Non-Special"].append(number)

special, nonSpecial = tuple(dict["Special"]), tuple(dict["Non-Special"])
dict = {"Special": special, 'Non-Special': nonSpecial}
print(dict)

    