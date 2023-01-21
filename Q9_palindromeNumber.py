def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False

    reversed_num = 0
    num = x
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    if reversed_num == x:
        return True
    return False