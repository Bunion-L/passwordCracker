import os
import hashlib
#Opens list of passwords
print(os.getcwd())
file = open("commonPasswords.txt", "r")
common_passwords = file.readlines()
#Hash of the password to be attacked
hashed_password = input("Enter the MD5 hash: ")
#print(hashed_password)
#Runs popular passwords and hashes them in MD5 to compare to the given hash
i = 0
answr = False
#hashes every password in the dictionary
while i < len(common_passwords):
    possible_password = common_passwords[i].rstrip()
    hashed_possible_password = hashlib.md5(bytes(possible_password, 'utf-8')).hexdigest()
    #compares hashed passwords to inputted hash
    if hashed_possible_password == hashed_password:
        print(f"Password found: {possible_password}")
        answr = True
        break
    else:
        i += 1
        continue
#prints "password not found" if the password is not in the dictionary
if answr == False:
    print("Password not found")
    file.close()