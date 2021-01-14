# Create a function that takes in a number and returns it's 
# # length, you can't use the len() function 
  
# def length(n):
#     count = 0
#     string = str(n)
#     for i in string:
#         count += 1
#     return count

# print(length(100))



# # write a function that takes in two lists 
# # and only returns elements that are found in both 

# def in_both(ls1,ls2):
#     both = []
#     for i in ls1:
#         if i in ls2:
#             both.append(i)
#     return both

# first = [1,2,3,4,5]
# second = [4,5,6,7,8]

# print(in_both(first,second))


# write a function that checks for the larges number 
# palindrome from 1*1 up to x*y 
# example 1*11 is a 11 a palindrome, the  
# function should take an x and a y and  
# only give you back the largest 

import time
start_time = time.time()


def palindrome2(x,y):
    ls1, ls2= range(1, x+1), range(1, y+1)
    highest_found = []

    for j in ls1:
       for k in ls2:
            n = j * k
            if str(n) == str(n)[::-1]:
                highest_found.append(int(n))

    return(max(highest_found))

print(palindrome2(1234, 4321))
print("Process palindrome2 finished --- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
def instructor_palindrome(x, y):
    tmp = []
    for i in range(1, x+1):
        for j in range(1, y+1):
            s = str(i*j)
            if s == s[::-1]:
                tmp.append(i*j)

    return max(tmp)


print(instructor_palindrome(1234, 4321))
print("Process instructor_pal1 finished --- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
def instructor_palindrome2(x,y):
    return max([i*j 
        for i in range(1,x+1) 
        for j in range(1, y+1) 
        if str(i*j) == str(i*j)[::-1]
        ]) 

print(instructor_palindrome2(1234, 4321))
print("Process instructor_pal2 finished --- %s seconds ---" % (time.time() - start_time))