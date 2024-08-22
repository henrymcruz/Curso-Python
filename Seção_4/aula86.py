"""
Argumentos nomeados e não noemados em gunções Python
Argumentos nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y):
    print(f'{x=} y={y}', '|', 'x + y =', x + y)

soma(10, 5)
soma(y=2, x=1)