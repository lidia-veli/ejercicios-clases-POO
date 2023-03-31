caracteres_validos = 'abcdefghijklmnñopqrstuvwxyzáéíóúABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ1234567890!"#$%&/()=?¡¿*+[{]}-_.:,;<>|@^~`'


class Palindromo:
    def __init__(self, palabra):
        self.palabra = palabra

        #comprobar que es una cadena de caracteres válida
        if not isinstance(palabra, str):
            raise TypeError('La palabra debe ser una cadena de caracteres')
        for caracter in palabra:
            if caracter not in caracteres_validos:
                raise ValueError('Caracter no válido: ' + caracter)

    @staticmethod
    def esPalindromo(cadena):
        palabra = cadena.replace(" ", "")  #quitamos espacios
        palabra = palabra.lower() #ponemos todo en minúsculas  
        palabra_invertida = palabra[::-1]
        if palabra == palabra_invertida:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Palindromo.esPalindromo('radar')) 
    print(Palindromo.esPalindromo('sonar')) 
    print(Palindromo.esPalindromo('Arde ya la yedra')) 
    print(Palindromo.esPalindromo('Ardeyalayedra')) 
    print(Palindromo.esPalindromo('!@#$% %$#@!')) 
    print(Palindromo.esPalindromo('L O L'))
