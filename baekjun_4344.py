c = int(input())
ans_list = []

for i in range(c):
    grade_list = []
    text = input()
    left,space,right = text.partition(" ")
    student_number = int(left)

    for j in range(student_number):
        left,space,right = right.partition(" ")
        grade_list.append(int(left))

    grade_average = sum(grade_list)/student_number

    temp_over_avg = 0
    for k in range(student_number):
        if grade_list[k] > grade_average:
            temp_over_avg += 1
        temp_ans = round(temp_over_avg/student_number * 100, 3)

    ans_list.append("%.3f" %temp_ans)

for i in range(c):
    print(str(ans_list[i])+"%")