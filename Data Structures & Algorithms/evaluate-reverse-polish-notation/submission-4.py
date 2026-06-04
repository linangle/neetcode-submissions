class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        digitstack = []
        for s in tokens:
            if s == "+":
                summ = digitstack.pop() + digitstack.pop() 
                digitstack.append(summ) # push this onto the top of the stack
            elif s == "-":
                # 12- ==> 1 - 2, need to reverse popped order
                a, b = digitstack.pop(), digitstack.pop()
                diff = b - a
                digitstack.append(diff) 
            elif s == "*":
                digitstack.append(digitstack.pop() * digitstack.pop())
            elif s == "/":
                a, b = digitstack.pop(), digitstack.pop()
                digitstack.append(int(b / a))
            else: # if we get a number, push it onto the stack ( currently str --> convert to int)
                digitstack.append(int(s))
        
        return digitstack[0]

            
        