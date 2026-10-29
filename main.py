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