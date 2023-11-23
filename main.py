import qrcode
import pandas as pd

# Criar uma lista de dados a serem codificados em QR codes
dados = ['''{
         "rua":1,
         "bloco":1,
         "nivel":1,
         "apartamento":1
    }''', '''{
         "rua":1,
         "bloco":1,
         "nivel":1,
         "apartamento":2
    }''']

# Criar uma lista vazia para armazenar as imagens dos QR codes
imagens = []

# Para cada dado na lista de dados
i = 1
for dado in dados:
  
  # Criar um QR code a partir do dado
  img = qrcode.make(dado)
  # Adicionar a imagem do QR code à lista de imagens
  img.save(f'qrcode{i}.png')
  i += 1
  imagens.append(img)

# Criar um DataFrame do pandas com os dados e as imagens
df = pd.DataFrame({"Dados": dados, "Imagens": imagens})

# Salvar o DataFrame em um arquivo Excel
df.to_excel("qrcodes.xlsx", index=False)