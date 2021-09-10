"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

import hashlib

text = 'abcabc'
sub_str = []
sub_str_hash = set()
for i in range(len(text)):
    for j in range(i + 1, len(text) + 1):
        if text[i:j] != text:
            sub_str.append(text[i:j])
print(f'Все подстроки: {sub_str}')
print(f'Количество подстрок = {len(sub_str)}')
for el in sub_str:
    sub_str_hash.add(hashlib.sha256(el.encode()).hexdigest())
print(f'Количество уникальных подстрок = {len(sub_str_hash)}')

