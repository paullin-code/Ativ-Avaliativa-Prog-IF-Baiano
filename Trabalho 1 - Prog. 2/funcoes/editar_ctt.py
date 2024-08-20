# importando as listas
from listas.listas_ctt import *

# funcao para editar contato
def editar(var_edit, id_edit):

    if var_edit == "nome":
        # solicitando novo nome
        novo_nome = input("Digite o novo nome: ").capitalize()
        nomes[id_edit] = novo_nome
        print("----------Contato Editado----------")
        print(f"ID: {id_edit} | Nome: {nomes[id_edit]} | Email: {emails[id_edit]} | Telefone: {telefones[id_edit]}")

    elif var_edit == "email":
        # solicitando novo email
        novo_email = input("Digite o novo email: ")
        emails[id_edit] = novo_email
        print("----------Contato Editado----------")
        print(f"ID: {id_edit} | Nome: {nomes[id_edit]} | Email: {emails[id_edit]} | Telefone: {telefones[id_edit]}")

    elif var_edit == "telefone":
        # solicitando novo telefone
        novo_tele = int(input("Digite o novo telefone: "))
        telefones[id_edit] = novo_tele
        print("----------Contato Editado----------")
        print(f"ID: {id_edit} | Nome: {nomes[id_edit]} | Email: {emails[id_edit]} | Telefone: {telefones[id_edit]}")()