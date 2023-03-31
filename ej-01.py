class Palindromo:

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
