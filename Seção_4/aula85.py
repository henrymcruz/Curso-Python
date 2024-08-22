"""
Introdução as funções (def) em python
Funções são trechos de códigos usados para
replicar determinada ação ao longo do seu codigo
Elas podem receber valores para parametros (argumentos)
e retornar um valor especifico.
Por padrão, funções Python retornam None (nada).
"""

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)