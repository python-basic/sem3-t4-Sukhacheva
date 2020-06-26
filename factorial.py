def main():
    n = -1
    num = input("Введите число: ")
    try:
        n = int(num)
    except:
        print("Вы ввели неверное значение")
    res = fact(n)
    print(res)


def fact(num):
    if type(num) is int and num >= 0:
        fc = 1
        i = num
        if num == 0:
            return 1
        else:
            while i > 1:
                fc = fc * i
                i -= 1
        return fc
    else:
        raise ValueError("Вы ввели неверное число")
