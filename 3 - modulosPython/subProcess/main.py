import subprocess

# Windows Comandos - ping 127.0.0.1

# Linux Comandos - ping 127.0.0.1 -c 4

# Executará o ping que mandei em formato de lista cada argumento, usei o parâmetro carpture output para pegar
# a saída do comando, e o text para converter essa saída que por padrão é bytes para text,
# assim posso manipular o retorno
proc = subprocess.run(['ping', '127.0.0.1'], capture_output=True, text=True)

# print(proc.stderr) # Para Capturar se houver erro
saida = proc.stdout  # Para capturar a saída do comando

print(saida)
# print(proc.returncode)
# print(proc.args) # Os argumentos que passei na lista mais acima
