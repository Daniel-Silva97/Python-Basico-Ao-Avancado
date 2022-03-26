import os
import shutil

caminho_original = r'C:\Users\user\Documents\aulamoverarquivo'
caminho_a_mover = r'C:\Users\user\Documents\moveraqui'

try:
    os.mkdir(caminho_a_mover)
except FileExistsError as e:
    print(f'Pasta {caminho_a_mover} já existe.')

# Navegando pelo diretório raiz (root), dirs (pastas) e files que são os arquivos
for root, dirs, files in os.walk(caminho_original):  # os.walk - Passa um caminho como parametro para caminhar dentro /
    # dessa pasta
    # Navegando arquivo a arquivo neste laço
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_a_mover, file)
        print(new_file_path)
        if '.txt' in file:  # Apenas arquivos com extensão TXT
            # shutil.move(old_file_path, new_file_path) # Mover Arquivo
            shutil.copy(old_file_path, new_file_path)  # Copiar arquivo
            print(f'Arquivo {file} movido com sucesso!')

print()
print()
print()

for root, dirs, files in os.walk(caminho_a_mover):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_a_mover, file)
        print(new_file_path)
        if '.txt' in file:
            os.remove(new_file_path)  # Removendo arquivos
            print(f'Arquivo {file} removido com sucesso!')
