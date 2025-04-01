class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def edited_string(input_string):
            stack=[]
            for char in input_string:
                if char=="#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack
        edited_s=edited_string(s)
        edited_t=edited_string(t)
        return edited_s==edited_t


