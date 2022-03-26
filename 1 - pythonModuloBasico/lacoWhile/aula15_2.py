"""
While / Else
contadores
Acumuladores
"""

contador = 1
acumulador = 1

while contador < 100:
    print(contador, acumulador)

    acumulador = acumulador + contador # Aqui estou acumulando valor a cada loop
    contador += 1 # Aqui atribuo +1 ao contador a cada loop
else: # NO while em python podemos usar o ELSE também
    print("Cheguei no else.")

#  Serve para casos em que há um break no While, em casos que queira quebrar o laço
#  Em determinado momento em que a condição ainda é true, mas não desejo executar o que está no
#  else, quando chegar no break o trecho else é pulado na execução.