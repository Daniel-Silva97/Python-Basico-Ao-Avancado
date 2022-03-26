print(123456)

print('Daniel', 'Silva', 'Pedro')

"""
Função sep no print serve para informar 
qual o separador deseja usar entre as palavras
PADRÃO = [ESPAÇO]
"""
print('Daniel', 'Silva', sep='_')

"""
Função END no print serve para mudar o padrão de quebra de linha 
após executar o print, por exemplo:
"""

print('Daniel', 'Silva', sep='_', end='')
#  Irá mudar de quebra linha para branco, mantendo na mesma linha
print('João', 'Silva', sep='_')

#  Print(www) Case sensitive, não funciona em maiusculo
print('824', '176', '070', sep='.', end='-')
print('18')
