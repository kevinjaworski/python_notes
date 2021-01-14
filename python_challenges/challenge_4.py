# Write a function that takes a number and returns a list of its digits. So for 2342 it should return [2,3,4,2].

def digits(s):
    digit_list = [int(i) for i in str(s)]
    return digit_list

# print(digits(1234))

# Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6]. You can do this quicker than concatenating them followed by a sort.

def list_combine(list1, list2):
    interim, i , j = [], 0 , 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            interim.append(list1[i])
            i += 1
        else:
            interim.append(list2[j])
            j += 1
    final = interim + list1[i:] + list2[j:]
    return final

one = [1,3,7,9]
two = [0,2,4,5,6,8]

print(list_combine(one,two))


# Write a function that combines two lists by alternatingly taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].

alpha = ['a', 'b', 'c']
num = [1,2,3]

def alternate(a,b):
    num = min(len(a), len(b))
    combined = [None]*(num*2)
    combined[::2] = a[:num]
    combined[1::2] = b[:num]
    combined.extend(a[num:])
    combined.extend(b[num:])
    return combined

# print(alternate(alpha,num))