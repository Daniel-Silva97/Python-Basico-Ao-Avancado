import os
from PIL import Image


def main(mainImagesFolder, newWidht=800):
    # Checando se a pasta existe
    if not os.path.isdir(mainImagesFolder):
        raise NotADirectoryError(f'{mainImagesFolder} Não é um diretório')

    # Caminhando pelo diretório
    for root, dirs, files in os.walk(mainImagesFolder):
        for file in files:
            caminhoCompleto = os.path.join(root, file)  # caminho completo arquivo original
            fileName, extension = os.path.splitext(file)  # Separando nome do arquivo da extensão
            convertedTag = '_CONVERTED'  # para usar no arquivo convertido
            newFile = fileName + convertedTag + extension  # montando o nome do arquivo novo (AINDA SEM CONVERTER)
            newFileFullPath = os.path.join(root, newFile)  # Pegando o novo caminho completo dos arquivos com o
            # CONVERTED

            if os.path.isfile(newFileFullPath):
                print(f'{newFileFullPath} já existe')
                continue

            if convertedTag in caminhoCompleto:  # Se já existir arquivo com CONVERTED ele não faz a conversão novamente
                print('Imagem já convertida')
                continue

            imgPillow = Image.open(caminhoCompleto)
            width, height = imgPillow.size
            # print(width, height)

            """ Pegando a nova Height de acordo com o Width passado:

            widht = height
            newWidth = X

            """
            # Gerando a nova altura
            newHeight = round(newWidht * height / width)
            # print(width, newWidht, height, newHeight)

            newImage = imgPillow.resize(
                (newWidht, newHeight),
                Image.LANCZOS
            )
            newImage.save(
                newFileFullPath,  # Usando o nome novo que criamos
                optimize=True,
                quality=70,
                exif=imgPillow.info['exif']  # Copiando as infos da imagens que aparece nas propriedades, como o nome
                # do Fotógrafo e dados da câmera por exemplo
            )
            print(f'{caminhoCompleto} convertido com sucesso!')
            newImage.close()
            imgPillow.close()


if __name__ == '__main__':
    mainImagesFolder = r'C:\Workspaces\ws-python\3 - modulosPython\redimensionandoImagensPillow\imagens'
    main(mainImagesFolder)
