def order(plot):
    if not plot or not plot[0]:
        return []
    
    row, column = len(plot), len(plot[0])
    result = []
     
    for j in range(column - 1, -1, -1):
        if (column - 1 - j) % 2 == 0:
            for i in range(row):
                result.append(plot[i][j])
        else:
            for i in range(row - 1, -1, -1):
                result.append(plot[i][j])
                
    return result