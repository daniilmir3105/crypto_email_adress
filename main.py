import csv
import re

alphabetWithOutYo = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alphabetWithYo = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# Создаем список из результатов
address_results = []
email_results = []
addresses = [
    "81-щ ъь ЬЪРФф.47 ът.494",  # 81-й км МКАДд.47 кв.494
    "Знтчузее шр.й.13 пз.438",  # Зинтоваа ул.д.13 кв.438 (5)
    "Лдждфчйжхомн уйф.и.57 ож.98",  # Лаваруевский пер.д.57 кв.98 (4) или Заваруевский пер.д.57 кв.98
    "Етяйэёгсыщъйц ьтэ.с.92 чп.87",  # Четырёхдомный пер.д.92 кв.87
    "Чншкцфисщтии ыу.м.28 тк.453",  # Червомайскаа ул.д.28 кв.453 (8) или Первомайскаа ул.д.28 кв.453
    "Ыьвсцъуйй шф.н.19 ул.494",  # Тущинскаа пл.д.19 кв.494
    "Гмклшжшвкгшш мд.ь.52 гъ.37",  # Густяняйскяя ул.г.52 кб.37 (25)
    "ид. Шгшьэебгш Гмлшнбжшь.88 гъ.444",  # пл. Академика .......
    "Тшркцшцощтрс чш.м.69 тк.275",  # Триворожский пр.д.69 кв.275 (8) или Криворожский пр.д.69 кв.275
    "Хдитждд чп.и.13 ож.234",  # Хадоваа ул.д.13 кв.234 (4) или Садоваа ул.д.13 кв.234
]

emails = [
    'ccfpt.sqjjye@vcqkcup.sfd',
    'pkjjsje@pthm.htr',  # kfeenez@koch.com (5)
    'levxqerr.izi@biwx.gsq',  # hartmann.eve@xest.com (5)
    'ryqfvqtr.fvhpuvr@yrognpx.pcz',
    'vwemtti.wzcqi@pwcuiqt.kwu',  # nowella.oruia@houmail.com (8)
    'bxcjurj42@jeomnbqjb.lxv',  # sotalia42@avfdeshas.com (9)
    'tjtgklym@bnkd.mds',
    'udqkhd.rbglhss@lyxdq.bnl',  # verlie.schmitt@mzyer.com (25)
    'pczivcwf@hipww.kwu',  # huranuox@zahoo.com (8)
    'vshvmks.pilriv@gvmwx.gsq',  # rodrigo.lehner@crist.com (4)
]


def caesar_decrypt(ciphertext, key, alphabet):
    plaintext = ''
    for c in ciphertext:
        if c in alphabet:
            idx = alphabet.index(c)
            new_idx = (idx - key) % len(alphabet)
            plaintext += alphabet[new_idx]
        elif c in alphabet.upper():
            idx = alphabet.upper().index(c)
            new_idx = (idx - key) % len(alphabet)
            plaintext += alphabet.upper()[new_idx]
        else:
            plaintext += c
    return plaintext


for ciphertext in addresses:
    for key in range(len(alphabetWithYo)):
        plaintext = caesar_decrypt(ciphertext, key, alphabetWithYo)
        plaintext2 = caesar_decrypt(ciphertext, key, alphabetWithOutYo)
        match = re.search(r' кв\.\d*$', plaintext2)
        match2 = re.search(r' кб\.\d*$', plaintext2)
        match3 = re.search(r' Академика\.\d*$', plaintext)
        if match or match2 or match3:
            if 'Академика' in plaintext:
                address_results.append([key, plaintext, ''])
            address_results.append([key, plaintext2, ''])

for email in emails:
    for key in range(len(alphabet)):
        plaintext = caesar_decrypt(email, key, alphabet)
        if '.com' in plaintext:
            email_results.append([key, plaintext, ''])

# Записываем результаты в файл
with open('results.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(['Адреса'])
    writer.writerow(['Ключ', 'Строка (без ё)', ''])
    writer.writerows(address_results)
    writer.writerow([])
    writer.writerow(['Email'])
    writer.writerow(['Ключ', 'Строка', ''])
    writer.writerows(email_results)
