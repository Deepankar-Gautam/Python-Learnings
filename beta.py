# Problem 1 : Does password contains any repeating character(s)?
# Method 1

password = input("Enter your password : ")

checking_list = []
occurrence_list = []

for ch in password:
    if ch in checking_list:
        occurrence_list.append(ch)
    else:
        checking_list.append(ch)

if len (occurrence_list) == 0:
    print (f"Your password has no repeating characters, great job")
else:
    print (f"Your password has following repeating characters : {", ".join(occurrence_list)}" )

# -------------------------------------------------------------------------------------

# Method 2

password = input("Enter your password : ")

dictionary = {}
repeated = "".split(",")
found = False

for ch in range (len(password)):
    if ch in dictionary:
        dictionary[ch] += 1
    else:
        dictionary[ch] = 1

for ch in dictionary:
    if dictionary[ch] > 1:
        found = True
        repeated = repeated + dictionary[ch] + ","

print(f"Your password has following repeating characters : {repeated}")

if found == False:
    print (f"Your password has no repeating characters, great job")

# -------------------------------------------------------------------------------------

# Problem 2 : Is the daily step goal reached ?

goal_achieved = 0
negative_steps = False

steps_list = input ('Enter you daily steps throughout the time with ", " : ').split(", ")

for steps in range(len(steps_list)):
    if int(steps_list[steps]) < 0:
        negative_steps = True
        print ("Invalid steps")
        exit(0)
    else: 
        continue

if negative_steps == False:
    step_goal = int(input ("Enter your step goal : "))
    for steps in range (len(steps_list)):
        if int(steps_list[steps]) >= step_goal:
            goal_achieved += 1
                
print (f"Days goal achieved : {goal_achieved}")            

