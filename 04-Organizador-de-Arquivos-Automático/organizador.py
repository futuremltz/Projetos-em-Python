import os
import shutil


pasta = "C:/Users/MeuUsuario/Downloads"

categorias = {
  ".pdf": "Documentos",
  ".docx": "Documentos",
  ".mp3": "Musicas",
  ".mp4": "Vídeos",
  ".png": "Imagens",
  ".jpg": "Imagens",
  ".c": "Programação"
}

lista_arquivos = os.listdir(pasta)

for arquivo in lista_arquivos:

  caminho = os.path.join(pasta, arquivo)

  if os.path.isdir(caminho):
    continue

  nome, extensao = os.path.splitext(arquivo)

  extensao = extensao.lower()

  if extensao in categorias:
    nome_pasta = categorias[extensao]
    caminho_pasta = os.path.join(pasta, nome_pasta)

    if not os.path.exists(caminho_pasta):
      os.makedirs(caminho_pasta)

    caminho_destino = os.path.join(caminho_pasta, arquivo)
    shutil.move(caminho, caminho_destino)

    print(f"Sucesso! O arquivo '{arquivo}' foi movido para a pasta '{nome_pasta}'")