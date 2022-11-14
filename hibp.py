# hibpython
# A simple module for haveibeenpwnd.com written in python which checks 
# if the password has been compromised or found in a data leak using the API from haveibeenpwnd.com
# Author : y5hn4v (https://github.com/y5hn4v)
# Version : 1.0.0
# Usage :
# - Clone the repository from github to your folder with your python program
# - import hibpython.hibp as hibp
# - example_variable = hibp.checkpwn(password=password) OR example_variable = hibp.checkpwn(password)


import requests
import hashlib


# Function to check if the password was compromised
def checkpwn(password):
    control = False

    if password == "":
        raise Exception("Password found empty")

    else:
        # To convert the password into a SHA-1 hash and then call the api 
        pwnhash = hashlib.sha1(password.encode("UTF-8")).hexdigest()
        pwnlist = requests.get(f"https://api.pwnedpasswords.com/range/{pwnhash[0:5]}").text.splitlines()
        # Checking if the hash matches with the list of hashes sent from haveibeenpwnd
        for hash in pwnlist:
            if pwnhash == pwnhash[0:5]+(hash[:hash.index(":")].lower()):
                control = True
                #Returns True and the number of times the password was spotted in the haveibeenpwnd database
                return True, hash[hash.index(":"):len(hash)] 
                exit()
        # If the hashes didnt match , returns False stating that the password is safe
        if control == False:
            return False