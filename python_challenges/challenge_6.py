# given an list of numbers, return the one that 
# occurs an odd number of times. 
# your input list will only have one that 
# qualifys  

ls = [1,1,2,2,3,3,4,5,5,5,5]

def odd_occur(ls):
    odd_one_out = None
    for i in ls:
        if ls.count(i) % 2 != 0:
            odd_one_out = i
    return odd_one_out


# print(odd_occur(ls))

# Write a function that generates the Fibonacci 
# sequence 
# 1, 2, 3, 5, 8, 13, 21, 34.... 
# who's total elements is equal to the number 
# the user passes into the function 
# Bonus: Return a tuple (x, y) 
# where x is the list of all generated elements 
# and y is the sum of those elements 


import time
start_time = time.time()
def fibonacci(i):
    ls = [0,1]
    num = 0
    loop = 0
    while loop <= i:
        print(ls[0])
        num = sum(ls)
        ls[0] = ls[1]
        ls[1] = num
        loop = loop + 1

fibonacci(100)
print("Process finished --- %s seconds ---" % (time.time() - start_time))

