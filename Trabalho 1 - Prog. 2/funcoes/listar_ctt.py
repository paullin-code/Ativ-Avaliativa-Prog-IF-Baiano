# importando as listas
from listas.listas_ctt import *

# funcao para listar contatos
def listar():
    resposta = ""
    print("----------Lista de Contatos----------")
    for ordem in ids:
        if ordem != ids[-1]:
            texto = f"ID: {ordem} | Nome: {nomes[ordem]} | Email: {emails[ordem]} | Telefone: {telefones[ordem]}\n"
        else:
            texto = f"ID: {ordem} | Nome: {nomes[ordem]} | Email: {emails[ordem]} | Telefone: {telefones[ordem]}"
        resposta += texto
    return resposta
