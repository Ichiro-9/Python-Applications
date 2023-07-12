# tempreature calculator program
import math

CELSIUS = 0
FAHRENHEIT = 1
KELVIN = 2

def Celcius(val,unit):
    val=int(val)
    if unit == FAHRENHEIT:
        statement = '{}°F is equal to {}°C'
        con = (val -32) * (5/9)
        if str(con)[-2:]=='.0':
            con = math.floor(con)
        else:
            con=round(con,3)
        return print(statement.format(val,con))
    elif unit == KELVIN:
        statement = '{}°K is equal to {}°C'
        con = val  - 273.15
        if str(con)[-2:] == '.0':
            con = math.floor(con)
        else:
            con = round(con, 3)
        return print(statement.format(val,con))
    else:
        return print('Unit is not Valid!')




def Fahrenheit(val,unit):
    val=int(val)
    if unit == CELSIUS:
        statement = '{}°C is equal to {}°F'
        con = (val * (9/5)) + 32
        if str(con)[-2:]=='.0':
            con = math.floor(con)
        else:
            con=round(con,3)
        return print(statement.format(val,con))
    elif unit == KELVIN:
        statement = '{}°K is equal to {}°F'
        con = (val * 9/5) - 459.67
        if str(con)[-2:] == '.0':
            con = math.floor(con)
        else:
            con = round(con, 3)
        return print(statement.format(val,con))
    else:
        return print('Unit is not Valid!')




def Kelvin(val,unit):
    val=int(val)
    if unit == FAHRENHEIT:
        statement = '{}°F is equal to {}°K'
        con = (val + 459.67) * (5/9)
        if str(con)[-2:]=='.0':
            con = math.floor(con)
        else:
            con=round(con,3)
        return print(statement.format(val,con))
    elif unit ==    CELSIUS:
        statement = '{}°C is equal to {}°K'
        con = val + 273.15
        if str(con)[-2:] == '.0':
            con = math.floor(con)
        else:
            con = round(con, 3)
        return print(statement.format(val,con))
    else:
        return print('Unit is not Valid!')

if __name__ == '__main__':
    Celcius(33,KELVIN)
    Fahrenheit(33,CELSIUS)
    Kelvin(33, FAHRENHEIT)
