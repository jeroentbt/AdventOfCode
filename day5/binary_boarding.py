def return_row(rowstring):
    binary_rowstring = rowstring.replace('B', '1').replace('F', '0')
    return int(binary_rowstring, 2)


def return_column(columnstring):
    binary_columnstring = columnstring.replace('R', '1').replace('L', '0')
    return int(binary_columnstring, 2)
