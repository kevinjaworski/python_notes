"""

Write a procedure that curates a new list of individuals that like to hike or ride motorcycles. The structure of a user profile is this:
User:
  - Name [STRING]
  - Age [INTEGER > 0] 
  - eMail  [STRING]
  - interests  [LIST]
       - Interests contains strings that describe the users interests, ranging from volleyball to wakeboarding.

Use this test data to verify your procedure works

"""
users = [
  {
    "name": "Shirley Hickman",
    "age": 43,
    "email": "shickman123@email.com",
    "interests": [
      "biking",
      "computers",
      "security"
    ]
  },
  {
    "name": "Arthur McInnis",
    "age": 23,
    "email": "amdub12@mail.com",
    "interests": [
      "whiskey",
      "motorcycles",
      "hiking",
      "fireworks"
    ]
  },

  {
    "name": "Leticia Green",
    "age": 36,
    "email": "greenthumbl.36@corpo.org",
    "interests": [
      "motorbikes",
      "books"
    ]
  }
]

# HINT: Your procedure should select both "Arthur McInnis" and "Leticia Green", but not "Shirley Hickman"

target = ["motorcycles", "motorbikes", "hiking"]
found = []

for entry in users:
    if any(item in target for item in entry["interests"]):
        found.append(entry["name"])    
print(found)        











# for entry in users:
#     check = any(item in target for item in entry["interests"])
#     if check is True:
#         print(entry["name"])


# # time O(n^2) space O(n)
# for user in users:
#     for interest in user["interests"]:
#         if interest in target:
#             print(user["name"])
#             break




# print(1 in [1, 2, 3])

# pairs = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6]]
# pairs = []
# for x in [1, 2, 3]:
#     for y in [4, 5, 6]:
#         pairs.append((x, y))


# print(pairs)