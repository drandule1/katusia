# 1. Написать класс Car
# Конструктор класса принимает атрибуты:
# color: str (цвет)
# count_passenger_seats: int (количество пассажирских мест)
# is_baby_seat: bool (наличие десткого кресла)
# is_busy: bool (определяется внутри конструктора со значением False, не принимается на
# вход)
# 1.1 Написать магический метод __str__ выводящий форматированную строку с информацией
# об автомобиле


class car:
    color: str
    count_passenger_seats: int
    is_baby_seat: bool
    is_busy : bool

    def  __init__(self, color, count_passenger_seats, is_baby_seat):
        self.color=color
        self.count_passenger_seats=count_passenger_seats
        self.is_baby_seat=is_baby_seat
        self.is_busy = False

    def __str__(self):
        baby=""
        if self.is_baby_seat:
            baby="детские места есть"
        else:
            baby = "детские места нет"
        busy = ""
        if self.is_busy:
            busy= "машина занята"
        else:
            busy= "машина свободна"

        return f"Данные о машине цвет {self.color} , количество мест {self.count_passenger_seats},{baby},{busy}"