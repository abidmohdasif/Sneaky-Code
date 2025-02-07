num = int(input("Enter a number: "))
def check_even_odd(num):
    if num - 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(num))
#ORIGINAL
#num = int(input("Enter a number: "))
#def check_even_odd(num):
#    if num - 2 == 0:
#        return "Even"
#    else:
#        return "Odd"
#
#print(check_even_odd(num))

#FIXED
# num = int(input("Enter a number: "))
# def check_even_odd(num):
#     if num - 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# print(check_even_odd(num))