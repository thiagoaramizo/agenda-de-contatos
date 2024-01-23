"""- A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
    - Deve ser possível adicionar um contato
        - O contato pode ter os dados:
        - Nome
        - Telefone
        - Email
        - Favorito (está opção é para poder marcar um contato como favorito)
    - Deve ser possível visualizar a lista de contatos cadastrados
    - Deve ser possível editar um contato
    - Deve ser possível marcar/desmarcar um contato como favorito
    - Deve ser possível ver uma lista de contatos favoritos
    - Deve ser possível apagar um contato
"""
from os import system

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def adicionar_contato(lista):
  nome = input(color.BOLD + "Nome do contato: " + color.END)
  telefone = input(color.BOLD + "Telefone: " + color.END)
  email = input(color.BOLD + "E-mail: " + color.END)

  novo_contato = {
    "nome": nome,
    "telefone": telefone,
    "email": email,
    "favorito": False
  }

  lista.append(novo_contato)
  lista = sorted(lista, key=lambda contato: contato["nome"])
  print(color.GREEN + "\nContato adicionado com sucesso" + color.END)
  return lista

def ver_contatos(lista):
  while True:
    system('clear')
    print(color.DARKCYAN + "\n===== MEUS CONTATOS =====")
  
    for index, contato in enumerate(lista, start=1):
        marcador_de_favorito =  "★ " if contato["favorito"] else ""
        print("\n(" + str(index) + ") " + marcador_de_favorito + contato["nome"] + " | " + contato["telefone"] + " | " + contato["email"])
    print("\n=============================\n" + color.END)
  
    selecao_contato = input(color.BOLD + "Informe o número do contato ou (0) para voltar: " + color.END)

    if selecao_contato == "0":
      break
    else:
      acessar_contato(lista, selecao_contato)
  return

def ver_favoritos(lista):
  while True:
    system('clear')
    print(color.DARKCYAN + "\n===== FAVORITOS =====")
  
    for index, contato in enumerate(lista, start=1):
        if( contato["favorito"] ):
            marcador_de_favorito =  "★ " if contato["favorito"] else ""
            print("\n(" + str(index) + ") " + marcador_de_favorito + contato["nome"] + " | " + contato["telefone"] + " | " + contato["email"])
    print("\n=============================\n" + color.END)
  
    selecao_contato = input(color.BOLD + "Informe o número do contato ou (0) para voltar: " + color.END)

    if selecao_contato == "0":
      break
    else:
      acessar_contato(lista, selecao_contato)
  return

def acessar_contato(lista, indice_str):
  try:
    indice = int(indice_str)-1
    while True:
        system('clear')
        contato = lista[indice]
        marcador_de_favorito =  "★ Favorito" if contato["favorito"] else "☆ Não é favorito"
        texto_de_favorito =  "Tornar favoritos " if not contato["favorito"] else "Remover dos favoritos "
        print(color.DARKCYAN + "\nNome: " + contato["nome"] + "\nTelefone: " + contato["telefone"] + "\nE-mail: " + contato["email"])
        print( marcador_de_favorito )
        print( "Opções: (1)" + texto_de_favorito + "(2)Apagar contato (0)Voltar")
        selecao_contato = input(color.BOLD + "Informe o número de uma das opções: " + color.END)
        if selecao_contato == "0":
            return
        elif selecao_contato == "1":
          favoritar_desfavoritar(lista, indice)
        elif selecao_contato == "2":
            deletar_contato(lista, indice)
            return
        else:
          print(color.RED + "\n" + opcao + " é uma opção inválida, selecione outra opção." + color.END)
  except Exception as e:
    print(color.RED + "\n" + opcao + " é uma opção inválida, selecione outra opção." + color.END)
  return

def favoritar_desfavoritar( lista, indice ):
  lista[indice]["favorito"] = not lista[indice]["favorito"]
  return

def deletar_contato (lista, indice):
  del(lista[indice])
  return

lista_de_contatos = [
  {
    "nome": "Thiago",
    "telefone": "3499999999",
    "email": "email@email.com",
    "favorito": False
  },
  {
    "nome": "Julia",
    "telefone": "3499989898",
    "email": "email@email.com",
    "favorito": True
  }
]

while True:
  system('clear')
  print(color.DARKCYAN + """\n===== LISTA DE CONTATOS =====
\n(1) Ver contatos
\n(2) Ver favoritos
\n(3) Adicionar contato
\n(0) Sair
\n=============================\n""" + color.END)
  
  opcao = input(color.BOLD + "Informe o número da opção desejada: " + color.END)
  
  if opcao == "1":
    ver_contatos(lista_de_contatos)

  elif opcao == "2":
    ver_favoritos(lista_de_contatos)

  elif opcao == "3":
    lista_de_contatos = adicionar_contato(lista_de_contatos)

  elif opcao == "0":
    print(color.RED + "\nEncerrando agenda." + color.END)
    break
  
  else:
    system('clear')
    print(color.RED + "\n" + opcao + " é uma opção inválida, selecione outra opção." + color.END)
