
# variáveis
idade = 18
ano = 2002
altura = 1.76
peso = 89.90
nome = "guilherme"
#variável complexa
a = 5 + 2j
b = 20 + 6j

print(type(idade))
print(type(ano))
print(type(altura))
print(type(peso))
print(type(a))
print(complex(2,5))

#Estrutura condicional simples

soma = 3
if soma > 0:
    print("maior que Zero")
else:    
    print("menor que Zero")

if idade > ano:
    print("a e b são iguais")
elif idade < ano:
    print("a é maior que b")
else:
    print("a é menor que b")
#loops com while
contador = 0
while contador < 10:
    print(f'valor do contadore é {contador}')
    contador += 1


#Loops utilizando while


contador2 = 0

while contador2 <= 100:
  print(f'valor do contador é {contador}')
  contador2 +=1
  





