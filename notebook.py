#Записываем данные в файл
#'notebook.txt'
# notes = {}
def write_to_file(file_name):
    with open(file_name, 'wt') as f:
        for title in notes:
            f.write(title)
            f.write('\n')
            f.write(notes[title])
            f.write('\n')

# #Считывать данные из файла в словарь
def read_from_file(file_name):
    with open(file_name, 'rt') as f:
        t = f.readline()
        s = f.readline()
        while s and t:
            if '\n' in s:
                s = s[:-1]
            if '\n' in t:
                t = t[:-1]
            notes[t] = s
            t = f.readline()
            s = f.readline()

def change_file(file_name,change='read'):
    if change == 'write':
        write_to_file(file_name)
    elif change == 'read':
        read_from_file(file_name)

def create_note():
    title = str(input("Enter title of your note to create: "))
    note = str(input("Enter your note to create: "))
    notes[title] = note

def big_note(command):
    if command.lower() == 'c':
        create_note()
    elif command.lower() == 'u':
        title = str(input("Enter title of your note to update: "))
        if title in notes:
            note = str(input("Enter your note to update: "))
            notes[title] = note
        else:
            print('Try create')
    elif command.lower() == 'r':
        for title in notes:
            print(title, notes[title])
    elif command.lower() == 'd':
        title = str(input("Enter title of your note to delete: "))
        del notes[title]

if __name__ == '__main__':
    while True:
        with open('notebook.txt', 'at') as f:
            pass
        notes = {}
        read_from_file('notebook.txt')
        command = str(input("Enter command : "))
        big_note(command)
        write_to_file('notebook.txt')

#Сделать выход
#Раздробить big_note
#Сделать возможность выбора имени файла
#Разные типы записей (разной длинны, если более 200 символов, форматировать в несколько строк)
#pet