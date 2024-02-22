tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(data):
    colWidths = [0] * len(data)
    for i in range(len(data)):
        colWidths[i] = max(len(word) for word in data[i])

    for i in range(len(data[0])):
        for j in range(len(data)):
            print(data[j][i].rjust(colWidths[j] + 1), end=' ')
        print()


printTable(tableData)