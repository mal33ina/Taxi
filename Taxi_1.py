# -*-coding: utf-8 -*-
import datetime




def vxod():# вход в программу через логин и пароль
    today = datetime.datetime.today()
    login = input("Введите логин:")
    password = input("Введите пароль:")
    f1 = open("Parol.txt", "r", 1, "utf-8")
    for line in f1:
        temp = line.split()
        if login == temp[0]:
            print('ok', 'time', today.strftime("%H-%M-%S day %d-%m-%Y"))
        if password == temp[1]:
            print('ok', 'time', today.strftime("%H-%M-%S day %d-%m-%Y"))
        else:
            print('Повторите попытку: time:', today.strftime("%H-%M-%S day %d-%m-%Y"))
            vxod()
    f1.close()



def menu():# главное меню программы
    vybor = int(input('Выбирите вкладку:\n'
                  '1 - Персонал\n'
                  '2 - Автомобили\n'
                  '3 - Склад\n'
                  '4 - Аренда\n'))
    if vybor == 1:
        personal()
    elif vybor == 2:
        avtomobili()
    elif vybor == 3:
        sklad()
    elif vybor == 4:
        arenda()
    else:
        menu()




def personal():# вкладка Персонал
    vybor = int(input('Выбирите вкладку:\n'
                      '1 - Офис\n'
                      '2 - Водители\n'
                      '3 - СТО\n'))
    t = True
    while t:
        choice = int(input('Для перехода в главное меню нажмите "0":\n'))
        if choice == 0:
            t = menu()

def offis():# вкладка Персонал
    vybor = int(input('Выбирите вкладку:\n'
                      '1 - Отдел кадров\n'
                      '2 - Бухгалтерия\n'
                      '3 - Юрист\n'
                      '4 - Специалист заказа товара\n'))
    t = True
    while t:
        choice = int(input('Для перехода в главное меню нажмите "0":\n'))
        if choice == 0:
            t = menu()



def avtomobili():# вкладка Автомобили
    vybor = int(input('Выбирите вкладку:\n'
                      '1 - База\n'
                      '2 - На линии\n'
                      '3 - Ремонт\n'
                      '4 - Гараж\n'))
    if vybor == 1:
        spisok_car()
    elif vybor == 2:
        avtomobili()
    elif vybor == 3:
        remont()
    elif vybor == 4:
        garag()
    else:
        menu()


class Baza:# вкладка база
    def __init__(self, id, Gos_nomer, Marka, model, Color, Probeg):
        self.id = id
        self.Gos_nomer = Gos_nomer
        self.Marka = Marka
        self.model = model
        self.Color = Color
        self.Probeg = Probeg

    def __str__(self):
        return f'{self.id} {self.Gos_nomer} {self.Marka} {self.model} {self.Color} {self.Probeg} км '

def read_file():  # читает значения из файла
    my_cars = []
    f1 = open("Car.txt", "r", 1, "utf-8")
    for line in f1:
        line_s = line.split()
        my_cars.append(Baza(line_s[0], line_s[1], line_s[2], line_s[3], line_s[4], line_s[5]))
    f1.close()
    return my_cars

def spisok_car():  # читает значения из файла и выводит полный список машин
    cars = read_file()
    for car in cars:
        print(car)
    t = True
    while t:
        choice = int(input('Для перехода в главное меню нажмите "0":\n'))
        if choice == 0:
            t = menu()



class Na_linii(Baza):# вкладка на линии
    def summer(self):
        spisok_names = []
        spisok_prices = []
        shopper = True
        while shopper:
            shoper = input("Введите машину, которую ищите (0 - если хотите закончить)\t")
            price = open("Car.txt", "r", 1, "utf-8")
            if shoper == "0":
                shopper = False
            else:
                for i in price:
                    ii = i.split()
                    if ii[0] == shoper.lower():
                        print("Машина есть в наличии")
                        spisok_names.append(ii[0])
                        col = int(input("Введите количество либо вес, который вам необходим\t"))
                        spisok_prices.append(float(ii[1]) * col)
            price.close()
        for elem in range(len(spisok_names)):
            print(f"{spisok_names[elem]} - {spisok_prices[elem]},''")
        Summ_chisel = sum(spisok_prices)
        print("", '% .2f ' % Summ_chisel, "")



class Remont(Baza):
    def __init__(self, pol, vuxod, polomka):
        Baza.__init__(self, id)
        self.pol = pol
        self.vuxod = vuxod
        self.polomka = polomka

    def datin(self):
        return f'{self.id} {self.pol} {self.vuxod} {self.polomka}'

def remont():# вкладка ремонт
    t = True
    while t:
        choice = int(input('Нажмите цифру 1 или для завершения нажмите "0":\n'))
        if choice == 0:
            t = menu()
        if choice == 1:
            today = datetime.datetime.today()
            car = int(input('Введите id машины: \n'))
            try:
                if car > 41:
                    print('Такого id нет "В парке 41 машина"')
                    car = int(input('Введите id машины: \n'))
            except:
                ''
            vvod = input('Введите поломку: \n')
            Mexanic = 'Хелкупин З.Н'
            my_cars = []
            f1 = open("wemont.txt", "a", 1, "utf-8")
            f1.write(today.strftime("%Y-%m-%d "))
            f1.write(f' id: {car}')
            f1.write(f' вид поломки: {vvod}')
            f1.write(f' Mexanic: {Mexanic} \n')
            f1.close()
            menu()
            return my_cars





def garag():# вкладка гараж
    t = True
    while t:
        choice = int(input(' 0 - продолжение\n 1 - предыдущее меню\n 2 - главное меню\n'))
        if choice == 2:
            t = menu()
        if choice == 1:
            t = avtomobili()
        if choice == 0:
            today = datetime.datetime.today()
            car = int(input('Введите id машины: \n'))
            try:
                if car > 41:
                    print('Такого id нет "В парке 41 машина"')
                    car = int(input('Введите id машины: \n'))
            except:''
            f1 = open("garage.txt", "a", 1, "utf-8")
            f1.write(today.strftime("\n%d-%m-%Y"))
            f1.write(f' id:{car}')
            f1.close()
            print(f1)











def sklad():  # вкладка Склад
    vybor = int(input('Выбирите вкладку:\n'
                        '1 - Поставщики\n'
                        '2 - Перемещение товара\n'))
    menu()



def arenda():# вкладка Аренда
    vybor = int(input('Выбирите вкладку:\n'
                      '1 - База\n'
                      '2 - На линии\n'
                      '3 - Ремонт\n'
                      '4 - Гараж\n'))

def fail():
    f1 = open("Car.txt", "r", 1, "utf-8")
    for line in f1:
        line_s = line.split()
        return line_s



menu()


