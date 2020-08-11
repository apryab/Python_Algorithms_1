# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

print('Введите номер вашей буквы')
a = int(input())
solution = ''
if a < 13:
    if a < 7:
        if a > 4:
            if a < 6:
                solution = 'e'
            else:
                solution = 'f'
        elif a < 4:
            if a < 2:
                solution = 'a'
            elif a > 2:
                solution = 'c'
            else:
                solution = 'b'
        else:
            solution = 'd'
    elif a > 7:
        if a > 10:
            if a < 12:
                solution = 'k'
            else:
                solution = 'l'
        elif a < 10:
            if a < 9:
                solution = 'h'
            else:
                solution = 'i'
        else:
            solution = 'j'
    else:
        solution = 'g'
elif a > 13:
    if a > 20:
        if a < 23:
            if a < 22:
                solution = 'u'
            else:
                solution = 'v'
        elif a > 23:
            if a < 25:
                solution = 'x'
            elif a > 25:
                solution = 'z'
            else:
                solution = 'y'
        else:
            solution = 'w'
    elif a < 20:
        if a < 16:
            if a < 15:
                solution = 'n'
            else:
                solution = 'o'
        elif a > 16:
            if a < 18:
                solution = 'q'
            elif a > 18:
                solution = 's'
            else:
                solution = 'r'
        else:
            solution = 'p'
    else:
        solution = 't'
else:
    solution = 'm'
print('Ваша буква -', solution)