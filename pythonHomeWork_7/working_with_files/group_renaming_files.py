# Напишите функцию группового переименования файлов.
# Она должна:
# * принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# * принимать параметр количество цифр в порядковом номере.
# * принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# * принимать параметр расширение конечного файла.
# * принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение.

from pathlib import Path

__all__ = ['group_renaming_files']

NUMBER_OF_DIGITS = 3


def group_renaming_files(source_extension: str, result_extension: str,
                         source_name: str = '', serial_number_length: int = NUMBER_OF_DIGITS, letters_range=None) -> None:
    if letters_range is None:
        letters_range = [3, 6]
    number = 0

    p = Path(Path().cwd())
    for obj in p.iterdir():
        if obj.is_file():
            start_name, start_extension = obj.name.split('.')
            if start_extension == source_extension:
                number += 1
                number_str = f'{number:0{serial_number_length}}'
                final_name = f'{start_name[letters_range[0] - 1:letters_range[1] - 1]}{source_name}{number_str}.{result_extension}'
                Path(obj.name).rename(final_name)


# if __name__ == '__main__':
#     group_renaming_files('txt', 'fb2', source_name='testfile')
