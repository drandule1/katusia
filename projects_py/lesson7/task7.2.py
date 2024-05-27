# 2.  Написать класс Taxi
# Конструктор класса принимает атрибуты:
# cars: list[Car] (список экземпляров класса Car)
# 2.1 Реализовать метод find_car
# На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров,
# наличие ребенка, примечание: количество пассажиров с учетом ребенка если он есть)
# На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и
# свободный (is_busy = False), у автомобиля сменить атрибут is_busy на значение True, если
# подходящего автомобиля нет, метод должен возвращать None

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

class taxi:
    cars: list

    def  __init__(self,cars):
        self.cars=cars

    def find_car(self,count_passengers,is_baby):
        for mycar in self.cars:
            #print(mycar)
            if mycar.is_busy == False  and  is_baby==False:
                if mycar.is_baby_seat and mycar.count_passenger_seats-1 >= count_passengers:
                    print(mycar)
                    mycar.is_busy=True
                    return mycar
                elif mycar.is_baby_seat == False  and mycar.count_passenger_seats >= count_passengers:
                    print(mycar)
                    mycar.is_busy = True
                    return mycar
            elif mycar.is_busy == False  and  is_baby==True:
                if mycar.is_baby_seat and mycar.count_passenger_seats >= count_passengers:
                    print(mycar)
                    mycar.is_busy = True
                    return mycar
                elif mycar.is_baby_seat == False:
                    continue
        else:
            print("машин нет")
            return None






car1=car("car1", 4, True)
car2=car("car2", 5, False)
car3=car("cat3", 4, False)
car4=car("car4", 2, True)
car5=car("car5", 6, True)

listcar=[car1,car2,car3,car4,car5]

mytaxi=taxi(listcar)
mytaxi.find_car(5,True)





