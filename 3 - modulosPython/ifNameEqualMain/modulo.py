def soma(x: float, y: float) -> float:
    return x + y

# Este trecho de código só executará se o arquivo modulo.py for executado DIRETAMENTE
# Se acionado por outros módulos através do import, não executa este trecho.
if __name__ == '__main__':
    print(soma(50, 60))
    print(__name__)
