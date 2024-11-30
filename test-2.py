def check_all_students_passed(scores_input: str,names_input: str )-> str:
    scores = scores_input.split(',')
    names = names_input.split(',')  
    passed = list()
    result = ''
    i = 0
    while i < len(scores):
        if int(scores[i]) < 65:
            pass     
        else:
            passed.append(i)      
        i = i + 1
    
    if len(passed) == len(scores):
        result = 'Все сдали'
    elif len(passed) == 0:
        result = 'Никто не сдал'
    else:
        for j in passed:
            result = result + f'{names[j]} сдал экзамен. Баллы: {scores[j]}'
    return result

scores_input = '30,40,20'
names_input = 'Alice,Bob,Charlie'
result = check_all_students_passed(scores_input, names_input)
print(result)
scores_input = '37,90,20'
names_input = 'Oleg,Jo,Mary'
result = check_all_students_passed(scores_input, names_input)
print(result)
scores_input = '89'
names_input = 'Vasya'
result = check_all_students_passed(scores_input, names_input)
print(result)