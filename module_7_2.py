def custom_write(file_name, strings):  #название файла для записи
    strings_positions= {}
    file = open(file_name, 'w', encoding='utf-8')
    for i, string in enumerate(strings, start=1):
        byte_start = file.tell()  #номер байта начала строки
        file.write(string + '\n')
        strings_positions[(i, byte_start)] = string
    file.close()
    return strings_positions


name = 'file_name.txt'
info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!',
    'Спасибо!']
result = custom_write('file_name.txt', info)
for elem in result.items():
  print(elem)
# print(result)


