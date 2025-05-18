class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        opening=n
        closing=n
        output=[]
        string=""
        def parentheses(n,opening,closing,string):
            if len(string)==2*n:
                output.append(string)
                return
            if opening>0:
                parentheses(n,opening-1,closing,string+"(")
            if opening-closing<0:
                parentheses(n,opening,closing-1,string+")")
        parentheses(n,opening,closing,string)
        return output
