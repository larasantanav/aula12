import os
import shutil
# Exercício 1: Criar um Arquivo
 with open('HOJE', 'w') as arquivo:
     os.mkdir('aula_de_python')


# Exemplo 2: Entrar em um Diretório
 with open('C:/Users/aluno/Desktop/hoje/aula_de_python/texto.txt') as arquivo:
    for arquivos in arquivo:
         print(arquivos)


#Exercício 3: Renomear um Diretório
 os.rename('aula_de_python', 'aula12')


#Exercício 4: Remover um Diretório
 shutil.rmtree("C:/Users/aluno/Desktop/hoje/pastateste")


# Exercício 5: Listar Arquivos em um Diretório
 with os.scandir('C:/Users/aluno/Desktop/hoje/aula12') as arquivos:
     for arquivo in arquivos:
         if arquivo.is_file():
             print(f'Arquivo encontrado: {arquivo}')



# Exercício 6: Copiar Arquivos em um Diretório
shutil.copytree('C:/Users/aluno/Desktop/hoje/aula12', 'teste3')