if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    student_score = student_marks[query_name]
    sum_student_score = sum(student_score)
    float_sum = float(sum_student_score)
    average = float_sum / 3
    format_average = '{:.2f}'.format(average)
    print(format_average)