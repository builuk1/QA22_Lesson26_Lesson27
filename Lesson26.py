# notes = {}
#
# while True:
#     command = str(input("Enter command : "))
#     if command.lower() == 'c':
#         title = str(input("Enter title of your note to create: "))
#         note = str(input("Enter your note to create: "))
#         notes[title] = note
#     elif command.lower() == 'u':
#         title = str(input("Enter title of your note to update: "))
#         if title in notes:
#             note = str(input("Enter your note to update: "))
#             notes[title] = note
#         else:
#             print('Try create')
#     elif command.lower() == 'r':
#         for title in notes:
#             print(title, notes[title])
#     elif command.lower() == 'd':
#         title = str(input("Enter title of your note to delete: "))
#         del notes[title]

# notes = {}
# #Считывать данные из файла в словарь
# with open('notebook.txt', 'rt') as f:
#     t = f.readline()
#     s = f.readline()
#     count = 1
#     while s and t:
#         if '\n' in s:
#             s = s[:-1]
#         if '\n' in t:
#             t = t[:-1]
#         notes[t] = s
#         t = f.readline()
#         s = f.readline()
#
# print(notes)
notes = {'123': '456', 'test': '123', 'ggg': '567'}
#Записываем данные в файл
with open('notebook.txt', 'wt') as f:
    for title in notes:
        f.write(title)
        f.write('\n')
        f.write(notes[title])
        f.write('\n')


#Сериализация
#https://code.tutsplus.com/tutorials/serialization-and-deserialization-of-python-objects-part-1--cms-26183