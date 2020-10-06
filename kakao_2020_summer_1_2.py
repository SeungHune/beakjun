import copy

def parsing(expression):
    num_list = []
    operator_list = []
    temp_expression = expression
    cnt = 0
    while True:
        a = temp_expression.find("-")
        b = temp_expression.find("+")
        c = temp_expression.find("*")
        if a == -1 and b == -1 and c == -1:
            num_list.append(temp_expression)
            break
        if a == -1 : a = 99
        if b == -1 : b = 99
        if c == -1 : c = 99
        if a == min(a,b,c):
            x,y,z = temp_expression.partition("-")
            num_list.append(x)
            operator_list.append(y)
            temp_expression = z
        elif b == min(a,b,c):
            x,y,z = temp_expression.partition("+")
            num_list.append(x)
            operator_list.append(y)
            temp_expression = z
        else:
            x,y,z = temp_expression.partition("*")
            num_list.append(x)
            operator_list.append(y)
            temp_expression = z
    return num_list, operator_list

def solution(expression):
    num_list, operator_list = parsing(expression)
    max_value = 0
    cnt = 0
    first_operator = copy.deepcopy(operator_list)
    first_result = []

    # 연산이후에 정리하는방법.....
    for i in range(len(operator_list)):
        if operator_list[i] == "-":
            temp = int(num_list[i]) - int(num_list[i+1])
            first_result.append(temp)
            first_operator.pop(i)
        else:
            first_result.append(int(num_list[i+1]))
    return first_result,first_operator



print(solution("100-200*300-500+20"))