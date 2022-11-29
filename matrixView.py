def clean_print(matrix):
    #code from https://stackoverflow.com/questions/13214809/pretty-print-2d-list
    """
    parameter is a 2D array called matrix
    """

    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))
    print("\n")