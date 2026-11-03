import datetime
import math
from typing import List


## datetime.strptime (string parse time) разбирает строку по шаблону
# и создает объект даты, позволяя вычитать одну дату из другой.
def deadline_score (pass_date: str, deadline_date: str) -> int:
    pass_date = datetime.datetime.strptime(pass_date, "%d.%m.%Y")
    deadline_date = datetime.datetime.strptime(deadline_date,
                                               "%d.%m.%Y")
    time_delta = pass_date - deadline_date
    # time_delta (модуля timedelta) хранит полную разницу между датами,
    # включая часы и минуты.
    # Свойство .days извлекает из этого объекта только целое число дней,
    # отбрасывая часы и минуты, чтобы с ним можно было проводить
    # математические расчеты.
    delta_days = time_delta.days
    if delta_days <= 0:
        return 5
    else:
        # модуль math.ceil округляет числа в бОльшую сторону
        # затем от оценки 5 отнимаем количество недель просрочки,
        # получаем оценку с учетом опоздания
        weeks_late = math.ceil(delta_days / 7)
        score = 5 - weeks_late
        # функция max сравнивает числа и возвращает бОльший результат
        # сравниваем с нулем, т.к. меньше нуля оценка быть не может
        return max(0, score)

def late_list(grades: dict, deadline_date: str) -> List[str]:
    deadline_date = datetime.datetime.strptime(deadline_date,
                                               "%d.%m.%Y")
    late_students = []
    for students, pass_date in grades.items():
        pass_date = datetime.datetime.strptime(pass_date, 
                                               "%d.%m.%Y")
        if pass_date > deadline_date:
            late_students.append(students)
    late_students.sort()
    return late_students


def main():
    def get_dates():
        while True:
            try:
                pass_date = input("Введите дату сдачи контрольной работы в \n"
                                  "формате (ДД.ММ.ГГГГ): ")
                #проверяет правильность формата введенных данных,
                # но результат не сохраняет
                datetime.datetime.strptime(pass_date,
                                                       "%d.%m.%Y")
                deadline_date = input("Введите дату дедлайна сдачи: ")
                # проверяет правильность формата введенных данных,
                # но результат не сохраняет
                datetime.datetime.strptime(deadline_date,
                                                       "%d.%m.%Y")
                return pass_date, deadline_date
            except ValueError:
                print("Ошибка! Формат дат: (ДД.ММ.ГГГГ)")


    pass_date, deadline_date = get_dates()

    def get_students_data():
        students_dict = {}
        while True:
            # strip() позволяет убрать " ", "\t", "\n", "\r" по краям строки.
            # На выходе получается строка.
            user_dict = input('Введите фамилию и дату сдачи '
                              'контрольной работы в формате: \n'
                              '"Фамилия ДД.ММ.ГГГГ", '
                              'для формирования списка нажмите 0: ').strip()
            if user_dict == "0":
                break

            # split() разбивает строку по пробельным символам
            # (" ", "\t", "\n", "\r") и удаляет лишние пробелы.
            # На выходе получается список.
            user_dict = user_dict.split()
            if len(user_dict) != 2:
                print("Ошибка! Введите фамилию и дату через пробел!")
                continue

            name, pass_date = user_dict

            try:
                datetime.datetime.strptime(pass_date, "%d.%m.%Y")
            except ValueError:
                print("Ошибка! Формат дат: (ДД.ММ.ГГГГ)")
                continue

            students_dict[name] = pass_date

        return students_dict


    while True:
        print("\n=====МЕНЮ=====")
        print("1. Вычислить оценку с учетом срока сдачи")
        print("2. Сформировать список студентов, просрочивших сдачу")
        print("3. Ввести даты заново")
        print("0. Завершить программу")

        try:
            answer = int(input("Выберите пункт меню. "
                               "Для выхода из программы нажмите 0: "))
        except ValueError:
            print("Ошибка! Попробуйте снова!")
            continue

        if answer == 1:
            print(deadline_score(pass_date, deadline_date))
        elif answer == 2:
            students_dict = get_students_data()
            if not students_dict:
                print("Список пуст")
            else:
                print("Должники: ", late_list(students_dict, deadline_date))
        elif answer == 3:
            pass_date, deadline_date = get_dates()
        elif answer == 0:
            print("Программа завершена")
            break
        else:
            print("Ошибка! В меню нет такого пункта!")


if __name__ == "__main__":
    main()