def pyramid(n):
    i = 0
    while i <= n:
        print('*' * i)
        i += 1  

# pyramid(5)


list1 = ["Testing", "this", "out.", "Hello", "World", "in", "a", "Frame"]

def frame(ls):
    top = max(len(i) for i in ls) + 4
    print("*" * top)
    for i in ls:
        f = ("* " + i)
        if len(f) + 1 == top:
            print(f + ' *')
        else:
            j = top - len(f) - 1
            print(f + (" ") * j + '*')
    print("*" * top)
    
frame(list1)


# list2 = [1,2,3,4,5,6]
# def rotator(n):
#     if i in ls
