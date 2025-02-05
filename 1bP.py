num = int(input("Enter your Age: "))
def election(number):
    if number >= 18:
        return "You can vote"
    else:
        return "You cannot vote"

print(election(num))