class Palindromo:
    global instancia
    instancia = []

    def __init__(self, palabra):
        self.palabra = palabra
        instancia.append(self.palabra) # añadimos a la lista de instanciados
        
        #comprobar que es una cadena de caracteres válida
        if not isinstance(palabra, str):
            raise TypeError('La palabra debe ser una cadena de caracteres')

        # enunciado
        if not self.esPalindromo(palabra): # si la palabra no es palíndromo
            print(instancia[-2].upper()) # imprime la palabra anterior en mayúsculas
        else:
            pass
    
    @staticmethod
    def esPalindromo(cadena):
        palabra = cadena.replace(" ", "")  #quitamos espacios
        palabra = palabra.lower() #ponemos todo en minúsculas  
        palabra_invertida = palabra[::-1]
        if palabra == palabra_invertida:
            return True
        else:
            return False


    def test(self):
        if self.esPalindromo(self.palabra): # si la palabra es palindromo
            return True
        else:
            print('False')
            return self.palabra.upper()


if __name__ == '__main__':
    p = Palindromo("radar") 
    print(p.test()) 
    p = Palindromo("sonar") 
    print(p.test())
