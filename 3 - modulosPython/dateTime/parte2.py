from datetime import datetime
# Importando o locale para definir a região da máquina
from locale import setlocale, LC_ALL
# Importando o calendar para saber o ultimo dia de cada mês com mdays
from calendar import mdays, monthrange

# Usando desta forma ele sempre tentará utilizar o local da máquina que executar
setlocale(LC_ALL, '')

# Salvando a data atual
data = datetime.now()
mes_atual = int(data.strftime('%m'))
formatandoData = data.strftime('%A, %d de %B de %Y')
formatandoData2 = data.strftime('%d/%m/%Y %H:%M:%S')

print(formatandoData)
print(formatandoData2)

# Vendo o último dia do mês atual
print(mes_atual, mdays[mes_atual])


# Para evitar erros em ano bissexto, abaixo criamos a lista do mdays validando tbm o ano bissexto
ultimos_dias_de_meses_do_ano_atual = [
    monthrange(datetime.now().year, mes)[1] for mes in range(1, 13)
]
print(ultimos_dias_de_meses_do_ano_atual)
# Saída: [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Observação: meu ano atual é 2020 neste momento
