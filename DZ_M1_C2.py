def zadanie_1():
    a = float(input("a "))
    b = float(input("b "))
    c = float(input("c "))
    print ('Addition = ' + str(a + b + c))
    print ('Multiplication = ' + str(a * b * c))


def zadanie_2():
    a = float(input("zarplata "))
    b = float(input("platez credita "))
    c = float(input("platez communal uslugi "))
    summa = a - b - c
    if summa < 0:
        print ('ne xvatilo deneg ' + str(summa))
    else:
        print ('ostalos deneg ' + str(summa))


def zadanie_3():
    a = float(input('diagonal a '))
    b = float(input('diagonal b '))
    s = a * b / 2
    print ('ploshad romba = ' + str(s))


def zadanie_4():
    ex = 'To be\n' + 'or not\n' + 'to be'
    print (ex)


def zadanie_5():
    ex = 'Life is what happens\n\t when\n\t\t you`re busy making other plans\n\t\t\t\t\t John Lennon.'
    print (ex)


def main():
    zadanie_1()
    zadanie_2()
    zadanie_3()
    zadanie_4()
    zadanie_5()


if __name__ == '__main__':
    main()
