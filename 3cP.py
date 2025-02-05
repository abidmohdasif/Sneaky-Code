string = input("Enter a string: ")
list = ["a", "e", "i", "o", "u"]
def vowel_count(s):
    count = 0
    for i in s:
        if i in list:
            count += 1
    return count

print(vowel_count(string))