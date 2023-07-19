"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII,
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
""""""
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
"""

def romanToInt(s):
    romanTable = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    
    s = s.replace("IV","IIII").replace("IX","VIIII")
    s = s.replace("XL","XXXX").replace("XC","LXXXX")
    s = s.replace("CD","CCCC").replace("CM","DCCCC")

    total = 0
    for i in s:
        total += romanTable[i]
    return total
"""
#2
def romanToInt(s):
    romanTable = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    prevValue = romanTable[s[0]]
    total = 0
    
    for current in s:
        if romanTable[current] > prevValue:
            total -= (prevValue * 2) #*2 because we already add prevValue to total 
            
        total += romanTable[current]
        prevValue = romanTable[current]
    return total"""


"""
#ilk aklıma gelen çözüm
def romanToInt(s):
    romanTable = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    x = 0
    count = 0
    for i in s:
        if (i == "V" and s[count-1] == "I") or (i == "X" and s[count-1] == "I"):
            x -= 2
        if (i == "L" and s[count-1] == "X") or (i == "C" and s[count-1] == "X"):
            x -= 20
        if (i == "D" and s[count-1] == "C") or (i == "M" and s[count-1] == "C"):
            x -= 200 
        x += romanTable[i]
        count += 1
    return x
"""
        
print(romanToInt("MMMCMXCIX"))
