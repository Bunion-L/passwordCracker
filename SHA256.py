import os
import hashlib
# Opens list of passwords
print(os.getcwd())
file = open("commonPasswords.txt", "r")
common_passwords = file.readlines()
# Hash of the password to be attacked
hashed_password = input("Enter the SHA256 hash: ")
#print(hashed_password)
# Runs popular passwords and encodes them in SHA256 to compare to the given hash
i = 0
answr = False
while i < len(common_passwords):
    possible_password = common_passwords[i].rstrip()
    #print(possible_password)
    hashed_possible_password = hashlib.sha256(bytes(possible_password, 'utf-8')).hexdigest()
    if hashed_possible_password == hashed_password:
            print(f"Password found: {possible_password}")
            answr = True
            break
    else:
        i += 1
        continue
if answr == False:
    print("Password not found")
    file.close()