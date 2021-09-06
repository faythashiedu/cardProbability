# import random

# match = 0
# total = 0

# # pack12 = [("red") for _ in range(12)] + [("black") for _ in range(12)]

# for i in range(100000):
#     pack12 = [("red") for _ in range(12)] + [("black") for _ in range(12)]

#     rand_choice1 = pack12.pop(random.randint(0,23))
#     rand_choice2 = pack12.pop(random.randint(0,22))

#     if rand_choice2 == rand_choice1:
#         match+=1
#     total+=1

# print("Pck of 12", round(match/total,3))

# import random

# match = 0
# total = 0

# for i in range(100000):
#     pack48 = [("red") for _ in range(24)] + [("black") for _ in range(24)]

#     rand_choice1 = pack48.pop(random.randint(0,47))
#     rand_choice2 = pack48.pop(random.randint(0,46))

#     if rand_choice2 == rand_choice1:
#         match+=1
#     total+=1

# print("Pck of 48", round(match/total,3))

import random

match = 0
total = 0
for i in range(10000):
    pack3 = [("Goat") for _ in range(2)] + [("Car") for _ in range(1)]

    randomchoice1 = pack3.pop(random.randint(0,2))
    if randomchoice1 == "Car":
        match += 1
    total += 1    

print(round(match/total, 2))


for i in range(10000):
    pack3 = [("Goat") for _ in range(2)] + [("Car") for _ in range(1)]

    # print(pack3)
    randomchoice1 = pack3.pop(random.randint(0,2))
    # print(pack3)
    # print(randomchoice1)
    if "Car" in pack3:
        randomchoice1 = "Car"
    else:
        randomchoice1 = "Goat"

    if randomchoice1 == "Car":
        match += 1

    total += 1    
        
        

print(round(match/total, 2))

