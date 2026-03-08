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
