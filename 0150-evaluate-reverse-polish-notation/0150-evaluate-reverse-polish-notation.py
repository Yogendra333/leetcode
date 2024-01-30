class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def fun(st,n1,n2):
            s1,s2=1,1
            if n1<0:
                s1=-1
            if n2<0:
                s2=-1
            if st=='+':
                return n1+n2
            elif st=='-':
                return n1-n2
            elif st=='*':
                return n1*n2
            elif st=='/':
                return floor(abs(n1)/abs(n2))*(s1*s2)
        digits=[]
        for i in tokens:
            if i.isdigit() or (len(i)>1):
                digits.append(int(i))
            else:
                n1=digits.pop()
                n2=digits.pop()
                digits.append(fun(i,n2,n1))
        return digits[0]