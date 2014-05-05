#lambdas ( + progr. funcional )
doble = lambda x: x * 2

print(doble(6))
print(doble(4))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


Point.getX = lambda self: self.x
Point.getY = lambda self: self.y
Point.__str__ = lambda self: str.format("({0}, {1})", self.getX(), self.getY())

# sentencia if reducida
y = 5
x = 4 if y == 7 else 2
# Si Y vale 7, el valor de X es 4, sino 2

car = lambda l: None if l == None or l == [] else l[0]
cdr = lambda l: None if l == None else l[1:]

l = [1, 2, 3]
print(car(l))
print(cdr(l))

lCopy = lambda l: None if l == None else [] if l == [] else [car(l)] + lCopy(cdr(l))
print(lCopy([]))
print(lCopy(l))

# Funcion lambda que crea una copia de la lista con los elementos multiplicados por dos
lCopyDoble = lambda l: None if l == None else [] if l == [] else [doble(car(l))] + lCopyDoble(cdr(l))
print(lCopyDoble([]))
print(lCopyDoble([1, 2, 3]))
# with map
map = lambda func, l: None if l == None else [] if l == [] else [func(car(l))] + map(func, cdr(l))
print(map(doble, []))
print(map(doble, [1, 2, 3]))
print(map(lambda x: x * x * x, [1, 2, 3]))

#override python filter function
filter = lambda f, l: None if l == None else [] if l == [] else [car(l)] + filter(f, cdr(l)) if f(car(l)) else filter(f,
                                                                                                                      cdr(
                                                                                                                          l))
print(filter(lambda x: True if x % 2 == 0 else False, [1, 2, 3, 4, 5, 6]))

reduce = lambda f, l: None if l == None else None if l == [] else car(l) if len(l) == 1 else f(car(l),
                                                                                               reduce(f, cdr(l)))
print(reduce(lambda x, y: x + y, [1, 2, 3]))
print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))

#override lCopy
lCopy = lambda l: map(lambda x: x, l)
print(lCopy([1, 2, 3]))

#Fibonacci with lambda
fibonacci = lambda x: [0] if x <= 0 else [0, 1] if x == 1 else fibonacci(x-1) + [ fibonacci(x-1)[-1] + fibonacci(x-1)[-2] ]
print(fibonacci(4))
print(fibonacci(6))
print(fibonacci(8))
print(fibonacci(10))

## Crear las siguientes funciones usando CAR y CDR
    ## ultimo(l)
    ## penultimo(l)
    ## reescribir fib() para utilizarlas
## Reescribir fibo en terminos de map, filter y reduce
ultimo = lambda l: None if l == [] or l == None else car(l) if len(l) == 1 else ultimo(cdr(l))
print(ultimo([1,2,3]))

##penultimo = lambda l: None if l == [] or l == None