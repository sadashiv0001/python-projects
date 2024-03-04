class Matrix:
    def __init__ (self, matrix):

        self.matrix = matrix
        self.row = len(matrix)
        self.column = len(matrix[0]) if matrix else 0
    
    def PrintMatrix(self):
        print("rows:", self.row)
        print("columns:", self.column)
        # print("matrix:", self.matrix)

        for row in self.matrix:
            print(row)



if __name__ == "__main__":
    matrix_input = [[1, 2, 3, 4], [4, 5, 6], [7, 8, 9],[10,11,12]]

    matrixObj = Matrix(matrix_input)

    matrixObj.PrintMatrix()
