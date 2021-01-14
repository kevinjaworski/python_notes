# for loop

# students = ["Jane", "John", "Kenn", "Sophia"]


# for i in students : 
#     print(i)
    
# state = {
#     "name" : "Wyoming",
#     "capital" : "Cheyenne",
#     "bird" : "Western Meadowlark",
#     "highest_point" : 13804
# }
# for item in state :
#     print(state.get(item))

# for item in state :
#     print(state[item])

# for item in state.values() :
#     print(item)

# for item in state.items():
#     value = item[1]
#     print(value)

# for key, value in state.items():
#     print(key,value)

# stations = ["Zarya","Skylab", "Mir"]

# for index, value in enumerate(stations):
#     print(f"The {value} station resides at position {index}")



#while loops

# x = 0

# while x < 10 : 
#     print('The loop is still going.')
#     x += 1
# print('The loop is done.')

# # menu example

# while True:
#     choice = input('Choose one: 1) Keep going. 0) Exit >')
#     if choice == '1':
#         print('The program will continue.')
#     elif choice == '0':
#         print('Goodbye, Dave.')
#         break
#     else:
#         print("I'm sorry, I can't do that, Dave.")

# loop controls

options = ['up', 'down', 'left', 'right']

for selection in options:
    if selection == 'left':
        print('Nope')
        break
else: # will only fire if the for loop is completed. If list is exhausted without clearing, will fire. 
    print('When does this fire?')

for selection in options:
    if selection == 'down':
        print("The air is thicker")
        continue
    print("You have moved in the dungeon")