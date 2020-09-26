class Simplex:
    def __init__(self, matrix, D, z):
        self.matrix = matrix
        self.D = D
        self.z = z
        self.zD = 0
        self.row_index = 0
        self.column_index = 0

    def set_basis(self, row_index, column_index):
        self.row_index = row_index
        self.column_index = column_index

    def getBasis(self):
        (_, column_index) = self.findMinWithIndex(self.z)
        (_, row_index) = self.findBasis(self.getColumn(column_index))
        return (row_index, column_index)

    def simplex_method(self):
        (_, column_index) = self.findMinWithIndex(self.z)
        (_, row_index) = self.findBasis(self.getColumn(column_index))
        self.set_basis(row_index, column_index)
        self.findZ(row_index, column_index)
        for index in range(len(self.matrix)):
            if index != row_index:
                self.allRowsMinusBasicRow(row_index, index, column_index)

    def findZ(self, row_index, column_index):
        k = (-self.z[column_index]) / self.matrix[row_index][column_index]
        self.zD += self.D[row_index] * k
        nRow = list(map(lambda x: x * k, self.matrix[row_index]))
        for i in range(len(self.z)):
            self.z[i] += nRow[i]

    def allRowsMinusBasicRow(self, basic_row_index, row_index, column_index):
        k = -self.matrix[row_index][column_index] / self.matrix[basic_row_index][column_index]
        self.D[row_index] += self.D[basic_row_index] * k
        nRow = list(map(lambda x: x * k, self.matrix[basic_row_index]))
        for i in range(len(self.z)):
            self.matrix[row_index][i] += nRow[i]

    def findMinWithIndex(self, targetList):
        return min(list(zip(targetList, list(range(len(targetList))))))

    def getColumn(self, columnIndex):
        return list(map(lambda val: val[columnIndex], self.matrix))

    def findBasis(self, column):
        values = zip(column, list(range(len(self.D))))
        values = filter(lambda val: val[0] > 0, values)
        return min(map(lambda val: (self.D[val[1]] / val[0], val[1]), values))
