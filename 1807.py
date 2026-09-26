s = "r(s)(hyb)(fu)yms(pw)u(m)(t)u(h)j(cxkc)iqv(k)(fv)tb(pbv)uc(i)(l)(ys)(gsvh)p(tdxt)fj(c)"
knowledge =[["m","bsm"],["s","s"],["hyb","sxsj"],["fu","zzro"],["l","n"],["ys","tty"],["k","veib"],["t","suyx"],["c","kzfw"],["gsvh","baub"],["pbv","dehp"],["pw","sic"],["fv","kc"],["cxkc","hhmr"],["i","ycqs"],["h","vid"]]

# s = "(a)(a)(a)aaa"
# knowledge = [["a","yes"]]


# s = "hi(name)"
# knowledge = [["a","b"]]


finals = []

i = 0
while i < len(s):
    if s[i] == '(':
        ty = []                        # reset per placeholder — patch 1
        i += 1
        while s[i] != ')':
            ty.append(s[i])
            i += 1
        val = ''.join(ty)

        matched = False
        for pair in knowledge:          # check ALL keys before deciding — patch 2
            key, value = pair[0], pair[1]
            if key == val:
                s = s.replace("(" + val + ")", value)
                matched = True
                break

        if not matched:
            s = s.replace("(" + val + ")", "?")
    else:
        i += 1

remove_chars = '(', ')'
result = ''.join(ch for ch in s if ch not in remove_chars)
print(result)








# def tehman(val):
#     for pair in knowledge:
#         key = pair[0]    
#         value = pair[1]
#         updatd = s.replace(key,value)
#         print(updatd)


#         if val == key:
#             return value

# ty = []
# final = []

# for i in range(0,len(s)):
#     if s[i] == '(':                # 0
#         while True:
#             ty.append(s[i+1])      # 1
#             i=i+1

#             if s[i+1] == ')':
#                 val = ''.join(ty)
#                 answer = tehman(val)
#                 # print(val, " ", answer)
#                 updated = s.replace(val,answer)
#                 ty = []
#                 final.append(answer)
#                 break

#     else:
#         continue
