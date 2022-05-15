matrix = [[1,2,3],[4,5,6],[7,8,9]]
# o/p --> [[1,4,7],[2,5,8],[3,6,9]]
transpose = [[0,0,0],[0,0,0],[0,0,0]]

''''[[[0][0],[0][1],[0][2]],[[1][0],[1][1],[1,2]],[[2][0],[2][1],[2][2]]]
-->
[[[0][0],[0][1],[0][2]],[[1][0],[1][1],[1,2]],[[2][0],[2][1],[2][2]]]'''

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
            transpose[j][i] = matrix[i][j]

print(transpose)
for t in transpose:
    print(t)


''' Program to transpose a matrix using list comprehension'''

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print(result)
for r in result:
   print(r)



def matrix_transpose(matrix):
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print(result)


matrix_transpose(matrix)


class MatrixTranspose():
    def __init__(self):
        self.matrix = [[1,2,3],[4,5,6],[7,8,9]]

    def matrix_transpose(self, matrix):
        result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        print(result)


mat_transpose = MatrixTranspose()
mat_transpose.matrix_transpose(matrix)
