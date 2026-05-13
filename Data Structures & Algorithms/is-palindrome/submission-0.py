class Solution:
    def isPalindrome(self, s: str) -> bool:
        rs = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return rs == rs[::-1]