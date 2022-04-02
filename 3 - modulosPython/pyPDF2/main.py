"""
Documentação:
https://pythonhosted.org/PyPDF2/

Mais exemplos de uso:
http://www.blog.pythonlibrary.org/2018/06/07/an=intro-to-pypdf2/

pip install pypdf2 # VirtualEnv
pipenv install pypdf2 # pipenv
"""
import PyPDF2
import os

"""
caminhoDosPdfs = 'pdf'  # Caminho dos arquivos no sistema

# Trecho de código que unifica dois arquivos PDF

novoPdf = PyPDF2.PdfFileMerger()  # Criando o objeto do PyPDF2

# Navegando na pasta dos arquivos PDF
for root, dirs, files in os.walk(caminhoDosPdfs):
    for file in files:
        caminhoCompleto = os.path.join(root, file)  # Pegando o caminho completo

        arquivoPdf = open(caminhoCompleto, 'rb')  # Unificando os arquivos
        novoPdf.append(arquivoPdf)

with open(f'{caminhoDosPdfs}/novoArquivo.pdf', 'wb') as meuNovoPdf:  # Criando um novo arquivo com os dados
    # unificados feitos acima
    novoPdf.write(meuNovoPdf)
"""

# Trecho que cria um arquivo PDF por página
with open('pdf/novoArquivo.pdf', 'rb') as arquivoPDF:
    leitor = PyPDF2.PdfFileReader(arquivoPDF)  # Criando o objeto que le o arquivo PDF que desejo separar
    numeroPaginas = leitor.getNumPages()  # Obtendo o número de páginas do arquivo

    for numeroPagina in range(numeroPaginas):  # Uso o número de páginas para o laço
        escritor = PyPDF2.PdfFileWriter()  # Criando o objeto que criará o novo arquivo
        paginaAtual = leitor.getPage(numeroPagina)  # obtendo a página atual
        escritor.addPage(paginaAtual)  # Adicionando no escritor a pagina atual do arquivo

        with open(f'novosPDFs/{numeroPagina}.pdf', 'wb') as novoPDF:  # Criando o novo arquivo
            escritor.write(novoPDF)  # Escrevendo a página atual nele
