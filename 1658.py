nums = [5207,5594,477,6938,8010,7606,2356,6349,3970,751,5997,6114,9903,3859,6900,7722,2378,1996,8902,228,4461,90,7321,7893,4879,9987,1146,8177,1073,7254,5088,402,4266,6443,3084,1403,5357,2565,3470,3639,9468,8932,3119,5839,8008,2712,2735,825,4236,3703,2711,530,9630,1521,2174,5027,4833,3483,445,8300,3194,8784,279,3097,1491,9864,4992,6164,2043,5364,9192,9649,9944,7230,7224,585,3722,5628,4833,8379,3967,5649,2554,5828,4331,3547,7847,5433,3394,4968,9983,3540,9224,6216,9665,8070,31,3555,4198,2626,9553,9724,4503,1951,9980,3975,6025,8928,2952,911,3674,6620,3745,6548,4985,5206,5777,1908,6029,2322,2626,2188,5639]
x = 565610
count = 0

if nums[0] > x and nums[-1] > x:
    print("NOT POSSIBLE") 

while True:
    if not nums:
        print("-1")
        break

    last = nums[-1]
    start = nums[0]

    first_difference = x - start
    last_difference =  x - last
    print(first_difference, last_difference)


    if first_difference < 0 and last_difference < 0:
        count = -1
        break
    if first_difference < 0:
        first_difference = float('inf')
    if last_difference < 0:
        last_difference = float('inf')

    if first_difference <= last_difference:
        x = first_difference
        count+=1
        del nums[0]
        if x ==0:
            break
        print(nums, x)

    elif first_difference >= last_difference:
        x = last_difference
        count+=1
        del nums[-1]
        if x == 0:
            break
        print(nums, x)

    elif nums[0] > x or nums[-1] > x:
        break

print(count)


