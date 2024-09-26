def leadingZeroCount(row):
    ans = 0
    for num in row:
        if num == 0:
            ans +=1
        else:
            break
    return ans
def leadingNonZeroIndex(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return "none"
    
def rearrange(matrix):
    for _ in range(len(matrix)):
        for i in range(len(matrix)-1):
            if leadingZeroCount(matrix[i]) > leadingZeroCount(matrix[i+1]):
                matrix[i], matrix[i+1] = matrix[i+1], matrix[i]
    return matrix

def replace(rowi, rowj, scalar):
    if scalar != "none":
        final = []
        for i in range(len(rowi)):
            final.append(round(rowj[i] - rowi[i]*scalar, 3))
        return final
    else:
        return rowj

def scale(row):
    index = leadingNonZeroIndex(row)
    final = row
    if index != "none":
        scalar = 1/row[index]
        for i in range(len(final)):
            final[i] = round(final[i] * scalar, 3)
    return final

'''
Some test cases below
'''

# matrix = [
#     [0, -3, -6, 4, 9],
#     [-1, -2, -1, 3, 1],
#     [-2, -3, 0, 3, -1],
#     [1, 4, 5, -9, -7]
# ]

# matrix = [
#     [0, 3, -6, 6, 4, -5],
#     [3, -7, 8, -5, 8, 9],
#     [3, -9, 12, -9, 6, 15]
# ]

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# Forward Phase

matrix = []
m = int(input("Enter the number of rows:" ))
n = int(input("Enter the number of columns: "))

for _ in range(m):
    row = list(map(float, input("Enter row: ").split()))
    assert len(row) == n, f"The number of elements in row must be equal to {n}"
    matrix.append(row)


rearrange(matrix)

for i in range(len(matrix)-1):
    index = leadingNonZeroIndex(matrix[i])
    for j in range(i+1, len(matrix)):
        scalar = matrix[j][index]/matrix[i][index]
        matrix[j] = replace(matrix[i], matrix[j], scalar)
    rearrange(matrix)

for i in range(len(matrix)):
    matrix[i] = scale(matrix[i])

# Backward Phase

for i in range(len(matrix)-1, 0, -1):
    index = leadingNonZeroIndex(matrix[i])
    for j in range(i-1, -1, -1):
        if index != "none":
            scalar = matrix[j][index]/matrix[i][index]
            matrix[j] = replace(matrix[i], matrix[j], scalar)
        else:
            break
for row in matrix:
    print(row)