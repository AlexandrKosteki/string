s=str(input('Introduce sirul de caractere'))
majuscule=0
cifre=0
speciale=0
for n in s:
    if ord(n) in range(65,91):
        majuscule+=1
    if ord(n) in range(48,58):
        cifre+=1
    if ord(n) in range(33,48) or ord in range(58,65) or ord in range(123,127) or ord in range(91,97):
        speciale+=1
print('Numarul de majuscule e {}'.format(majuscule))
print('Numarul de cifre e {}'.format(cifre))
print('Numarul de caractere speciaale e {}'.format(speciale))