def go_game(board):
    dense_stones={'W':[],'B':[]}
    global stones_counted
    stones_counted=set()
    global dimension
    dimension=len(board)
    global flag
    flag=1
    for i in range(dimension):
        for j in range(dimension):
            if (board[i][j] not in stones_counted) and board[i][j]!='+':
                #print((i,j))
                #print(stones_counted)
                points=[]
                stones_counted_last=stones_counted.copy()
                if j+1<dimension and board[i][j]==board[i][j+1]:
                    points.append('right')
                if i+1<dimension and board[i][j]==board[i+1][j]:
                    points.append('down')
                count_dense_stones(board,i,j,*points)
                #print(stones_counted-stones_counted_last)
                print(flag)
                if flag:
                    for item in stones_counted - stones_counted_last:
                        #print(item)
                        dense_stones[board[i][j]].append(item)
                else:
                    flag=1
                    continue
            else:
                continue
    return {'B':len(dense_stones['B']), 'W':len(dense_stones['W'])}

def count_dense_stones(board,m,n,*args):
    #global stones_counted
    global flag
    #global dimension
    print((m,n))
    stones_counted.add((m,n))
    points=[]
    if (n-1 >= 0 and board[m][n-1]=='+') or (n+1 < dimension and board[m][n+1]=='+') or (m+1 < dimension and board[m+1][n]=='+') or (m-1 >= 0 and board[m-1][n]=='+'):
        flag=0
    if not args:
        return 
    if 'left' in args:
        if n-2 >= 0 and board[m][n-1]==board[m][n-2]:
            count_dense_stones(board,m,n-1,'left')
        else:
            count_dense_stones(board,m,n-1)
    if 'right' in args:
        if n+2 < dimension and board[m][n+1]==board[m][n+2]:
            count_dense_stones(board,m,n+1,'right')
        else:
            count_dense_stones(board,m,n+1)
    if 'down' in args:
        if n-1 >= 0 and board[m+1][n]==board[m+1][n-1]:
            points.append('left')
        if n+1 < dimension and board[m+1][n]==board[m+1][n+1]:
            points.append('right')
        if m+2 < dimension and board[m+1][n]==board[m+2][n]:
            points.append('down')
        count_dense_stones(board,m+1,n,*points)

if __name__ == '__main__':
    print("Example:")
    print(go_game(['++++W++++',
                   '+++WBW+++',
                   '++BWBBW++',
                   '+W++WWB++',
                   '+W++B+B++',
                   '+W+BWBWB+',
                   '++++BWB++',
                   '+B++BWB++',
                   '+++++B+++']))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert go_game(['++++W++++',
                    '+++WBW+++',
                    '++BWBBW++',
                    '+W++WWB++',
                    '+W++B+B++',
                    '+W+BWBWB+',
                    '++++BWB++',
                    '+B++BWB++',
                    '+++++B+++']) == {'B': 3, 'W': 4}
    print("Coding complete? Click 'Check' to earn cool rewards!")
