print("rasdgadg")


number = 0


MIN_32 = -2147483648
MAX_32 = 21474833647


if number < 0:
    newNumber = number * (-1)
    arr = [int(newNumber) for newNumber in str(newNumber)]

    arr.reverse()
    # 321
    final_numb = int("".join(str(i) for i in arr))
    # 321

    finalyy = final_numb * (-1)

    if MIN_32 <= finalyy <= MAX_32:
        print(finalyy)
    else:
        print("0")
else:
    arr = [int(number) for number in str(number)]

    arr.reverse()

    # ty = False
    # for i in arr:
    #     if ty == True:
    #         break
    #     elif arr[i-1] == 0:
    #         print(arr[i])
    #         arr.pop(i)
    #     else:
    #         ty = True

    final_numb = int("".join(str(i) for i in arr))
    if MIN_32 <= final_numb<= MAX_32:
        print(final_numb)
    else:
        print("0")




