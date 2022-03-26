#  https://ffmpeg.zeranoe.com/builds

"""

Comando FFMPEG

ffmpeg -i "ENTRADA" -i "LEGENDA" -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k
-c:s srt -map v:0 -map a -map 1:0 -ss 00:00:00 to 00:00:10 "SAIDA"
"""

import os
import fnmatch
import sys

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'C:\Users\user\Documents\ffmpeg\ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'

caminho_origem = r'C:\Users\user\Videos'
caminho_destino = r'C:\Workspaces\ws-python\3 - modulosPython\FFMPEG\saida'

for raiz, pasta, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*.mkv'):
            continue

        caminho_completo = os.path.join(raiz, arquivo)
        nomeArquivo, extesaoArquivo = os.path.splitext(caminho_completo)
        caminho_legenda = nomeArquivo + '.srt'

        if os.path.isfile(caminho_legenda):
            input_legenda = f'-i "{caminho_legenda}"'
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            input_legenda = ''
            map_legenda = ''

        nomeArquivo, extesaoArquivo = os.path.splitext(arquivo)
        arquivoSaida = f'{caminho_destino}/{nomeArquivo}_NOVO{extesaoArquivo}'

        comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} ' \
                  f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio} ' \
                  f'{debug} {map_legenda} "{arquivoSaida}"'

        os.system(comando)
