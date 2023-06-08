"""
    Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""

liste = []
def fizzBuzz(n: int):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            liste.append("FizzBuzz")
            continue
        elif i % 3 == 0:
            liste.append("Fizz")
            continue
        elif i % 5 == 0:
            liste.append("Buzz")
            continue
        else:
            liste.append(str(i))
    return liste  

print(fizzBuzz(5))