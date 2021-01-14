# [Lists, Strings] Challenges
# Write a function that returns the largest element in a list

the_list = ["j", "ta", "oz", "apao"]

def return_largest(l):
    for i in l: 
        if type(i) == int:
            print(max(l))
            break
        else:
            highest = -1
            for i in l:
                if len(i) > highest:
                    highest = len(i)
            print(i)
            break
            
# return_largest(the_list)


def get_largest(col):
    if col:
        tmp = col[0]
        for i in col[1:]:
            if tmp < i:
                tmp = 1
        return tmp
    return None    

x = [1,2,3,4,5]
# print(get_largest(x))

# Write a function that checks whether an element occurs in a list

list_2 = [1, 6, 5, 1]

def return_in(check, list):
    if check in list: 
        print("Occurs")
    else: 
        print("Does not occur")

# return_in(2, list_2)

def is_in(ls, elm):
    for item in ls:
        if item == elm:
            return True
    return False

x = [1, 2, 3]
# print(is_in(x, 1))




# Write a function that returns the element s on odd positions in a list

list_4 = [20, 25, 100, 60, 6, 5, 1, "j", "ta", "oz", "apao"]

def return_odd(l):
    tmp = []
    for i in l: 
        if l.index(i) % 2 != 0:
            tmp.append(i)    
    return tmp    

# print(return_odd(list_4))

# Write a function that computes the running total of a list

list_3 = [20, 25, 100, 60]

def running_total(l):
    total = 0
    for i in l:
        total += i 
        print(total)

# running_total(list_3)      

# Write a function that tests whether a string is a palindrome

        
def is_palindrome(s):
    i = 0
    j =len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

# print(is_palindrome("appa"))



# [BONUS SPICY CHALLENGE]
# Write a function that reverses a list, if you can do it in place

list_5 = [1, 2, 3, 4, 5]

# def reverse_list(l):
#     l.reverse()
#     return l

# print(reverse_list(list_5))


def rev_inplace(arr):
    i = 0 
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

print(list_5)
rev_inplace(list_5)
print(list_5)
