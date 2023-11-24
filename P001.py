a = 5
b = 3
#Exercicio 2 Atividade 1  - Tópico 01
# Operadores Aritméticos
soma = a + b
print(f'Adição: {soma}')

subtracao = a - b
print(f'Subtração: {subtracao}')

multiplicacao = a * b
print(f'Multiplicação: {multiplicacao}')

divisao = a / b
print(f'Divisão: {divisao}')

divisao_inteira = a // b
print(f'Divisão Inteira: {divisao_inteira}')

resto_divisao = a % b
print(f'Resto da Divisão: {resto_divisao}')

potencia = a ** b
print(f'Potenciação: {potencia}')

# Operadores Aritméticos Compostos
c = 2

c += a
print(f'Adição e Atribuição: {c}')

c -= b
print(f'Subtração e Atribuição: {c}')

c *= a
print(f'Multiplicação e Atribuição: {c}')

c /= b
print(f'Divisão e Atribuição: {c}')

c //= a
print(f'Divisão Inteira e Atribuição: {c}')

c %= b
print(f'Resto da Divisão e Atribuição: {c}')

c **= b
print(f'Potenciação e Atribuição: {c}')

#Tópico 02, 03 e 04
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

resultado_fatorial = fatorial(30)
print(f'O fatorial de 30 é: {resultado_fatorial}')

import ctypes

maior_valor_inteiro_cpp = ctypes.c_ulonglong(-1).value
print(f'Maior valor inteiro em C++: {maior_valor_inteiro_cpp}')

a = 5
b = a + 3
print(f'Depois da alteração: {b}')

num = 12345

str_num = str(num)
print(f'Número como string: {str_num}')

bin_num = bin(num)
print(f'Representação binária: {bin_num}')

hex_num = hex(num)
print(f'Representação hexadecimal: {hex_num}')

oct_num = oct(num)
print(f'Representação octal: {oct_num}')
