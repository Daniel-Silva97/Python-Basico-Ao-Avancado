from datetime import datetime, timedelta

# Criando uma data com DateTime
# Formato é (Ano, Mês, Dia, Hora (Opcional), Minutos (Opcional), Segundos (Opcional))
data = datetime(2022, 3, 21, 18, 29, 20)
# Cria no padrão americano
print(data)
# Convertendo para BR com strftime()
print(data.strftime('%d/%m/%Y %H:%M:%S'))

# Convertendo um valor data recebido para o objeto Data usando strptime()
converteParaObjetoData = datetime.strptime('11/01/2022', '%d/%m/%Y')
print(converteParaObjetoData)

# Adquirindo o TimeStamp de uma data
timestamp = data.timestamp()
print(timestamp)

# Pegando a data por meio do Timestamp
print(datetime.fromtimestamp(timestamp))

# Usando o timedelta
# Acrescentando 5 dias a uma data específica
novaData = data + timedelta(days=5)
print(novaData)
# Acrescentando 5 horas a uma data específica
novaData = data + timedelta(hours=5)
print(novaData)
# Acrescentando 5 minutos a uma data específica
novaData = data + timedelta(minutes=5)
print(novaData)
# Acrescentando 5 segundos a uma data específica
novaData = data + timedelta(seconds=5)
print(novaData)

# Acrescentando horas usando calculos
novaData = data + timedelta(hours=5 * 60)
print(novaData)

# Calculos entre datas
data1 = datetime.strptime('11/01/2022 22:00:00', '%d/%m/%Y %H:%M:%S')
data2 = datetime.strptime('20/01/2022 10:00:00', '%d/%m/%Y %H:%M:%S')
diferencaEntreDatas = data2 - data1

# Vendo a diferença total
print(diferencaEntreDatas)
# Vendo os segundos
print(diferencaEntreDatas.seconds)
print(diferencaEntreDatas.total_seconds())

# Vendo o total de dias
print(diferencaEntreDatas.days)

# Vendo somente a hora do objeto
print(data1.time())

# Comparações entre datas
print(data2 > data1)



