class Solution:
    def isValid(self, s: str) -> bool:
        # idea : closing bracket cannot be before its opening bracket
        # push the opening brackets onto a stack
        # if we see a closing bracket, its corresponding opening bracket must be at the top of the stack
        # pop the top of the stack to make sure the types of brackets line up properly

        # use a dictionary to map corresponding opening, closing brackets
        closeopen_pairs = { ")" : "(", 
                            "]" : "[",
                            "}" : "{"}
        stack = []
        # for each character in the string
        for c in s:
            if c in closeopen_pairs: # if we see a closing bracket, because we make the closing brackets the key values
                if stack and stack[-1] == closeopen_pairs[c]: # if the stack is not empty and the last opening bracket matches the closing bracket
                    stack.pop() # remove that opening bracket from the stack
            
                else: # the opening and closing bracket do not match
                    return False
            else: # if we see an opening bracket, push it onto the stack
                stack.append(c)

        return True if not stack else False # the stack should be empty by the end (all opening bracket were popped because they met a corresponding closing bracket)
    