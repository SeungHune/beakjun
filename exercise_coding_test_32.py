# 2019 카카오 - 크레인 인형뽑기

def solution(board, moves):
    answer = 0
    answer_list = []
    for col in moves:
        new_col = col - 1
        for i in range(len(board)):
            # print(i)
            if board[i][new_col] != 0:
                answer_list.append(board[i][new_col])
                # print(board)
                board[i][new_col] = 0
                # print(board)
                # print("----------------------")
                if len(answer_list) > 1 and answer_list[len(answer_list)-1] == answer_list[len(answer_list)-2]:
                    answer_list.pop(len(answer_list)-1)
                    answer_list.pop(len(answer_list)-1)
                    answer += 2
                break

    # print(answer_list)
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
               [1,5,3,5,1,2,1,4]))

