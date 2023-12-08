import os
import bcrypt
# Opens list of passwords
print(os.getcwd())
file = open("commonPasswords.txt", "r")
common_passwords = file.readlines()
# Hash of the password to be attacked
hashed_password = input("Enter the BCrypt hash: ")
#print(hashed_password)
#Runs popular passwords and hash them in BCrypt to compare to the given hash
i = 0
answr = False
#hashes every password in the dictionary
for line in common_passwords:
    temp_line = line.rstrip().encode('utf-8')
    temp_hash = hashed_password.rstrip().encode('utf-8')
    check = ""
    #compares hashed passwords to inputted hash
    if bcrypt.checkpw(temp_line, temp_hash):
        print("Password Found: " + line)
        answr = True
        break
    else:
        i += 1
        continue

if answr == False:
    print("Password not found")
    file.close()