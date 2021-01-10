#21/1/9
def solution(board, moves):
    answer = 0
    i = 0
    basket = []
    while i < len(moves):
        catch = moves[i]-1
        for j in range(len(board)):
            if board[j][catch] ==0:
                pass
            else:
                basket.append(board[j][catch])
                board[j][catch] = 0
                break
                
        if len(basket)>1:
            if basket[len(basket)-1] == basket[len(basket)-2]:
                basket.pop()
                basket.pop()
                answer += 1
                
            else:
                pass
        else:
            pass
        
        i += 1                 
    return answer*2

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))