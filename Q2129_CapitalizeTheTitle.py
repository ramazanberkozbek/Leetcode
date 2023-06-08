"""You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. Capitalize the string by changing the capitalization of each word such that:

If the length of the word is 1 or 2 letters, change all letters to lowercase.
Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
Return the capitalized title."""
def capitalizeTitle(x: str) -> str:
    x = x.split(" ")
    y = ""

    for i in range(len(x)):
        if len(x[i]) <= 2:
            x[i] = x[i].lower()
        else: x[i] = x[i].title()
        if i != len(x)-1:
            y += x[i] + " "
        else: y += x[i]
    
    return y

print(capitalizeTitle("united states of america"))