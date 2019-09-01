
import settings as st
import re


def dirty_test_by_equal():
    all_ok_flag = True
    errors_list = []
    num_list = []
    pattern = r'quest(\d{1,3})=\D'
    with open(st.answers_store_file, 'r', encoding='utf-8') as f:
        list_text = f.readlines()
    for row in list_text:
        if len(row) > 3:
            try:
                a, b, c = row.split('=')
            except ValueError:
                all_ok_flag = False
                errors_list.append(row)
        q = re.match(pattern, row)
        if q:
            a = q.groups()
            num_list.append(a[0])
    return all_ok_flag, errors_list, num_list


def dirty_test_by_available_all_components(num_list):
    errors_list_2 = []
    with open(st.answers_store_file, 'r', encoding='utf-8') as f:
        list_text = f.read()
    for row in num_list:
        if f'r{row}right' not in list_text:
            errors_list_2.append(f'ошибка наличия - r{row}right - отсутствует')
        if f'a{row}ans' not in list_text:
            errors_list_2.append(f'ошибка наличия - a{row}ans - отсутствует')
    return errors_list_2
