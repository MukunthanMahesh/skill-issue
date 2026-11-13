class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for tok in tokens:
            if tok == "+":
                y, x = st.pop(), st.pop()
                st.append(x + y)
            elif tok == "-":
                y, x = st.pop(), st.pop()
                st.append(x - y)
            elif tok == "*":
                y, x = st.pop(), st.pop()
                st.append(x * y)
            elif tok == "/":
                y, x = st.pop(), st.pop()
                st.append(int(x / y))
            else:
                st.append(int(tok))
        return st[-1]