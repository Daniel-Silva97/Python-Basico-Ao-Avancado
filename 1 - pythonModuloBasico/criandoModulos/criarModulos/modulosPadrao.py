"""
Módulos padrão do Python
Modulos são arquivos .py (que contém códigos python) e servem para expandir
as funcionalidades padrão da linguagem.
Veja todos os módulos padrão do Python em:
https://docs.python.org/3/py-modindex.html
"""

# Há 2 formas de importar os módulos
# O módulo completo
import sys

# Somente uma opção deste módulo
from sys import platform
# Nesse caso não precisa digitar sys.platform para usar, apenas platform é o suficiente

print(sys.platform)
