def return_row(rowstring):
    binary_rowstring = rowstring.replace('B', '1').replace('F', '0')
    return int(binary_rowstring, 2)
