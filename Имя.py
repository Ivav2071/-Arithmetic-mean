def aver(args):
    num = [i for i in args if i != 0]
    return sum(num) / len(num)

num1 = input("Введите числа,через запятую: ")
list = num1.split(",")
list1 =[]
for i in list:
    list1.append(int(i))


print(aver(list1))
int(input("Нажмите""Enter""чтобы закрыть программу"))

