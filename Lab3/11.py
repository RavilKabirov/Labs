def permute(s, answer=""):
    if len(s) == 0:
        print(answer)
        return
    
    for i in range(len(s)):
        ch = s[i] 
        left_substr = s[:i] + s[i+1:]  
        permute(left_substr, answer + ch)

user_input = input()
permute(user_input)
