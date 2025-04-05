class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for char in s:
            if stack and ord(char)==ord(stack[-1]):
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
        