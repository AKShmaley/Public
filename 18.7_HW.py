import random
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks[student][class_] = marks
for student in students:
    print(f'''{student}
           {students_marks[student]}''')
print ()
print('''Список команд:
            1. Добавить оценку ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Добавить ученика
            5. Удалить ученика
            6. Добавить предмет
            7. Удалить предмет
            8. Редактировать оценку ученика по предмету
            9. Удалить оценку ученика по предмету
            10. Вывести все оценки для определённого ученика
            11. Вывести средний балл по каждому предмету по определённому ученику
            12. Редактировать имя ученика
            13. Вывести список учеников
            14. Вывести список предметов
            15. Выход из программы''')
print ()

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
            print()

    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'\t{class_} - {marks_sum//marks_count}')
            print()

    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()

    elif command == 4:
        print('4. Добавить ученика')
        name = input("Введите имя нового ученика: ")
        if name in students:
            print("Такой ученик уже есть в списке.")
        else:
            students.append(name)
            students.sort()
            students_marks[name] = {}
            for class_ in classes:
                students_marks[name][class_] = []
        print(f"Новый ученик {name} добавлен.")
        print()

    elif command == 5:
        print('5. Удалить ученика')
        name = input("Введите имя ученика, которого нужно удалить: ")
        if name not in students:
            print("Ученика с таким именем нет в списке.")
        else:
            students.remove(name)
            del students_marks[name]
        print(f"Ученик {name} удален.")
        print()

    elif command == 6:
        print('6. Добавить предмет')
        class_to_add = input("Введите название предмета, который нужно добавить: ")
        if class_to_add in classes:
            print("Предмет с таким названием есть в списке.")
        else:
            classes.append(class_to_add)
            for student in students_marks:
                students_marks[student][class_to_add] = []
        print(f"Предмет {class_to_add} добавлен.")
        print()

    elif command == 7:
        print('7. Удалить предмет')
        class_to_remove = input("Введите название предмета, который нужно удалить: ")
        if class_to_remove not in classes:
            print("Предмета с таким названием нет в списке.")
        else:
            classes.remove(class_to_remove)
            for student in students_marks:
                del students_marks[student][class_to_remove]
        print(f"Предмет {class_to_remove} удален.")
        print()

    elif command == 8:
        print('8. Редактировать оценку ученика по предмету')
        while True:
            name = input("Введите имя ученика, оценку которого нужно изменить: ")
            if name not in students:
                print("Ученика с таким именем нет в списке.")
                continue
            if name in students:
                while True:
                    class_to_edit = input("Введите название предмета, оценку по которому нужно изменить: ")
                    if class_to_edit not in classes:
                        print("Предмета с таким названием нет в списке.")
                        continue
                    if class_to_edit in classes:
                        print(f"Оценки ученика {name} по предмету {class_to_edit}: {students_marks[name][class_to_edit]}")
                        while True:
                            try:
                                index_to_edit = int(input("Введите номер оценки (1, 2 или 3), которую нужно изменить: ")) - 1
                            except ValueError:
                                print("Некорректный ввод. Введите число.")
                                continue
                            if not (0 <= index_to_edit < 3):
                                print("Некорректный номер оценки.")
                                continue
                            try:
                                new_mark = int(input("Введите новую оценку (от 1 до 5): "))
                            except ValueError:
                                print("Некорректный ввод. Введите число.")
                                continue
                            if not (1 <= new_mark <= 5):
                                print("Некорректная оценка. Введите число от 1 до 5.")
                                continue
                            students_marks[name][class_to_edit][index_to_edit] = new_mark
                            print(f"Оценка изменена. Новые оценки ученика {name} по предмету {class_to_edit}: {students_marks[name][class_to_edit]}")
                            print()
                            break
                    break
            break
    elif command == 9:
        print('9. Удалить оценку ученика по предмету')
        while True:
            name = input("Введите имя ученика, оценку которого нужно удалить: ")
            if name not in students:
                print("Ученика с таким именем нет в списке.")
                continue
            while True:
                class_to_edit = input("Введите название предмета, оценку по которому нужно удалить: ")
                if class_to_edit not in classes:
                    print("Предмета с таким названием нет в списке.")
                    continue
                if class_to_edit not in students_marks[name]:
                    print(f"У ученика {name} нет оценок по предмету {class_to_edit}.")
                    continue
                print(f"Оценки ученика {name} по предмету {class_to_edit}: {students_marks[name][class_to_edit]}")
                while True:
                    try:
                        index_to_edit = int(input("Введите номер оценки (1, 2 или 3), которую нужно удалить: ")) - 1
                    except ValueError:
                        print("Некорректный ввод. Введите число.")
                        continue
                    if not (0 <= index_to_edit < 3):
                        print("Некорректный номер оценки.")
                        continue
                    del students_marks[name][class_to_edit][index_to_edit]
                    print(f"Оценка удалена. Новые оценки ученика {name} по предмету {class_to_edit}: {students_marks[name][class_to_edit]}")
                    break
                another_mark = input("Удалить еще одну оценку для этого предмета (y/n)? ")
                if another_mark.lower() != 'y':
                    break
            another_class = input("Удалить оценку по другому предмету для этого ученика (y/n)? ")
            if another_class.lower() != 'y':
                break
        print("Удаление оценки завершено.")
        print ()

    elif command == 10:
        print('10. Вывести все оценки для определённого ученика')
        while True:
            name = input("Введите имя ученика, оценки которого нужно вывести: ")
            if name not in students:
                print("Ученика с таким именем нет в списке.")
                continue
            print(f"Оценки ученика {name}:")
            for class_, marks in students_marks[name].items():
                print(f"  {class_}: {marks}")
            another_student = input("Вывести оценки для другого ученика (y/n)? ")
            if another_student.lower() != 'y':
                break
        print("Вывод оценок завершен.")
        print()

    elif command == 11:
        print('11. Вывести средний балл по каждому предмету по определённому ученику')
        student_name = input("Введите имя ученика, средние оценки которого нужно вывести: ")
        if student_name in students_marks:
            print(f"Средние баллы для ученика {student_name}:")
            for subject, marks in students_marks[student_name].items():
                average = sum(marks) / len(marks)
                print(f"{subject}: {average:.2f}")
        else:
            print("Ученик с таким именем не найден.")
            print()

    elif command == 12:
        print('12. Редактировать имя ученика')
        while True:
            old_name = input("Введите имя ученика, которое нужно изменить: ")
            if old_name not in students:
                print("Ученика с таким именем нет в списке.")
                continue
            new_name = input("Введите новое имя ученика: ")
            if new_name in students:
                print("Ученик с таким именем уже есть в списке.")
                continue
            index = students.index(old_name)
            students[index] = new_name
            students.sort()
            students_marks[new_name] = students_marks.pop(old_name)
            print(f"Имя ученика изменено с {old_name} на {new_name}.")
            another_student = input("Редактировать имя другого ученика (y/n)? ")
            if another_student.lower() != 'y':
                break
        print("Редактирование имен завершено.")
        print()

    elif command == 13:
        print('13. Вывести список учеников')
        print("Список учеников:")
        print()
        for student in students:
            print(f"- {student}")
            print()

    elif command == 14:
        print('14. Вывести список предметов')
        print("Список предметов:")
        print()
        for class_ in classes:
            print(f"- {class_}")
            print()

    elif command == 15:
        print('15. Выход из программы')
        break