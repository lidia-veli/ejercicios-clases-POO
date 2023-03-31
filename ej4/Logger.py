class Test:
    def llamada(self, string, file):
        file.write(string)

#Definimos la funcion que importamos desde el main.py y el archivo cat log.txt para su modificacion
def log():
    file = open("ej4/log.txt", "w") # abrir el archivo en modo edición
    file.write("--Start log--\n") # escribir

# utilizamos un bucle para sobreescribir el archivo
    test = Test() # creamos una instancia de la clase Test
    for i in range(1,6): 
        if i == 1: 
            test.llamada("Primera llamada\n", file) 
        else:
                test.llamada("{}a llamada\n".format(i), file) 
    
    file.write("--End log: {} log(s)--".format(i))
    file.close()



if __name__ == "__main__":
    log()
