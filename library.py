import library_methods
def print_library(book):
    print('№', book[0])
    print('Автор книги:', book [1])
    print('Название книги:', book [2])
    print('Год издания:', book [3])
    print('Жанр:', book [4])    

def view():
    with open('library.txt', 'r') as file:
            for line in file:
                line = line.split('*')
                print_library(line)
    return True

def add():
    print('\nВы хотите добавить книгу, следуйте инструкциям:\n')
    author = input('Введите автора: ')
    title = input('Введите название: ')
    year = input('Введите год издания: ')
    genre = input('Введите жанр: ')
    mas = [author, title, year, genre]
    li = '*'.join(mas)
    with open('library.txt', 'r+') as f:
        count = 1
        for line in f:
            count+=1
        f.write('\n')
        f.write(str(count))
        f.write('*')
        f.write(li)
    print('\nКнига добавлена')
    return True
    
def delete():
    index = int(input('''\n  Как хотите удалить элемент?
1 - по порядковому номеру
2 - по автору
3 - по названию\n '''))-1
    elem = input('Введите элемент: ')
    list_change = []

    with open('library.txt', 'r') as file:
        for line in file:
            line_split = line.split('*')
            if index == 0:
                if int(elem) == int(line_split[0]):
                    continue
            else:
                if str(elem) in line_split[index]:
                    continue
            line_out = '*'.join(line_split)
            list_change.append(line_out)
    
        
        
    new_data = ''.join(str(i) for i in list_change)
    with open('library.txt', 'w') as file:
        file.write(new_data)
    print('\nКнига удалена')
    return True
                    
def find():
    index = int(input('''\n  Как хотите найти элемент?
1 - по порядковому номеру
2 - по автору
3 - по названию
4 - по году издания
5 - по жанру
6 - вывести весь список\n '''))-1
    
    if index == 0:
        elem = input('Введите искомый элемент: ')
        with open('library.txt', 'r') as file:
            for line in file:
                line = line.split('*')
                if int(elem) == int(line[0]):
                    print_library(line)
                    
    elif index == 5: view()
    else: extra_find(index, elem)
    return True
    
def extra_find(num, elem):
    with open('library.txt', 'r') as file:
            for line in file:
                line = line.split('*')
                if elem in line[num]:
                    print_library(line)
    

def change():
    state_change = True
    while state_change == True:
        num = int(input('''\n  Введите номер изменяемой книги
  (если не знаете, вольпользуйтесь поиском, нажав 0): '''))
        if num == 0:
            find()
        else: state_change = False
    index = int(input('''\n Какую информацию хотите изменить?
1 - автор
2 - название
3 - год издания
4 - жанр \n  '''))
    text_change = str(input('Введите текст изменения: '))
    extra_change(num, index, text_change)
    return True
    
def extra_change(num, index, text):
    list_change = []
    with open('library.txt', 'r') as file:
        for line in file:
            line_split = line.split('*')
            if int(line_split[0]) == num:
                line_split[index] = text
            line_out = '*'.join(str(i) for i in line_split)
            list_change.append(line_out)            
    new_data = ''.join(str(i) for i in list_change)
    with open('library.txt', 'w') as file:
        file.write(new_data)                   
    


while True:
    index = int(input('''\n\n  Меню:
1 - просмотреть всю библиотеку
2 - добавить книгу
3 - удалить книгу
4 - найти книгу
5 - изменить информацию о книге
6 - выход \n  '''))
    if index == 1: view()
    elif index == 2: add()
    elif index == 3: delete()
    elif index == 4: find()
    elif index == 5: change()
    elif index == 6: False



    
        
