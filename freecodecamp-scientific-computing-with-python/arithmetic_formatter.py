def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    problems_elements_list = []

    for problem in problems:
        elements_list = problem.split()
        if not elements_list[0].isdigit() or not elements_list[2].isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(elements_list[0]) > 4 or len(elements_list[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if elements_list[1] != '+' and elements_list[1] != '-':
            return "Error: Operator must be '+' or '-'."
        elements_list.append(max(len(elements_list[0]), len(elements_list[2])))
        problems_elements_list.append(elements_list)
        
    answer = ''
    for index in range(3) :
        if index == 0:
            for j in range(len(problems_elements_list)):
                answer += ''.join([' ' for i in range(2 + problems_elements_list[j][3] - len(problems_elements_list[j][0]))]) + problems_elements_list[j][0]
                if j < (len(problems_elements_list) - 1):
                    answer += '    '
            answer += '\n'
        
        if index == 1:
            for j in range(len(problems_elements_list)):
                answer += problems_elements_list[j][1] + ' ' + ''.join([' ' for i in range(problems_elements_list[j][3] - len(problems_elements_list[j][2]))]) + problems_elements_list[j][2]
                if j < (len(problems_elements_list) - 1):
                    answer += '    '
            answer += '\n'
        
        if index == 2:
            for j in range(len(problems_elements_list)):
                answer += ''.join(['-' for _ in range(problems_elements_list[j][3] + 2)])
                if j < (len(problems_elements_list) - 1):
                    answer += '    '
            if show_answers:
                answer += '\n'
                for j in range(len(problems_elements_list)):
                    result = ''
                    if problems_elements_list[j][1] == '+':
                        result = int(problems_elements_list[j][0]) + int(problems_elements_list[j][2])
                    else:
                        result = int(problems_elements_list[j][0]) - int(problems_elements_list[j][2])
                    result = str(result)
                    if len(result) > problems_elements_list[j][3]:
                        answer += ' '
                    else:
                        answer += ''.join([' ' for _ in range(problems_elements_list[j][3] - len(result) + 2)])
                    answer += result
                    if j < (len(problems_elements_list) - 1):
                        answer += '    '

    return answer

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "988 + 40"])}')