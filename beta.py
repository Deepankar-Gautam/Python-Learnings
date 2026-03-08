#problem 1, find repeaitng characters in password
# psuedo code

password = ("passwordpassword")
empty_list = []
occurance_list = [] 

for ch in password:
    if ch in empty_list:
        occurance_list.append(ch) 
    else:
        empty_list.append(ch)

print (f"repeated characters : {occurance_list}")
# ----------------------------------------------------------------------------

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

