
'''

quest101=период?=
r101right=1=
a101ans1=1 раз в 6-8 лет.=
a101ans2=1 раз в 2-3 года.=
a101ans3=1 раз в 10 лет.=

import string
a = 'a101ans3'
b = a.strip('a101ans')
print(b)

3
[Finished in 0.2s]

print(a.partition('ans'))
('a101', 'ans', '3')
[Finished in 0.2s]

ДЛЯ ОТЛАДКИ ЧТОБЫ ВИДЕТЬ ВЕРНЫЕ ОТВЕТЫ
ВВЕДИ ТРЕТИЙ АРГУМЕНТ В КОММАНДНОЙ СТРОКЕ
python play.py x
на строке 211
'''
from random import choice
from time import sleep
import sys
import dirty_test as dtest
import settings as st
import re


def convert_rght_answrs_to_int_and_dict(answers, right_answers):
    ready_correct_answers = {}
    right_answers_num_list = [int(i) for i in right_answers]
    for a, b in answers.items():
        if a in right_answers_num_list:
            ready_correct_answers[a] = b
    return right_answers_num_list, ready_correct_answers


def find_values_in_file(random_num):
    answers = {}
    with open(st.answers_store_file, 'r', encoding='utf-8') as file:
        read = file.readlines()
        for row in read:
            if f'quest{random_num}=' in row:
                _, question, _ = row.split('=')
            if f'a{random_num}ans' in row:
                a, answer, _ = row.split('=')
                num = a.partition('ans')
                answers[int(num[2])] = answer
            if f'r{random_num}right' in row:
                _, right_answers, _ = row.split('=')
    return question, answers, right_answers


def validation_user_answer_right_or_not(user_answer, right_answers):
    user_answer = [int(i) for i in user_answer]
    if user_answer != right_answers:
        return False
    return True


def check_is_the_answer_a_number(user_answer):
    try:
        user_answer = int(user_answer)
    except ValueError:
        return False
    return True


def write_file_with_errors(question, answers, right_answers_str_list):
    with open(st.file_for_errors, 'a') as file:
        file.write(f'\n\n{question}\n\n')
        for a, b in answers.items():
            file.write(f'{a}. {b}\n\n')
        file.write(f'Правильные ответы: {right_answers_str_list}\n\n\n\n')


def check_for_the_word_stop_or_open(user_answer):
    action = True
    result = False
    if user_answer == 'stop':
        action = False
        result = True
    if user_answer == 'open':
        result = True
    return action, result


def loop_with_useranswering_and_checking_it(right_answers_int_list):
    answer_flag = True  # состояние ответа, верный или нет
    action = True  # состояние основного верхнего цикла

    while True:

        user_answer = input('>>>Введи ответ, stop или open(увидеть ответ)>>> ')

        action, result = check_for_the_word_stop_or_open(user_answer)
        if result:
            print(f'верный ответ - {right_answers_int_list}')
            answer_flag = False
            sleep(st.sleep_after_open_stop)
            break

        if not check_is_the_answer_a_number(user_answer):
            print('...Только цифры, stop или open(увидеть ответ)>>>')
            sleep(st.sleep_for_check_is_the_answer_a_number)
            continue

        elif validation_user_answer_right_or_not(
                user_answer, right_answers_int_list):
            print('...Это верный ответ...')
            sleep(st.sleep_after_right_answer)
            break

        print('...Это неверный ответ, попробуй еще раз...')
        answer_flag = False
        sleep(st.sleep_after_wrong_answer)
    print('\n' * st.space_after_answer)
    return action, user_answer, answer_flag


def spread_of_random_numbers():
    # найти все номера вопросов в файле теста
    with open(st.answers_store_file, 'r', encoding='utf-8') as file:
        f = file.read()
        fa = re.findall(r'quest(\d{1,3})=\D+', f)
        return fa


def store_closed_questions(num, writing_mode):
    # сохранить пройденный вопрос в файл что бы не повторяться
    with open(st.file_for_old_qwestions, writing_mode, encoding='utf-8') as f:
        f.write(f'{num}\n')
    return True


def find_spread_of_numbers(spread_of_numbers, old_qwestions):
    # вычисление списка допустимых вопросов
    spread_of_numbers = set(spread_of_numbers) - set(old_qwestions)
    spread_of_numbers = sorted(list(spread_of_numbers))
    return spread_of_numbers


def spread_of_numbers_after_subtract_old_qwest(spread_of_numbers):
    # получить случайное число из вопросов с учетом вычета уже пройденных
    try:
        with open(st.file_for_old_qwestions, 'r', encoding='utf-8') as file:
            f = file.readlines()
    except FileNotFoundError:
        store_closed_questions('0', 'w')
        f = ['0']
    old_qwestions = sorted([w.rstrip() for w in f])

    actually_spread_of_numbers = find_spread_of_numbers(
        spread_of_numbers, old_qwestions)

    if actually_spread_of_numbers == []:
        store_closed_questions('0', 'w')
        old_qwestions = '0'

        actually_spread_of_numbers = find_spread_of_numbers(
            spread_of_numbers, old_qwestions)

    return actually_spread_of_numbers, old_qwestions


if __name__ == '__main__':

    # dirty test for values in store file
    # проверяет делятся ли строки сплитом на 3 части
    all_ok_flag, errors_list, num_list = dtest.dirty_test_by_equal()
    # проверяет присутствует ли у вопроса ответ и варианты ответов
    errors_list_2 = dtest.dirty_test_by_available_all_components(num_list)
    error_flag = False
    if errors_list_2 != []:
        for error in errors_list_2:
            print(error)
        error_flag = True
    if all_ok_flag is False:
        for row in errors_list:
            print(f'''Ошибка значения в {row}{'-' * 30}''')
        error_flag = True
    if error_flag:
        raise ValueError

    spread_of_numbers = spread_of_random_numbers()
    print(f'Список номеров вопросов\n{spread_of_numbers}')
    print('\n' * st.space_after_answer)

    while True:

        # получение случайно числа из диапазона в файле, кроме пройденных ранее
        a, b = spread_of_numbers_after_subtract_old_qwest(spread_of_numbers)
        actually_spread_of_numbers = a
        old_qwestions = b
        print(f'изученные вопросы:\
            \n{sorted([int(w) for w in old_qwestions])}\n\n\n')
        random_num = choice(actually_spread_of_numbers)

        # нахождение значений в файлах
        a, b, c = find_values_in_file(random_num)
        question = a
        answers = b
        right_answers_str_list = c

        # конвертирование ответов в инт и занесение в словарь
        a, b = convert_rght_answrs_to_int_and_dict(
            answers, right_answers_str_list)
        right_answers_int_list = a
        ready_correct_answers = b

        # output question
        print('\n', '_' * 50)
        print(question, '\n')
        if sys.argv[1:]:
            print(right_answers_str_list, '\n')

        # output answers
        for k, v in answers.items():
            print(f'{k}. {v}\n')
        print('\n')

        # цикл для ответов пользователя и проверка их
        a, b, c = loop_with_useranswering_and_checking_it(
            right_answers_int_list)
        action = a
        user_answer = b
        answer_flag = c

        # записать в файл вопросы с допущенными ошибками
        if not answer_flag:
            write_file_with_errors(question, answers, right_answers_str_list)
        if action is False:
            break
        if answer_flag:
            store_closed_questions(random_num, 'a')


