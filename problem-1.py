import re
def check_email(email):
    parts = email.split("@")
    if(len(parts) != 2):
        return False
    #check if prefix of string is correct
    prefix = parts[0]
    sufix = parts[1]
    li = ['.','_','-']
    #considering only 3 special characters to be acceptable in prefix
    if(len(prefix) > 64 and len(prefix) == 0):
        return False
    # check if first and last characters are not special characters.
    if (prefix[0] in li) or (prefix[-1] in li):
        return False
    k = prefix.split('.')
    for each in k:
        if each[0] in li or each[-1] in li:
            return False
        if not(bool(re.match("^[A-Za-z0-9_-]*$",each))):
            return False
    dot = [i for i, letter in enumerate(prefix) if letter == '.']
    hypen = [i for i, letter in enumerate(prefix) if letter == '-']
    underscore = [i for i, letter in enumerate(prefix) if letter == '_']
    total = dot + hypen + underscore
    toatl = sorted(total)
    prev = None
    for each in total:
        if(prev == each - 1):
            return False
        prev = each
    if(len(sufix) > 253 and len(sufix) == 0):
        return False
    p = sufix.split('.')
    if len(p) < 2:
        return False
    for each in p:
        if not(bool(re.match("^[A-Za-z0-9-]*$",each))):
            return False
    return True

n = int(input("Enter number of emails n:"))
print("Enter each emails one by one. ")
emails = []
for i in range(0,n):
    email = input()
    emails.append(email)
    if check_email(email):
        print(email)
