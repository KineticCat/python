def printWord(matrix):
    word = ""
    for x in range(8):
        for y in range(8):
            if matrix[y][x] != ".":
                word += matrix[y][x]
    print(word)

t = int(input())

for _ in range(t):
    matrix =[]
    for _ in range(8):
        matrix.append(input())
    printWord(matrix)
