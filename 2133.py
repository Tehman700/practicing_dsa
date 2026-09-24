matrix = [[1,1,1],[1,2,3],[1,2,3]]
n = len(matrix[0])
print(n)
ty = 0


for col in zip(*matrix):
    col_array = list(col)
    for i in range(1,n+1):
        if i not in col_array:
            ty = 1
        else:
            continue




for i in range(0,len(matrix)):
    arr = matrix[i]

    for i in range(1,n+1):
        if i not in arr:
            ty = 1
        else:
            continue


if ty == 1:
    print("FALSE")
else:
    print("TRUE")

        

