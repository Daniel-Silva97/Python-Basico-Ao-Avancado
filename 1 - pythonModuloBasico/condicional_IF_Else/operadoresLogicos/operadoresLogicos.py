"""
Operadores Lógicos

* and - Será true somente se todas as expressões forem verdadeiras
* or - Será true quando uma das expressões for verdadeira
* not - É o inverso de alguma expressão
* in -
* not in -
"""


#  AND
#  (Verdadeiro   E  Verdadeiro) = Verdadeiro
#    comparacao1 and comparacao2
#  (Verdadeiro   E  Falso)      = Falso
#    comparacao1 and comparacao2

#  OR
#  (Verdadeiro  OU  Verdadeiro) = Verdadeiro
#    comparacao1 or  comparacao2
#  (Verdadeiro  OU  Falso)      = Verdadeiro
#    comparacao1 or  comparacao2
#  (False       OU  Falso)      = Falso
#    comparacao1 or  comparacao2


#NOT
#  A expressão abaixo significa "Se comparacao1 não for maior do que comparacao2"
#  if not comparacao1 > comparacao2

# Podemos usar para validar se uma variável precisa ser preenchida, por exemplo:
#  if not a:
#    print('Preencha o valor de A.')


#IN
#  name = 'Daniel Silva'
#IN é usado para saber se na variável há o valor que busco, por exemplo:
#  if 'u' in name:
#    print('Existe a letra')


#NOT IN (Inverso de IN) "Se não existe"
#  if 'u' in name:
#    print('Não existe a letra')