class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()
        rev_s = cleaned[::-1]
        if rev_s == cleaned:
            return True
        else:
            return False