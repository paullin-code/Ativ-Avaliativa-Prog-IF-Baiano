# importando as listas
from listas.listas_ctt import *

# funcao para remover contato
def remover(id_remov):
    ids.pop(id_remov)
    nomes.pop(id_remov)
    emails.pop(id_remov)
    telefones.pop(id_remov)

    for i in range(len(ids)):
        if ids[i] >= id_remov:
            ids[i] -= 1

    print("----------Agenda Editada----------")
    for ordem in ids:
        print(f"ID: {ordem} | Nome: {nomes[ordem]} | Email: {emails[ordem]} | Telefone: {telefones[ordem]}")
