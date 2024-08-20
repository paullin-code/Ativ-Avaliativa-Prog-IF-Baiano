# importando as funcoes de arquivos separados
from funcoes.adicionar_ctt import adicionar
from funcoes.remover_ctt import remover
from funcoes.editar_ctt import editar
from funcoes.pesquisar_ctt import pesquisar
from funcoes.listar_ctt import listar

# importando as listas
from listas.listas_ctt import *

# importando todas as funcoes do outros arquivos (funcoes.py)
# from funcoes import *

# importando apenas o system para limparmos o teminal com o "cls"
from os import system

# menu criado para interacao com usuario
menu = '''
----Agenda----
1 - Adicionar
2 - Editar
3 - Remover
4 - Listar
5 - Pesquisar Contato
--------------
0 - Sair
--------------

Opção: ''' 

# repeticao principal
resp_principal = "s"
while resp_principal == "s":

    # limpando a tela
    system("cls")

    # exibindo menu e capturando opcao
    opcao = input(menu)
    
    if opcao == "1":

        # repeticao secundaria para adicionar contato
        while True:
            # limpando a tela
            system("cls")
            # entrada de dados
            nome = input("Digite o NOME do contato: ").capitalize()
            email = input("Digite o EMAIL do contato: ")

            # verificando validade do email
            if "@" not in email:
                resp = input("O E-Mail pode estar incorreto!\nDeseja tentar adicionar novamente: (s/n): ").lower()
                if resp == "s":
                    continue
                elif resp == "n":
                    print("Retornaremos ao menu inicial!")
                    break
                else:
                    print("Resposta não identificada!")
                    break
            # verificando validade do telefone
            telefone = input("Digite o TELEFONE do contato: OBS: (Conter no mínimo oito/8 dígitos): ")
            if len(telefone) < 8:
                resp = input("O Telefone tem menos de oito/8 dígitos!\nDeseja tentar adicionar novamente: (s/n): ").lower()
                if resp == "s":
                    continue
                elif resp == "n":
                    print("Retornaremos ao menu inicial!")
                    break
                else:
                    print("Resposta não identificada!")
                    break

            # chamando a funcao que adiciona o contato
            adicionar(nome, email, telefone)

            # exibindo mensagem de sucesso
            print("Contato adicionado com sucesso!")
            input("Pressione Enter para continuar...")
            break

    elif opcao == "2":

        # repeticao secundaria para editar contato
        while True:
            # limpando a tela
            system("cls")
            # exibindo lista de contatos
            print("----------Lista de contatos----------")
            for ordem in ids:
                print(f"ID: {ordem} | Nome: {nomes[ordem]} | Email: {emails[ordem]} | Telefone: {telefones[ordem]}")

            id_edit = int(input("Digite o ID que deseja editar: "))

            if id_edit in ids:
                # exibindo contato selecionado
                print("----------Contato Selecionado----------")
                print(f"ID: {id_edit} | Nome: {nomes[id_edit]} | Email: {emails[id_edit]} | Telefone: {telefones[id_edit]}")
                var_edit = input("Deseja editar qual item (nome/email/telefone): ").lower()
                if var_edit in ["nome", "email", "telefone"]:
                    editar(var_edit, id_edit)
                    print("Contato editado com sucesso!")
                    input("Pressione Enter para continuar...")
                    break
                else:
                    print("O item que você digitou não foi encontrado!")
                    resp = input("Deseja tentar editar novamente: (s/n): ").lower()
                    if resp == "s":
                        continue
                    elif resp == "n":
                        break
                    else:
                        print("Resposta não identificada!")
                        break
            else:
                # verificacao caso nao encontre o ID que esta sendo procurado
                print(f'Não há ninguém com o ID "{id_edit}" na agenda!')
                resp = input("Deseja tentar editar novamente: (s/n): ").lower()
                if resp == "s":
                    continue
                elif resp == "n":
                    break
                else:
                    print("Resposta não identificada!")
                    break

    elif opcao == "3":
        
        # repeticao secundaria para remover contato
        while True:
            # limpando a tela
            system("cls")
            # exibindo lista de contatos
            print("----------Lista de contatos----------")
            for ordem in ids:
                print(f"ID: {ordem} | Nome: {nomes[ordem]} | Email: {emails[ordem]} | Telefone: {telefones[ordem]}")

            id_remov = int(input("Digite o ID que deseja remover: "))

            if id_remov in ids:
                # exibindo contato selecionado
                print("----------Contato Selecionado----------")
                print(f"ID: {id_remov} | Nome: {nomes[id_remov]} | Email: {emails[id_remov]} | Telefone: {telefones[id_remov]}")
                
                # garantindo que o usuario realmente deseja remover esse contato
                certeza = input("Deseja remover esse contato: (s/n): ").lower()
                if certeza == "s":
                    remover(id_remov)
                    print("Contato removido com sucesso!")
                    input("Pressione Enter para continuar...")
                    break
                elif certeza == "n":
                    break
                else:
                    print("Resposta não identificada!")
                    break
            # verificacao caso nao encontre o ID que esta sendo procurado
            else:
                print(f'Não há ninguém com o ID "{id_remov}" na agenda!')
                resp = input("Deseja tentar remover novamente: (s/n): ").lower()
                if resp == "s":
                    continue
                elif resp == "n":
                    print("Retornaremos ao menu inicial!")
                    break
                else:
                    print("Resposta não identificada!")
                    break

    elif opcao == "4":
        # limpando a tela
        system("cls")
        # exibindo contatos
        print(listar())
        input("Pressione Enter para continuar...")

    elif opcao == "5":

        # repeticao secundaria para pesquisar contato
        while True:
            # limpando a tela
            system("cls")
            nome_pes = input("Digite o nome que deseja encontrar: ").capitalize()
            resp = pesquisar(nome_pes)

            # verificando o que ira voltar da funcao pesquisar()
            if resp == None:
                break
            elif resp == "s":
                continue
            elif resp == "n":
                print("Retornaremos ao menu inicial!")
                break
            else:
                print("Resposta não identificada!")
                break

    # saindo da agenda
    elif opcao == "0":
        print("Saindo da agenda...")
        resp_principal = "n"
        break

    #verificando caso a opcao nao seja uma valida
    else:
        print("Opção não identificada!\nVamos tentar novamente...")
        input("Pressione Enter para continuar...")
        resp_principal = "s"
