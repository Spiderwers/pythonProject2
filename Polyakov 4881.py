#Amin :
#задать пустое А
#добавить все х, в которых f - ложь

#задать все множества, задать функцию, перебор знач. x, вывод A

p = {1, 12}
q = {12, 13, 14, 15, 16}
a = set()


def f(x):
    return (x not in a) <= ((x not in p) and (x not in q))


for x in range(1, 1000):
    if f(x) == 0:
        a.add(x)

print(a)


