# if block

x = 0

if x > 0 :
    print("Hello")
elif x == 0 :
    print("World")
else:
    print('blank')


#ternary

is_on = 1

message = "I am on" if is_on == 1 else "I am stuck" if is_on == 3 else "I am off"
print(message)


a, b, c, d = False, True, True, True


print(c and d)

print((a and b and not a) or (not b) or (b and a) or (a and not a and not b))