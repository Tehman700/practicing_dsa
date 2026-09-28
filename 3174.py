s = "pl5v0jttxe9acvd0t9vtxwrhvwajpasfe2nhtws48pweam4vsomd79nw14ed"

for ch in s:
    if ch in '0123456789':        
        indd = s.index(ch)
        prev = indd-1
        s[indd] = ""
        s[prev] = ""
    else:
        continue

print(s)
