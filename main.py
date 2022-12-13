import pyAesCrypt

password = input("Введите пароль для файла: ")

#шифрование
pyAesCrypt.encryptFile("file.txt", "cryptfile.txt.aes", password)
#первым указываем файл который хотим зашифровать
#вторым указываем название зашифрованного файла
#третьим указываем пароль

#дешифрование
pyAesCrypt.decryptFile("cryptfile.txt.aes", "decryptfile.txt", password)
#первым указываем зашифрованный файл
#вторым указываем название дешифрованного файла
#третьим указываем пароль