arr = [3,4,6,1,3,7,9,3]

# Two pointers approach

l = 0
r = len(arr) -1

# while l < r:
#     if arr[l] == arr[r]:
#         print("matched")
#     else:
#         print("not clasgdsdgf")

#     l+=1
#     r-=1



yr = [10,30,20,30,30]
iu = 30

l = 0
count = 0
r = len(yr) -1

while l <r:
    if yr[l] == iu:
        count +=1
    elif yr[r] == iu:
        count +=1
    else:
        continue

    l +=1
    r -=1

print(count)


