class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for operator in tokens:
            if operator=="+":
                st.append(st.pop()+st.pop())
            elif operator=="-":
                second,first=st.pop(),st.pop()
                st.append(first-second)
            elif operator=="*":
                st.append(st.pop()*st.pop())
            elif operator=="/":
                second,first=st.pop(),st.pop()
                st.append(int(first/second))
            else:
                st.append(int(operator))
        return st[0]
        