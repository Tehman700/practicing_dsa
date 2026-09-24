nums = [1,2,3]

minumium = 0
ty = []

def sumss(n):
    total = 0
    n = abs(n)  # Handle negative numbers
    
    while n > 0:
        total += n % 10
        n //= 10
        
    return total

for i in range(0,len(nums)):

    index_sum = sumss(nums[i])
    if i == index_sum:
        ty.append(i)


if len(ty) == 0:
    print("-1")

ty.sort()
print(ty[0])






