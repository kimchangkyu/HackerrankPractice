if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    
    number = sum(student_marks[query_name]) / len(student_marks[query_name])
    if (len(str(number)) == 4) or (len(str(number)) == 3):
        print(str(number) + '0')
    elif len(str(number)) > 4:
        print(round(number, 2))