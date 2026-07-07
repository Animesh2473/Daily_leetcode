class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        x = -1
        if len(s)%2 == 0:
            for i in range(len(s)//2):
                if s[i] != s[x]:
                    return False
                x -= 1
        else:
            for i in range((len(s)-1)//2):
                if s[i] != s[x]:
                    return False
                x-= 1
        return True