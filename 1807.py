s = "(name)is(age)yearsold"
knowledge = [["name","bob"],["age","two"],["age","two"],["ali","chaka"]]

def tehman(val):
    for pair in knowledge:
        key = pair[0]    
        value = pair[1]  
        if val == key:
            return value
        print(key, value)

ty = []
final = []

for i in range(0,len(s)):
    if s[i] == '(':                # 0
        while True:
            ty.append(s[i+1])      # 1
            i=i+1

            if s[i+1] == ')':
                val = ''.join(ty)
                answer = tehman(val)
                ty = []
                final.append(answer)
                break

    else:
        continue

    
    # print(s[i])

print(final)

