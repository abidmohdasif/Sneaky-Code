userstr = input("Enter a string: ")

def vowelsFunc(userstr):
    userlst = list(userstr.lower())
    vowels = ["a","e","i","o","u"]  # I have to add "u" to the list
    x = 0
    for i in userlst:
        if i in vowels:
            x += 1
    print(x)

vowelsFunc(userstr)