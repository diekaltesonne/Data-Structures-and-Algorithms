class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        number = []
        power = 1
        while x:
            remainder = x % 10**power
            x -= remainder
            number.append(remainder // 10**(power-1))
            power += 1
        return number == number[::-1]