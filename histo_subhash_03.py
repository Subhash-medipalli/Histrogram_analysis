"""
Author : Subhash Medipalli
File Name : histo_subhash_03.py
Purpose : Analyzing text using histogram technique
Revisions :
    00 : Announce
    01 : prompt, get user response and using necessary for and if loops to analyze the characters count
    02 : Printing the variable and number of times it has been repeated

"""
### Step 1 : Announce

# Announce
print("Text analysis using histogram technique \n")

### Step 2 : prompt, get user response and using necessary for and if loops to analyze the characters count

user_inp = input('Enter text to analyze ... \n')
print("\n\n")
all_caps = user_inp.upper()
# upper() to covert user input to capital letters
all_caps = all_caps.strip(',.')
# strip() to remove spaces, commas and full stops
hiN = 0
hiC = ''  # empty string
bar = '='  # converting equals to sign to string

for b in range(65,91):
    # For loop is used to access the sequence of number from 65-90
    count = 0
    for i in all_caps:
        # For loop is used to access the sequence of characters from user input
        if b == ord(i):
            # If loop to check the variable b values is equal to UTF-8 value of ord(i)
            count += 1
            # Incrementing the count
    print(f'{chr(b)}:', bar * count)
    # printing letters using chr() to convert UTF-8 values to characters and bars according to repetition
    if hiN < count:
        # If the loop check weather hiN values is less than count
        hiN = count
        hiC = chr(b)  # assigning highest frequency character to hiC

### Step 3 : Printing the variable and number of times it has been repeated

print(f'\n\n\n {hiC} was used most ({hiN} times)')

