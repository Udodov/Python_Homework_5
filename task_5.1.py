import os
import codecs


def read_from_file(path_file: str) -> str:
    with codecs.open(path_file, 'r', encoding='utf-8') as file:
        return file.readline()


def del_some_words(text: str) -> str:
    text = list(filter(lambda x: deleted_word not in x, text.split()))
    return " ".join(text)


path = os.path.join('documentation5', 'task_5.1.txt')

print(f'There is text in the file:\n ', read_from_file(path))
deleted_word = input('Enter the word you want to remove from the text as a string:')
print()
print(f'The final text looks like this:\n ', del_some_words(read_from_file(path)))
