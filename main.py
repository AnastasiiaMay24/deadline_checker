import datetime
import math

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

def main():
    def get_datas():
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


    pass_date, deadline_date = get_datas()

    while True:
        print("\n=====МЕНЮ=====")
        print("1. Вычислить оценку с учетом срока сдачи")
        print("2. Вывести фамилии студентов, просрочивших сдачу")
        print("3. Ввести данные заново")
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
            print("сюда поместим вторую функцию")
        elif answer == 3:
            pass_date, deadline_date = get_datas()
        elif answer == 0:
            print("Программа завершена")
            break
        else:
            print("Ошибка! в меню нет такого пункта!")


if __name__ == "__main__":
    main()