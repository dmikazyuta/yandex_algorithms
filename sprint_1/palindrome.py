'''
В единственной строке записана фраза или слово. Буквы могут быть только латинские.
Длина текста не превосходит 20000 символов.
Фраза может состоять из строчных и прописных латинских букв, цифр, знаков препинания.
'''

import string

a = input()

word = a.upper().translate(str.maketrans('', '', string.punctuation)).replace(' ','')
word_inv = word[::-1]

if word == word_inv:
    print('True')
else:
    print('False')
