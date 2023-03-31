class A: 
    def z(self): 
        return self 
 
    def y(self, t): 
        return len(t) 
 
a = A 
y = a.z 
print(y(a))  # definimos la variable y como la función de z de la clase A
aa = a() 
print(aa is a())  # no es verdad que aa sea una instancia de a
z = aa.y  # la variable z es la función y() de la instancia aa
print(z(()))  # entonces la longitud de 0 arumentos es 0
print(a().y((a,)))  # la funcion y() de la instancia de a tiene 1 argumento entonces la longitud es 1
print(A.y(aa, (a,z)))  # la funcion y() de la clase A tiene 2 argumentos entonces la longitud es 2
print(aa.y((z,1,'z')))  # la funcion y() de la instancia aa tiene 3 argumentos entonces la longitud es 3
