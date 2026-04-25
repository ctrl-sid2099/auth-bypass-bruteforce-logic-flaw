# Wordlist Injector Tool
# ----------------------
# This script modifies a wordlist by inserting a specific value
# (username or password) after every N lines.
#
# Use case:
# Helps simulate bypassing brute-force protections where
# login attempt counters reset after a successful login.
#
# Inspired by a PortSwigger lab on brute-force logic flaws.

path=input("Path To Wordlist (Username/Password) :")
try:
    with open(path,"r") as f:
        lines=f.readlines()
except FileNotFoundError:
    print("File not Found. Please Check The Path")
    exit()

value = input("The Password/Username :")
if not value:
    print("Value Is Required, Please Enter The Value")
    exit()

try:
    position=int(input("At What Number of Line you Want Pass to Repeat? :"))
    if position <= 0:
        print("Position must be greater than 0")
        exit()
except ValueError:
    print("Please Enter A Valid Number")
    exit()

output = input("Enter output filename (leave blank for default): ")

if output == "":
    output = value + "_output.txt"

elif not output.lower().endswith(".txt"):
    output=output+ ".txt"

with open(output,"w") as y:
    counter=0
    for line in lines:
        y.write(line)
        counter +=1

        if counter == position:
            y.write(value + "\n")
            counter=0

print("[+] Wordlist Saved As: " + output + " [+]")


