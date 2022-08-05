import os
import codecs


def read_from_file(path_file: str) -> str:
    with codecs.open(path_file, 'r', encoding='utf-8') as file:
        return file.readline()


def compression(text):
    count = 1
    result = ''
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            count += 1
        else:
            result = result + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text) - 2] != text[-1]):
        result = result + str(count) + text[-1]
    return result


def recovery(text):
    number = ''
    result = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            number += text[i]
        else:
            result = result + text[i] * int(number)
            number = ''
    return result


path_1 = os.path.join('documentation5', 'task_5.4(source).txt')
path_2 = os.path.join('documentation5', 'task_5.4(compressed).txt')
path_3 = os.path.join('documentation5', 'task_5.4(restored).txt')

source_file = read_from_file(path_1)
compressed_file = compression(source_file)
recovered_file = recovery(compressed_file)

with open(path_2, 'w', encoding='utf-8') as file:
    file.write(compressed_file)

with open(path_3, 'w', encoding='utf-8') as file:
    file.write(recovered_file)

print(f'Source text: {source_file}')
print(f'Compressed text: {compressed_file}')
print(f'Restored text: {recovered_file}')