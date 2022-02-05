#Sintaxis
#variable = lambda argumento: codigo a ejecutar

palindromo = lambda string: string == string[::-1]

print(palindromo("ana"))
#Esto es lo mismo que

def palindrome(string2):
    return string2 == string2[::-1]

print(palindrome("ana"))

