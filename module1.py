from math import pow
a=0
time=10#int(input('Введите время != 0'))
start_speed=0#int(input('Введите скорость'))
final_speed=20#int(input('Введите скорость'))

def Decorator(calculator):
    def wrapper(t,sV,fV):
        a=calculator(t,sV,fV)
        S=sV*t+(1/2)*a*pow(t,2)
        print('Расстояние --',S)
    return wrapper
try:

    @Decorator
    def calculator(t,sV,fV):
        a=(fV-sV)/t
        print('Ускорение --',a)
        return(a)


    calculator(time,start_speed,final_speed)
except ZeroDivisionError:
    print('Время не должно быть равно 0')
except ValueError:
    print('Не корректное значения')


